import logging

# Set root logger to DEBUG
logging.basicConfig(level=logging.DEBUG)

from nicegui import ui

ui.label('Hello, NiceGUI!').classes('text-sm')

ui.button('Run', on_click=lambda: ui.notify('Button clicked!'))

ui.run()
logging.debug("NiceGUI app is running")
logging.debug("This is a debug message from the NiceGUI app")
logging.debug("Another debug message for tracing")


