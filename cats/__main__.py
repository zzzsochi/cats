import argparse
import sys

from cats import __version__
import cats.database


def run_print(parser, args, file=sys.stdout):
    cat = cats.database.get_random()
    print(cat)


def run_parse(parser, args):
    if sys.version_info < (3, 5):
        print("'cats parse' require python 3.5.0 or better.", file=sys.stderr)
        print("This cat for your:\n", file=sys.stderr)
        run_print(parser, args, file=sys.stderr)
        sys.exit(1)

    try:
        import asyncio
        import aiohttp  # noqa
        import bs4  # noqa
    except ImportError:
        print("\"pip install 'cats[parse]'\" first!", file=sys.stderr)
        sys.exit(1)

    import cats.parsers

    loop = asyncio.get_event_loop()
    loop.run_until_complete(cats.parsers.parse_all(loop=loop))


def run_help(parser, args):
    parser.print_help()


def run_version(parser, args):
    print(__version__)


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # print

    parser_print = subparsers.add_parser('print', help="random cat")
    parser_print.set_defaults(func=run_print)

    # parse

    parser_parse = subparsers.add_parser('parse', help="parse cats")
    parser_parse.set_defaults(func=run_parse)

    # help

    parser_help = subparsers.add_parser('help', help="show this help message and exit")
    parser_help.set_defaults(func=run_help)

    # version

    parser_version = subparsers.add_parser('version', help="show version and exit")
    parser_version.set_defaults(func=run_version)

    args = parser.parse_args()
    getattr(args, 'func', run_print)(parser, args)

if __name__ == '__main__':
    main()
