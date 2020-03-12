# coding: utf-8

import json
from os import makedirs, getenv
from os.path import join, expanduser, exists

config_folder = getenv(
    'XDG_CONFIG_HOME',
    join(
        expanduser('~'),
        '.config'
    )
)

if not exists(config_folder):
    makedirs(config_folder)

config_file = join(
    config_folder,
    'watson-overloaded',
    'config.json'
)

# ⚠️ Create file automagically
if not exists(config_file):
    print('File {} does not exists, please create it.'.format(config_file))  # Color
    topics = []
    projects = []
    moods = []

else:
    with open(config_file) as json_file:
        data = json.load(json_file)

        topics = data['topics']
        projects = data['projects']
        moods = data['moods']
