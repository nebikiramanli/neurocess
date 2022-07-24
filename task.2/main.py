from enum import Enum
import data_helper
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse, ORJSONResponse, HTMLResponse
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")
AMAZON_URL = "https://www.amazon.com.tr/s?k=apple&rh=n%3A12466496031%2Cn%3A26232650031&dc&ds=v1%3A24QIKEr1whZX7fY03aG1Rzroi24YQzoigI1WMNytis0&__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=9UPC9JZMBEZY&qid=1658327018&rnid=13818411031&sprefix=appl%2Caps%2C122&ref=sr_nr_n_4"

class ResponseType(Enum):
    JSON = "json"
    HTML = "html"
    ORJSON = "orjson"


@app.get("/")
def welcome(request: Request):

    return templates.TemplateResponse("welcome.html", {"request":request}, status_code=200, media_type="text/html")


@app.get("/products", response_class=HTMLResponse)
def read_item(request: Request):
    products = data_helper.get_data_from_url(AMAZON_URL)

    if products is None:
        return templates.TemplateResponse("error.html", {"request":request}, status_code=200, media_type="text/html")

    return templates.TemplateResponse("index.html", {"request": request, "products": products}, status_code=200, media_type="text/html")


@app.get("/products/{response_type}", response_class=JSONResponse)
def read_item(request: Request, response_type: str):
    products = data_helper.get_data_from_url(AMAZON_URL)
    
    if products is None:
        return templates.TemplateResponse("error.html", {"request":request}, status_code=200, media_type="text/html")
    
    if response_type == ResponseType.JSON.value:
        return JSONResponse(products, status_code=200, media_type="application/json")
    elif response_type == ResponseType.ORJSON.value:
        return ORJSONResponse(products, status_code=200, media_type="application/json")
    else:
        return templates.TemplateResponse("index.html", {"request": request, "products": products}, status_code=200, media_type="text/html")
    

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
