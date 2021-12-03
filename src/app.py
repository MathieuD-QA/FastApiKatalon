from fastapi import FastAPI
from src.scrapping.KatalonDocWebUI import KatalonDoc


app = FastAPI()
apiKatalon = KatalonDoc()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}




@app.get("/WebUIAcceptAlert")
def get_WebUIAcceptAlert():
    apiKatalon.WebUIAcceptAlert()
    return {
        'title': apiKatalon.title,
        'note': apiKatalon.note,
        'description_id': apiKatalon.description,
        'description': apiKatalon.descriptionText,
        'parameters_id': apiKatalon.parameters,
        'parameters': apiKatalon.parametersText,
        'exemple_id': apiKatalon.exemple,
        'exemple': apiKatalon.exempleText
    }



@app.get("/WebUIBack")
def get_WebUIBack():
    apiKatalon.WebUIBack()
    return {
        'title': apiKatalon.title,
        'note': apiKatalon.note,
        'description_id': apiKatalon.description,
        'description': apiKatalon.descriptionText,
        'parameters_id': apiKatalon.parameters,
        'parameters': apiKatalon.parametersText,
        'exemple_id': apiKatalon.exemple,
        'exemple': apiKatalon.exempleText
    }



@app.get("/WebUICheck")
def get_WebUICheck():
    apiKatalon.WebUICheck()
    return {
        'title': apiKatalon.title,
        'note': apiKatalon.note,
        'description_id': apiKatalon.description,
        'description': apiKatalon.descriptionText,
        'parameters_id': apiKatalon.parameters,
        'parameters': apiKatalon.parametersText,
        'exemple_id': apiKatalon.exemple,
        'exemple': apiKatalon.exempleText
    }




@app.get("/WebUIClickImage")
def get_WebUIClickImage():
    apiKatalon.WebUIClickImage()
    return {
        'title': apiKatalon.title,
        'note': apiKatalon.note,
        'description_id': apiKatalon.description,
        'description': apiKatalon.descriptionText,
        'parameters_id': apiKatalon.parameters,
        'parameters': apiKatalon.parametersText,
        'exemple_id': apiKatalon.exemple,
        'exemple': apiKatalon.exempleText
    }



@app.get("/WebUIClickOffset")
def get_WebUIClickOffset():
    apiKatalon.WebUIClickOffset()
    return {
        'title': apiKatalon.title,
        'note': apiKatalon.note,
        'description_id': apiKatalon.description,
        'description': apiKatalon.descriptionText,
        'parameters_id': apiKatalon.parameters,
        'parameters': apiKatalon.parametersText,
        'exemple_id': apiKatalon.exemple,
        'exemple': apiKatalon.exempleText
    }

@app.get("/WebUICloseBrowser")
def get_WebUICloseBrowser():
    apiKatalon.WebUICloseBrowser()
    return {
        'title': apiKatalon.title,
        'note': apiKatalon.note,
        'description_id': apiKatalon.description,
        'description': apiKatalon.descriptionText,
        'parameters_id': apiKatalon.parameters,
        'parameters': apiKatalon.parametersText,
        'exemple_id': apiKatalon.exemple,
        'exemple': apiKatalon.exempleText
    }



@app.get("/WebUICloseWindowTitle")
def get_WebUICloseWindowTitle():
    apiKatalon.WebUICloseWindowTitle
    return {
        'title': apiKatalon.title,
        'note': apiKatalon.note,
        'description_id': apiKatalon.description,
        'description': apiKatalon.descriptionText,
        'parameters_id': apiKatalon.parameters,
        'parameters': apiKatalon.parametersText,
        'exemple_id': apiKatalon.exemple,
        'exemple': apiKatalon.exempleText
    }






@app.get("/WebUIDeleteAllCookies")
def get_WebUIDeleteAllCookies():
    apiKatalon.WebUIDeleteAllCookies()
    return {
        'title': apiKatalon.title,
        'note': apiKatalon.note,
        'description_id': apiKatalon.description,
        'description': apiKatalon.descriptionText,
        'parameters_id': apiKatalon.parameters,
        'parameters': apiKatalon.parametersText,
        'exemple_id': apiKatalon.exemple,
        'exemple': apiKatalon.exempleText
    }
















