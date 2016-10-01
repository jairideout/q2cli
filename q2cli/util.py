# ----------------------------------------------------------------------------
# Copyright (c) 2016--, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------


def get_app_dir():
    import click
    return click.get_app_dir('q2cli', roaming=False)


def to_cli_name(name):
    return name.replace('_', '-')
