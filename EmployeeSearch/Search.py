"""
Name:           Trishal Varma

Human Language Technologies
Objective:      Employee Search using python implementing regress, and pickle
"""
import re
import pickle

class Person:

    # Get input data.

    def __init__(self, data):

        parsed_data = self.preprocess(data)
        self.last_name = parsed_data[0]
        self.first_name = parsed_data[1]
        self.middle_initial = parsed_data[2]
        self.id = parsed_data[3]
        self.phone = parsed_data[4]

    def display(self):

        # print information in order from the Person object.
        print(self.last_name, self.first_name, self.middle_initial, self.id, self.phone)
        return self.first_name, self.middle_initial, self.last_name, self.id, self.phone

    def preprocess(self, inputs):
        print(inputs)
        # remove white space, use token to get rid of ","
        tokens = inputs.strip().split(',')

        # order tokens: last, first middle, the id, number.
        # NA for middle initial missing

        for index in range(len(tokens[:3])):
            if tokens[index]:
                tokens[index] = tokens[index].lower()
                tokens[index] = tokens[index][0].upper() + tokens[index][1:] # display of the index length.
            else:
                tokens[index] = 'NA'
                # misssing would become NA so can be easily seen.

        # ID requirements and pattern set
        id_pat = "^[A-Za-z]{2}[0-9]{4}$"
        while not re.match(id_pat, tokens[3]):
            print('invalid ID', tokens[3])
            print('ID must have two letters followed by 4 digits. Enter valid ID: ')
            tokens[3] = input()
            tokens[3] = tokens[3].upper()

        # Phone number pattern requirements and pattern set
        phone_pat = "^[0-9]{3}-[0-9]{3}-[0-9]{4}$"
        if not re.match(phone_pat, tokens[4]):
            tokens[4] = re.sub('[^0-9]', '', tokens[4]) # letters will give error, only numberic
            tokens[4] = ''.join(tokens[4][:3]) + '-' + ''.join(tokens[4][3:6]) + '-' + ''.join(tokens[4][6:])
        return tokens

def main():
    # Data must be saved in the same directory (if not then specefy)
    with open('data.csv', 'r') as f:
        data = f.readlines()[1:]  # [1:] Ignores the top header.

    persons = {}
    for person in data:
        p = Person(person)
        if not p.id in persons.keys():
            persons[p.id] = p
        else:
            print("Error! {} Already exists in file.".format(p.id))

# Using pickle
    with open('persons', 'wb') as file:
        pickle.dump(persons, file)
        file.close()

    # open picke and verify if crrect
    with open('persons', 'rb') as file:
        persons = pickle.load(file)
        file.close()

    for id, person in persons.items():
        print('Employee id: {}'.format(person.id))
        print('\t', person.first_name, person.middle_initial, person.last_name)
        print('\t', person.phone)

if __name__ == '__main__':
    main()

    """
    Name:           Trishal Varma
    Date:           August 28th, 2020
    Class:          Human Language Technologies 
    Professor:      Karen Mazidi
    Objective:      Employee Search using python implementing regress, and pickle 
    """
