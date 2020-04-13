# encoding: utf-8
import configparser
import os.path as path


def get_properties_sections(ar_properties_file):

    exitValue = None

    try:
        config = configparser.RawConfigParser()
        config.read(ar_properties_file)
        exitValue = config.sections()
    except:
        exitValue = None

    return exitValue


def get_properties_key(ar_properties_file, ar_section, ar_key):

    exitValue = None

    try:
        config = configparser.RawConfigParser()
        config.read(ar_properties_file)
        dictionary = dict(config.items(ar_section))
        exitValue = dictionary[ar_key]
    except:
        exitValue = None

    return exitValue


def get_properties_section(ar_properties_file, ar_section):

    exitValue = None

    try:
        config = configparser.RawConfigParser()
        config.read(ar_properties_file)
        dictionary = dict(config.items(ar_section))
        exitValue = dictionary
    except:
        exitValue = None

    return exitValue


def modify_properties_key(ar_properties_file, ar_section, ar_key, ar_new_value):

    config = configparser.RawConfigParser()
    config.read(ar_properties_file)

    config.set(ar_section, ar_key, ar_new_value)
    with open(ar_properties_file, 'wb') as file:
        config.write(file)


def read(ar_file_name):

    exitValue = None

    try:
        with open(ar_file_name) as file:
            lines = file.readlines()

        exitValue = lines
    except:
        exitValue = None

    return exitValue


def full_read(ar_file_name):


    exitValue = None

    try:
        with open(ar_file_name, 'r') as file:
            lines = file.read()

        exitValue = lines
    except:
        exitValue = None

    return exitValue

def full_read_binary(ar_file_name):


    exitValue = None

    try:
        with open(ar_file_name, 'rb') as file:
            lines = file.read()

        exitValue = lines
    except:
        exitValue = None

    return exitValue


def write(ar_file_name, ar_content):

    with open(ar_file_name, 'w') as file:
        file.write(ar_content)


def exists_file(ar_file_name):

    exitValue = None

    if path.isfile(ar_file_name):
        exitValue = True
    else:
        exitValue = False

    return exitValue


def exists_path(ar_path):

    exitValue = None

    if path.isdir(ar_path):
        exitValue = True
    else:
        exitValue = False

    return exitValue


def write_binary(ar_file_name, ar_content):

    with open(ar_file_name, 'wb') as file:
        file.write(ar_content)