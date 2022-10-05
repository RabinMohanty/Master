from pantry_details import pantry_dict,ingr_dict

user_choice = {}
for serial,i in enumerate(ingr_dict.keys()):
    user_choice[str(serial + 1)] = i



while True:
    print("\n\n")
    for key,value in user_choice.items():
        print ("Press {} for choosing recipe of {}".format(key,value))
    print ("Press 0 to exit")
    user_input = input()
    if user_input in user_choice.keys():
        print("User has choosen {} for dish : {}".format(user_input,user_choice[user_input]))
        ingr_list = list(ingr_dict[user_choice[user_input]].keys())
        for j in ingr_list:
            print("ingredient name : {}".format(j))
            req_qty = ingr_dict[user_choice[user_input]][j]
            available_qty = pantry_dict.get(j,0)
            print("available qty : {}".format(available_qty))
            print("Required qty : {}".format(req_qty))
            if available_qty >= req_qty:
                pantry_dict[j] = available_qty - req_qty
                print("ingredient {} for {} is available, left in stock {}".format(j,user_choice[user_input],pantry_dict[j]))
            else:
                necessary_qty = req_qty - available_qty
                print("Shortage by {}".format(necessary_qty))
    elif user_input == "0":
        break
