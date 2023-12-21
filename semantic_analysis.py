import static_variable as sv
class SemanticError(Exception):
    pass

class SymbolTable:
    def __init__(self):
        # Initialize an empty symbol table
        self.table = {}

    def insert(self, identifier, type):
        # Insert a new identifier with its type into the symbol table
        if identifier in self.table:
            # Handle re-declaration error
            raise SemanticError(f"Identifier '{identifier}' is already declared")
        else:
            self.table[identifier] = type
            

    def lookup(self, identifier):
        # Look up the type of an identifier in the symbol table
        if identifier in self.table:
            return self.table[identifier]
        else:
            # Handle undeclared identifier error
            raise SemanticError(f"Undeclared identifier '{identifier}'")

class ScopeManager:
    def __init__(self):
        # Initialize the scope manager with a global scope
        self.symbol_tables = [SymbolTable()]

    def enter_scope(self):
        # Create a new scope and add it to the scope stack
        self.symbol_tables.append(SymbolTable())

    def exit_scope(self):
        # Remove the top scope from the stack
        if len(self.symbol_tables) > 1:
            self.symbol_tables.pop()
        else:
            # Handle exiting global scope error
            raise SemanticError("Cannot exit global scope")

    def current_scope(self):
        # Return the top scope from the stack
        return self.symbol_tables[-1]

def semantic_analysis(ast):
    # Initialize the scope manager
    scope_manager = ScopeManager()

    # Recursive function for semantic analysis
    def analyze(node):
        if node == "variable_declaration":
            # Insert the variable into the symbol table
            scope_manager.current_scope().insert(node["identifier"], node["type"])

        elif node == "function_declaration":
            # Insert the function into the symbol table
            scope_manager.current_scope().insert(node["name"], node["return_type"])

            # Enter a new scope for the function body
            scope_manager.enter_scope()

            # Insert function parameters into the symbol table
            for param in node["parameters"]:
                scope_manager.current_scope().insert(param["name"], param["type"])

            # Analyze the function body
            for statement in node["body"]:
                analyze(statement)

            # Exit the function scope
            scope_manager.exit_scope()

        elif node == "identifier":
            # Check if the identifier is declared
            scope_manager.current_scope().lookup(node["name"])

        elif node == "binary_operation":
            # Recursively analyze the operands
            analyze(node["left"])
            analyze(node["right"])

            # Perform type checking and set the result type
            node["type"] = sv.type_check(node["left"]["type"], node["right"]["type"])

        # Add more cases based on the features of your language

    # Start the analysis with the root of the AST
    analyze(ast)

# Example
ast = {
    "type": "function_declaration",
    "name": "my_function",
    "return_type": "int",
    "parameters": [{"name": "param1", "type": "float"}],
    "body": [
        {"type": "variable_declaration", "identifier": "x", "type": "int"},
        {"type": "binary_operation", "left": {"type": "identifier", "name": "x"}, "right": {"type": "identifier", "name": "param1"}}
    ]
}

semantic_analysis(ast)
