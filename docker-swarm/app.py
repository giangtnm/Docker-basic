from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    #count = redis.incr('hits')
    #return 'Hello World! I have been seen {} times.\n'.format(count)
    print socket.gethostname()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
