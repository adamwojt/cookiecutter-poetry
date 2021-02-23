#!/usr/bin/env python

"""Tests for `{{ cookiecutter.module_name }}` package."""

import pytest
{%- if cookiecutter.command_line_interface | lower == "click" %}
from click.testing import CliRunner
{%- endif %}

from {{ cookiecutter.module_name }} import {{ cookiecutter.module_name }}
{%- if cookiecutter.command_line_interface | lower == "click" %}
from {{ cookiecutter.module_name }} import cli
{%- endif %}

{%- if cookiecutter.command_line_interface | lower == "click" %}
def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "{{ cookiecutter.module_name }}.cli.main" in result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output
{%- endif %}
