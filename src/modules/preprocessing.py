from nltk import word_tokenize
import pandas as pd

def preprocessing_df(raw_dataset: pd.DataFrame) -> pd.DataFrame:
  """Preprocesses the raw dataset.

  Args:
      raw_dataset (pd.DataFrame): The raw dataset.

  Returns:
      pd.DataFrame: The preprocessed dataset.
  """
  core_part = raw_dataset.iloc[:, 0:10]
  comments = raw_dataset.iloc[:, 10:]
  reduced_dataset = core_part.copy(deep=True)
  reduced_dataset["comments"] = comments.apply(lambda x: list(x.dropna()), axis=1)
  # print(reduced_dataset)
  return reduced_dataset

def proprocessing_text(dataset: pd.DataFrame) -> pd.DataFrame:
  """Perform the preprocessing and tokenization of the text.

  Args:
      raw_dataset (pd.DataFrame): The raw dataset.

  Returns:
      pd.DataFrame: The tokenized preprocessed dataset.
  """
  return None # TODO

from spellchecker import SpellChecker
spell_checker = SpellChecker()
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import stopwords
english_stop_words = set(stopwords.words('english'))

def _core_preprocessing_and_tokenizing(text: str) -> list:
  """Preprocesses and tokenizes the text.

  Args:
      text (str): The text to preprocess and tokenize.

  Returns:
      list: The tokenized text.
  """
  t1 = text.strip().lower()
  token = word_tokenize(t1)
  # remove URLs
  # remove punctuation
  # remove other notations, emojis
  # do correction
  token2 = [spell_checker.correction(t) for t in token]
  # lemmaization
  token3 = _lemmaization(token2)
  # remove common words
  token4 = [t for t in token3 if t not in english_stop_words]

  final_token = token4
  return final_token


from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
lemmatizer = WordNetLemmatizer()

def _lemmaization(token: list[str]) -> list[str]:
  """Lemmatizes the token.

  Args:
      token (list[str]): The token to lemmatize.

  Returns:
      list[str]: The lemmatized token.
  """
  pos_tagged_token = pos_tag(token)
  lemmaized_token = [lemmatizer.lemmatize(t[0], pos=t[1]) for t in pos_tagged_token]
  return lemmaized_token