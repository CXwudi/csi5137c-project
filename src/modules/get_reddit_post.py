import pandas as pd
import praw
import random

def get_post_from(reddit: praw.Reddit, subreddit: str, amount: int = 10, total: int = 100) -> pd.DataFrame:
  """Get the posts from a subreddit.

  Args:
      reddit (praw.Reddit): The reddit instance.
      subreddit (str): The subreddit to get the posts from.
      amount (int, optional): The amount of posts to get. Defaults to 10.
      total (int, optional): The total amount of posts to get. Defaults to 100.

  Returns:
      pd.DataFrame: The posts.
  """
  subreddit = reddit.subreddit(subreddit)
  posts = []
  for post in subreddit.top(limit=total):
    posts.append(post)
  random.shuffle(posts)
  chosen_posts = posts[:amount]
  df = pd.DataFrame(columns=["no.Comments", "ups", "title", "selftext", "comments"])
  for post in chosen_posts:
    comments = [str(c.body) for c in post.comments]
    # print(post)
    # print(comments)
    df = pd.concat([df, pd.DataFrame.from_dict({
      "no.Comments": [post.num_comments],
      "ups": [post.score],
      "title": [post.title],
      "selftext": [post.selftext],
      "comments": [comments]
    })])
  return df
