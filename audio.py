import whisper
model = whisper.load_model("base")

filePath = input("Enter file Path: ")
result = model.transcribe(filePath)

print("Audio Transcribed -->" + result["text"])
