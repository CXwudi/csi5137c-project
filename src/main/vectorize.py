import math

def tf_idf(word: str, tokens: list[str], documents: list[list[str]]) -> float:
    """Calculate the tf-idf score for a word in a document.

    Args:
        word (str): The word to calculate the tf-idf score for.
        tokens (list[str]): The list of tokens in the document.

    Returns:
        float: The tf-idf score for the word in the document.
    """
    tf = tokens.count(word) / len(tokens)
    idf = math.log(len(documents) / sum([1 for doc in documents if word in doc]))
    return tf * idf
