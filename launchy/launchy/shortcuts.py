import LnkParse3

with open(r'C:\Users\Lynx\Desktop\Prism Launcher.lnk', 'rb') as indata:
    lnk = LnkParse3.lnk_file(indata)
    lnk.print_json()
