#!/usr/bin/python3

def isWinner(x, nums):
    # Step 1: Precompute primes up to the largest
    max_n = max(nums)
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(max_n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    # Function to simulate a single game round
    def simulate_game(n):
        # Create a set of numbers from 1 to n
        available = [True] * (n + 1)

        # Turn tracking: True for Maria's turn, False for Ben's turn
        turn = True  # Maria goes first

        while True:
            # Find the smallest prime available
            for i in range(2, n + 1):
                if primes[i] and available[i]:
                    prime = i
                    break
            else:
                # No primes left, current player loses
                return "Ben" if turn else "Maria"

            # Remove the prime and its multiples
            for i in range(prime, n + 1, prime):
                available[i] = False

            # Switch turns
            turn = not turn

    # Step 2: Simulate all rounds and count wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = simulate_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    # Step 3: Return the player with the most wins, or None if it's a tie
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
