# Emotion Recognition API
This repository provides a FastAPI-based service for emotion recognition from text input using a pre-trained model.

## Description
Recognizing emotions is essential for effective communication, adding depth and meaning to our interactions. 
In the digital age, emotions expressed in product reviews significantly influence customers' buying decisions. Thus, identifying these emotions is crucial for businesses to understand customer sentiments and enhance their products and services.

### Output
I intend to create an emotion recognition system that categorizes each customers’ reviews to its emotion sentiment, 
so the input will be the text of product review and the model will recognize its emotion label and give the output of highest score of predicted emotion of that review. 
The system will be presented in an intuitive user interface that takes an input from a form and show its output below it

## Requirements for Data
To use the emotion recognition API, your input should consist of short text strings that represent product reviews or any other form of text where emotions are expressed.

## Project Architecture

## Expected Input Payload
The API expects a JSON payload in the following format:
```
{
  "text": "Your input text goes here"
}
```

## Response Format
```
{
  "label": score,
}
```

## Dataset
[PRDECT-ID](https://data.mendeley.com/datasets/574v66hf2v/1) 
it is a compilation of Indonesian product reviews that come with emotion and sentiment labels. These reviews were gathered from one of Indonesia's largest e-commerce platforms, Tokopedia. 
I focused on simplifying the dataset by narrowing it down to just customer review texts and their corresponding emotion labels for model development.

## Further Improvements
* trained the same dataset to other pretrained indonesian language models
* streamline the inference service to a real ecommerce as part of its feature
* hyperparameter tuning & cross validation to increase model performance
* train the model from scratch

## References
* https://medium.com/@ahmettsdmr1312/fine-tuning-distilbert-for-emotion-classification-84a4e038e90e 
* https://www.kaggle.com/code/sudalairajkumar/getting-started-with-text-preprocessing
* https://www.kaggle.com/code/mohamedabdelmohsen/emotion-analysis-and-classification-using-lstm-93
* https://www.kaggle.com/code/pashupatigupta/starter-notebook-a-to-z-emotion-detection
* https://huggingface.co/learn/nlp-course/
* https://www.kaggle.com/code/jhoward/getting-started-with-nlp-for-absolute-beginners 
