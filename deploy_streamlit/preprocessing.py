import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
# Set of English stopwords
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def lower_case(text):
    """Convert text to lowercase."""
    return text.lower()

def remove_stop_words(text):
    """Remove stop words from the text."""
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return " ".join(filtered_words)

def removing_numbers(text):
    """Remove numbers from the text."""
    return re.sub(r'\d+', '', text)

def removing_punctuations(text):
    """Remove punctuations from the text."""
    text = re.sub(r'[^\w\s]', '', text)
    return text

def removing_urls(text):
    """Remove URLs from the text."""
    return re.sub(r'https?://\S+|www\.\S+', '', text)

def lemmatization(text):
    """Lemmatize the text."""
    words = text.split()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    return " ".join(lemmatized_words)

def preprocess_text(text):
    """
    Apply all preprocessing steps to the input text.

    Parameters:
    text (str): The text to preprocess.

    Returns:
    str: The preprocessed text.
    """
    text = lower_case(text)
    text = remove_stop_words(text)
    text = removing_numbers(text)
    text = removing_punctuations(text)
    text = removing_urls(text)
    text = lemmatization(text)
    return text
