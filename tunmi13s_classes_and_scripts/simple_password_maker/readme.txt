Simple Password maker
This isn't really a class, but a set of random functions I made to easily come up with passwords and what not. Of course, the algorithm isn't top-class, but it should hopefully help those who just need something simple to use. 
If you plan to encrypt data, my advice is either to hash the data using the string hash function, or use string encrypt. For more details consult the BGT help document.
Another thing you can do is use the simple password maker to create a password for the string you'd like to encrypt, and then encrypt the data that way.
Note, before using these functions, be sure to put this line at the top of your script.
#include "password_functs.bgt"
Or
#include "file_path/password_functs.bgt"

Alphanumeric
string generate_alphanumeric_password(int length=10)
Parameters:
length: The length of the password to generate. Default is 10.
Return value:
The string containing the password. No errors are given unless you actually do something dumb, such as setting the password length to 0 or lower.
Remarks:
This script generates an alphanumeric password (with both letters and numbers). There are also uppercase letters thrown in there for extra security.
Example:
string protect_me=generate_alphanumeric_password(5);
alert("Hi,","I'm protected by a password, but I trust you enough so I'll let you know what it is. My password is: "+protect_me+".");

Numeric
string generate_numeric_password(int length=10)
Parameters:
length: The length of the password to generate. Default is 10.
Return value:
The string containing the password. No errors are given unless you actually do something dumb, such as setting the password length to 0 or lower.
Remarks:
This script generates a numeric password with pure digits.
Example:
string protect_me=generate_numeric_password(5);
alert("Hi,","I have a PIN number set on my computer to access my files. But today, I will give you full access! Here you go: "+protect_me+".");

Alphabetic
string generate_alphabetic_password(int length=10)
Parameters:
length: The length of the password to generate. Default is 10.
Return value:
The string containing the password. No errors are given unless you actually do something dumb, such as setting the password length to 0 or lower.
Remarks:
This script generates an alphabetic password with uppercase and lowercase letters.
Example:
string protect_me=generate_alphabetic_password(5);
alert("Hi,","I have a code set on my computer to access my files. But today, I will give you full access! Here you go: "+protect_me+".");

Alphanumeric plus
string generate_alphanumeric_password_plus(int length=10)
Parameters:
length: The length of the password to generate. Default is 10.
Return value:
The string containing the password. No errors are given unless you actually do something dumb, such as setting the password length to 0 or lower.
Remarks:
This script generates an alphanumeric password, with the exception that this version also contains symbols of various types.
string protect_me=generate_alphanumeric_password_plus();
alert("Hi,","I'm protected by a very strong password, but I trust you enough so I'll let you know what it is. My password is: "+protect_me+".");
