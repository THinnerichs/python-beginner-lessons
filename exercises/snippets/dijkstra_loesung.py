
from math import inf

def dijkstra(vertices, edges, starting_point, target=None):

	# Anlegen der Dictonaries
	distances = {} # derzeit beste ermittelte Entfernungen
	p = {} # direkte Vorgänger auf dem derzeit besten Weg

	# Initialisere die Knoteninformationen
	for vertex in vertices:
		distances[vertex] = inf # Knoten sind am Anfang nicht erreichbar
		p[vertex] = None # keine bekannten Wege bedeutet keine Vorgänger

	# der Startknoten ist direkt erreichbar
	distances[starting_point] = 0
	reachable = [starting_point] 
	# reachable ist Liste von Knoten, die erreichbar, aber noch nicht besucht sind

	# solange noch (nicht besuchte) Knoten erreichbar sind
	while (len(reachable) > 0):
		# Bestimme den am kürzesten erreichbaren Knoten (von den noch zu betrachtenden Konten)
		shortest = inf
		current_vertex = None
		for vertex in reachable: # Betrachte jeden erreichbaren Knoten
			if distances[vertex] < shortest: # wenn der aktuelle Knoten einen kürzeren Weg hat, ...
				shortest = distances[vertex] # ... dann aktualisiere die kürzeste Entfernugn ...
				current_vertex = vertex # ... und merke dir den Knoten

		# Markiere (den gerade ermittelten) Knoten als besucht
		reachable.remove(current_vertex)

		# Aktualisere Knoteninformationen
		for vertex in vertices:
			# Wenn der Knoten auf kürzeren Weg erreichbar ist ...
			if distances[current_vertex] + edges.get((current_vertex, vertex), inf) < distances[vertex]:
				# ... dann aktualisiere den bisher besten Weg und die Vorgängerinformationen ...
				distances[vertex] = distances[current_vertex] + edges.get((current_vertex, vertex))
				p[vertex] = current_vertex
				# ... und wenn der Knoten nicht erreichbar war, dann markiere ihn als erreichbar
				if vertex not in reachable:
					reachable.append(vertex)
	
	# Wege bauen
	paths = {}
	for vertex in vertices:
		paths[vertex] = build_path(vertex, p)

	# falls dem Algorithmus ein Zielknoten übergeben wurde, gib das Ergebnis für diesen Knoten aus
	if target:
		print("{k} ist in {t} Zeiteinheiten erreichbar über: {s}".format(k=target, t=distances[target], s=paths[target]))

	return (paths, distances)



def build_path(vertex, p):
	prev = p.get(vertex, None)
	if prev is None:
		return []
	else:
		result = build_path(prev, p)
		result.append(prev)
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
	dijkstra(knoten, kanten, 1, 4)
	dijkstra(knoten, kanten, 1, 7)
