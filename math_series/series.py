fibonacci_arr = [0,1]

def fibonacci_series(num):
    """
    A function that take a (num) as argument
    and retun the nth number of fibonacci series
    which start the series with 0 , 1
    """
    if num<0:
        return 0
    i = len(fibonacci_arr)
    if i>=num:
        return fibonacci_arr[num-1]
    else:
        fibonacci_arr.append(fibonacci_arr[i-2] + fibonacci_arr[i-1])
        if i == num:
            return fibonacci_arr[i-1]
        else:
            return fibonacci_series(num) 

lucas_arr = [2,1]
def lucas_series(num):
    """
    A function that take a (num) as argument
    and retun the nth number of lucas series
    which start the series with 2 , 1
    """
    if num<0:
        return 2
    i = len(lucas_arr)
    if i>=num:
        return lucas_arr[num - 1]
    else:
        lucas_arr.append(lucas_arr[i-2] + lucas_arr[i-1])
        if i == num:
            return lucas_arr[i-1]
        else:
            return lucas_series(num)

def sum_series(num,ob1=0,ob2=1):
    """
    A function that take a (num), (ob1) (ob2) as argument
    and retun the nth number of a series
    which start the series with ob1 , ob2
    Note : ob1 = 0 , ob2 = 1 as default
    """
    if num<0:
        return ob1
    arr =[ob1,ob2]
    if num < len(arr):
        return arr[num]
    else:
        arr.append(ob1 + ob2)
        if len(arr) == num:
            return arr[num-1]
        else:
            ob1 , ob2 = ob2 , arr[2]
            return sum_series(num - 1,ob1,ob2)

if __name__ == "__main__":
    print("Please enter the nth number you ask for")
    num = int(input(" > "))
    print("Please enter the first numbers of the series")
    ob1 = int(input(" > "))
    print("Please enter the second numbers of the series")
    ob2 = int(input(" > "))
    print(sum_series(num,ob1,ob2)) 
