# Jack Wagner
# 11/17/19
# COSC 016
# Richard Granger
# Naive Bayes Classifier for SMS Spam Detection


def train_data():
    global words_dict, spam_num, ham_num, total_denom
    file = open("selected_training.txt", "r")  # Open the SMS data set, only to read

    words_dict = {}     # Create a dictionary for every word in SMS data set

    spam_num = 0        # Initially no spam texts encountered
    ham_num = 0         # Initially no ham texts encountered
    total_denom = 0     # Initially no texts encountered

    is_Spam = False     # Boolean to keep track of if text is spam

    for line in file:
        message_info = line.lower().split()    # Split line and make into list
        if message_info[0] == "spam":           # Check if message was identified as spam
            spam_num += 1                       # If so, increase number of spam texts
            total_denom += 1                    # Increase total number of texts encountered
            is_Spam = True
        if message_info[0] == "ham":
            ham_num += 1
            total_denom += 1
            is_Spam = False

        for i in range (1, len(message_info)):
            if message_info[i] in words_dict:   # Check to see if word is already in the dictionary
                if is_Spam:
                    words_dict.get(message_info[i])[0] = words_dict.get(message_info[i])[0] + 1     # Retrieve the appearances list, Increase spam appearances
                if not is_Spam:
                    words_dict.get(message_info[i])[1] = words_dict.get(message_info[i])[1] + 1     # Retrieve the appearances list, Increase ham appearances
            else:
                ind_appearances = [0, 0]  # First index is spam appearances, Second index is ham appearances
                if is_Spam:
                    ind_appearances[0] = ind_appearances[0] + 1     # Increase appearances of spam
                if not is_Spam:
                    ind_appearances[1] = ind_appearances[1] + 1     # Increase appearances of ham
                words_dict[message_info[i]] = ind_appearances       # Add to dictionary with value as list of appearances

    file.close()

    print(words_dict)
    print("Total number of spam SMS messages analized: " + str(spam_num))
    print("Total number of ham SMS messages analized: " + str(ham_num))
    print("Total number of SMS messages analized: " + str(total_denom) + "\n")


def make_output_file():
    outputFile = open("words_in_spam_SMS.txt", "w")     # Write to an output file to see which words were included in spam SMS messages
    for word in words_dict:
        if words_dict.get(word)[0] > 0:
            outputFile.write(str(word) + " has " + str(words_dict.get(word)[0]) + " appearances in spam SMS messages" + "\n")
    outputFile.close()


def test_data():
    correct_test = 0
    test_total = 0
    test_file = open("selected_testing.txt", "r")
    for line in test_file:
        test_total += 1
        test_line_info = line.lower().split()    # Split line and make into list
        expected_result = test_line_info[0]
        line_words_dict = {}
        for i in range (1, len(test_line_info)):
            if test_line_info[i] in words_dict:
                line_words_dict[test_line_info[i]] = None
        find_prob_of_input(line_words_dict)
        if final_spam_prob > final_ham_prob and expected_result == "spam" or final_ham_prob > final_spam_prob and expected_result == "ham":
            correct_test += 1
    print("Testing has predicted " + str(correct_test) + " correct out of " + str(test_total) + " total SMS testing messages.")
    test_file.close()


def user_input_SMS():
    global in_SMS_dict
    user = True
    while user:
        in_SMS = raw_input ("Please type an SMS message to see if it is ham or spam (or type STOP to stop running the program): ")
        in_SMS_list = in_SMS.lower().split(" ")         # Split input SMS message at every space

        if in_SMS_list[0] == "stop":
            user = False
            return

        in_SMS_dict = {}        # Create dictionary to hold all the words in the input SMS message

        for word in in_SMS_list:
            if word in words_dict:      # Ignore all words that don't occur in the training dictionary
                in_SMS_dict[word] = None

        find_prob_of_input(in_SMS_dict)
        print("The probability that your SMS message is spam given that it includes those input words is " + str(final_spam_prob))
        print("The probability that your SMS message is ham give that it includes those input words is " + str(final_ham_prob) + "\n")


def find_prob_of_input(small_dict):
    global spam_prob, ham_prob, final_spam_prob, final_ham_prob
    spam_prob = 1
    for training_word in words_dict:
        if training_word in small_dict and words_dict.get(training_word)[0] > 0:    # If training word is in the input SMS message, multiply by that probability
            spam_prob *= (float(words_dict.get(training_word)[0]) / spam_num)
        elif training_word not in small_dict and words_dict.get(training_word)[0] > 0:       # If the training word is not in the input SMS message, multiply by the compliment of that probability
            spam_prob *= (float(1) - float(words_dict.get(training_word)[0]) / spam_num)

    ham_prob = 1
    for training_word in words_dict:
        if training_word in small_dict and words_dict.get(training_word)[1] > 0:    # If training word is in the input SMS message, multiply by that probability
            ham_prob *= (float(words_dict.get(training_word)[1]) / ham_num)
        elif training_word not in small_dict and words_dict.get(training_word)[1] > 0:       # If the training word is not in the input SMS message, multiply by the compliment of that probability
            ham_prob *= (float(1) - float(words_dict.get(training_word)[1]) / ham_num)

    # Compute final conditional probabilities
    final_spam_prob = float(spam_prob * float(spam_num) / total_denom) / (float(spam_prob * float(spam_num) / total_denom) + float(ham_prob * float(ham_num) / total_denom))
    final_ham_prob = float(ham_prob * float(ham_num) / total_denom) / (float(ham_prob * float(ham_num) / total_denom) + float(spam_prob * float(spam_num) / total_denom))


train_data()
test_data()
make_output_file()
user_input_SMS()

