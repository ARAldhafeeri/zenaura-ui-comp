import logging
import os
from flask import render_template, Flask
from public.routes import ClientRoutes
from zenaura.server import DevServer

app = Flask(__name__, static_folder="public", template_folder="public")

DEVSERVER = DevServer(app, port=5001, debug=True)

@DEVSERVER.app.route(ClientRoutes.menu.value)
@DEVSERVER.app.route(ClientRoutes.home.value)
@DEVSERVER.app.route(ClientRoutes.breadcrumbs.value)
@DEVSERVER.app.route(ClientRoutes.button.value)
@DEVSERVER.app.route(ClientRoutes.input.value)
@DEVSERVER.app.route(ClientRoutes.select.value)
@DEVSERVER.app.route(ClientRoutes.form.value)
@DEVSERVER.app.route(ClientRoutes.badge.value)
@DEVSERVER.app.route(ClientRoutes.card.value)
@DEVSERVER.app.route(ClientRoutes.popover.value)
@DEVSERVER.app.route(ClientRoutes.modal.value)
@DEVSERVER.app.route(ClientRoutes.table.value)
@DEVSERVER.app.route(ClientRoutes.tabs.value)
@DEVSERVER.app.route(ClientRoutes.message.value)
def root():
    try:
        return render_template("index.html")
    except Exception as e:
        logging.info(f"Error rendering template: {e}")
        return "An error occurred.", 500

if __name__ == "__main__":
    DEVSERVER.run()


