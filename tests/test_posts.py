from lib.posts import Post

"""
Artist constructs with an id, title and conent
"""
def test_post_constructs():
    post = Post(1, "Test Title", "Test Content")
    assert post.id == 1
    assert post.title == "Test Title"
    assert post.content == "Test Content"

# """
# We can format artists to strings nicely
# """
def test_post_format_nicely():
    post = Post(1, "Test Title", "Test Content")
    assert str(post) == "Post(1, Test Title, Test Content)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

# """
# We can compare two identical artists
# And have them be equal
# """
def test_posts_are_equal():
    post1 = Post(1, "Test Title", "Test Content")
    post2 = Post(1, "Test Title", "Test Content")
    assert post1 == post2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.