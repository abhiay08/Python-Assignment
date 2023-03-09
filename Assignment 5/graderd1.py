# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 09:41:03 2023

@author: HP
"""

'''5.B.1: ASSIGNMENT
'''
# Assignment 5 que 1
import random

class Card:
    def __init__(self, suit, value):
            self.suit = suit
            self.value = value

    def __repr__(self):
         return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
          self.cards = []
          suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
          values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
          for suit in suits:
                 for value in values:
                        self.cards.append(Card(suit, value))

    def deal(self):
            if  len(self.cards) > 0:
                   return self.cards.pop()
            else:
                   return None

    def shuffle(self):
                if len(self.cards) < 52:
                    self.__init__()
                    random.shuffle(self.cards)
deck = Deck()
print(deck.deal()) # for example: 'A of Hearts'
deck.shuffle()
print(deck.deal()) # for example: '8 of Clubs'


#run

###################



# import random
#
# class card:
#     def __init__(self,suit,value):
#         self.suit=suit
#         self.value=value
#
#     def __repr__(self):
#         return f"{self.value} of {self.suit}"
#
# class deck:
#     def __init__(self):
#         self.cards=[]
#         suits=["hearts","diamonds","clubs","spades"]
#         values=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
#         for suit in suits:
#             for value in values:
#                 self.cards.append(card(suit, value))
#     def deal(self):
#         if len(self.cards)>0:
#             return self.cards.pop()
#         else:
#             return none
#
#     def shuffle(self):
#         if len(self.cards)<52:
#             self.__init__()
#         random.shuffle(self.cards)
#
# dec=deck()
# print(dec.deal())
# dec.shuffle()
# print(dec.deal)

############################check once again