#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            try:
                if i >= len(my_list_1) or i >= len(my_list_2):
                    raise IndexError
                x = my_list_1[i]
                y = my_list_2[i]
                try:
                    result.append(x / y)
                except ZeroDivisionError:
                    print("division by 0")
                    result.append(0)
            except (TypeError, ValueError):
                print("wrong type")
                result.append(0)
            except IndexError:
                print("out of range")
                result.append(0)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        return result
