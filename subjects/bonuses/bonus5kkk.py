from subjects import CombKingType

BONUS_KKK = {
    CombKingType.ROYAL_FLUSH.value: 3000 ,             
    CombKingType.STRAIGHT_FLUSH_K.value: 2000,        
    CombKingType.STRAIGHT_FLUSH.value:1000,          
    CombKingType.FOUR_OF_KIND_KKKK.value:1000,       
    CombKingType.FOUR_OF_KIND.value: 300,            
    CombKingType.FULL_HOUSE_KKK.value : 250,          
    CombKingType.FULL_HOUSE_KK.value : 250,           
    CombKingType.FULL_HOUSE.value: 70,              
    CombKingType.FLUSH_K.value: 100,                 
    CombKingType.FLUSH.value: 50,                   
    CombKingType.STRAIGHT_K.value: 70,              
    CombKingType.STRAIGHT.value :20,                
    CombKingType.THREE_OF_KIND_KKK.value: 30,       
    CombKingType.THREE_OF_KIND.value:5,           
    CombKingType.TWO_PAIRS_KK.value:10,            
    CombKingType.TWO_PAIRS.value : 2,               
    CombKingType.ONE_PAIR_KK.value: 1,             
    CombKingType.ONE_PAIR.value:-1,                
    CombKingType.ACE_KING.value:-1,                
    CombKingType.HIGH_CARD.value:-1,               
    
}