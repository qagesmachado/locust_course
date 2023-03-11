from locust import HttpUser, task, between, User

class MyUser(User):
    wait_time = between(1,2) # min and max random wait in seconds

    @task  # what will be execute
    def login_URL(self):
        print('I am loggin into URL') # print to simulate request