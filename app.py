import logging

from flask import Flask, request, render_template, send_from_directory, Blueprint  # запрос, воспроизводить шаблон, отправить из каталога

from loader.views import loader_blueprint
from main_.views import main_blueprint

# from functions import ...

POST_PATH = "posts.json"  # почта путь
UPLOAD_FOLDER = "uploads/images"  #  загрузка папки

app = Flask(__name__)  # приложение

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)
logging.basicConfig(filename="basic.log", level=logging.INFO)


@app.route("/uploads/<path:path>")
def static_dir(path):  # статик каталог
    return send_from_directory("uploads", path)  # отправить из каталога


app.run()

