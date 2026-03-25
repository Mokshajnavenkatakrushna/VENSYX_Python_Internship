# Smart AI Document & Bill Extractor

The **Smart AI Document & Bill Extractor** is a modern, premium web application built with Python and Flask. It uses the state-of-the-art **Google Gemini Multimodal AI (gemini-2.5-flash)** to extract structured, categorized information directly from scanned documents, invoices, bills, and images. 

By utilizing native multimodal document processing, it completely bypasses the limitations and errors of traditional OCR (like Tesseract), resulting in pixel-perfect extraction and high-quality Markdown tables.

## 🚀 Features
- **Multimodal AI Extraction:** Upload physical media directly to Gemini without relying on low-quality intermediate OCR.
- **Premium User Interface:** A stunning, responsive frontend built with CSS Glassmorphism and modern gradient typography.
- **Broad File Support:** Upload standard images (JPG, PNG) or documents (PDF, DOCX, XLSX, TXT).
- **Intelligent Formatting:** Automatically converts extracted data into highly readable Markdown tables and categorized key-value lists using `Marked.js`.
- **Auto-Correction:** The AI is instructed to contextually correct obvious typos or scanning artifacts while extracting fields.

## 🛠️ Technologies Used
- **Backend:** Python, Flask, dotenv
- **AI Engine:** Google GenAI SDK (`gemini-2.5-flash`)
- **Frontend:** HTML5, Vanilla CSS, JS (Marked.js)

## ⚙️ Setup & Installation

### 1. Requirements
Ensure you have Python 3.9+ installed.

### 2. Clone/Open the Project
Navigate to the project directory in your terminal:
```bash
cd task3
```

### 3. Install Dependencies
Install all required Python packages using pip:
```bash
python -m pip install -r requirements.txt
```

### 4. Configure Environment Variables
You need a Google Gemini API Key. Get yours from the [Google AI Studio](https://aistudio.google.com/app/apikey).
Create or open the `.env` file in the root directory and add your key:
```ini
GEMINI_API_KEY=your_actual_api_key_here
```

### 5. Run the Application
Start the Flask development server:
```bash
python app.py
```
> **Note:** The server runs on port 5001 to avoid conflicts with macOS AirPlay settings.

### 6. Access the App
Open your web browser and navigate to:
```
http://127.0.0.1:5001
```

## 📄 Usage
1. Drag and drop your utility bill, invoice, or physical document onto the upload page.
2. Click **Extract Intelligence ⚡️**.
3. Allow a few seconds for the multimodal AI to process the image file entirely.
4. The system will display the cleanly formatted tabular/list data on the screen.

## 🔮 Future Enhancements
- **Export to CSV:** Direct download functionality to transition AI-extracted tables into Excel.
- **Batch Uploads:** Capable of processing dozens of documents concurrently.
- **Database Integration:** Saving histories of extractions per user.

## 🤝 Project Information
Developed as a project for extracting structured, context-aware information securely and accurately from unstructured formats.
