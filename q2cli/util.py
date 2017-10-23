# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


def get_app_dir():
    import click
    return click.get_app_dir('q2cli', roaming=False)


# NOTE: `get_cache_dir` and `get_completion_path` live here instead of
# `q2cli.cache` because `q2cli.cache` can be  slow to import.
# `get_completion_path` (which relies on `get_cache_dir`) is imported and
# executed by the Bash completion function each time the user hits <tab>, so it
# must be quick to import.
def get_cache_dir():
    import os.path
    return os.path.join(get_app_dir(), 'cache')


def get_completion_path():
    import os.path
    return os.path.join(get_cache_dir(), 'completion.sh')


def to_cli_name(name):
    return name.replace('_', '-')


def exit_with_error(e, header='An error has been encountered:', file=None,
                    suppress_footer=False):
    import sys
    import traceback
    import textwrap
    import click

    if file is None:
        file = sys.stderr
        footer = 'See above for debug info.'
    else:
        footer = 'Debug info has been saved to %s' % file.name

    error = textwrap.indent(str(e), '  ')

    segments = [header, error]
    if not suppress_footer:
        segments.append(footer)

    traceback.print_exception(type(e), e, e.__traceback__, file=file)
    file.write('\n')

    click.secho('\n\n'.join(segments), fg='red', bold=True, err=True)

    click.get_current_context().exit(1)
