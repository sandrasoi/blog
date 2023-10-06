class Comment:
    def __init__(self,id,content,name, post_id):
        self.id = id
        self.content = content
        self.name = name
        self.post_id = post_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Comment({self.id}, {self.content}, {self.name}, {self.post_id})"