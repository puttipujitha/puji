def count_calls(func):
    c=0
    def inner():
        c+=1
        if c>func:
            print(c)
        else:
            print("not found")
@count_calls
def generate_ticket():
    return 1234
generate_ticket()



