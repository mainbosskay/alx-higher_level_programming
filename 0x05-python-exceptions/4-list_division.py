#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    divlist = []
    for k in range(list_length):
        try:
            div = my_list_1[k] / my_list_2[k]
        except TypeError:
            print("Wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            divlist.append(div)
    return (divlist)
