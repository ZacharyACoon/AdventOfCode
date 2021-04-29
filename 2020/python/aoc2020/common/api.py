import urllib.request
import urllib.parse
from html.parser import HTMLParser


class AdventOfCodeHTMLParser(HTMLParser):
    def __init__(self, *args, **kwargs):
        super(AdventOfCodeHTMLParser, self).__init__(*args, **kwargs)
        self.inside_article = False
        self.inside_example = False
        self.articles = []
        self.examples = []
        self.path = []

    def handle_starttag(self, tag, attrs):
        self.path.append(tag)
        if "article" in tag:
            for key, value in attrs:
                if "class" in key and "day-desc" in value:
                    self.inside_article = True
                    self.articles.append("")
        elif len(self.path) > 1 and self.path[-2:] == ["pre", "code"]:
            self.inside_example = True

    def handle_data(self, data):
        if self.inside_article:
            self.articles[-1] += data
            if self.inside_example:
                self.examples.append(data)
                self.inside_example = False

    def handle_endtag(self, tag):
        self.path.pop(-1)
        if self.inside_article and tag[0] == "h":
            self.articles[-1] += "\n"
        elif "article" in tag:
            self.inside_article = False


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
        return response


class TokenRequired(Exception):
    pass


class API:
    def __init__(self, token=None):
        self.url = "https://adventofcode.com/{year}/day/{day}"
        self.request = urllib.request.Request(self.url)
        self.token = token
        if self.token:
            self.request.add_header("Cookie", f"session={self.token}")

        self.html_cache = {}
        self.html_parser = AdventOfCodeHTMLParser()

    def _token_required(f):
        def new_f(self, *args):
            if not self.token:
                raise TokenRequired
            return f(self, *args)
        return new_f

    def get_puzzle(self, year, day):
        self.request.full_url = self.url.format(year=year, day=day)
        with urllib.request.urlopen(self.request) as response:
            html = response.read().decode("utf-8")
        self.html_cache[(year, day)] = html
        self.html_parser.reset()
        self.html_parser.feed(html)
        return self.html_parser.article

    def get_examples(self, year, day):
        if not (year, day) in self.html_cache:
            self.get_puzzle(year, day)

        self.html_parser.reset()
        self.html_parser.feed(self.html_cache[(year, day)])
        return self.html_parser.examples


    @_token_required
    def get_input(self, year, day):
        self.request.full_url = f"{self.request.full_url}/input"
        with urllib.request.urlopen(self.request) as response:
            return response.read()

    @_token_required
    def submit_answer(self, year, day):
        pass
