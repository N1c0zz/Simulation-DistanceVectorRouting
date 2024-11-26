import copy
import time

# Inizializzazione delle tabelle di routing con la seguente
# logica:
# - Distanza verso sé stesso: 0
# - Distanza verso i vicini: costo del collegamento
# - Distanza verso tutti gli altri nodi: infinito
def initialize_routing_tables(network):

    routing_tables = {}
    for node in network:
        # Inizializza tutte le distanze a infinito
        routing_tables[node] = {n: float('inf') for n in network}
        routing_tables[node][node] = 0  # La distanza verso sé stesso è 0
        for neighbor, cost in network[node].items():
            routing_tables[node][neighbor] = cost  # Distanza verso i vicini
    return routing_tables

# Funzione per aggiornare le tabelle di routing.
# Aggiorna le tabelle di routing basandosi sulle
# informazioni ricevute dai vicini.
def update_routing_tables(network, routing_tables):
    updated = False  # Flag per verificare se ci sono stati cambiamenti
    new_tables = copy.deepcopy(routing_tables)  # Copia delle tabelle attuali

    for node in network:  # Per ogni nodo
        for neighbor, cost in network[node].items():  # Per ogni vicino
            for dest, distance in routing_tables[neighbor].items():
                # Calcola la distanza passando dal vicino
                if routing_tables[node][neighbor] != float('inf'):
                    new_distance = routing_tables[node][neighbor] + distance
                    # Se la nuova distanza è minore, aggiorna
                    if new_distance < new_tables[node][dest]:
                        new_tables[node][dest] = new_distance
                        updated = True  # Cambiamento rilevato

    return new_tables, updated

# Simulazione del Distance Vector Routing.
# Simula il Distance Vector Routing aggiornando iterativamente
# le tabelle di routing fino alla convergenza o al raggiungimento
# del numero massimo di iterazioni.
def simulate_distance_vector_routing(network, max_iterations=100):
    # Inizializza le tabelle di routing
    routing_tables = initialize_routing_tables(network)
    print("\nInizializzazione delle tabelle di routing:")
    print_routing_tables(routing_tables)

    # Iterazioni per l'aggiornamento delle tabelle
    for iteration in range(max_iterations):
        print(f"\nIterazione {iteration + 1}:")
        new_routing_tables, updated = update_routing_tables(network, routing_tables)
        print_routing_tables(new_routing_tables)

        if not updated:  # Se non ci sono cambiamenti, la convergenza è raggiunta
            print("\nConvergenza raggiunta")
            print("\nTabelle finali dopo la convergenza:")
            print_routing_tables(new_routing_tables)
            break

        routing_tables = new_routing_tables  # Aggiorna le tabelle per la prossima iterazione
        
        time.sleep(1)  # Sleep di 1 secondo tra le iterazioni
    else:
        print("\nMassimo numero di iterazioni raggiunto senza convergenza.")

    return routing_tables

# Stampa le tabelle di routing per ogni nodo.
def print_routing_tables(routing_tables):
    for node, table in routing_tables.items():
        print(f"Tabella di {node}: {table}")