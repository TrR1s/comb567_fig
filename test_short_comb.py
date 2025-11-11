from subjects import Deck,DeckTools,CombRanks,CombRanksTool

deck = DeckTools.do_full_deck()


str_key = "3,8,9,9,14"

comb_rank = CombRanksTool.do_combrank_from_str_rank_key(str_key)
amount_comb = comb_rank.count_amount_in_deck(deck)
print(amount_comb)