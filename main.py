import pystray
import PIL.Image
from notify import notify
from clean import empty

icon = PIL.Image.open("trash.png")

def on_click():
    try:
        empty()
        notify("Корзина успешно очищена!", "Готово")
    except:
        notify("Корзина пуста!", "Ошибка")

tray = pystray.Icon("TrayTrash", icon, menu=pystray.Menu(pystray.MenuItem("Очистить корзину", on_click)))
tray.run()