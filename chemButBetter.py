import re
import os
os.system("cls" if os.name == "nt" else "clear")
# list of elements and there atomic mass
periodicTable = {
    'H': 1.0079,
    'He': 4.0026,
    'Li': 6.941,
    'Be': 9.0122,
    'B': 10.811,
    'C': 12.0107,
    'N': 14.0067,
    'O': 15.9994,
    'F': 18.9984,
    'Ne': 20.1797,
    'Na': 22.9897,
    'Mg': 24.305,
    'Al': 26.9815,
    'Si': 28.0855,
    'P': 30.9738,
    'S': 32.065,
    'Cl': 35.453,
    'Ar': 39.948,
    'K': 39.0983,
    'Ca': 40.078,
    'Sc': 44.9559,
    'Ti': 47.867,
    'V': 50.9415,
    'Cr': 51.9961,
    'Mn': 54.938,
    'Fe': 55.845,
    'Co': 58.9332,
    'Ni': 58.6934,
    'Cu': 63.546,
    'Zn': 65.39,
    'Ga': 69.723,
    'Ge': 72.64,
    'As': 74.9216,
    'Se': 78.96,
    'Br': 79.904,
    'Kr': 83.798,
    'Rb': 85.4678,
    'Sr': 87.62,
    'Y': 88.906,
    'Zr': 91.224,
    'Nb': 92.906,
    'Mo': 95.94,
    'Tc': 98,
    'Ru': 101.07,
    'Rh': 102.91,
    'Pd': 106.42,
    'Ag': 107.87,
    'Cd': 112.411,
    'In': 114.82,
    'Sn': 118.71,
    'Sb': 121.76,
    'Te': 127.6,
    'I': 126.9045,
    'Xe': 131.293,
    'Cs': 132.91,
    'Ba': 137.327,
    'La': 138.91,
    'Ce': 140.12,
    'Pr': 140.9077,
    'Nd': 144.24,
    'Pm': 145,
    'Sm': 150.36,
    'Eu': 151.964,
    'Gd': 157.25,
    'Tb': 158.9253,
    'Dy': 162.5,
    'Ho': 164.9303,
    'Er': 167.259,
    'Tm': 168.9342,
    'Yb': 173.04,
    'Lu': 174.967,
    'Hf': 178.49,
    'Ta': 180.9479,
    'W': 183.84,
    'Re': 186.207,
    'Os': 190.23,
    'Ir': 192.22,
    'Pt': 195.08,
    'Au': 196.97,
    'Hg': 200.59,
    'Tl': 204.3833,
    'Pb': 207.2,
    'Bi': 208.9804,
    'Po': 209,
    'At': 210,
    'Rn': 222,
    'Fr': 223,
    'Ra': 226,
    'Ac': 227,
    'Th': 232.0381,
    'Pa': 231.0359,
    'U': 238.0289,
    'Np': 237,
    'Pu': 244,
    'Am': 243,
    'Cm': 247,
    'Bk': 247,
    'Cf': 251,
    'Es': 252,
    'Fm': 257,
    'Md': 258,
    'No': 259,
    'Lr': 262,
    'Rf': 267,
    'Db': 268,
    'Sg': 269,
    'Bh': 270,
    'Hs': 269,
    'Mt': 277,
    'Ds': 281,
    'Rg': 282,
    'Cn': 285,
    'Nh': 286,
    'Fl': 290,
    'Mc': 290,
    'Lv': 293,
    'Ts': 294,
    'Og': 294,
}
validity = '''
When Entering Compound:
No spaces
Capitals for first letter of an element and lowercase if second
Subscript (if any) uses regular numbers and put after the element
For compounds surround them with brackets and subscripts (if any) at the end
eg: "Ca3(PO4)2" or H2O
'''


