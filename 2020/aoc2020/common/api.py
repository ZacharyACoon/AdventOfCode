import urllib.request
import urllib.parse
from functools import partial

def get_base_endpoint(year, day):
    return f"https://adventofcode.com/{year}/day/{day}"


def prepare_request(endpoint, token):
    request = urllib.request.Request(endpoint)
    request.add_header("Cookie", f"session={token}")
    return request


def get_partial_request(endpoint, token):
    return partial(prepare_request, endpoint, token)


def fetch_puzzle_page(partial_request):
    request = partial_request()
    request.full_url = f"{request.full_url}/input"
    with urllib.request.urlopen(request) as response:
        return response.read()


def fetch_input(partial_request):
    request = partial_request()
    request.full_url = f"{request.full_url}/input"
    with urllib.request.urlopen(request) as response:
        return response.read().decode("utf-8")


def submit_answer(partial_request, part, answer):
    request = partial_request()
    request.full_url = f"{request.full_url}/answer"
    request.method = "POST"
    request.data = urllib.parse.urlencode({"level": part, "answer": answer}).encode("ascii")
    with urllib.request.urlopen(request) as response:
        return response.status
