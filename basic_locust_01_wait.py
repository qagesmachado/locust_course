from locust import HttpUser, task, between, User, constant,constant_pacing
from datetime import datetime

class MyUser(User):
    wait_time = between(1,3) # min and max random wait in seconds
    # wait_time = constant(3) # constant wait time
    # wait_time = constant_pacing(3) # the time will be adjusted according to the time spent on the request

    @task  # what will be execute
    def login_URL(self):
        print(datetime.now()) # print to simulate request