import asyncio

from cats.database import save

PARSERS = [
    'user_xmission_com',
]

async def parse_all(loop):

    futures = []

    for parser_name in PARSERS:
        parser = __import__('cats.parsers.' + parser_name,
                            fromlist=['cats', 'parsers'])

        fut = asyncio.ensure_future(parser.parse(loop=loop), loop=loop)
        futures.append(fut)

    while futures:
        done, futures = await asyncio.wait(
            futures, loop=loop,
            return_when=asyncio.FIRST_COMPLETED)

        for name, cats in [f.result() for f in done]:
            save(name, cats)
