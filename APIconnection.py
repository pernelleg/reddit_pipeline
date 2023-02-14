import praw

reddit = praw.Reddit(
    client_id="E9XxQJStijJyVNog9WSLmA",
    client_secret="lcv3DwUvS2eINl752ylgCLTGUyZhmg",
    password="Sevenoaks01",
    user_agent="test-pipeline by u/Limp-Conclusion-9328",
    username="Limp-Conclusion-9328",
)

url = "https://www.reddit.com/r/funny/comments/3g1jfi/buttons/"
submission = reddit.submission(url=url)

for top_level_comment in submission.comments:
    print(top_level_comment.body)
