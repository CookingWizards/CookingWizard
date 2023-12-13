from neo4j import GraphDatabase

from .example_data import nodes, relationships

class DbHandler:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def initDb(self):
        with self.driver.session() as session:
            # create example database contents for dev purposes
            session.run("MATCH(n) DETACH DELETE n")
            for key, node in nodes.items():
                self.addNode(node)
            for key, relationship in relationships.items():
                self.addRelationship(relationship)


    def addNode(self, node):
        with self.driver.session() as session:
            # add a node
            contents = ""
            for key, val in node.contents.items():
                contents+=key   
                contents+=f" : '{val}', "
            contents = contents[:-2]
            constraint = f"CREATE CONSTRAINT UNIQUE_NODENAME IF NOT EXISTS FOR (n:{node.type}) REQUIRE n.uniquename IS UNIQUE"
            create = f"CREATE ({node.uniquename}:{node.type} {{ {contents} }})"
            session.run(constraint)
            session.run(create)

    def addRelationship(self, relationship):
        with self.driver.session() as session:
            # add a relationship
            query = f"MATCH (from:{relationship.fromNode.type} {{uniquename:'{relationship.fromNode.uniquename}'}}), \
                    (to:{relationship.toNode.type} {{uniquename:'{relationship.toNode.uniquename}'}})\
                    CREATE ( (from)-[: {relationship.type} {{ {relationship.tagName}: {relationship.tagValue} }}]->(to) )"
            session.run(query)
