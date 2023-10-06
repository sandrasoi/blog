from lib.posts import Post
from lib.comments import Comment
from lib.posts_repository import PostRepository

def test_print_all_comments_from_one_post(db_connection):
    db_connection.seed('seeds/posts_directory.sql')
    recipe_repository = PostDirectory(db_connection)