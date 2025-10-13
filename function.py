# These are called common function. They are used in all data types.

# len
len('hello world')      # output: 11


#  max
max('hello world')        # output: w

# min
min('hello world')       # output: ' '

# sorted
sorted('hello world',reverse=True)     # Output: ['w','r','o','o','i','i','i','h','e','d',' ']




# These functions are used in only strings.

# Capitalize function
u='hello world'
u.capitalize()       # output: 'Hello world'
u.title()       # output: 'Hello World'
u.upper()       # output: 'HELLO WORLD'
u.lower()       # output: 'hello world'
'HeLLo WoRld' .swapcase()    # output: 'hEllO wOrLD'

# count function
'my name is utkarsh' .count('a')     # output: 2

# find function
'my name is utkarsh' .find('utkarsh')   # output: 9
'my name is utkarsh' .find('ram')   # output: -1

# index function
'my name is utkarsh' .index('utkarsh')   # output: 9
'my name is utkarsh' .index('ram')   # output: error

# endswith function
'my name is utkarsh' .endswith('sh')   # output: true
'my name is utkarsh' .endswith('sho')   # output: false

# startwith function
'my name is utkarsh' .startswith('my')   # output: true
'my name is utkarsh' .startswith('your')   # output: false

# format function
name='urkarsh'
gender='male'

'Hi my name is{} and I am a {}'.format(name,gender)   
# output: 'Hi i am utkarsh and i am a male.'

# isalnum (alphanumeric)
'utkarsh1234'.isalnum()  # output: true
'utkarsh1234%'.isalnum()  # output: false

# isalpha function
'utkarsh'.isalpha()   #output: true
'utkarsh12'.isalpha()  # output:False

# isdigit function
'1234'.isdigit()   # output: true
'utka1234'.isdigit   #output: false

# isidentifier function
'name1'.isidentifier()  #output:true
'1name',IndentationError()   # output:false
'first_name'.isidentifier()    # output:true
'first-name'.isidentifier()     # output:false


# split function
'Hi my name is utkarsh'.split()     # output: ['Hi','my','name','is','utkarsh']

# join function
"".join['Hi','my','name','is','utkarsh']    # outout:'Hi my name is utkarsh'

# replace function
'Hi my name is utkarsh'.replace('utkarsh','prakhar')    # output:'Hi my name is prakhar'

# strip function
'utkarsh'                                .strip()     # output:'utkarsh'
