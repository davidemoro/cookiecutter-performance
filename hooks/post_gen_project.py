#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(*filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, *filepath))


def remove_folder(*folderpath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, *folderpath))


if __name__ == '__main__':
    if '{{ cookiecutter.molotov }}' != 'y':
        remove_file('example_molotov.yml')

    if '{{ cookiecutter.locust }}' != 'y':
        remove_file('example_locust.yml')

    if '{{ cookiecutter.jmeter }}' != 'y':
        remove_file('example_jmeter.yml')
