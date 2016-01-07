import aiohttp
import bs4

from .helpers import prepare_cat

URL = 'https://user.xmission.com/~emailbox/ascii_cats.htm'


async def parse(loop):
    async with aiohttp.get(URL) as r:
        raw = await r.text()

    html = bs4.BeautifulSoup(raw, "html.parser")
    tbody = html.body.find_all('table')[1].tbody

    cats = []

    for tr in tbody.find_all('tr'):
        tt = tr.tt
        cat = (str(tt)
               .replace('\xa0', ' ')
               .replace('\n', ' ')
               .replace('<br>', '\n')
               .replace('</br>', '')
               .replace('<tt>', ' ')
               .replace('</tt>', '')
               .replace('<b>', '')
               .replace('</b>', '')
               .replace('<font color="#ffffff">', '')
               .replace('</font>', '')
               )

        cat = prepare_cat(cat)

        if len(cat.strip()) > 5:
            cats.append(cat)

    return 'user_xmission_com', cats
