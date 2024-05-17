def auth(permission):
    def deco(foo):
        def wrapper(*args,**kwargs):
            if permission=="success":
                return foo(*args,**kwargs)
            raise ValueError("unouthorized")
        return wrapper
    return deco


@auth("Denied")
def user(name):
    print (f"user:{name}")

@auth("success")
def user2(name):
    print(f"user is {name}")