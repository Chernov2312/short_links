from routes import setup_routes
from sanic import Sanic

app = Sanic('ShortLinksApp')

setup_routes(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True, auto_reload=True)
