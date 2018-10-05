# importing flask
from flask import Flask

app = Flask(__name__)


# routing the app for view
@app.route('/')
def front_page():
    return 'hello world'   #write 'localhost:5000' on your browser to run the app


#running the server
if __name__ == '__main__':
    app.run(debug=True)
