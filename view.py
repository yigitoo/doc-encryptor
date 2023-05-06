import webview

url_of_server = "localhost:3000"

window = webview.create_window(
    title = "ÜMİT ŞENYURT | ASKİ ELEKTRONİK TEKNİSYENİ",
    url = url_of_server,
    fullscreen=True
)

webview.start()