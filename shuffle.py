#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 21:06:46 2023

@author: mhaynam
"""

import itertools

class_ = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
suits = ['heart','diamond','spade','club']
cards = list(itertools.product(suits, class_))
# cards = list(range(1, 5, 1))
og_cards = cards

cards_n = len(cards)

# print(cards)

def shuffle(n): 
    mid = int(round(n/2))
    half_a = cards[0:mid]
    half_b = cards[mid:n]
    cards_i = []
    for i in range(mid):
        cards_i.append(half_a[i])
        cards_i.append(half_b[i])
    # print(cards_i)
    return cards_i
    
shuffle_n = 0
deck_n = cards_n
while og_cards != shuffle(deck_n):
    shuffle_n = shuffle_n + 1
    print(cards)
    cards = shuffle(deck_n)
print(cards)
shuffle_n = shuffle_n + 1
print(shuffle(deck_n))
print('Shuffles: ' + str(shuffle_n))
    

        
    




