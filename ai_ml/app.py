from fastapi import FastAPI
from pydantic import BaseModel
from pyngrok import ngrok
import uvicorn
import joblib
import nest_asyncio

# Patch the running event loop
nest_asyncio.apply()

app = FastAPI()

# Define the request body structure
class FraudDetectionRequest(BaseModel):
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float

# Load your pre-trained model
model = joblib.load('model.pkl')

@app.post("/predict")
def predict(request: FraudDetectionRequest):
    data = [[request.V1, request.V2, request.V3, request.V4, request.V5, request.V6, request.V7,
             request.V8, request.V9, request.V10, request.V11, request.V12, request.V13,
             request.V14, request.V15, request.V16, request.V17, request.V18, request.V19,
             request.V20, request.V21, request.V22, request.V23, request.V24, request.V25,
             request.V26, request.V27, request.V28, request.Amount]]
    prediction = model.predict(data)
    return {"prediction": int(prediction[0])}
    
# Expose the FastAPI app through ngrok
port = 8000
public_url = ngrok.connect(port)
print(f"ngrok tunnel {public_url} -> http://127.0.0.1:{port}")

# Start the FastAPI app
uvicorn.run(app, host="127.0.0.1", port=port)
