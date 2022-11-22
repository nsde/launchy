from duckduckgo_search import ddg_images


def get_wallpaper(title):
    queries = [
        f'{title} wallpaper',
        f'{title} screenshot',
        f'{title} logo banner'
    ]

    for query in queries:
        try:
            print(query)
            return ddg_images(query, max_results=1)[0]['image']
        except KeyError:
            continue

