import os
import json
import argparse
from collections import ChainMap


parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument("-c", "--configuration", type=open, nargs='?')
parser.add_argument("-p", "--playerclass", type=str,
                    nargs='?', default="Simple")
cmdline = parser.parse_args("-p Aggressive".split())


if cmdline.configuration:
    config_file = json.load(cmdline.configuration)
    cmdline.configuration.close()
else:
    config_file = {}

with open("defaults.json") as installation:
    defaults = json.load(installation)

print('-', vars(cmdline))
print('-', config_file)
print('-', os.environ)
print('-', defaults)

combined = ChainMap(vars(cmdline), config_file, os.environ, defaults)
print("combined", combined['playerclass'])
print("cmdline", cmdline.playerclass)
print("config_file", config_file.get('playerclass', None))
print("defaults", defaults.get('playerclass', None))
