#Problema LeetCode 28

#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

#Dados dos strings hay que encontrar la primera ocurrencia de la segunda en la primera.
#Si no se encuentra la segunda cadena en la primera, se devuelve -1.

#Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

#ejemplos con imput:
haystack = input("Introduce la cadena haystack: ")
needle = input("Introduce la cadena needle: ")

#ejemplos con variables predeterminadas (remover # para que funcione y comentar ejemplos con imput):
#haystack = "sadbutsad"
#needle = "sad"

if needle in haystack:
    (print("La subcadena " + needle + " se encuentra en la cadena " + haystack + " en la posicion " + str(haystack.index(needle)) + "."))
else:
    print(print("La subcadena " + needle + " no se encuentra en la cadena " + haystack + " posicion -1."))



