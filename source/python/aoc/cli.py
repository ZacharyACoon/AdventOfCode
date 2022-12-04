import click
import importlib


@click.group()
@click.argument("year", type=click.IntRange(2015, 2022))
@click.argument("day", type=click.IntRange(1, 25))
@click.pass_context
def cli(ctx, year, day):
    ctx.obj = {
        "year": year,
        "day": day,
        "module": f"aoc.year{year}.day{day:02d}"
    }


@cli.command()
@click.pass_context
def test(ctx):
    import unittest
    module = ctx.obj["module"]
    unittest.main(f"{module}.test", argv=["aoc"])


@cli.command()
@click.pass_context
@click.argument("input_file", type=click.File("r"))
def solve(ctx, input_file):
    module = ctx.obj["module"]
    input = input_file.read()
    solution_module = importlib.import_module(f"{module}.solution")

    for p in range(2):
        print(f"Part {p}")
        part_result = getattr(solution_module, f"part{p+1}")(input)
        print(part_result)
