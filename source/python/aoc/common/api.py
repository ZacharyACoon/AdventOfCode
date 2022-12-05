import webbrowser
import requests


class AdventOfCodeAPIClient:
    url = "https://adventofcode.com/"

    def __init__(self, session_token: str):
        self.session = requests.Session()
        self.session.cookies.set("session", session_token)

    @staticmethod
    def open_browser_for_session_token():
        webbrowser.open(AdventOfCodeAPIClient.url, autoraise=True)

    def _base_request(self, endpoint):
        return requests.Request(
            method="GET",
            url=self.url + endpoint
        )

    def fetch_year_day_part_challenge(self, year, day):
        request = self._base_request(f"{year}/day/{int(day)}").prepare()
        response = self.session.send(request)
        if response.status_code == 200:
            main = response.text.split("<main>")[1].split("</main>")[0]
            print(main)
