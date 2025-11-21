from subjects import Comb7Tools
from subjects import Deck,DeckTools
deck = DeckTools.do_full_deck()

comb7_tuple = ([10, 10, 10, 11, 12, 13, 14], [10, 11, 12, 13, 14])
print(Comb7Tools.find_best_comb5(comb7_tuple))
print(Comb7Tools.do_str_key(comb7_tuple))

print(Comb7Tools.count_amount_in_deck(comb7_tuple,deck))