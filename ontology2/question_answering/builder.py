from transformers import pipeline

classifier = pipeline(task='document-question-answering')