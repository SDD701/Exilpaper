from textural.app import App, ComposeResult
from textural.widgets import Header, Footer

import requests


class ExilPaper(App)
    # Interface app

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

# Start
ExilPaper.run()

#responce = requests.get("https://www.wallpaperflare.com/tag")
#print(responce.text)
