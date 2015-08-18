import json
import os
import urllib2, urllib
import requests

def make_guess(guess, prev_min, prev_max):
    url = 'http://52.8.142.239:8080/guess'
    payload = {"guess":guess}
    header = {'Content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers = header)

    j = json.loads(response.text)
    answer = j[u'message']

    if answer == 'correct!':
        print("Answer found!!! The correct answer is: " + str(guess))
        return

    #if the current guess is too high, the true answer resides somewhere between the current gues and the previous min
    if answer == 'too high':
        print("made a guess of " + str(guess) + ", but it was too high... next guess is: " + str((prev_min+guess)/2))
        make_guess((guess+prev_min)/2, prev_min, guess)

    #if answer was too low, next guess should be half-way between current guess and the previous max
    else:
        print("made a guess of " + str(guess) + ", but it was too low... next guess is: " + str((guess+prev_max)/2))
        make_guess((guess+prev_max)/2,guess, prev_max)

if __name__ == '__main__':
    make_guess(5000, 0, 2147483648)