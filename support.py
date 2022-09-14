from random import randint
from string import ascii_letters
from random import choice


class Support():

    def cpf_generator(self):
        cpf = str(randint(100000000, 999999999))
        new_cpf = cpf
        total = index = 0
        c = 10

        while True:
            total += int(new_cpf[index]) * c
            if c == 2:
                digit = 11 - (total % 11)
                if digit > 9:
                    digit = 0
                new_cpf += str(digit)
                if len(new_cpf) == 11:
                    return new_cpf
                total = index = 0
                c = 11
            c -= 1
            index += 1

    def mask_email_generator(self):
        c = 0
        mail = ""
        for c in range(16):
            mail += choice(ascii_letters)
            if c == 8:
                mail += '@'
            elif c == 12:
                mail += '.'

        return mail
