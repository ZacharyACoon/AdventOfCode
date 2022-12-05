import click
import importlib
from types import SimpleNamespace
from pathlib import Path


@click.group()
@click.option("--documentation_path", type=click.Path(exists=True), default="../../documentation")
@click.argument("year", type=click.IntRange(2015, 2022))
@click.argument("day", type=click.IntRange(1, 25))
@click.pass_context
def cli(ctx, documentation_path, year, day):
    documentation_path = Path(documentation_path)
    year = str(year)
    day = f"{day:02d}"

    ctx.obj = SimpleNamespace(
        year=year,
        day=day,
        documentation_path=documentation_path,
        puzzle_input_path=documentation_path / year / f"{day}_puzzle_input.txt",
        module=f"aoc.year{year}.day{day}"
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
    source_day_directory = Path(__file__).parent.parent / f"year{ctx.year}" / f"day{ctx.day}"
    try:
        shutil.copytree(source_day_template_directory, source_day_directory, dirs_exist_ok=False)
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
    ctx = ctx.obj
    if input_file is None:
        input_file = ctx.documentation_path / ctx.year / f"{ctx.day}_puzzle_input.txt"
    input = Path(input_file).read_text()
    solution_module = importlib.import_module(f"{ctx.module}.solution")
    for p in range(2):
        print(f"Part {p}")
        part_result = getattr(solution_module, f"part{p+1}")(input)
        print(part_result)
