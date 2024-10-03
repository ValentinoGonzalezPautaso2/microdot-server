from microdot import Microdot, send_file
from machine import Pin

app = Microdot()

@app.get('/')
async def index(request):
    return send_file('/index.html')

@app.route('/<dir>/<file>') # Definimos la ruta con dos parámetros
async def index(request, dir, file):
    return send_file("/" + dir + "/" + file) # Cambiamos el nombre del archivo a enviar
    

@app.route('/toggle/led/<int:id>') # Definimos la ruta con un parámetro entero
async def index(request, id):

    if id == 1:
        led1.value(not led1.value())
        
    elif id == 2:
        led2.value(not led2.value())
        
    elif id == 3:
        led3.value(not led3.value())
    
    
    return 'OK'




app.run(port = 80)

