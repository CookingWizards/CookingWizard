
class Recipy:

    def __init__(self, name: str, description: str, servings: int):
        self.type = 'recipy'
        self.uniquename = name
        self.name = name
        self.description = description
        self.servings = servings
        self.contents = {
            'uniquename': self.uniquename,
            'name': name,
            'description': description,
            'servings': servings
        }
