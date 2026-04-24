from flask import Flask
from database import init_db, db
from routes import bp
import time


def create_app():
    app = Flask(__name__)

    # подключаем базу данных
    init_db(app)

    # подключаем маршруты
    app.register_blueprint(bp)

    return app


app = create_app()


def wait_for_db():
    for _ in range(10):
        try:
            with app.app_context():
                db.create_all()
            return
        except Exception:
            time.sleep(2)
    raise RuntimeError("База данных не стала доступна вовремя")


if __name__ == "__main__":
    wait_for_db()
    app.run(host="0.0.0.0", port=5000, debug=True)