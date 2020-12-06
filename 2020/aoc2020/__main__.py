import importlib
from aoc2020.common import api
import sys
import time


if __name__ == "__main__":
    assert len(sys.argv) > 1
    token = sys.argv[1]

    for day in range(1, 26):
        try:
            solution = importlib.import_module(f"aoc2020.day{day}.solution")
        except ImportError:
            break

        endpoint = api.get_base_endpoint(2020, day)
        partial_request = api.get_partial_request(endpoint, token)

        print(f"Day {day}")
        print("    fetching")
        input = api.fetch_input(partial_request)
        print("    solving")

        answer1 = solution.part1(input)
        print("    Part 1:", answer1)
        print("        submitting")
        time.sleep(1)  # respectful rate limit
        response = api.submit_answer(partial_request, 1, answer1)
        print("        ", api.submit_answer(partial_request, 2, answer1))

        answer2 = solution.part2(input)
        print("    Part 2:", answer2)
        print("        submitting")
        time.sleep(1)  # respectful rate limit
        print("        ", api.submit_answer(partial_request, 2, answer2))
