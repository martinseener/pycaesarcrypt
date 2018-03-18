#!/usr/bin/env python
# # -*- coding: utf-8 -*-

__version__ = '1.0.0'


class pycaesarcrypt(object):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def caesar(self, string, shift):
        result = ''
        for char in string:
            if char.isalpha():
                index = (self.alphabet.find(char.lower()) + shift) % 26
                if char.isupper():
                    result += self.alphabet[index].upper()
                else:
                    result += self.alphabet[index]
            else:
                result += char
        return result

    def encrypt(self, plaintext, shift):
        return self.caesar(plaintext, shift)

    def decrypt(self, chiffre, shift):
        return self.caesar(chiffre, -shift)

    def rot13(self, string, mode=True):
        if mode is True:
            return self.encrypt(string, 13)
        else:
            return self.decrypt(string, 13)


if __name__ == '__main__':
    print('You have to import this module in order to use it.')
