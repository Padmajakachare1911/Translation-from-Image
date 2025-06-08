Translation from Image
✅ Description
This project implements an OCR-based translation system that extracts English text from images and translates it into a user-selected target language.

Key Features:

Processes only English text.

Ignores non-English words.

Provides an intuitive GUI for:

Uploading images or videos.

Displaying extracted text.

Displaying translated output.

⚙️ Technologies Used
Python

Tkinter - GUI

Tesseract OCR via pytesseract

Googletrans (or alternative) for translation

OpenCV for video frame extraction (optional)

sklearn.metrics for accuracy calculation (Levenshtein distance)

🧠 How It Works
Image Upload: User uploads an image (or video frame).

OCR Processing: English text is extracted using Tesseract OCR.

Language Filter: Non-English words are skipped.

Translation: Extracted English words are translated into a target language.

Display: Both extracted and translated texts are shown on the GUI.

Evaluation: OCR accuracy is evaluated against a predefined ground truth using text similarity metrics.

🖥️ GUI Preview
Upload image button

Dropdown to select target language

"Extract and Translate" button

Text boxes to display:

Extracted text

Translated text

OCR accuracy

📥 How to Run
Install Dependencies:

bash
Copy
Edit
pip install pytesseract opencv-python googletrans==4.0.0-rc1 scikit-learn pillow
Ensure Tesseract OCR is Installed:

Download and install from Tesseract OCR
Update path in your script if necessary:

python
Copy
Edit
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
Run the Application:

bash
Copy
Edit
python gui_main.py
📊 Sample Output
plaintext
Copy
Edit
🖼️ Sample 1  
OCR Accuracy: 97.76%  

🖼️ Sample 2  
OCR Accuracy: 100.00%  

🖼️ Sample 3  
OCR Accuracy: 99.64%  

✅ Average OCR Accuracy across all samples: 99.13%
⚠️ Minimum accuracy requirement (70%) has been successfully met.

📂 Project Structure
graphql
Copy
Edit
task2/
├── gui_main.py                # Main GUI file
├── ocr_translator.py         # OCR and translation logic
├── sample_img.jpg            # Sample input image
├── sample_img2.jpg
├── sample_img3.jpg
├── README.md



