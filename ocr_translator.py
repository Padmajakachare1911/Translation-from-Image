#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install -r requirements.txt')


# In[7]:


import cv2
import pytesseract
from PIL import Image
from googletrans import Translator
from difflib import SequenceMatcher
import string

# -------- TEXT EXTRACTION -------- #
def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not read image {image_path}")
        return ""

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    processed = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    text = pytesseract.image_to_string(processed, lang='eng')
    return text

# -------- TRANSLATION -------- #
def translate_english_text(text, dest_lang='hi'):
    translator = Translator()
    try:
        translated = translator.translate(text, dest=dest_lang)
        return translated.text
    except Exception as e:
        return f"Translation error: {e}"

# -------- CLEAN TEXT FOR ACCURACY -------- #
def clean_text(text):
    return text.strip().lower().translate(str.maketrans('', '', string.punctuation))

# -------- ACCURACY MEASUREMENT -------- #
def calculate_ocr_accuracy(gt_text, predicted_text):
    gt = clean_text(gt_text)
    pred = clean_text(predicted_text)
    if not gt or not pred:
        return 0.0
    return SequenceMatcher(None, gt, pred).ratio() * 100


# In[ ]:




