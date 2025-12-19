
The application uses a pre-trained transformer model from Hugging Face for sentiment analysis. These models are based on deep learning architectures like BERT and DistilBERT, trained on large datasets to understand natural language and classify sentiment as positive or negative.

The models are pre-trained on datasets from HuggingFace as well as the model. The dataset used for this app is the Stanford Sentiment Treebank (SST-2). These datasets contain labeled text data used to fine-tune the models for sentiment classification tasks.

I selected the distilbert-base-uncased-finetuned-sst-2-english model for its efficiency and accuracy. I built a simple application that takes user input, processes it through the model, and displays the sentiment classification result. The app was developed using Python and the Hugging Face transformers pipeline, integrated into a user-friendly interface.

