from enum import Enum

class CombKingType(str, Enum):
    
    ROYAL_FLUSH = "ROYAL_FLUSH"
    STRAIGHT_FLUSH_K = 'STRAIGHT_FLUSH_K'
    STRAIGHT_FLUSH = 'STRAIGHT_FLUSH'
    FOUR_OF_KIND_KKKK = 'FOUR_OF_KIND_KKKK'
    FOUR_OF_KIND = 'FOUR_OF_KIND'
    FULL_HOUSE_KKK = 'FULL_HOUSE_KKK'
    FULL_HOUSE_KK = 'FULL_HOUSE_KK'
    FULL_HOUSE = 'FULL_HOUSE'
    FLUSH_K = 'FLUSH_K'
    FLUSH = 'FLUSH'
    STRAIGHT_K = 'STRAIGHT_K'
    STRAIGHT = 'STRAIGHT'
    THREE_OF_KIND_KKK = 'THREE_OF_KIND_KKK'
    THREE_OF_KIND = 'THREE_OF_KIND'
    TWO_PAIRS_KK = 'TWO_PAIRS_KK'
    TWO_PAIRS = 'TWO_PAIRS'
    ONE_PAIR_KK = 'ONE_PAIR_KK'
    ONE_PAIR = 'ONE_PAIR'
    ACE_KING = 'ACE_KING'
    HIGH_CARD = 'HIGH_CARD'
    
    
    
    
    
if __name__ == "__main__":
    print(CombKingType('ROYAL_FLUSH'))
    print(CombKingType.ACE_KING.value)
    