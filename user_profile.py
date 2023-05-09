""" 8- 13 start with userprofile, build a profile of myself
name, last name, 3 other characteristics"""


def build_profile(name, last_name, **user_profile):
    """ Take some user arguments and return a dictionary """
    user_profile["name"] = name
    user_profile["last name"] = last_name
    return user_profile


profile = build_profile("arturo", "mendoza", city="Metepec",
                        activity="programming", language="python")
print(profile)
