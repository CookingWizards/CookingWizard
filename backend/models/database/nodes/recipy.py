from .node import Node

class Recipy(Node):

    def __init__(self, name: str, description: str, servings: int):
        super().__init__(name, 'recipy')
        self.name = name
        self.description = description
        self.servings = servings
        self.contents = {
            'uniquename': self.uniquename,
            'name': name,
            'description': description,
            'servings': servings
        }
