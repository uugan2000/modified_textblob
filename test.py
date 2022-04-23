from textblob import TextBlob

blob = TextBlob("энэ бараа чанар муутай юм байна")
print(blob.translate(to="en"))
