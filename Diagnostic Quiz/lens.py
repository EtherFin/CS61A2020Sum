def lens(prev=lambda x:0):
    """
    A lens store is a store that associates keys with values.
    
    To create a lens store, call the function 'lens', to get a 'put' fucntion.
    This fucntion enables you to "put" a key-value pair into the store and
    return two functions 'get' and another 'put'. The 'get' function should
    let you look up a key and return its corresponding value, while the 
    new 'put' function should let you continue adding on to the existing
    lens store.
    
    Note that you can assume that every key provided is unique. If you try to
    get the value for a key that does not exist, return 0.
    
    For details, refer to the doctest.
    
    >>>put1 = lens()
    >>>get2,put2 = put1('cat', 'animal')
    >>>get3,put3 = put2('table', 'furniture')
    >>>get4,put4 = put3('cup', 'utensil')
    >>>get5,put5 = put4('thesis', 'paper')
    >>>get5('thesis')
    'paper'
    >>>get5('cup')
    'utensil'
    >>>get5('table')
    'furniture'
    >>>get5('cat')
    'animal'
    >>>get3('cup')
    0
    """
    def put(k,v):
        def get(k2):
            if k2==k:
                return v
            else:
                return prev(k2)
        return get,lens(get)
    return put

# put1 = lens()
# get2,put2 = put1('cat', 'animal')
# get3,put3 = put2('table', 'furniture')
# get4,put4 = put3('cup', 'utensil')
# get5,put5 = put4('thesis', 'paper')
# get5('thesis')
# get5('cup')
# get5('table')
# get5('cat')
# get3('cup')

