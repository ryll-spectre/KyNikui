
import traceback


if __name__ == "__main__":

    from src.kynikui import KyNikui
    app = KyNikui()

    try:
        app.run()
    except Exception as error:
        traceback.print_exc()
        app.stop()