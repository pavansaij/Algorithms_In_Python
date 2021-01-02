def decorator(func):
    def perform(*args, **kwargs):
        try:
            if kwargs['api_options']['is_paginated'] and (not kwargs['api_options'].get('generator_created', False)):
                return "iterator recieved"
        except:
            pass

        return func(*args, **kwargs)

    return perform

@decorator
def func1(arg1, arg2, api_options=None):
    print(arg1)
    print(arg2)
    return 'func1 called'

@decorator
def func2(arg1, api_options=None):
    print(arg1)
    return 'func2 called'

print(func1(api_options={'is_paginated':True}, arg1=1, arg2="Yes"))
print(func1(api_options={'is_paginated':True, 'generator_created': False}, arg1=1, arg2="Yes"))
print(func1(api_options={'is_paginated':True, 'generator_created': True}, arg1=1, arg2="Yes"))

print(func2(arg1={'prasad': 133}))