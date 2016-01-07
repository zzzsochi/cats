import aiohttp
import bs4

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
               .replace('&gt;', '>')
               .replace('&lt;', '<')
               .replace('&amp;', '&')
               )

        def strip_first(lines):
            res = lines.copy()
            for line in lines:
                if not line.strip():
                    del res[0]
                else:
                    break

            return res

        cat = '\n'.join(strip_first(cat.split('\n')))
        cat = '\n'.join(reversed(strip_first(list(reversed(cat.split('\n'))))))

        if len(cat.strip()) > 5:
            cats.append(cat)

    return 'user_xmission_com', cats
