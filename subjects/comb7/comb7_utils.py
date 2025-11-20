from itertools import combinations
# from subjects.comb7.comb_7_list_wo_suit import do_comb7_with_fl_list
from subjects.comb5.comb5_simple import Comb5Simple

class Comb7Tools():
    
    def find_best_comb5(comb7_tuple:tuple[list[int], list[int]]) -> dict:
        all_comb7, fl_comb7 = comb7_tuple
        best_nn =-1
        best_name = ''
        best_str_key_5 = ''
        for curr_comb_5 in combinations(all_comb7,5):
            
            comb5 = Comb5Simple( rank_list = curr_comb_5,
                                flush_is = False)
            if comb5.comb_fig['nn'] > best_nn:
                    best_nn = comb5.comb_fig['nn']
                    best_name = comb5.comb_fig['name']
                    best_str_key_5 = comb5.str_key
        
        if fl_comb7 != []:
            for curr_comb_5 in combinations(fl_comb7,5):
                comb5 = Comb5Simple(rank_list = curr_comb_5,flush_is = True)
                if comb5.comb_fig['nn'] > best_nn:
                    best_nn = comb5.comb_fig['nn']
                    best_name = comb5.comb_fig['name']
                    best_str_key_5 = comb5.str_key
        return {
            'best_nn' :best_nn,
            'best_name': best_name,
            'str_key': best_str_key_5
        }             