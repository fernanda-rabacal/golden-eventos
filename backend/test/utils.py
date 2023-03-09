import random
from string import ascii_lowercase, ascii_uppercase, digits


VALID_CHARS = ascii_lowercase + ascii_uppercase + digits


def random_email() -> str:
    login = ''.join(random.sample(VALID_CHARS, random.randint(4, 8)))
    while login[0].isdigit():
        login = random.choice(VALID_CHARS) + login[1:]

    servers=['@gmail','@yahoo','@redmail','@hotmail','@bing']
    email = login + random.choice(servers)

    tlds=['.com','.in','.gov','.ac.in','.net','.org']
    email = email + random.choice(tlds)
    return email

def random_password() -> str:
    return ''.join(random.sample(VALID_CHARS, random.randint(4, 8)))