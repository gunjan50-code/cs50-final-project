import re
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

# --- Load pre-trained NLP model ---
model_name = "dslim/bert-base-NER"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

# Create a Named Entity Recognition (NER) pipeline
ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

def detect_sensitive_info(text):
    """
    Detects sensitive info using both NLP and regex.
    Returns a dictionary of detected elements.
    """

    # --- 1️ NLP-based detection ---
    entities = ner_pipeline(text)
    sensitive = {
        "names": [],
        "organizations": [],
        "locations": [],
        "emails": [],
        "phones": []
    }

    for entity in entities:
        label = entity["entity_group"]
        word = entity["word"]

        if label == "PER" and word not in sensitive["names"]:
            sensitive["names"].append(word)
        elif label == "ORG" and word not in sensitive["organizations"]:
            sensitive["organizations"].append(word)
        elif label in ["LOC", "GPE"] and word not in sensitive["locations"]:
            sensitive["locations"].append(word)

    # --- 2️ Regex-based detection for emails and phones ---
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    phone_pattern = r'(\+?\d[\d\s-]{8,}\d)'

    sensitive["emails"] = list(set(re.findall(email_pattern, text)))
    sensitive["phones"] = list(set(re.findall(phone_pattern, text)))

    return sensitive
