from locust import HttpUser, task, between, User

# If you wish to simulate more users of a certain type you can set 
# a weight attribute on those classes. 
# Say for example, web users are three 
# times more likely than mobile users:


class MyUser(User):
    wait_time = between(1,2) # min and max random wait in seconds
    
    # the higher the weight compared to another user the more it will run
    weight = 3 

    @task  # what will be execute
    def login_URL(self):
        print('I am loggin into URL') # print to simulate request

class MyMobileUser(User):
    wait_time = between(1,2) # min and max random wait in seconds

    # the higher the weight compared to another user the more it will run
    weight = 1

    @task  # what will be execute
    def login_URL(self):
        print('I am loggin into URL by Mobile') # print to simulate request


# To run from command line
# locust -f basic_locust_02_weightage.py -u 5 -r 1 -t 15s --headless --logfile logfiles/mylog.log --loglevel DEBUG