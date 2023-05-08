from fastapi import FastAPI
from fastapi import FastAPI, Response

app = FastAPI(title= 'Aplicacion DDP', 
              description= 'Proyecto de pruebas de api de la asignatura DDP', 
              version='1.0')

@app.get('/hello')
def index():
    return {"mensaje": "Hello FastAPI"}

@app.post("/isPrime/{n}")
def verificar_primo(n: str, response: Response):

    validacion = validaciones(n, "primo")
    if validacion != "Solicitud Exitosa":
        response.status_code = 400
        return {"validacion": validacion}
    
    respuesta = es_primo(n)
    return {"validacion": validacion, "respuesta": respuesta}

@app.post("/fibonacci/{position}")
def fibonacci(position: str, response: Response):

    validacion = validaciones(position, "fibonacci")
    if validacion != "Solicitud Exitosa":
        response.status_code = 400
        return {"validacion": validacion}
    respuesta = fibonacci_exe(position)

    return {"validacion": validacion, "respuesta": respuesta}




def validaciones(x, type):
    try:
        num = int(x)
    except:
        return "Error: el valor introducido no es un numero entero"
        
    if num < 0:
        return "Error: el valor introducido es negativo"
    
    if num > 1000 and type == "fibonacci":
        return "Error: El limite de la posicion es 1000"
    
    if num >= 4.3466557686937455e+208 and type == "primo":
        return "Error: El valor introducido supera el limite: 4.3466557686937455e+208"
    return "Solicitud Exitosa"



def fibonacci_exe(position):
    position = int(position)

    if position <= 0:
        return 0
    if position == 1 or position == 2:
        return 1

    fib_1 = 1
    fib_2 = 1

    for i in range(3, position + 1):
        fib_i = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fib_i

    return fib_i


def es_primo(n):
    n = int(n)
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
