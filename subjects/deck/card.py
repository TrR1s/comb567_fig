from pydantic import BaseModel, computed_field,model_validator,Field
from enum import StrEnum

class Rank(StrEnum):
    ACE = 'A',
    KING = 'K',
    QUEEN = 'Q',
    JACK = 'J',
    _10 = '10',
    _9 = '9',
    _8 = '8',
    _7 = '7',
    _6 = '6',
    _5 = '5',
    _4 = '4',
    _3 = '3',
    _2 = '2',
    

class Suit(StrEnum):
    HEARTS = 'h',
    CLUBS = 'c',
    DIAMONDS = 'd',
    SPADES = 's',


class Card(BaseModel):
    rank: Rank  
    suit: Suit
    
    @computed_field
    def short_name(self) -> str:
        return f'{self.rank}{self.suit}'
    
    
class Deck(BaseModel):
    cards_list: list[Card]
    
    @computed_field
    def short_view(self) -> dict[Suit,list[str]]:
        deck_view = {
            Suit.HEARTS:[],
            Suit.CLUBS:[],
            Suit.DIAMONDS:[],
            Suit.SPADES:[],
        }
        for curr_card in self.cards_list:
            deck_view[curr_card.suit].append(curr_card.short_name)
        return deck_view

def do_full_deck() -> Deck:
    cards_list = []
    for curr_s in Suit:
        for curr_r in Rank:
            card = Card(
                        rank=curr_r,
                        suit=curr_s)
            cards_list.append(card) 
    return Deck(cards_list=cards_list)

if __name__ == "__main__":
    rank = Rank._10
    suit = Suit.CLUBS
    
    card = Card(
        rank=rank,
        suit=suit)
    print(card)
    full_deck = do_full_deck()
    print(full_deck.short_view)
    full_deck.cards_list.remove(card)        
    print(full_deck.short_view)
    