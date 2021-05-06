import math

def paint_cans_price(wall_size):
    NUMBER_OF_LITERS = math.trunc(wall_size / 3)
    NUMBER_OF_CANS = math.ceil(NUMBER_OF_LITERS / 18)
    FULL_PRICE = NUMBER_OF_CANS * 80
    
    RESULT = (NUMBER_OF_CANS, FULL_PRICE)
    
    print("You will have to buy {0} cans of paint and the full price is R$ {1},00."
      .format(RESULT[0], RESULT[1]))
    

paint_cans_price(160)
