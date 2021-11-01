fibonacci_arr = [0,1]

def fibonacci_series(num):
    if num<=0:
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
    if num<0:
        return 0
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
    if num<=0:
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