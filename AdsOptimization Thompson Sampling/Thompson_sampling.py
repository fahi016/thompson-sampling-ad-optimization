import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

# Load the dataset
dataset = pd.read_csv('Ads_CTR.csv')

# Initialize parameters
Total_Rounds = 1000
Total_Ads = 10
selected_ads = []
reward_zero_counts = [0] * Total_Ads
reward_one_counts = [0] * Total_Ads
total_reward = 0

# Loop over each round
for n in range(0, Total_Rounds):
    current_ad = 0
    max_random_value = 0
    
    # Loop over each ad to select the one with the highest beta value
    for i in range(0, Total_Ads):
        # Generate a random beta value for each ad based on its rewards
        random_beta = random.betavariate(reward_one_counts[i] + 1, reward_zero_counts[i] + 1)
        
        # Select the ad with the highest beta value
        if random_beta > max_random_value:
            max_random_value = random_beta
            current_ad = i
    
    # Append the selected ad index to the list
    selected_ads.append(current_ad)
    
    # Get the reward of the selected ad from the dataset
    current_reward = dataset.values[n, current_ad]
    
    # Update the rewards lists based on the received reward
    if current_reward == 1:
        reward_one_counts[current_ad] += 1
    else:
        reward_zero_counts[current_ad] += 1
    
    # Update the total reward
    total_reward += current_reward

# Plot the histogram of ad selections
plt.hist(selected_ads)
plt.title('Histogram of ad selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()
