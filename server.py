from sanic import Sanic
from sanic.response import json

app = Sanic(__name__)

@app.route('/', methods=['GET'])
async def initial(request):
    return json({"hello":"world"})

from routes import ROUTES
app.blueprint(ROUTES)

if __name__ == '__main__':
    app.run(host="localhost", port=7777, auto_reload=True)