from .relationship import Relationship

class Requires(Relationship):

    def __init__(self, fromNode, toNode, amount: int) -> None:
        super().__init__(fromNode, toNode, 'requires')
        self.tagName = 'amount'
        self.tagValue = amount
