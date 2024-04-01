import whisper

model = whisper.load_model("tiny")
result = model.transcribe("video.mp3")
phrase = result["text"]
with open("input.txt", "w", encoding="utf=8") as f:
    f.write(phrase)