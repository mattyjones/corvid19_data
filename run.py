from app import app
import config

DEBUG = True

if DEBUG or config.DEBUG:
    RUN_DEBUG = True
else:
    RUN_DEBUG = False

if __name__ == '__main__':
    app.run(debug=RUN_DEBUG)
