# 9.3
def test(func):
    def new_func(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_func

@test
def greeting():
    print("Greetings,Earthling")

greeting()


#9.4

class OopsException(Exception):
    pass

raise OopsException()

__main__.OopsException

try:
    raise OopsException
except OopsException:
    print('Caught an oops')
