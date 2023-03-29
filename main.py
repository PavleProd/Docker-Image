from flask import Flask

app = Flask("python web server")


@app.route('/')  # root page
def helloWorld():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # starts web server
