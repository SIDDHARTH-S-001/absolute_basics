Find the bash type: `ps | grep $$` // usually of type 'bash' <br>
Find the bash path: `which bash` // like /usr/bin/bash <br>

#### Referencing the variable 
A backslash `\` is used to escape special character meaning
```
PRICE_PER_APPLE=5
echo "The price of an Apple today is: \$HK $PRICE_PER_APPLE"
```

Encapsulating the variable name with ${} is used to avoid ambiguity
```
MyFirstLetters=ABC
echo "The first 10 letters in the alphabet are: ${MyFirstLetters}DEFGHIJ"
```
Encapsulating the variable name with "" will preserve any white space values
```
greeting='Hello        world!'
echo $greeting" now with spaces: $greeting"
```

#### Passing arguments
The variable `$#` holds the number of arguments passed to the script. <br>
The variable `$@` holds a space-delimited string of all arguments passed to the script. <br>

##### Arrays
Array naming is the same as variables naming. An array is initialized by assign space-delimited values enclosed in () <br>
The total number of elements in the array is referenced by `${#arrayname[@]}` <br>
The array elements can be accessed with their numeric index. The index of the first element is 0. <br>

#### Operations
Simple arithmetics on variables can be done using the arithmetic expression: `$((expression))`













