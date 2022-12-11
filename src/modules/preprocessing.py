import string
from nltk import word_tokenize
import pandas as pd
import re

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
  reduced_dataset["comments"] = comments.agg(lambda x: list(x.dropna()), axis=1)
  # print(reduced_dataset)
  return reduced_dataset

def proprocessing_text(dataset: pd.DataFrame) -> pd.DataFrame:
  """Perform the preprocessing and tokenization of the text.

  Args:
      raw_dataset (pd.DataFrame): The raw dataset.

  Returns:
      pd.DataFrame: The tokenized preprocessed dataset.
  """
  dataset["title"] = dataset["title"].apply(_core_preprocessing_and_tokenizing)
  dataset["selftext"] = dataset["selftext"].apply(_core_preprocessing_and_tokenizing)
  dataset["comments"] = dataset["comments"].apply(lambda x: [_core_preprocessing_and_tokenizing(c) for c in x])
  return dataset


import nltk
import math
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import stopwords
english_stop_words = set(stopwords.words('english'))
url_pattern = re.compile(r'https?://\S+|www\.\S+')
import emoji
from nltk.tokenize import RegexpTokenizer
only_words_tokenizer = RegexpTokenizer(r"\w+")


def _core_preprocessing_and_tokenizing(text: str | float) -> list:
  """Preprocesses and tokenizes the text.
  DO NOT modify the order of each preprocessing step.

  Args:
      text (str): The text to preprocess and tokenize.

  Returns:
      list: The tokenized text.
  """
  text = str(text) # convert to float
  # print(text)
  t1 = text.strip().lower()
  if (t1 is None or t1 == "" or t1.lower() == "nan"):
    return []
  # remove URLs
  t2 = url_pattern.sub(r'', t1)
  # remove emojis
  t3 = emoji.replace_emoji(t2, "")
  # tokenize
  token2 = word_tokenize(t3)
  # do correction
  token3 = [_spell_correction(t) for t in token2]
  # lemmaization
  token4 = _lemmaization(token3)
  # remove punctuation
  token5 = [t for t in token4 if t not in string.punctuation]
  # remove other notations
  token6 = only_words_tokenizer.tokenize(" ".join(token5))
  # remove common words
  token7 = [t for t in token6 if t not in english_stop_words]

  final_token = token7
  return final_token

spell_correction_cache = {}
from spellchecker import SpellChecker
spell_checker = SpellChecker()

def _spell_correction(word: str) -> str:
  """Corrects the spelling of the word.

  Args:
      word (str): The word to correct.

  Returns:
      str: The corrected word.
  """
  if (word in spell_correction_cache):
    return spell_correction_cache[word]
  else:
    corr_opt = spell_checker.correction(word)
    corr = word if (corr_opt is None) else corr_opt
    spell_correction_cache[word] = corr
    return corr

from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
lemmatizer = WordNetLemmatizer()
only_words_pattern = re.compile(r"\w+")

def _lemmaization(token: list[str]) -> list[str]:
  """Lemmatizes the token.

  Args:
      token (list[str]): The token to lemmatize.

  Returns:
      list[str]: The lemmatized token.
  """
  pos_tagged_token = pos_tag(token)
#   print(pos_tagged_token)
  lemmaized_token=[]
  for t in pos_tagged_token:
    if t[1].startswith('NN'):
      lemmaized_token.append(lemmatizer.lemmatize(t[0], pos='n'))
    elif t[1].startswith('VB'):
      lemmaized_token.append(lemmatizer.lemmatize(t[0], pos='v'))
    elif t[1].startswith('JJ'):
      lemmaized_token.append(lemmatizer.lemmatize(t[0], pos='a'))
    elif t[1].startswith('R'):
      lemmaized_token.append(lemmatizer.lemmatize(t[0], pos='r'))
    elif only_words_pattern.match(t[0]):
      lemmaized_token.append(lemmatizer.lemmatize(t[0]))
    else:
      lemmaized_token.append(t[0])
  return lemmaized_token