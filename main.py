import csv
from graphviz import Digraph

dot = Digraph()

with open('tree.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    family_tree_dict = {}
    for i, row in enumerate(reader):
        if i == 0:
            header = row
        else:
            data = row

            splitted_data = data[0].split(",")
            all_member_data = filter(lambda val: val !=  "null", splitted_data)
            name = all_member_data[0]
            parent_reference_id = all_member_data[1]
            children_reference_ids = all_member_data[2:]

            family_tree_dict[str(i+1)] = {
                "name": name,
                "parent_reference_id": parent_reference_id,
                "children_reference_ids": children_reference_ids
            }
            dot.node(name, name)

all_edges_ids_only = []
for member_id in family_tree_dict:
    for child_reference_id in family_tree_dict[member_id]["children_reference_ids"]:
        #print(member_id, child_reference_id, family_tree_dict[member_id]["children_reference_ids"])
        all_edges_ids_only.append((member_id, child_reference_id))


#child_edge_set.append(family_tree_dict[member_id]["name"] + family_tree_dict[child_reference_id]["name"])       
#dot.edges(child_edge_set)
#print(all_edges_ids_only)

#for key in family_tree_dict:
#   print(key, family_tree_dict[key])

for tup in all_edges_ids_only:
    print(str(tup[0]), str(tup[1]))
    dot.edge(family_tree_dict[str(tup[0])]["name"], family_tree_dict[str(tup[1])]["name"])
        
x = dot
x.view()
