# CS16 Final Project: Naive Bayes Classifier Artificial Neural Network 
## John (Jack) Wagner, CS16 Fall 2019


This artificial neural network was created to detect the legitimacy of SMS messages from the dataset *SMS Spam Collection Data Set*. 

###### Nota Bene: "Ham" means "legitamate" in this dataset. Addionally, equations and screenhots can be found in the project submission under *Wagner COSC 16 Final Project Summary.pdf*     

### Usage

All training and testing can be done with a single terminal command line:

`python spamDetection.py`

### Functions

1. *train-data* : creates dictionary from training data set where keys are words and values are arrays of size 2 that hold the number of spam and ham appearances for that word
2. *make-output-file* : writes all words that appeared in spam messages to an output file
3. *test-data* : calls *find-prob-of-input* on each line of file and compares calculated spam and ham probabilities to expected result
4. *user-input-SMS* : takes input string from user to determine if it would be spam or ham 
5. *find-prob-of-input* : calculates final-spam-prob and final-ham-prob based on complimentary probabilities or word appearances


### Limitations
- The dataset was rather small to create a high level of accuracy for the high level of variation in the SMS messages.  Therefore, *user-input-SMS* was only sometimes accurate.

