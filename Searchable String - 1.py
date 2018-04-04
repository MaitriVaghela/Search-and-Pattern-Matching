"""
language: python3
description: To perform various forms of search and pattern matching on its own contents.
"""


class SearchableStr:
    def __init__(self, tobesearchedstring):
        """
                Constructor that creates a class member variable.
                :param tobesearchedstring: The string to be searched/matched within
        """
        self.searchedstring = tobesearchedstring
        self.index = -1
        self.charmatched = 0

    def __str__(self):
        """
                Returns a string with the contents of the class member variable.
        """
        return str(self.searchedstring)

    def searchChar(self, target):
        """
                This function will take a character and return a Boolean value which indicates whether or not
                the character is in the class instance's member string
                :param target: character to be matched
                :return: a boolean value(True or False)
        """
        found = False
        self.index += 1

        # It checks whether we have reached the end of the string to be searched
        if len(self.searchedstring) <= self.index:
            found = False
            return found

        # It checks whether the character at the given index of the string is the character we are looking for
        elif self.searchedstring[self.index] == target:
            found = True
            return found

        # If the character at the given index of the string is not the character we are looking for,
        # we call the function again
        else:
            return (self.searchChar(target))

    def searchString(self, target, ind=0, indx=-1):
        """
                This function will take a string(to be searched for) and return a Boolean value which indicates
                whether or not the first string is in the class instance's member string
                :param target: string to be matched
                :param ind: index of the string to be matched
                :param indx: index of the string to be matched with
                :return: a boolean value(True or False)

        """
        self.index = indx
        # It checks the length of the target i.e string to be matched is 0. If it is, it returns True.
        if len(target) == 0:
            return True

        # It checks whether the length of the string to be matched with is less than the length of the string to be matched
        # If it is, it returns False
        if len(self.searchedstring) < len(target):
            return False

        # It checks whether the length of the string to be matched with is equal to the index of the string to be matched
        # If it is, it returns False
        if len(self.searchedstring) == ind:
            return False

        # It calls two functions i.e matchString() and searchString() simultaneously
        # Whichever function's output will be true, will return the answer as a whole True else False.
        return self.matchString(target, self.index) or self.searchString(target, ind + 1, self.index)

    def matchString(self, target, ind=-1):
        """
            This function will take a prefix string and return a Boolean value which indicates
            whether or not the prefix string is the prefix of class instance's member string
            :param target: string to be matched
            :param ind: index of the string to be matched with
            :return: a boolean value(True or False)

                """
        self.index = ind
        self.index += 1

        # It checks the length of the target is 0. If it is, it returns True.
        if len(target) == 0:
            return True

        # It checks if the length of the string to be matched with is equal to its current index
        # If it is, it returns False
        if len(self.searchedstring) == self.index:
            return False

        # It checks whether the first character of the string to be matched with and the string to be matched matches
        #  and also whether the rest of the characters matches
        return self.searchedstring[self.index] == target[0] and self.matchString(target[1:], self.index)

    def matchPat(self, target, index=-1):
        """
                    This function will take a pattern string and return a Boolean value which indicates
                    whether or not the pattern matches the initial portion of the class instance's member string
                    :param target: string to be matched
                    :param index: index of the string to be matched
                    :return: a boolean value(True or False)

        """

        self.ind = index
        self.ind += 1

        # It checks whether the length of the target is equal to the self.ind
        # If it is, it return True
        if len(target) == self.ind:
            return True

        # It checks whether the length of the string to be matched with is 0 and also the target at self.ind is *
        # If it is, it calls the function again
        if len(self.searchedstring) == 0 and target[self.ind] == "*":
            return self.matchPat(target, self.ind)

        # It checks if length of the string to be matched with is 0.
        # if it is, it calls searchPat function
        elif len(self.searchedstring) == 0:
            return self.searchPat(target, -1)


        # It slices the string to be matched with to its half
        # and calls the searchPat function which will compute the function based on the
        # sliced string to be matched with and the target passed along with its index.
        else:
            length = len(self.searchedstring) // 2
            self.searchedstring = self.searchedstring[:length]
            return self.searchPat(target, ind=-1)

    def searchPat(self, target, ind, charmat=0):
        """
            This function will take a pattern string and return a Boolean value which indicates
            whether or not the pattern matches some portion of the class instance's member string
            :param target: string to be matched
            :param ind: index of the string to be matched with
            :param charmat: it keeps a track on the number of characters matched
            :return: a boolean value(True or False)

        """
        self.index = ind
        self.index += 1
        flag = False
        i = 0
        j = 0
        self.charmatched = charmat

        # It checks if the length of the string to be matched is 0
        # If it is, it returns True
        if len(target) == 0:
            return True

        # It checks whether length of the string to be matched with is less than the length of the string to be matched
        elif len(self.searchedstring) < len(target):
            for j in range(0, len(target)):
                if (target[j] == "*"):
                    flag = True
                else:
                    flag = False
            return flag

        # It checks whether the first character of the string to be matched is '*'
        elif target[0] == '*':
            if len(target) == 1:
                return True
            else:
                if len(self.searchedstring) == 0:
                    return True
                else:
                    while (i <= len(target) - 1):
                        if target[i] != "*":
                            target = target[i:]
                            flag = True
                        else:
                            if i == len(target) - 1:
                                flag = True
                                return flag
                            else:
                                i += 1

                    while (self.index < len(self.searchedstring)):
                        if self.searchedstring[self.index] == target[0]:
                            flag = True
                            break
                        else:
                            self.index += 1
                            flag = False

                    return flag

        # It checks if the string to be matched with has reached its end.
        # If it has, it returns False
        elif len(self.searchedstring) == self.index:
            return False

        # It checks whether character of string to be matched with at a particular index is same as
        # the first character of the string to be matched
        elif self.searchedstring[self.index] == target[0]:
            self.charmatched += 1
            return self.searchPat(target[1:], self.index, self.charmatched)

        # It checks whether number of characters matched is greater than or less than zero
        else:
            if self.charmatched > 0:
                return False
            else:
                return self.searchPat(target, self.index, self.charmatched)


if __name__ == '__main__':
    source = SearchableStr(str(input("Enter the string to match with")))
    #target1 = str(input("enter the character to be matched"))
    # target2 = str(input("enter the prefix string to be matched"))
    target3 = str(input("enter the string to be matched"))
    # target4 = str(input("enter the pattern string to be matched with initial portion of the SearchableStr's instance"))
    target5 = str(input("enter the pattern string to be matched"))
    source.index = -1
    #print(source.searchChar(target1))
    #print(source.matchString(target2))
    print(source.searchString(target3))
    #print(source.matchPat(target4, -1))
    print(source.searchPat(target5, -1))



