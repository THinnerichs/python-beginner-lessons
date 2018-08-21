
from math import inf

def dijkstra(vertices, edges, starting_point):
	pass


''' Die Funktion liefert für einen Knoten und die Vorgängerinformationen predecessors als Dictonary {Knoten:Vorgänger} eine Liste, die den Weg vom Startknoten zum Knoten Vertex beschreibt'''
def build_path(knoten, predecessors):
	pre = predecessors.get(knoten, None)
	if pre is None:
		return []
	else:
		result = build_path(pre, predecessors)
		result.append(pre)
		return result



if __name__ == '__main__':
	knoten = [i for i in range(1,8)]
	kanten = {(1,2):4, (1,3):1, (1,4):4,
				(2,4):3, (2,5):3,
				(3,4):2, (3,6):7,
				(4,2):2, (4,5):5, (4,6):1,
				(5,4):3, (5,7):2,
				(6,5):4, (6,7):3,
				(7,5):2}
	print(dijkstra(knoten, kanten, 1))
