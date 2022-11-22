import launchy
import webview
import threading

PORT = 2077
LOCAL = f'http://127.0.0.1:{PORT}'

def serve(debug_mode: bool=False):
    print(LOCAL)
    
    app = launchy.create_app()
    app.run(port=PORT, debug=debug_mode, use_evalex=False, use_reloader=debug_mode)

# serve(debug_mode=True)

threading.Thread(target=serve).start()

webview.create_window(
    title='Launchy Desktop App',
    url=LOCAL,
    width=1920,
    height=1080,
    frameless=True,
    transparent=True   
    # background_color='#111111'
)

webview.start(debug=True, user_agent='Launchy Desktop 1.0')

