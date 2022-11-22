import os
import launchy
import webview
import keyboard
import threading

PORT = 2077
LOCAL = f'http://127.0.0.1:{PORT}'

def stop():
    os._exit(-1)
    
keyboard.add_hotkey('alt+q', lambda: stop())

def serve(debug_mode: bool=False):    
    app = launchy.create_app()
    print(f'-> {LOCAL} <-')
    app.run(port=PORT, debug=debug_mode, use_evalex=False, use_reloader=debug_mode)

serve(debug_mode=True)
exit()
threading.Thread(target=serve).start()

webview.create_window(
    title='Launchy',
    url=LOCAL,
    width=1700,
    height=900,
    # frameless=True,
    # transparent=True   
    # background_color='#111111'
)

webview.start(debug=True, user_agent='LaunchyDesktop_1_0')

