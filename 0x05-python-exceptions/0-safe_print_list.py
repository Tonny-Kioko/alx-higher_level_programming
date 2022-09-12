#!/usr/bin/python3

def safe_print_list(my_list=[], x = 0):
    """Prints the x elements in the list

    Args:
        my_list(list): Thee list to print the elements
        x (int): The eelements in the list

    Returns:
        The required elemnts printed/
    """
    ret = 0
    for i in range (x):
        try:
            print("{}".format(my_list[i]), end = "")
            ret +=1
        except IndexError:
            break
    print("")
    return (ret)
