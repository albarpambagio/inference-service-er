from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Load your model
model_name = "albarpambagio/indobertweet-base-uncased-emotion-recognition"
emotion_classifier = pipeline("text-classification", model=model_name)

class TextInput(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predict")
def predict_emotion(input: TextInput):
    predictions = emotion_classifier(input.text)
    return {pred['label']: pred['score'] for pred in predictions}

