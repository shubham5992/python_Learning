# This script contains examples of dictionaries

# Example 1: Simple dictionary
info = {
    "Name": "shubham",
    "Learning": "python",
    "Scope": "devops"
}

print(info)
info["Name"] = "Tiwari"
print(info)

# Example 2: Nested dictionary
Info = {
    "Name": "Shubham",
    "Score": {
        "maths": 90,
        "science": 89,
        "hindi": 33
    },
    "language": "English"
}

print(Info["Score"]["hindi"])
