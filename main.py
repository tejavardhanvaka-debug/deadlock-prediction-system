# Deadlock Prediction Project
# Step 1 update
# step 2 update
# step 3 update 
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

n = int(input("Enter number of processes: "))

for i in range(n):
    p = input(f"Enter process {i+1} name: ")
    G.add_node(p)

m = int(input("Enter number of waiting relations: "))

for i in range(m):
    p1 = input("Process waiting: ")
    p2 = input("Waiting for process: ")
    G.add_edge(p1, p2)

try:
    cycle = nx.find_cycle(G)
    print("🔴 Deadlock detected:", cycle)
except:
    print("🟢 No deadlock")

edge_count = len(G.edges())
node_count = len(G.nodes())

if edge_count >= node_count:
    print("⚠️ High risk of deadlock!")
elif edge_count >= node_count - 1:
    print("⚠️ Medium risk of deadlock!")
else:
    print("✅ Low risk")

plt.figure()
pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, node_size=2000, font_size=10)
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20)

plt.title("Process Wait-For Graph")
plt.show()
