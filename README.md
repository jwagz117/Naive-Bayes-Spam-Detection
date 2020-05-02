# Naive-Bayes-Spam-Detection
Final Project for Introduction to Computational Neuroscience

I used the Naive Bayes Classifier to detect whether SMS messages were considered to be
ham​ (i.e. legit messages) or ​spam​. I used the “SMS Spam Collection Data Set” which consisted of 5574 different SMS messages and whether they were spam or ham. I used 4676 of these messages to train my program then the remaining 898 messages to test my program.
The first step of my implementation was taking the training file line by line and splitting apart the different words. Then I made a dictionary of all the words in the training file. Each word was a key and pointed to a 2-item list in which the first item was the number of times where that word appeared in spam messages, and the second item was the number of times where that word appeared in ham messages.
Next, to test against the training data and dictionary I created, I took the testing file and made a dictionary of each line’s words. I then called my main function, find_prob_of_input(dictionary)​ on each line. If the output of that function matched the expected output of the training line (whether it was supposed to be ham or spam) then that line was considered to be interpreted correctly. Using 898 test lines, my testing predicted 338 correct, at a 37.6% success rate. I will discuss different possibilities of error in a moment.
The function ​find_prob_of_input(dictionary)​ is what did the Naive Bayes Classification. The following formula was used:
To do this, I had to consider every word from the training dictionary. If a word in the training dictionary did not appear in the test line, then its complement probability was used. However, if the word in the training dictionary ​did​ appear in the test line, then its corresponding spam or ham
 
 probability was used. The sample problem I used to teach myself this concept is from https://www.youtube.com/watch?v=8aZNAmWKGfs​ and appears here:
** The 1s mean that “review” and “us” are in the training set ​and​ in the test sentence.. The 0s mean that “password”, “send”, “your”, and “account” did n​ ot​ appear in the test sentence.**
One of the things that I debated heavily when creating my program was the use of punctuation. When I split apart the lines in both training and testing, I ultimately decided to keep the punctuation because spam and ham messages followed different trends in their punctuation. For example, as seen from the ​SMSSpamCollection​ data file and also my output words_in_spam_SMS,​ punctuation such as “=”, “!”, and “?” had unique roles in spam and ham messages. I decided to keep the punctuation in my training because of this.
I think that one of the main problems with this method was indeed the punctuation. The punctuation varied widely in the spam messages, but I did not want to sacrifice the uniqueness of words with their punctuation in spam messages to make my program more general. Also, however, the length of the messages also played a role in the output. I created a method in which the user can type their own string to see if that would be considered ham or spam based off my training, and I noticed from many of my own testing messages that shorter messages had a higher probability of being considered ham messages. Even if I typed an input string of multiple
    
 words words that appeared in spam messages, the string was still considered to be spam. Some example outputs are shown here:
 The last message I inputted is a direct copy from line 893 of my testing file. It was correctly identified as a spam SMS message.
I do believe that this could be improved if a smaller dataset was used and if the problem with the punctuation could be handled more carefully. I think that, if done correctly, it would make it more accurate without losing the unique punctuation from some spam messages. This program could also be used on other data as well. For example, if there was a dataset of words spoken from two different people, then this program could use the frequency of words between the two people to predict if a certain testing phrase was said by one or the other.

RESOURCES “How to Clean Text for Machine Learning in Python?”:
https://machinelearningmastery.com/clean-text-machine-learning-python/
Naive Bayes for Spam Detection YouTube:
https://www.youtube.com/watch?v=8aZNAmWKGfs
“Python Numbers, Type Conversion, and Mathematics”:
https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection#
SMS Spam Collection Data Set: ​https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection#
“Why Doesn’t This Division Work in Python?”:
https://stackoverflow.com/questions/1787249/why-doesnt-this-division-work-in-python
“3 Ways to Write Text to a File in Python?”:
https://cmdlinetips.com/2012/09/three-ways-to-write-text-to-a-file-in-python/
