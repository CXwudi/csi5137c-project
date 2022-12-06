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
    print(reduced_dataset)
    return reduced_dataset
    