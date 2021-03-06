# Date: 7/30/2021
# Exercise 2

# 1. How many seconds are there in 42 minutes 42 seconds?

def time_convert(minutes, seconds):
    """
    time_convert function converts minutes into seconds
    :param minutes: integer
    :param seconds: integer
    :return: integer
    """
    converts = minutes * 60  # 1 min = 60s
    total_seconds = converts + seconds
    return total_seconds


"""
print(time_convert(42, 42))
# Solution: 2562
"""


# 2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
def kilo_to_mile(kilometers):
    """
    kilo_to_mile function takes kilometers as input and will convert it to mile. 
    :param kilometers: float
    :return: float
    """
    miles = kilometers / 1.61
    return miles


"""
print(kilo_to_mile(10))
# Solutions: 6.211180124223602
"""

# 3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace
# (time per mile in minutes and seconds)? What is your average speed in miles per hour?


def avg_pace(kilometers, minutes, seconds):
    """
    avg_pace function divide distance by time to get the average pace.
    :param kilometers:float, in kilometers
    :param minutes: integer
    :param seconds: integer
    :return: time per mile in minutes and seconds.
    """
    # average pace = time / mile
    return time_convert(minutes, seconds) / kilo_to_mile(kilometers)


"""
print(avg_pace(10, 42, 42))
# Solution: 412.482
"""

# What is your average speed in miles per hour? (average speed = miles / hour)


def avg_speed(kilometers, minutes, seconds):
    """
    avg_speed function divide miles by hours.
    :param kilometers: float
    :param minutes: integer
    :param seconds: integer
    :return: average speed in miles per hour
    """
    return kilo_to_mile(kilometers) / (time_convert(minutes, seconds) / 60 / 60)


"""
print(avg_speed(10, 42, 42))
# solution: 8.727653570337614
"""