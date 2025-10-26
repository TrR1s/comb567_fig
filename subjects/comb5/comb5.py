from pydantic import BaseModel, computed_field,field_validator,Field
from utils.read_json5 import read_json
from subjects.deck.card import Card,Rank,Suit,rank_to_int

class Comb5Dict():
    comb5_dict = read_json()


class Comb5(BaseModel):
    cards_set: set[Card]
    
    
    @field_validator('cards_set')
    def check_card_amount(cls, value):
        if len(value) != 5:
            raise ValueError('Card amount must be 5')
        return value
    
    @computed_field 
    def flush_is(self)-> bool:
        suit_list = [card.suit for card in self.cards_set]
        return True if len(set(suit_list)) == 1 else False
    
    @computed_field
    def str_key(self) -> str:
        rank_list = [rank_to_int(card.rank)+2 for card in self.cards_set]
        flush = 'fl' if self.flush_is else 'unfl'
        return ','.join(map(str, sorted(rank_list))) + '_' + flush
    
    @computed_field
    def comb_fig(self) -> tuple[str,int]:
        name, nn = Comb5Dict.comb5_dict[self.str_key]
        return (name, nn)
        
    
  