import networkx as nx
import matplotlib.pyplot as plt
import json


with open('inode.json') as json_data:   # Reads json file and saves the data in d
    d = json.load(json_data)

G = nx.Graph(d)   # Converts the data in d into the networkx graph

#nx.draw(G)

#pos = nx.spring_layout(G)
#pos = nx.random_layout(G)
pos = nx.shell_layout(G)
#pos = nx.spectral_layout(G)

nx.draw_networkx(G, pos)
plt.show()
