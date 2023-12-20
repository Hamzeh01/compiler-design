# Extend the AST nodes to include type information
class BinaryOpNode:
    def __init__(self, op, left, right, type=None):
        self.op = op
        self.left = left
        self.right = right
        self.type = type

class IdentifierNode:
    def __init__(self, name, type=None):
        self.name = name
        self.type = type

# Type checking function
def type_check(node):
    if isinstance(node, BinaryOpNode):
        # Recursive type checking for binary operations
        type_check(node.left)
        type_check(node.right)

        # Check type compatibility
        if node.left.type != node.right.type:
            raise TypeError(f"Type mismatch in {node.op} operation: {node.left.type} vs {node.right.type}")

        # Set the type of the binary operation node
        node.type = node.left.type

    elif isinstance(node, IdentifierNode):
        # Check if the identifier has a declared type
        if not node.type:
            raise TypeError(f"Undeclared type for identifier '{node.name}'")

# Example usage
ast = BinaryOpNode('+', IdentifierNode('a', 'int'), IdentifierNode('b', 'int'))
type_check(ast)
