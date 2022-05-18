
def ex1(num):
    try:
        return 6 / num
    except ZeroDivisionError:
         print("division by zero")
    except TypeError:
        print ("letter in num")

    finally:
        print("function done!")

def ex2(index, my_tuple=(1,2,3,4,5)):

    try:
        return my_tuple[index]
    except TypeError:
        print ("letter in index")
    except IndexError:
        print ("number in index is out of range" )
    finally:
        print ("function ex2 is done")
def ex3(name):
    try:
        return "hello" + name
    except TypeError:
        print("number in name")

if __name__ == '__main__':
    # Run your functions here
    print("Good Luck!")
    print(ex3(6))