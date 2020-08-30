from flask import Flask
from flask_celery import make_celery
# from celery import Celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://guest:@localhost:5672//'
app.config['CELERY_RESULT_BACKEND'] = 'db+sqlite:///db.sqlite3'
celery = make_celery(app)
# celery = Celery('main', backend='rpc://', broker='amqp://guest:@localhost:5672//')
# You can also use above single line of code to run run celery worker

@app.route('/process/<name>')
def process(name):
    reverse.delay(name)
    return 'I sent an name'
    # return name

@celery.task(name='main.reverse')
def reverse(string):
    return string[::-1]

if __name__ == '__main__':
    app.run(debug=True)