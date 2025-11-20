from subjects import CombType

BONUS_5_1_STEP = {
    CombType.ROYAL_FLUSH.value: 200 ,             
    CombType.STRAIGHT_FLUSH.value:100,          
    CombType.FOUR_OF_KIND.value: 40,            
    CombType.FULL_HOUSE.value: 15,              
    CombType.FLUSH.value: 8,                   
    CombType.STRAIGHT.value :7,                
    CombType.THREE_OF_KIND.value:5,           
    CombType.TWO_PAIRS.value : 2,               
    CombType.ONE_PAIR.value:-1,                
    CombType.ACE_KING.value:-1,                
    CombType.HIGH_CARD.value:-1,               
    
}