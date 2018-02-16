from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h3>Adding the title for the route</h3>"
    return html.format()

def main():
    app.run(host='0.0.0.0', port=80)

if __name__ == '__main__':
    main()
