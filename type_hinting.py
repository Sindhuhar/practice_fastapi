from fastapi import FastAPI
app = FastAPI()

@app.get("/shipment")

def read_shipment(id : int):
    return {
        "id" : id,
        "status" : "devivered"
    }

