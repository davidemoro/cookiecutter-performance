import pytest
from contextlib import contextmanager
import shlex
import os
import subprocess
from cookiecutter.utils import rmtree


@pytest.fixture
def default_extra_context():
    return {
        'project_name': 'qa performance'
    }


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies, cookie to be baked and its
                    temporalfiles will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        if os.getenv('TRAVIS'):
            with open(os.devnull, 'w') as devnull:
                return subprocess.check_call(shlex.split(command),
                                             stdout=devnull,
                                             stderr=devnull)
        else:
            return subprocess.check_call(shlex.split(command))


def check_output_inside_dir(command, dirpath):
    "Run a command from inside a given directory, returning the command output"
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))


def project_info(result):
    """Get toplevel dir, project_slug, and project dir from baked cookies"""
    project_path = str(result.project)
    project_slug = os.path.split(project_path)[-1]
    project_dir = os.path.join(project_path, project_slug)
    return project_path, project_slug, project_dir


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert 'requirements.txt' in found_toplevel_files
        assert 'tox.ini' in found_toplevel_files
        assert 'example_yml.yml' in found_toplevel_files

        assert 'example_jmeter.yml' not in found_toplevel_files
        assert 'example_locust.yml' not in found_toplevel_files
        assert 'example_molotov.yml' not in found_toplevel_files

        example_yml = result.project.join('example_yml.yml')
        assert 'project name' in example_yml.read()


def test_bake_with_defaults_extra_context(cookies, default_extra_context):
    extra_context = default_extra_context.copy()
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert 'requirements.txt' in found_toplevel_files
        assert 'tox.ini' in found_toplevel_files
        assert 'example_yml.yml' in found_toplevel_files

        assert 'example_jmeter.yml' not in found_toplevel_files
        assert 'example_locust.yml' not in found_toplevel_files
        assert 'example_molotov.yml' not in found_toplevel_files

        example_yml = result.project.join('example_yml.yml')
        assert default_extra_context['project_name'] in example_yml.read()
