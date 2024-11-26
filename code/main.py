from network_input import choose_mode
from routing import simulate_distance_vector_routing

if __name__ == "__main__":
    # Scegli la rete
    network = choose_mode()
    # Avvia la simulazione
    simulate_distance_vector_routing(network)