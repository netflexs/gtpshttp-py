from flask import Flask, render_template
import subprocess as sp

app = Flask(__name__, static_folder='assets', static_url_path='')

# Pass the required route to the decorator.
@app.route("/growtopia/server_data.php", methods = ['POST'])
def hello():
    return app.send_static_file('server-data.html')
	
@app.route("/")
def index():
	return app.send_static_file('redir.html')

if __name__ == "__main__":
	app.run(debug=True, port=3000)
