import unittest
from unittest import TestCase
import pandas as pd
import praw
from get_reddit_post import get_post_from

class TestGetRedditPost(TestCase):
  def test_get_post_from(self):
    from get_reddit_refresh_token import get_token
    reddit = praw.Reddit(
      client_id="vhyGsaPnkmH5XDV5MwEJmg",
      client_secret="Qq9GYZ1nCMF8en3zuqsEryIg4-kqMw",
      user_agent="CSI5137C-Project-Agent",
      redirect_uri="http://localhost:51373",
    )
    refresh_token = get_token(reddit = reddit, local_port = 51373)
    df = get_post_from(reddit, "learnpython")
    print(df)

  # def test_df_poc(self):
  #   df = pd.DataFrame.from_dict({"no.Comments": ["asd"], "ups": [[4, 5, 6]], "title": ["asd"], "selftext": ["asd"], "comments": ["asd"]})
  #   print(df)
  #   df2 = pd.DataFrame(columns=["no.Comments", "ups", "title", "selftext", "comments"])
  #   print(df2)
  #   df3 = pd.concat([df2, df])
  #   print(df3)

if __name__ == "__main__":
  unittest.main()