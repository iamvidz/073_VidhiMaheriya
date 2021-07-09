import nltk 
from nltk.corpus import twitter_samples # sample Twitter dataset from NLTK
import matplotlib.pyplot as plt # library for visualization
import random # pseudo-random number generator

nltk.download("twitter_samples")

all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')

print('Number of positive tweets: ', len(all_positive_tweets))
print('Number of negative tweets: ', len(all_negative_tweets))
print('\nThe type of all_positive_tweets is: ', type(all_positive_tweets))
print('The type of a tweet entry is: ', type(all_negative_tweets[0]))


fig = plt.figure(figsize=(5, 5))
labels = 'ML-BSB-Lec', 'ML-HAP-Lec','ML-HAP-Lab'
sizes = [40, 35, 25]
plt.pie(sizes, labels=labels, autopct='%.2f%%',
shadow=True, startangle=90)
plt.axis('equal')
plt.show()


fig = plt.figure(figsize=(5, 5))

labels = 'Positives', 'Negative'
sizes = [len(all_positive_tweets), len(all_negative_tweets)]
plt.pie(sizes, labels=labels, autopct='%1.1f%%',
shadow=True, startangle=90)
plt.axis('equal')
plt.show()


print('\033[92m' + all_positive_tweets[random.randint(0,5000)])

print('\033[91m' + all_negative_tweets[random.randint(0,5000)])

tweet = all_positive_tweets[2277]
print(tweet)