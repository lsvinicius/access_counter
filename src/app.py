import datetime

from flask import Flask

from src import settings, counter, logger

app = Flask(__name__)
count = counter.get_saved_count()


@app.route('/')
def home():
    global count
    count += 1
    counter.save_count(count)
    logger.logger.warn('request at {}'.format(datetime.datetime.now()))
    return 'You are the {} visitor'.format(count)


if __name__ == '__main__':

    port = settings.get_port()
    debug = settings.get_debug()
    app.run(debug=debug, port=port)
