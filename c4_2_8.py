def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:',func.__name__) #関数の名前が入る
        print('args:',args) #
        print('kwargs',kwargs)
        result = func(*args,**kwargs)
        print('result:',result)
        return result
    return wrapper

@print_more #ここではじめてコードが実行される
def add_num(a,b):
    return a + b

r = add_num(10,20)
print(r)