def inputCompound(): # retruns a valid input for compound
    while True:
        compound = input('Enter Compound: ')

        if compound.lower() == 'end': #ending if empy string is returned
            print('Ending')
            quit() # ends the program
        elif compound.lower() == 'help': # if help is selected
            print(validity) # explains rules on how to input correctly
        else:
            if re.search('[^a-zA-Z0-9()]+', compound): # searches for invalid characters
                print('Invalid Characters\n')
        
            elif compound.count('(') != compound.count(')'): #checks if an equal number of ( to ) are enterd
                print('Unequal number of brackets\n')
            else: 
                elementsAmount = breakUpCompound(compound) # breaks the program up into the dict
                for element in elementsAmount: # checks if each one is an element
                    if element not in periodicTable:
                        print(f'Not a valid element: {element}\n')
                    else:
                        return compound, elementsAmount # returns the compound and the dictonary if all elements are correct

def breakUpCompound(compound):
    elementsAmount = {}
    elements = re.findall('[A-Z][a-z]?\d*|\([^)]+\)\d*', compound) # splits elements up in the compound
    # print(elements) # look here if u want
    for element in elements:
        if '(' in element:
            removeBrackets(element, elementsAmount) # takes parts of the compound with brackets and handles them seperatly
            elements.pop(elements.index(element)) # removes the element with brackets from the list
    elementsAmount = elementsToDict(elementsAmount, elements, 1) # takes a list of elements and converts them into dictionary from
    return elementsAmount

def removeBrackets(brackets, elementsAmount): # takes parts of the compound with brackets and handles them seperatly
    brackets = brackets[1:] # removes first char which is a bracket
    if brackets[-1] == ')': # if no coefficent
        coefficient = 1
        brackets = brackets[:-1] # remove last char which is a bracket
    else:
        match = re.match('(\w+)\)(\d+)', brackets) # matches inside the brackets and the outside
        if match:
            brackets = match.group(1) # gets the first match
            coefficient = int(match.group(2)) # gets the second match
    elements = re.findall('[A-Z][a-z]?\d*|\([^)]+\)\d*', brackets) # gets the elements that are inside the brackets
    elementsToDict(elementsAmount, elements, coefficient) # takes a list of elements and converts them into dictionary from

def elementsToDict(elementsAmount, elementsList, coefficient): # takes a list of elements and converts them into dictionary from
    for element in elementsList:
        parts = re.split('(\d+)', element) # splits the element and its coefficent
        parts.append('1') # adds 1 on the end so  an element with no coefficent will be 1
        if parts[0] in elementsAmount: # if element already in the dic
            elementsAmount[parts[0]] += int(parts[1]) * coefficient # adds the element times its coefficent
        else:
            elementsAmount[parts[0]] = int(parts[1]) * coefficient # adds the new element times its coefficent
    return elementsAmount #return dict

def dictToMolarMass(elementsAmount):
    molarMass = 0
    for element in elementsAmount:
        molarMass += periodicTable[element] * elementsAmount[element] # finds the mass of each element * total appearences and adds them
    return round(molarMass, 4)

def percentage(elementsAmount, molarMass, target): # finds the percentage of the mass an element is
    return round(periodicTable[target] * elementsAmount[target] / molarMass * 100, 4) # mass of 1 element * total appearences / total mass

# testers some arent real compounds but it doesnt matter       
# 'H2O'
# 'CO2'
# 'Ba(OH)2'
# 'Pb(NO3)2'
# 'H2O(H2O)2'
########## main program ##########
print('For help write "help"\nTo end program leave blank and press enter')

while True:
    compound, elementsAmount = inputCompound() # inputs the compound and makes dict on everyelement and how many times they appear
    molarMass = dictToMolarMass(elementsAmount) # finds molar mass

    print(f'\n\nMolar mass {molarMass}')
    print('\nPercentage of weight in the compound:')

    for element in elementsAmount:
        print(f'{element}: {percentage(elementsAmount, molarMass, element)}') # prints the elements percentage
    print('\n')