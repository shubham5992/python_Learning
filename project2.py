
# This project is a simple Python script that generates a random password of length 12. It uses a combination of letters (both uppercase and lowercase), digits, and punctuation symbols. The random.choice() function randomly selects characters from this combination and adds them to the password string until it reaches the desired length. Finally, it prints out the generated password.

import random
import string

paas_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range (paas_len):
    password += random.choice(charValues)

print("your random password is : ", password)



