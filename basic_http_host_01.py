from locust import HttpUser, task, between, User

class MyUser(User):
    wait_time = between(1,2) # min and max random wait in seconds
    host="http://netours.demoaut.com" # destiny of request, can be define by command line

    @task  # what will be execute
    def login_URL(self):
        print('I am loggin into URL') # print to simulate request