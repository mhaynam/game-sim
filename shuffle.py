#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 21:06:46 2023

@author: mhaynam
"""

import itertools
import matplotlib.pyplot as plt

def shuffle(cards, n): 
    mid = int(round(n/2))
    half_a = cards[0:mid]
    half_b = cards[mid:n]
    cards_i = []
    for i in range(mid):
        cards_i.append(half_a[i])
        cards_i.append(half_b[i])
    return cards_i

def count_shuffles(deck_size):
    cards = list(range(1, deck_size + 1))
    og_cards = cards[:]
    shuffle_n = 0
    while True:
        cards = shuffle(cards, deck_size)
        shuffle_n += 1
        if cards == og_cards:
            break
    return shuffle_n

def count_multiples(deck_size):
    return sum(1 for i in range(1, deck_size + 1) if deck_size % i == 0)

def count_factors(deck_size):
    return sum(1 for i in range(1, deck_size + 1) if deck_size % i == 0)

# Calculate shuffles and factors for even ranges from 1 to 2000
deck_sizes = range(2, 10001, 10)
shuffles_needed = [count_shuffles(deck_size) for deck_size in deck_sizes]
factors_count = [count_factors(deck_size) for deck_size in deck_sizes]

# Plot the results for shuffles
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(deck_sizes, shuffles_needed, marker='o')
plt.xlabel('Deck Size')
plt.ylabel('Number of Shuffles')
plt.title('Number of Shuffles to Return to Original Order')
plt.grid(True)

# Plot the results for factors
plt.subplot(1, 2, 2)
plt.scatter(deck_sizes, factors_count, marker='o')
plt.xlabel('Deck Size')
plt.ylabel('Number of Factors')
plt.title('Number of Factors for Each Deck Size')
plt.grid(True)

plt.tight_layout()
plt.show()



