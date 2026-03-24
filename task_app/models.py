class User:
    def __init__(self, id, first_name, last_name, age) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Task:
    def __init__(self, id, name, user_id, description, completed) -> None:
        self.id = id
        self.name = name
        self.user_id = user_id
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
            "description": self.description,
            "completed": self.completed,
        }