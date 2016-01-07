import aiohttp
import bs4

from .helpers import prepare_cat

URL = 'http://www.asciiworld.com/-Cats-.html'


async def parse(loop):
    async with aiohttp.get(URL) as r:
        raw = await r.text()

    html = bs4.BeautifulSoup(raw, "html.parser")

    cats = []

    for pre in html.find_all('pre'):
        cat = (str(pre)
               .replace('<pre>', '')
               .replace('</pre>', '')
               )

        cat = prepare_cat(cat)

        if len(cat.strip()) > 5:
            cats.append(cat)

    return 'asciiworld', cats
