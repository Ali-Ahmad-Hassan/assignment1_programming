import random

def simulate_non_aces_before_ace(num_simulations=100000):
    total_non_aces_before_first_ace = 0
    deck = ['A'] * 4 + ['NA'] * 48  # 'A' for Ace, 'NA' for Non-Ace

    for _ in range(num_simulations):
        random.shuffle(deck)  # Shuffle the deck
        non_aces_before_ace = 0
        for card in deck:
            if card == 'A':
                break  # Stop counting when the first ace is found
            non_aces_before_ace += 1
        total_non_aces_before_first_ace += non_aces_before_ace

    # Return the average (expected) number of non-aces before the first ace
    return total_non_aces_before_first_ace / num_simulations

# Run the simulation
expected_non_aces_before_ace = simulate_non_aces_before_ace()
print(f"Expected number of non-aces before the first ace: {expected_non_aces_before_ace:.2f}")
