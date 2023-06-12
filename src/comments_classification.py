# MANAGE ENVIRONNEMENT
import tensorflow as tf
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification

# Loading tokenizer and classification model
tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")
model = TFAutoModelForSequenceClassification.\
    from_pretrained("bert-base-multilingual-cased")


def Bert_Classification(comments: list) -> list:

    results = []

    for comment in comments:
        # Tokenization
        input_ids = tokenizer(comment, add_special_tokens=True,
                              truncation=True, padding='max_length',
                              max_length=128, return_tensors='tf')

        # Sentiment prediction (Positive/Negative)
        outputs = model(input_ids)
        logits = outputs.logits
        probabilities = tf.nn.softmax(logits, axis=1)[0]
        sentiment_labels = ["Negative", "Positive"]
        predicted_sentiment = sentiment_labels[tf.argmax(probabilities).numpy()]

        results.append(predicted_sentiment)

    return results
