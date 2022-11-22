from duckduckgo_search import ddg_images

def get_wallpaper(title):
    return ddg_images(f'{title} screenshot|wallpaper|logo|icon', layout='Wide', max_results=1)[0]['image']
