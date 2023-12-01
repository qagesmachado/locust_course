from locust import HttpUser, task, between, User

class MyUser(User):
    wait_time = between(1,2) # min and max random wait in seconds

    @task(2)  # what will be execute with weight 2
    def add_cart(self):
        print('I am add to cart') # print to simulate request

    @task(4)  # what will be execute with weight 4
    def view_product(self):
        print('I am view product') # print to simulate request