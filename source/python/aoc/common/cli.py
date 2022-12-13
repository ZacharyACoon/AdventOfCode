import click
import importlib
from types import SimpleNamespace
from pathlib import Path


@click.group()
@click.option("--documentation_path", type=click.Path(exists=True), default="../../documentation")
@click.option("--token", type=click.STRING, default=None)
@click.argument("year", type=click.IntRange(2015, 2022))
@click.argument("day", type=click.IntRange(1, 25))
@click.pass_context
def cli(ctx, token, documentation_path, year, day):
    documentation_path = Path(documentation_path)
    year = str(year)
    day = f"{day:02d}"
    module = f"aoc.year{year}.day{day}"
    ctx.obj = SimpleNamespace(
        token=token,
        documentation_path=documentation_path,
        year=year,
        day=day,
        puzzle_input_path=documentation_path / year / f"{day}_puzzle_input.txt",
        module=module,
        module_path=Path(module.replace(".", "/"))
    )


@cli.command()
@click.pass_context
def skeleton(ctx):
    import shutil
    ctx = ctx.obj

    # skeleton documentation
    day_markdown_path = ctx.documentation_path / ctx.year / f"{ctx.day}.md"
    day_markdown_path.touch(exist_ok=True)
    ctx.puzzle_input_path.touch(exist_ok=True)

    # skeleton source
    source_day_template_directory = Path(__file__).parent / f"day_template"
    try:
        shutil.copytree(source_day_template_directory, ctx.module_path, dirs_exist_ok=False)
    except FileExistsError:
        pass


@cli.command()
@click.pass_context
def test(ctx):
    import unittest
    unittest.main(f"{ctx.obj.module}.test", argv=["aoc"])


@cli.command()
@click.pass_context
@click.argument("input_file", type=click.Path(), required=False, default=None)
def solve(ctx, input_file):
    if input_file is None:
        input_file = ctx.obj.puzzle_input_path
    input = Path(input_file).read_text()
    solution_module = importlib.import_module(f"{ctx.obj.module}.solution")
    for p in range(2):
        print(f"Part {p+1}")
        part_result = getattr(solution_module, f"part{p+1}")(input)
        print(part_result)


@cli.command()
@click.pass_context
@click.option("--session_token", prompt=True, hide_input=True)
def fetch(ctx, session_token):
    from aoc.common.api import AdventOfCodeAPIClient
    client = AdventOfCodeAPIClient(session_token)
    client.fetch_year_day_part_challenge(ctx.obj.year, int(ctx.obj.day))
