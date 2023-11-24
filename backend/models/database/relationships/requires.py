
class Requires:

    def __init__(self, fromNode, toNode, amount: int) -> None:
        self.type = 'requires'
        self.fromNode = fromNode
        self.toNode = toNode
        self.tagName = 'amount'
        self.tagValue = amount
