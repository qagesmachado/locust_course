from locust import HttpUser, task, between, User, events

# locust -f test_start_stop.py -u 3 -r 1 -t 15s --headless --logfile logfiles/mylog.log --only-summary --loglevel DEBUG

# These two methods will be executed only once either with you have a lot of users
@events.test_start.add_listener
def script_start(**kwargs):
        print('I am connecting to DB') # print to simulate request

@events.test_stop.add_listener
def script_stop(**kwargs):
        print('I am disconnecting from DB') # print to simulate request

class MyUser(User):
    wait_time = between(1,2) # min and max random wait in seconds

    # Deleting @task this method will be execute once in the begining
    # This def will be repeat by the number of users, 2 user then 2 logins
    def on_start(self):
        print('I am loggin into URL') # print to simulate request

    @task  # what will be execute
    def doing_work(self):
        print('I am doing my work') # print to simulate request

    # Deleting @task this method will be execute once in the ending
    # This def will be repeat by the number of users, 2 user then 2 logout
    def on_stop(self):
        print('I am logout') # print to simulate request

