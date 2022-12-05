import math

def tf_idf(documents: list[list[str]]) -> list[list[float]]:
    """Calculate the tf-idf scores for all words in all documents.

    Args:
        documents (list[list[str]]): The list of documents.

    Returns:
        list[list[float]]: The tf-idf scores for all words in all documents.
    """
    return [[tf_idf_core(word, tokens, documents) for word in tokens] for tokens in documents]

def tf_idf_core(word: str, tokens: list[str], documents: list[list[str]]) -> float:
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
