from flask import Flask
import tensorflow as tf

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h3>Adding the title for the route</h3>"
    return html.format()

def main():
    app.run(host='0.0.0.0', port=80)
    x = tf.constant(5, dtype=tf.float32)
    init = tf.global_variables_initializer()
    interactive_session = tf.InteractiveSession()
    init.run()
    print(x.eval())
    interactive_session.close()

if __name__ == '__main__':
    main()
