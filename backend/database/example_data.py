from ..models.database.nodes.ingredient import Ingredient 
from ..models.database.nodes.recipy import Recipy 
from ..models.database.relationships.requires import Requires

tea = Recipy('tea', 'put in hot water', 1)
teabag = Ingredient('teabag', 'bag', False)
nodes = {
    'tea': tea,
    'teabag': teabag,
    'water': Ingredient('water', 'glass', True),
}

relationships = {
    'requires': Requires(tea, teabag, 1)
}