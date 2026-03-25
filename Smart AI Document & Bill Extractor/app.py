from flask import Flask, render_template, request
import os
from dotenv import load_dotenv

from readers.ai_processor import process_document_with_ai

load_dotenv()

app = Flask(__name__)

UPLOAD = "uploads"
os.makedirs(UPLOAD, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def home():

    structured_text = ""

    if request.method == "POST":

        file = request.files["file"]

        path = os.path.join(UPLOAD, file.filename)

        file.save(path)

        # Let Gemini process the raw image / document natively for perfect extraction
        structured_text = process_document_with_ai(path)

    return render_template("index.html", text=structured_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)