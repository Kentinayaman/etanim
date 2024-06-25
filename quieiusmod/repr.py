from transformers import AutoTokenizer

# Load the tokenizer for the specific model
tokenizer = AutoTokenizer.from_pretrained(model)

# Tokenize and encode the input text
encoded_input = tokenizer("square", return_tensors="pt").input_ids
