import pandas as pd
from subjects import Comb7Tools,do_comb7_with_fl_list
from subjects import Deck,DeckTools
deck = DeckTools.do_full_deck()

comb7_tuple = ([8,9,10,11,12,13,14], [])
# comb7_tuple = ([10, 10, 10, 11, 12, 13, 14], [10, 11, 12, 13, 14])  
print(Comb7Tools.find_best_comb5(comb7_tuple))
print(Comb7Tools.do_str_key(comb7_tuple))

print(Comb7Tools.count_amount_in_deck(comb7_tuple,deck))

comb_7_tuple_list = do_comb7_with_fl_list()
comb7_dict_list =[]
total_amount = 0
for curr_comb7_tuple in comb_7_tuple_list[:5]:
    print(0,curr_comb7_tuple)
    str7_key = Comb7Tools.do_str_key(curr_comb7_tuple)
    print(1,curr_comb7_tuple)
    curr_comb5_info = Comb7Tools.find_best_comb5(curr_comb7_tuple)
    print(2,curr_comb7_tuple)
    curr_am= Comb7Tools.count_amount_in_deck(curr_comb7_tuple,deck)
    print(3,curr_comb7_tuple)
    # best_nn=curr_comb5_info['best_nn']
    # best_name= curr_comb5_info['best_name']
    # str_key= curr_comb5_info['str_key']
    # curr_comb7_dict = {

    #         'str7_key': str7_key,
    #         'best_nn' :best_nn,
    #         'best_name': best_name,
    #         'str_key': str_key,
    #         # 'amount': curr_am
    #     }  
    # # total_amount += Comb7Tools.count_amount_in_deck(curr_comb7_tuple,deck)
    # comb7_dict_list.append(curr_comb7_dict.copy())
# print(total_amount)
# comb7_df = pd.DataFrame(comb7_dict_list)
# comb7_df.to_csv('comb7_df.csv')