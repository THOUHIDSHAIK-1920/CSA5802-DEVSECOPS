import networkx as nx
import random
import matplotlib.pyplot as plt

random.seed(1)

G = nx.erdos_renyi_graph(n=15, p=0.2, seed=1)
labels = {i: f"Host-{i}" for i in G.nodes()}
nx.set_node_attributes(G, labels, "name")

degree_centrality = nx.degree_centrality(G)
most_exposed = max(degree_centrality, key=degree_centrality.get)

print("----------------------------------")
print("Attack Surface Analysis")
print(f"Total Hosts: {G.number_of_nodes()}")
print(f"Total Connections: {G.number_of_edges()}")
print(f"Most Exposed Host: Host-{most_exposed} (Degree Centrality: {degree_centrality[most_exposed]:.2f})")

infected = {most_exposed}
infection_prob = 0.4
propagation_log = []

for round_num in range(1, 6):
    new_infections = set()
    for node in infected:
        for neighbor in G.neighbors(node):
            if neighbor not in infected and random.random() < infection_prob:
                new_infections.add(neighbor)
    infected.update(new_infections)
    propagation_log.append((round_num, len(infected)))
    print(f"Round {round_num}: Infected Hosts = {len(infected)}")

print("----------------------------------")

colors = ["red" if n in infected else "lightgreen" for n in G.nodes()]
nx.draw(G, with_labels=True, node_color=colors, node_size=500)
plt.title("Threat Propagation Result (Red = Infected)")
plt.savefig("threat_propagation.png")

print("Propagation graph saved as threat_propagation.png")
