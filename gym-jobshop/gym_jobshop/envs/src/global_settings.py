"""
HOWTO:
The most important settings (for controlling the experimental design) are right below this text.
The less important settings are down further.
"""
#########################################################
################## Important settings: ##################
#########################################################
duration_of_one_period = 960  # default value is 960 steps per period
number_of_periods = 8000  # Default: 8000 periods

overtime_setup = 2
# Setup A: overtime_setup = 1
# Setup B: overtime_setup = 2

# Setup A will result in the following parameters:
# overtime_multiplier_1 = 1.125
# overtime_multiplier_2 = 1.25
# cost_for_action_1 = 16
# cost_for_action_2 = 32

# Setup B will result in the following parameters:
# overtime_multiplier_1 = 1.25
# overtime_multiplier_2 = 1.5
# cost_for_action_1 = 32
# cost_for_action_2 = 64

demand_distribution = "exponential"  # must be "exponential" or "uniform". Used in
# environment.py/set_next_order_arrival_time()

processing_time_distribution = "exponential"  # must be "exponential" or "uniform"
# It is recommended to use exponential distribution, as some values have been optimized for that.
# Uniform distribution might lead to worse results

# Parameters for UNIFORM DEMAND
next_order_arrival_lower_bound = 78  # lower limit for when the next order can arrive.
next_order_arrival_upper_bound = 158  # upper limit for when the next order can arrive

# Parameters for EXPONENTIAL DEMAND
next_order_arrival_exponential_rate_parameter = 118  # this is the λ (lambda) or
# rate parameter of the exponential distribution

# Machine processing times. Each number refers to an exponential distribution, e.g. Exp(95)
# This is the expected processing time for the single machine inside the 1 machine scenario:
processingtime_machine_A_job_shop_1_machine = 106.1999115  # default 106.1999115
# Expected processing time in job shop scenario with three machines:
processingtime_machine_A_job_shop = 80  # default 80
processingtime_machine_B_job_shop = 77.5  # default 77.5
processingtime_machine_C_job_shop = 110  # default 110
# The uniform processing times are located at main.py -> setup_environment()

order_release_policy = "bil"  # must be "periodic" (=immediate release) or "bil" (= backward infinite loading)
# When using BIL, don't forget to set planned_release_date_multiplier
scheduling_policy = "earliest_due_date"  # must be "first_come_first_serve" or "earliest_due_date"

due_date_slack_mode = "variable"  # must be "variable" or "fixed"

# For due_date_slack_mode == fixed:
fixed_due_date_slack = 9  # how many periods the due date of new orders is in the future (due date slack).
# Default: 10 periods. Note that the fixed_due_date_slack must be 1 lower than the intended due date slack.
# Example: if you want a due date slack of 10 periods, the fixed_due_date_slack must be set to 9.

# For due_date_slack_mode == variable:
# Upper and lower boundaries for the uniform distribution
variable_due_date_upper_bound = 4
variable_due_date_lower_bound = 1

planned_release_date_multiplier = 2  # used for the BIL order release policy.
# Planned release date is always planned_release_date_multiplier * duration_of_one_period + current_time
# See more at order_release.py --> release_using_bil()

processing_times_multiplier = 1  # Each step, the affected machines (bottleneck machines) subtract
# 1 * processing_times_multiplier from their
# current order's remaining processing time. Thus a processing_times_multiplier > 1 means that machines subtract MORE
# than the default amount of remaining processing time from the order, which means that the production capacity of
# the machine is increased. If the processing_times_multiplier were below 1, this would mean that the
# capacity of the machines is lower than the default value and thus the machines subtract less remaining processing
# time and take longer to process orders. As this is not a desired behaviour, we only consider
# processing_times_multiplier > 1.
# A processing_times_multiplier of 1 is the default value (subtract 1 each step), indicated by overtime_multiplier_1
# The other two variables overtime_multiplier_2 and overtime_multiplier_3 indicate overtime
# The variables below are used in main.adjust_processing_times()
# To adjust the overtime, change the variable overtime_setup

# Cost rates:
cost_per_item_in_shopfloor = 1  # Cost per period for every order which is either inside a machine or wip. Default: 0
cost_per_item_in_fgi = 4  # Cost per period for storing one order in finished goods inventory. Default: 4
cost_per_late_item = 16  # Cost per period for exceeding an order's due date. Default: 16
overtime_base_cost = 8  # Overtime cost per hour. Gets multiplied depending on chosen overtime

revenues = {1: 10, 2: 12, 3: 14, 4: 16, 5: 18, 6: 20, 7: 22}

#########################################################
############### Less important settings: ################
#########################################################

# Variables for the initial setup
current_time = 0  # this variable keeps track of the current time/step/tick in the simulation
maximum_simulation_duration = duration_of_one_period * number_of_periods  # maximum duration in steps
warmup_duration = 1000  # costs are reset after warmup phase
repetitions = 1  # how often should the entire simulation be repeated NOT USED CURRENTLY -> use agent instead
random_seed = 0  # Setting the random seed to a fixed value allows reproducing the results
# (meaning that all random numbers are the same every time the simulation runs)
shop_type = None  # Must be either "job_shop" or "job_shop_1_machine".
# Shop type is automatically set depending on number_of_machines in class JobShopEnv().__init__
# flow_shop is currently not supported
time_of_next_order_arrival = 0  # gets overwritten for every new order

# Variables used during the simulation runtime
overtime_multiplier_1 = 1.0  # default 1.0
overtime_multiplier_2 = 1 + 0.125 * overtime_setup  # default 1.125 (setup A) or 1.25 (setup B)
overtime_multiplier_3 = 1 + 0.25 * overtime_setup  # default 1.25 (setup A) or 1.5 (setup B)

# Variables that are used as result metrics
count_of_generated_orders = 0
# Cost for 2 hours is 8*2=16, cost for 4 hours is 8*4=32, for 8 hours is 8*8=64
cost_for_action_1 = overtime_base_cost * 2 * overtime_setup  # default: 2 hours (setup A) or 4 hours (setup B)
cost_for_action_2 = overtime_base_cost * 4 * overtime_setup  # default: 4 hours (setup A) or 8 (setup B)

total_cost = 0
sum_shopfloor_cost = 0
sum_fgi_cost = 0
sum_lateness_cost = 0
sum_overtime_cost = 0
sum_revenue = 0
temp_sum_of_late_orders_this_period = 0
temp_cost_this_period = 0
temp_overtime_cost = 0
temp_wip_cost = 0
temp_lateness_cost = 0
temp_fgi_cost = 0
temp_amount_of_shipped_orders = 0
temp_revenue = 0
bottleneck_utilization_per_step = 0  # Integer, which gets increased by up to 1 per step inside
# performance_measurement -> measure_bottleneck_utilization()
past_rewards = []
shipped_orders_by_prodtype_and_lateness = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                                           [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                                           [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


def reset_global_settings():
    global current_time
    global count_of_generated_orders
    current_time = 0
    count_of_generated_orders = 0
    return
