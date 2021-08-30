import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
G.add_node('a')
G.add_nodes_from(['b','c','d','e'])
G.add_edge("a","b")
edge=("b","c")

G.add_edge(*edge)
G.add_edges_from([("a","e"),("e","d"),("e","c")])

options={
    'with_labels': True,
    'font_weight' : 'bold',
    'node_color': 'red',
    'edge_color' : 'green',
    'node_size' : 500,
    'width' : 7
}

G.add_node('g')
G.add_edge('g','a')
G.add_edge('g','c')

def degree_centrality(g,node):
    if(not g.has_node(node)):
        return ''
    v=g.number_of_nodes()
    return g.degree(node) / (v-1)

print('degree centrality of a is:', degree_centrality(G,'a'))
print('degree centrality of B is:', degree_centrality(G,'b'))
print('degree centrality of c is:', degree_centrality(G,'c'))
print('degree centrality of d is:', degree_centrality(G,'d'))
print('degree centrality of e is:', degree_centrality(G,'e'))
print('degree centrality of g is:', degree_centrality(G,'g'))

print(nx.degree_centrality(G))


def closeness_centrality(g,node):
    if (not g.has_node(node)):
        return ''
    v=g.number_of_nodes()
    ls=list(g.nodes())
    ls.remove(node)
    sum=0
    for n in ls:
        d=len(nx.shortest_path(g,node,n)) -1
        sum=sum+d
    return (v-1) / sum


print('closeness centrality of c',closeness_centrality(G,'c'))
print(nx.closeness_centrality(G))
def num_of_shortest_path(g,node1,node2):
    s_distance=len(nx.shortest_path(g,node1,node2))-1
    count=0
    all_paths=nx.all_simple_paths(g,node1,node2)
    for path in all_paths:
        if len(path)-1==s_distance:
            count=count+1

    return count

def num_of_shortest_path_i(g,node1,node2,i):
    if not g.has_node(node1) or not g.has_node(node2) or not g.has_node(node1):
        return ''
    s_distance = len(nx.shortest_path(g, node1, node2)) - 1
    count = 0
    all_paths = nx.all_simple_paths(g, node1, node2)
    for path in all_paths:
        if len(path) - 1 == s_distance and i in path:
            count=count+1

    return count

def betweenness_centrality(g,node):
    if not g.has_node(node):
        return ''
    all_nodes=list(g.nodes())
    all_nodes.remove(node)
    ratio_sum=0
    added_pairs=[]
    reverse_equal=False
    for i in all_nodes:
        for j in all_nodes:
            reverse_equal=False
            for t in added_pairs:
                new_tup = t[::-1]
                if (i,j)==new_tup:
                    reverse_equal=True
            if reverse_equal or i==j:
                continue
            added_pairs.append((i,j))

            i_total_path=num_of_shortest_path(g,i,j)
            i_cut_path=num_of_shortest_path_i(g,i,j,node)

            i_ratio=i_cut_path/i_total_path
            ratio_sum=ratio_sum + i_ratio

    neigh_combination=((g.number_of_nodes() -1) *(g.number_of_nodes() -2))/ 2
    return ratio_sum / neigh_combination

print('betweeness of a:',betweenness_centrality(G,'a'))
print('betweeness of b:',betweenness_centrality(G,'b'))
print('betweeness of c:',betweenness_centrality(G,'c'))
print('betweeness of d:',betweenness_centrality(G,'d'))
print('betweeness of e:',betweenness_centrality(G,'e'))
print('betweeness of g:',betweenness_centrality(G,'g'))
print(nx.betweenness_centrality(G))










