import gradio as gr
from transformers import pipeline
import numpy as np

MODEL_PATH = "models/whisper-base-finetune"
transcriber = pipeline("automatic-speech-recognition", model=MODEL_PATH)


def transcribe(audio):
    sr, y = audio
    y = y.astype(np.float32)
    y /= np.max(np.abs(y))

    return transcriber({"sampling_rate": sr, "raw": y})["text"]


demo = gr.Interface(
    transcribe,
    gr.Audio(sources=["microphone"]),
    "text",
)

demo.launch()
