from itertools import chain

class P_Iter(object):
    def __init__(self, args, kwargs, callable):
        self.args = args
        self.kwargs = kwargs
        self.callable = callable
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >1:
            raise StopIteration
        print("paginating for inp ", self.kwargs['b'])
        filt = self.kwargs['b'][self.i]
        k_wargs = {'a': self.kwargs['a'], 'b': filt}
        self.i+=1
        return self.callable(*self.args, **k_wargs)

def batched(batch_func=None, batch_args=None, batch_attribute=None, batch_size=None):
    def inner(func):
        def wrap(*args, **kwargs):
            print("In batched with filt as ", kwargs['b'], batch_size)
            chunks = [kwargs['b'][:2], kwargs['b'][2:4], kwargs['b'][4:6]]
            res = []
            it_res = None
            n = 1
            for chunk in chunks:
                kwargs['b'] = chunk
                tmp = func(*args, **kwargs)

                if isinstance(tmp, P_Iter):
                    if it_res:
                        it_res = chain(tmp,it_res)
                    else:
                        it_res = tmp
                else:
                    print("Result for batch : ", n , " is ", tmp)
                    n+=1
                    res += tmp

            print("Batched")
            return res if res else it_res
        return wrap
    return inner

def paginated(func):
    def wrap(*args, **kwargs):
        print("In paginated with batch chunk ", kwargs['b'])
        it = P_Iter(args, kwargs, func)

        if kwargs.get('api_opts', {}).get('is_paginated', False):
            return it

        res = []
        n = 1
        for r in it:
            print("Result for page no : ", n, " is ", r)
            n+=1
            res.append(r)

        print("Paginated")
        return res
    return wrap

def rename_attr(func):
    def wrap(*args, **kwargs):
        print("In rename attrs")
        pass
        print("Renamed")
        return func(*args, **kwargs)
    return wrap

@batched(batch_size=2, batch_attribute=None)
@paginated
@rename_attr
def func1(a=None, b=None, c=2, api_opts=None):
    print("In actual function")
    return b

#it = func1(a=4, b=[1,2,3,4,5,6], api_opts={'is_paginated':True})
it = func1(a=4, b=[1,2,3,4,5,6])
print(it)

for r in it:
    print(r)

'''
[1,2]
    [1,2] -> 1
    [1,2] -> 2
[3,4]
    3
    4
[5,6]
    5
    6

1,2,3,4,5,6
'''