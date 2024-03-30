from sanic import Sanic
from sanic.response import json
from routes import ROUTES

app = Sanic(__name__)


@app.route('/', methods=['GET'])
async def initial(request):
    return json({"API": "Petshop"})


app.blueprint(ROUTES)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7777, auto_reload=True)
