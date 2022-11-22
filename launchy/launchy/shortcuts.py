import LnkParse3
from pprint import pprint

def get_command(path: str) -> str:
    with open(path, 'rb') as data:
        lnk = LnkParse3.lnk_file(data)
        lnk = lnk.get_json()

    px = ''
    args = lnk['data'].get('command_line_arguments')
    
    if args:
        args = ' ' + args
    # else:
    #     px = 'start '

    pprint(lnk)
    return f"{px}\"{lnk['link_info']['local_base_path']}\"{args or ''}"

if __name__ == '__main__':
    test = r'C:\Users\Lynx\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Control Panel.lnk'
    print(get_command(test))
