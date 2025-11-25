import pickle
import tensorflow as tf
import sys

# Patch to load old Keras Tokenizer
from tensorflow.keras.preprocessing.text import Tokenizer
sys.modules['keras.preprocessing.text'] = sys.modules['tensorflow.keras.preprocessing.text']

print("\n===== LOADING MODEL =====")
model = tf.keras.models.load_model("model_9.h5", compile=False)
print("Model loaded successfully.\n")

print("===== MODEL SUMMARY =====")
model.summary()

print("\n===== LOADING TOKENIZER =====")
with open("tokens.pkl", "rb") as f:
    tokenizer = pickle.load(f)

print("Tokenizer loaded.")
print("Vocabulary size:", len(tokenizer.word_index))

print("\nFirst 40 tokens:")
for i, (word, idx) in enumerate(tokenizer.word_index.items()):
    if i >= 40:
        break
    print(idx, word)
