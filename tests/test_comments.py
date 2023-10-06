from lib.comments import Comment

"""
Comment constructs with an id, title and conent
"""
def test_post_constructs():
    comment = Comment(1, "Test Content", "Test Name", "Post_id")
    assert comment.id == 1
    assert comment.content == "Test Content"
    assert comment.name == "Test Name"
    assert comment.post_id == "Post_id"

# # """
# # We can format artists to strings nicely
# # """
def test_comment_format_nicely():
    comment = Comment(1, "Test Content", "Test Name", "Post_id")
    assert str(comment) == "Comment(1, Test Content, Test Name, Post_id)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

# # """
# # We can compare two identical artists
# # And have them be equal
# # """
def test_posts_are_equal():
    comment1 = Comment(1, "Test Content", "Test Name", "Post_id")
    comment2 = Comment(1, "Test Content", "Test Name", "Post_id")
    assert comment1 == comment2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.