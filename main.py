import json
from faker import Faker
import random

fake = Faker()

def random_text(max_chars):
    if max_chars < 5:
        return fake.word()[:max_chars]
    return fake.text(max_nb_chars=random.randint(5, max_chars)).strip()

def max_text(max_chars):
    if max_chars < 5:
        return fake.word()[:max_chars]
    text = fake.text(max_nb_chars=max_chars)
    while len(text) < max_chars:
        remaining = max_chars - len(text)
        if remaining < 5:
            text += " " + fake.word()[:remaining]
        else:
            text += " " + fake.text(max_nb_chars=remaining)
    return text[:max_chars].strip()

def generate_dummy_text(maximize_length=False):
    text_func = max_text if maximize_length else random_text
    
    company_description = text_func(1500)
    
    contact_sections = []
    for _ in range(random.randint(0, 3)):
        contact_sections.append(text_func(40))
    
    image_titles = []
    for _ in range(random.randint(1, 10)):
        image_titles.append(text_func(40))
    
    video_title = text_func(40) if random.choice([True, False]) else None
    
    document_titles = []
    for _ in range(random.randint(0, 2)):
        document_titles.append(text_func(40))
    
    return {
        "Company Description": company_description,
        "Contact Sections": contact_sections,
        "Image Titles": image_titles,
        "Video Title": video_title,
        "Document Titles": document_titles
    }

# Generate dummy text with randomized length
random_length_text = generate_dummy_text(maximize_length=False)

# Generate dummy text with maximized length
max_length_text = generate_dummy_text(maximize_length=True)

# Combine both results into a single JSON object
result = {
    "Randomized Length": random_length_text,
    "Maximized Length": max_length_text
}

# Output as JSON
print(json.dumps(result, indent=2))
