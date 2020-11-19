C = 100
D_max = 1000
units_per_level = D_max / C
b_cells = 13

def levels_to_units(l):
    return l * units_per_level

def units_to_levels(u):
    round(u / units_per_level)

def vertex_index(cluster, endpoint, level):
    return (cluster * 2 * C) + (endpoint * C) + level

def index_cluster(index):
    return index // (2 * C)

def index_endpoint(index):
    return (index // C) % 2

def index_level(index):
    return index % C

index = 0
for i in range(0, b_cells):
    for j in range(0, 2):
        for k in range(0, C):
            #create_node(index)
            index += 1
