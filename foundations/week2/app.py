from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='static')


@app.route('/', defaults={'path': ''})  # This is the default route
@app.route('/<path:path>')  # This is the route for all other paths
def serve_index(path):
    # In all cases just send back index.html
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run(debug=True)
