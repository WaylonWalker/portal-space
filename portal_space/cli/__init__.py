# SPDX-FileCopyrightText: 2022-present Waylon S. Walker <waylon@waylonwalker.com>
#
# SPDX-License-Identifier: MIT
import click

from portal_space.__about__ import __version__
from portal_space.game import MyGame


@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
    invoke_without_command=True,
)
@click.version_option(version=__version__, prog_name="portal-space")
@click.pass_context
def portal_space(ctx: click.Context):
    game = MyGame()
    game.run()
