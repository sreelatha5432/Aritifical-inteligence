def is_valid_assignment(node, color, assignment, graph):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def map_coloring(countries, colors, graph):
    def backtrack(assignment):
        if len(assignment) == len(countries):
            return assignment
        
        node = None
        for country in countries:
            if country not in assignment:
                node = country
                break
        
        for color in colors:
            if is_valid_assignment(node, color, assignment, graph):
                assignment[node] = color
                result = backtrack(assignment)
                if result is not None:
                    return result
                del assignment[node]
        
        return None

    return backtrack({})

graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW']
}

countries = list(graph.keys())

colors = ['Red', 'Green', 'Blue']

assignment = map_coloring(countries, colors, graph)

if assignment is not None:
    print("Map Coloring Solution:")
    for country, color in assignment.items():
        print(f"{country}: {color}")
else:
    print("No solution found.")
