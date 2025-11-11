from pydantic import BaseModel, computed_field,field_validator,Field
import numpy as np


class Comb5short(BaseModel):
    rank_dict: dict[int,int] # {rank_nn: amount_rank}
    flush_is: bool # if flush - True
    
    @computed_field
    def str_key(self) -> str:
        rank_list = list(self.rank_dict.keys())
        flush = 'fl' if self.flush_is else 'unfl'
        return ','.join(map(str, sorted(rank_list))) + '_' + flush

    
    
def do_comb5_from_str_key( str_key: str) -> Comb5short:
    str_key_split = str_key.split('_')
    ranks_str = str_key_split[0].split(',')
    ranks = np.array(list(map(lambda x: int(x),ranks_str)))
    unique_elements, counts = np.unique(ranks, return_counts=True)
    rank_dict = dict(zip(unique_elements,counts))
    flush_is = True if str_key_split[1] == 'fl' else False
    return Comb5short(
        rank_dict = rank_dict,
        flush_is = flush_is
    )
    


if __name__ =="__main__":
    str_key = "3,8,9,9,14_fl"
    
    comb5_sh = do_comb5_from_str_key(str_key)
    print(comb5_sh)
    # ranks_str = str_key.split('_')[0].split(',')
    # ranks = np.array(list(map(lambda x: int(x),ranks_str)))
    # unique_elements, counts = np.unique(ranks, return_counts=True)
    # # print(ranks_str.split(',').map(lambda x: int(x)))
    # print( unique_elements, counts)
    # res_dict = dict(zip(unique_elements,counts))
    # print(res_dict)