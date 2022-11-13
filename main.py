import launchy
import webview
import threading

LOCAL = 'http://127.0.0.1:2077'

def serve(debug_mode: bool=False):
    app = launchy.create_app()
    app.run(port=2077, debug=debug_mode, use_evalex=False, use_reloader=debug_mode)

serve(debug_mode=True)

# threading.Thread(target=serve).start()

# webview.create_window(
#     title='Launchy Desktop App',
#     url=LOCAL,
#     width=450,
#     height=650,
#     background_color='#111111'
# )

# webview.start(debug=True, user_agent='Launchy Desktop 1.0')

