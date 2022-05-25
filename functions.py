import sys
import numpy as np

def convert_rawdata2tsv(inputfilename, outputfilename):
    import re
    foutput = open(outputfilename, 'w')
    option=0
    
    # '^([\w]+) \((.+)\)\: (.+)$' perverted justice grooming Yim
    # '^([\w].+)\: (.+)$ ' normalConvo1-3 
    # '^([\d]+),(.+)$' bullyData_Label https://github.com/joshimiloni/Cyber-Bullying-Detection/tree/master/Bully-detection/datasets
    # '^([\w]+)\: (.+)\b (.+\d.+)$' Jake Lewis Pattern 2 (Text)
    # '^([\w].+) \-(.+)$' Jake Lewis Pattern 3 (Meetme.com)
    # '([^w].+) \((.+)\)\: (.+)$' Jagjen pattern
    # '^([\w].+)\: \((.+)\) (.+)' JoeBiden
    new_file = []
    if inputfilename=='data_JakeLewis.txt':
        try:
            # Make sure file gets closed after being iterated
            with open(inputfilename, 'r') as f:
            # Read the file contents and generate a list with each line
                lines = f.readlines()

            pattern1='^([\w]+) \((.+)\)\: (.+)$'
            pattern2='^([\w].+)\: (.+) (\d.+)$'
            pattern3='^([\w].+) \-(.+)$'

            # Iterate each line
            for line in lines:
            # Regex applied to each line
                match = re.search(pattern1, line)
                match2= re.search(pattern2, line)
                match3= re.search(pattern3, line)
                if match:
                    foutput.write(match.group(1)) # ID
                    foutput.write("\t")
                    foutput.write(match.group(2)) # Date
                    foutput.write("\t")
                    foutput.write(match.group(3)) # Message
                    foutput.write("\n")
                elif match2:
                    foutput.write(match2.group(1)) # ID
                    foutput.write("\t")
                    foutput.write(match2.group(3)) # Message
                    foutput.write("\t")
                    foutput.write(match2.group(2)) # Time
                    foutput.write("\n")
                elif match3:
                    foutput.write(match3.group(1)) # ID
                    foutput.write("\t\t")
                    foutput.write(match3.group(2)) # Message
                    foutput.write("\n")
                    
            foutput.close()
            f.close()
            return 1
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
            return 0
        except: #handle other exceptions such as attribute errors
            print("Unexpected error:", sys.exc_info()[0])
            return 0
    elif inputfilename=='data_jagjen2003.txt':
        try:
            # Make sure file gets closed after being iterated
            with open(inputfilename, 'r') as f:
            # Read the file contents and generate a list with each line
                lines = f.readlines()

            pattern='([^w].+) \((.+)\)\: (.+)$'

            # Iterate each line
            for line in lines:
            # Regex applied to each line
                match = re.search(pattern, line)

                if match:
                    foutput.write(match.group(1)) # ID
                    foutput.write("\t")
                    foutput.write(match.group(2)) # Date
                    foutput.write("\t")
                    foutput.write(match.group(3)) # Message
                    foutput.write("\n")

            foutput.close()
            f.close()
            return 1
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
            return 0
        except: #handle other exceptions such as attribute errors
            print("Unexpected error:", sys.exc_info()[0])
            return 0
    elif inputfilename=='Elon_Musk_interview.txt':
        try:
            # Make sure file gets closed after being iterated
            with open(inputfilename, 'r') as f:
            # Read the file contents and generate a list with each line
                lines = f.readlines()

            pattern='([^w].+)\: (.+)$'

            # Iterate each line
            for line in lines:
            # Regex applied to each line
                match = re.search(pattern, line)

                if match:
                    foutput.write(match.group(1)) # ID
                    foutput.write("\t")
                    foutput.write(match.group(2)) # Message
                    foutput.write("\n")

            foutput.close()
            f.close()
            return 2
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
            return 0
        except: #handle other exceptions such as attribute errors
            print("Unexpected error:", sys.exc_info()[0])
            return 0
    elif inputfilename=='Bill_Gates_interview.txt':
        try:
            # Make sure file gets closed after being iterated
            with open(inputfilename, 'r') as f:
            # Read the file contents and generate a list with each line
                lines = f.readlines()

            pattern='([^w].+)\: (.+)$'

            # Iterate each line
            for line in lines:
            # Regex applied to each line
                match = re.search(pattern, line)

                if match:
                    foutput.write(match.group(1)) # ID
                    foutput.write("\t")
                    foutput.write(match.group(2)) # Message
                    foutput.write("\n")

            foutput.close()
            f.close()
            return 2
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
            return 0
        except: #handle other exceptions such as attribute errors
            print("Unexpected error:", sys.exc_info()[0])
            return 0
    elif inputfilename=='normalConvo3.txt':
        try:
            # Make sure file gets closed after being iterated
            with open(inputfilename, 'r') as f:
            # Read the file contents and generate a list with each line
                lines = f.readlines()

            pattern='([^w].+)\: (.+)$'

            # Iterate each line
            for line in lines:
            # Regex applied to each line
                match = re.search(pattern, line)

                if match:
                    foutput.write(match.group(1)) # ID
                    foutput.write("\t")
                    foutput.write(match.group(2)) # Message
                    foutput.write("\n")

            foutput.close()
            f.close()
            return 2
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
            return 0
        except: #handle other exceptions such as attribute errors
            print("Unexpected error:", sys.exc_info()[0])
            return 0
    elif inputfilename=='Joe_Biden_60mins_interview.txt':
        try:
            # Make sure file gets closed after being iterated
            with open(inputfilename, 'r') as f:
            # Read the file contents and generate a list with each line
                lines = f.readlines()

            pattern='([^w].+)\: \((.+)\) (.+)$'

            # Iterate each line
            for line in lines:
            # Regex applied to each line
                match = re.search(pattern, line)

                if match:
                    foutput.write(match.group(1)) # ID
                    foutput.write("\t")
                    foutput.write(match.group(2)) # Time
                    foutput.write("\t")
                    foutput.write(match.group(3)) # message
                    foutput.write("\n")

            foutput.close()
            f.close()
            return 1
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
            return 0
        except: #handle other exceptions such as attribute errors
            print("Unexpected error:", sys.exc_info()[0])
            return 0
    elif inputfilename=='movieDialougue.v2.txt':
        try:
            # Make sure file gets closed after being iterated
            with open(inputfilename, 'r') as f:
            # Read the file contents and generate a list with each line
                lines = f.readlines()

            pattern='([^w].+)\: (.+)$'

            # Iterate each line
            for line in lines:
            # Regex applied to each line
                match = re.search(pattern, line)

                if match:
                    foutput.write(match.group(1)) # ID
                    foutput.write("\t")
                    foutput.write(match.group(2)) # Message
                    foutput.write("\n")

            foutput.close()
            f.close()
            return 2
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
            return 0
        except: #handle other exceptions such as attribute errors
            print("Unexpected error:", sys.exc_info()[0])
            return 0
    elif inputfilename=='normalConvo2.txt':
        try:
            # Make sure file gets closed after being iterated
            with open(inputfilename, 'r') as f:
            # Read the file contents and generate a list with each line
                lines = f.readlines()

            pattern='([^w].+)\: (.+)$'

            # Iterate each line
            for line in lines:
            # Regex applied to each line
                match = re.search(pattern, line)

                if match:
                    foutput.write(match.group(1)) # ID
                    foutput.write("\t")
                    foutput.write(match.group(2)) # Message
                    foutput.write("\n")

            foutput.close()
            f.close()
            return 2
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
            return 0
        except: #handle other exceptions such as attribute errors
            print("Unexpected error:", sys.exc_info()[0])
            return 0
    elif inputfilename=='normalConvo1.txt':
        try:
            # Make sure file gets closed after being iterated
            with open(inputfilename, 'r') as f:
            # Read the file contents and generate a list with each line
                lines = f.readlines()

            pattern='([^w].+)\: (.+)$'

            # Iterate each line
            for line in lines:
            # Regex applied to each line
                match = re.search(pattern, line)

                if match:
                    foutput.write(match.group(1)) # ID
                    foutput.write("\t")
                    foutput.write(match.group(2)) # Message
                    foutput.write("\n")

            foutput.close()
            f.close()
            return 2
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
            return 0
        except: #handle other exceptions such as attribute errors
            print("Unexpected error:", sys.exc_info()[0])
            return 0
    elif inputfilename=='Joe_Biden_60mins_interview.txt':
        try:
            # Make sure file gets closed after being iterated
            with open(inputfilename, 'r') as f:
            # Read the file contents and generate a list with each line
                lines = f.readlines()

            pattern='^([\w].+)\: \((.+)\) (.+)'

            # Iterate each line
            for line in lines:
            # Regex applied to each line
                match = re.search(pattern, line)

                if match:
                    foutput.write(match.group(1)) # ID
                    foutput.write("\t")
                    foutput.write(match.group(2)) # Date
                    foutput.write("\t")
                    foutput.write(match.group(3)) # Message
                    foutput.write("\n")

            foutput.close()
            f.close()
            return 1
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
            return 0
        except: #handle other exceptions such as attribute errors
            print("Unexpected error:", sys.exc_info()[0])
            return 0
        
    elif inputfilename=='data_blandmtthw.txt':
        try:
            # Make sure file gets closed after being iterated
            with open(inputfilename, 'r') as f:
            # Read the file contents and generate a list with each line
                lines = f.readlines()

            pattern='([^w].+) \[(\d.+)\]: (.+)$'

            # Iterate each line
            for line in lines:
            # Regex applied to each line
                match = re.search(pattern, line)

                if match:
                    foutput.write(match.group(1)) # ID
                    foutput.write("\t")
                    foutput.write(match.group(2)) # Time
                    foutput.write("\t")
                    foutput.write(match.group(3)) # Message
                    foutput.write("\n")

            foutput.close()
            f.close()
            return 1
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
            return 0
        except: #handle other exceptions such as attribute errors
            print("Unexpected error:", sys.exc_info()[0])
            return 0
    
    else:
         pattern  = '^([\w]+) \((.+)\)\: (.+)$' # designed with https://regex101.com/
         try:
             # Make sure file gets closed after being iterated
             with open(inputfilename, 'r') as f:
             # Read the file contents and generate a list with each line
                 lines = f.readlines()

             # Iterate each line
             for line in lines:
             # Regex applied to each line
                 match = re.search(pattern, line)
                 if match:
                     foutput.write(match.group(1)) # ID
                     foutput.write("\t")
                     foutput.write(match.group(2)) # Date
                     foutput.write("\t")
                     foutput.write(match.group(3)) # Message
                     foutput.write("\n")

             foutput.close()
             f.close()
             return 1
         except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
            return 0
         except: #handle other exceptions such as attribute errors
            print("Unexpected error:", sys.exc_info()[0])
            return 0
    


def determineBullying(word, dictionary):
    found = dictionary[dictionary['Keywords'] == word]
    if len(found) == 0:  # no matched word found
        return 0
    return 1    # match word found


def determineGrooming(word,dictionary):
    found = dictionary[dictionary['Keywords'] == word]
    if len(found) == 0:  # no matched word found
        return 0
    return 1    # match word found


def determinePolarities(word, dictionary):
    found = dictionary[dictionary['Words'] == word]
    if len(found) == 0:   # no matched word found so assume word is neutral
        return 0
    if (found['Positivity'].iloc[:1] == 'positive').bool():  # positive word
        return 1
    elif (found['Positivity'].iloc[:1] == 'negative').bool():    # negative word
        return -1
    
    return -999    # unkown error


def checkIfStop(word, dictionary):
    found = dictionary[dictionary['StopWords'] == word]

    if len(found)!=0:
        return 1
    else :
        return 0
