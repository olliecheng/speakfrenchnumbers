from gtts import gTTS
import pyglet
import random
from num2words import num2words
import time


#load AVBin
pyglet.lib.load_library('avbin')
pyglet.have_avbin=True

minimumRange = raw_input("Lowest number [1]: ")
maximumRange = raw_input("Highest number [100]: ")
total = raw_input("Test with how many numbers [10]: ")

defaults = {"minimumRange": 1, "maximumRange": 100, "total": 10}

try:
    int_item = int(minimumRange)
    minimumRange = int_item
except ValueError:
    minimumRange = defaults["minimumRange"]

try:
    int_item = int(maximumRange)
    maximumRange = int_item
except ValueError:
    maximumRange = defaults["maximumRange"]

try:
    int_item = int(total)
    total = int_item
except ValueError:
    total = defaults["total"]

maximumRange += 1

numbers = range(minimumRange, maximumRange)
testNumbers = []

for _ in range(total):
    while True:
        num = random.choice(numbers)
        if num not in testNumbers:
            testNumbers.append(num)
            break

correct = 0
wrong = 0

q_times = []
for number in testNumbers:
    word = num2words(number, lang="fr")
    tts = gTTS(text=word, lang="fr")
    tts.save("word.mp3")

    player = pyglet.media.Player()
    speech = pyglet.media.load("word.mp3", streaming=False)

    start = time.time()
    player.queue(speech)
    player.queue(speech)
    player.play()

    word_i = raw_input("What was the word? ")
    end = time.time()
    player.pause()

    try:
        num = int(word_i)
    except ValueError:
        num = "FAIL"
    if word_i.strip().lower() == word.strip().lower() or (num != "FAIL" and num2words(num, lang="fr") == word):
        raw_input("Correct! Press Enter to continue...")
        correct += 1
    else:
        print("*"*20)
        raw_input("Wrong... It was actually {word}. Press Enter to continue.\n".format(word=word)+"*"*20)
        wrong += 1
    q_times.append(end-start)

    player.delete()


percent = correct*100/float(total)
print "Good job, {percent}%!".format(percent=percent)
print "You chose {total} numbers out of a list, from {min}-{max}.".format(total=total, min=minimumRange, max=maximumRange-1)

_total = 0
for item in q_times: _total += item
average = _total/total
print "You took an average of %s seconds per question." % average
raw_input("Enter to continue...")
