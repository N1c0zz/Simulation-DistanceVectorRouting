default_network = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 3, 'D': 1},
    'C': {'A': 5, 'B': 3, 'E': 7},
    'D': {'B': 1, 'E': 4, 'F': 8},
    'E': {'C': 7, 'D': 4, 'G': 2},
    'F': {'D': 8, 'G': 6, 'H': 3},
    'G': {'E': 2, 'F': 6, 'H': 1},
    'H': {'F': 3, 'G': 1}
}

# Funzione per acquisire la rete da input dell'utente.
# Permette all'utente di configurare manualmente una rete
# definendo nodi, connessioni e relativi costi.
def get_network_from_input():
    network = {}
    print("Configurazione manuale della rete...")

    # Numero di nodi della rete che si vuole inserire
    num_nodes = int(input("Inserire il numero di nodi nella rete:"))

    # Configurazione dei nodi e dei loro collegamenti
    for i in range(num_nodes):
        node = input(f"Inserisci il nome del nodo {i+1}: ")
        network[node] = {}
        print(f"Inserisci i collegamenti per il nodo {node}:")

        # Aggiunta dei collegamenti (destinazione e costo)
        while True:
            connection = input(f"Collegamenti per {node} (forma: Nodo destinazione,Costo) oppure 'fine' per terminare: ")
            if connection == "fine":
                break

            try:
                # Utilizzo la funzione split() sull'input per separare il nodo di destinazione
                # e il costo del collegamento nelle rispettive variabili
                dest, cost = connection.split(',')
                cost = int(cost)
                network[node][dest] = cost
                # Aggiungo anche il collegamento inverso (grafo non orientato)
                if dest not in network:
                    network[dest] = {}
                network[dest][node] = cost
            except ValueError:
                print("Errore nel formato del collegamento, riprova (es. 'B,1').")
    # Ritorno la rete completa da utilizzare
    return network

# Funzione per stampare la rete
# in un formato leggibile.
def print_network(network):
    print("\nRete attuale:")
    for node, connections in network.items():
        print(f"{node} -> {connections}")

# Funzione per chiedere all'utente quale rete usare.
# L'utente può scegliere se usare la rete predefinita
# oppure se inserire la propria personalizzata.
def choose_mode():

    print("Vuoi utilizzare una rete predefinita o inserire la tua rete?")
    choice = input("Scrivi 'predefinita' per usare la rete di default o 'personalizzata' per inserirne una tu: ").strip().lower()

    if choice == 'predefinita':
        print("\nUtilizzando la rete predefinita:")
        print_network(default_network)  # Stampa la rete predefinita
        return default_network
    elif choice == 'personalizzata':
        return get_network_from_input()
    else:
        print("Scelta non valida, usando la rete predefinita.")
        print_network(default_network)
        return default_network
