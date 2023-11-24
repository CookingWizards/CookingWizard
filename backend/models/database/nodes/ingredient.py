from .node import Node

class Ingredient(Node):

    def __init__(self, name: str, unit: str, is_partitionable: bool):
        super().__init__(f'{name}_{unit}', 'ingredient')
        self.name = name
        self.unit = unit
        self.is_paritionable = is_partitionable
        self.contents = {
            'uniquename': self.uniquename,
            'name': name,
            'unit': unit,
            'is_partionable': is_partitionable
        }
