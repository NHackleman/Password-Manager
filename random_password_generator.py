import random
def create_password(password):

    pass_list = []
    join_char = ''

    upper_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    has_upper = False
    lower_list = 'abcdefghijklmnopqrstuvwxyz'
    has_lower = False
    num_list = '1234567890'
    has_num = False
    special_list = '!@#$%^&*()'
    has_special = False

    list_list = [upper_list, lower_list, num_list, special_list]

    while len(pass_list) <= 12:
        if len(pass_list) < 8:
            pass_list.append(random.choice(random.choice(list_list)))

        else:
            add_char = random.randint(1, 4)
            if add_char == 3:
                break
            
            else:
                pass_list.append(random.choice(random.choice(list_list)))
    
    while not has_upper and not has_lower and not has_num and not has_special:
        check =  any(item in pass_list for item in upper_list)
        if check:
            has_upper = True
        else:
            pass_list.append(random.choice(upper_list))
        
        check =  any(item in pass_list for item in lower_list)
        if check:
            has_lower = True
        else:
            pass_list.append(random.choice(lower_list))
                
        check =  any(item in pass_list for item in num_list)
        if check:
            has_num = True
        else:
            pass_list.append(random.choice(num_list))
                
        check =  any(item in pass_list for item in special_list)
        if check:
            has_special = True
        else:
            pass_list.append(random.choice(special_list))

    password = join_char.join(pass_list)
    return password
