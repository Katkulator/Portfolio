class Comment:
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes


c = Comment("davey123", "lol you're so silly", 3)
c.username
c.text
c.likes
another_comment = Comment("rosa77", "sooo cutee")
