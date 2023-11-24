
class Ingredient:

    def __init__(self, name: str, unit: str, is_partitionable: bool):
        self.type = 'ingredient'
        self.uniquename = f'{name}_{unit}'
        self.name = name
        self.unit = unit
        self.is_paritionable = is_partitionable
        self.contents = {
            'uniquename': self.uniquename,
            'name': name,
            'unit': unit,
            'is_partionable': is_partitionable
        }