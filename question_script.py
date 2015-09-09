import json
import os
import urllib2, urllib
import requests

#params:
    #guess is the current guess
    #min is the minimum possible value--true answer is somewhere above min
    #max is the maximum possible value--true answer is somewhere below the max

def make_guess(guess, min, max):
    url = 'http://52.8.142.239:8080/guess'
    payload = {"guess":guess}
    header = {'Content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers = header)

    j = json.loads(response.text)
    answer = j[u'message']

    #terminate the recursive call when the correct answer is obtained
    if answer == 'correct!':
        print("Answer found!!! The correct answer is: " + str(guess))
        return


    #if the current guess is too high, the true answer resides somewhere between the current guess and the min.
    #Thus, next guess should be the half-way point between min and the current guess,and max should be
    #updated to the current guess during the recursive call

    if answer == 'too high':
        print("made a guess of " + str(guess) + ", but it was too high... next guess is: " + str((min+guess)/2))
        make_guess((guess+min)/2, min, guess-1)

    #if the current guess is too low, the true answer resides somewhere between the current guess and the max
    #Thus, next guess should be the half-way point between min and the current guess, and min should be updated
    #to the current guess during the recusive call

    else:
        print("made a guess of " + str(guess) + ", but it was too low... next guess is: " + str((guess+max)/2))
        make_guess((guess+max)/2,guess+1, max)

if __name__ == '__main__':
    make_guess(50000, 0, 2147483648)