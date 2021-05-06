def get_biggest_name(name_array):
    bigger_name = ""
  
    for each in name_array:
        # print(each)
        # print(len(each))
        
        if len(each) > len(bigger_name):
            bigger_name = each
        
    print(bigger_name, "has the bigger name. It has", len(bigger_name), "characters.")

NAMES = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]

get_biggest_name(NAMES)
