import argparse


parser = argparse.ArgumentParser(
    description='Search engine', prog='Search Programme'
)

parser.add_argument(
    'text', action='store', help='request text', nargs='+'
)
parser.add_argument(
    '-s', '--search', dest='search', action='store',
    choices=('google.com', 'yandex.ru'), default='yandex.ru', metavar=''
)
parser.add_argument(
    '-q', '--quantity', dest='quantity', action='store',
    default=5, type=int, help='Quantity', metavar=''
)
parser.add_argument(
    '-r', '--recursion', dest='recursion', action='store',
    type=int, choices=(0, 1), default=0, metavar=''
)
parser.add_argument(
    '-f', '--format', dest='format', action='store',
    choices=('console', 'json', 'csv'), default='console',
    metavar=''
)
