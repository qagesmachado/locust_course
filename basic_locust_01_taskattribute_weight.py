from locust import HttpUser, task, between, User


def add_cart(userclass):
    print('I am add to cart') # print to simulate request

def view_product(userclass):
    print('I am view product') # print to simulate request

class MyUser(User):
    wait_time = between(1,2) # min and max random wait in seconds

    # You will define the fuction outside the class then here you will call the function using this list
    # tasks = [add_cart, view_product]

    # With you want to define weight then you need to use as a dictionaty by this way
    tasks = {add_cart:2, view_product:6}