import numpy as np
import math
from itertools import combinations
# from subjects.comb7.comb_7_list_wo_suit import do_comb7_with_fl_list
from subjects.comb5.comb5_simple import Comb5Simple
from subjects import Deck

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
    
    def do_str_key(comb7_tuple:tuple[list[int], list[int]]) -> str:
        rank_list, flush_list = comb7_tuple
        rank_list_str = ','.join(map(str, sorted(rank_list)))
        flush_str = 'unfl'
        if flush_list != []:
            flush_str = ','.join(map(str, sorted(flush_list)))
        
        return f'{rank_list_str}_{flush_str}'
    
    def count_amount_in_deck(comb7_tuple:tuple[list[int], list[int]],deck: Deck) -> int:
        
        
        
        
        rank_list =comb7_tuple[0][:]
        flush_list =comb7_tuple[1][:]
        
        rank_list_np = np.array(rank_list)
        rank_flat, _ = np.unique(rank_list_np, return_counts=True)
        rank_flat -=2
        
        if  flush_list: 
            for curr_fl_card in flush_list:
                rank_list.remove(curr_fl_card) 
        
        
        # count flash amount
        flush_am = 0
        flush_list = np.array(flush_list)
        flush_list -=2
        
        
        for suit_i in range(4):
            fl_can = True
            for curr_rank in flush_list:
                if deck.suits_0_1[suit_i][curr_rank] == 0:
                    fl_can = False
                    break
            if fl_can:
                flush_am +=1
                    
        rank_amount_wo_flset = deck.rank_amount[:]
        
        if flush_list.size > 0:
            if flush_am == 0 : return 0
        else:
            flush_am = 1
        
        for curr_rank in flush_list:
            rank_amount_wo_flset[curr_rank] -=1
        
        
        rank_list_np = np.array(rank_list)
        rank, freq = np.unique(rank_list_np, return_counts=True)
        rank -=2
        total_amount = 1
        for i,cur_rank in enumerate(rank):
            curr_amount = freq[i]
            
            total_amount *= math.comb(rank_amount_wo_flset[cur_rank],curr_amount)
        
            
        return total_amount*flush_am