from search_engine.functions import (
    get_search_request, get_simple_request, get_links,
    save_in_json, save_in_csv
)
from search_engine.argvparser import parser


args = parser.parse_args()
search_page = get_search_request(' '.join(args.text), args.search)

if args.recursion:
    links = [get_links(search_page, 1, args.search)]
    for _ in range(args.quantity - 1):
        page = get_simple_request(links[-1])
        links.append(get_links(page))
else:
    links = get_links(search_page, args.quantity, args.search)


if args.format == 'console':
    print(links)
elif args.format == 'json':
    save_in_json(links)
elif args.format == 'csv':
    save_in_csv(links)
