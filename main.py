from fastapi import FastAPI, Form
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def root():
    return FileResponse("index.html")


@app.post("/postdata")
def postdata(number1 = Form(), act=Form(), number2=Form()):
    if act == 'summ':
        result = number1 + number2
    elif act == 'minus':
        result = number1 - number2
    elif act == 'mult':
        result = number1 * number2
    elif act == 'div':
        result = number1 / number2
    else:
        result = 'Operation impossible'

    return {"result": result}