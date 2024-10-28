# import PyPDF2
# import pandas as pd

# # Create an empty list to store the extracted text
# extracted_text = []

# # Open the PDF file in read-binary mode
# with open('tab.pdf', 'rb') as pdf_file:
#     reader = PyPDF2.PdfReader(pdf_file)
#     num_pages = len(reader.pages)

#     # Iterate through each page and extract text
#     for page_num in range(num_pages):
#         page = reader.pages[page_num]
#         text = page.extract_text()
#         extracted_text.append(text)

# # Create a DataFrame from the extracted text
# df = pd.DataFrame({'Text': extracted_text})

# # Print the DataFrame
# print(df)


# import PyPDF2
# import pandas as pd


# extracted_text = []


# with open('tab.pdf', 'rb') as pdf_file:
#     reader = PyPDF2.PdfReader(pdf_file)
#     num_pages = len(reader.pages)

   
#     for page_num in range(num_pages):
#         page = reader.pages[page_num]
#         text = page.extract_text()
#         extracted_text.append(text)

# df = pd.DataFrame({'Text': extracted_text})


# output_file = 'extracted_text.json'

# df.to_json(output_file, orient='records', lines=True)

# df.head

# print(f'DataFrame saved as {output_file}')

import PyPDF2
import pandas as pd
import re

# Create an empty list to store the extracted text
extracted_text = []

# Define a function to clean the text by removing special characters and newline characters
def clean_text(text):
    text = re.sub(r'[^A-Za-z0-9\s.]', '', text)  # Remove special characters
    text = text.replace('\n', ' ')  # Replace newline characters with spaces
    text = re.sub(r'\.{2,}', '.', text)
    text = re.sub(r'\s{2,}', ' ', text)
    return text

# Open the PDF file in read-binary mode
with open('tab.pdf', 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    num_pages = len(reader.pages)

    # Iterate through each page and extract text
    for page_num in range(num_pages):
        page = reader.pages[page_num]
        text = page.extract_text()
        cleaned_text = clean_text(text)
        extracted_text.append(cleaned_text)

# Create a DataFrame from the cleaned text
df = pd.DataFrame({'Text': extracted_text})

# Define the file name for the output JSON file
output_file = 'extracted_text.json'

# Save the DataFrame as a JSON file
df.to_json(output_file, orient='records', lines=True)

print(f'DataFrame saved as {output_file}')

