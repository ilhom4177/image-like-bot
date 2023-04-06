from tinydb import TinyDB
from tinydb.database import Document

class LikeDB:
    def __init__(self, file_path):
        # Initialize the database
        self.db = TinyDB(file_path, indent=4)

    def add_student(self, user_id):
        """
        Add student in Database
        """
        cond = self.db.contains(doc_id=user_id)
        if not cond:
            document = Document({"like":0, "dislike":0}, doc_id=user_id)
            self.db.insert(document)
            return {"status": "Added student"}
        else:
            return {"status": "Already exist"}
    
    def all_likes(self):
        """
        Count all users likes
        """
        data = self.db.all()
        count = 0

        for i in data:
            count += i['like']
        return count

    def all_dislikes(self):
        """
        Count all users dislikes
        """
        data = self.db.all()
        count = 0

        for i in data:
            count += i['dislike']
        return count

    def add_like(self, user_id:int):
        """
        Add like to the database
        
        Args:
            user_id (str): telegram user id
        Returns:
            The number of likes and dislikes for the post
        """
        data = self.db.get(doc_id=user_id)

        like = data.get("like")

        if like == 1:
            data["like"] = 0
        elif like == 0:
            data["like"] = 1
            data["dislike"] = 0
        self.db.update(data, doc_ids=[user_id])



    def add_dislike(self, user_id:int):
        """
        Add dislike to the database
        
        Args:
            user_id (str): telegram user id
        Returns:
            The number of likes and dislikes for the post
        """
        
        data = self.db.get(doc_id=user_id)

        dislike = data.get("dislike")

        if dislike == 1:
            data["dislike"] = 0
        elif dislike == 0:
            data["dislike"] = 1
            data["like"] = 0
        self.db.update(data, doc_ids=[user_id])
