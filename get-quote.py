import random

def ain():
  f = open("quotes.txt")
  quotes = f.readlines()
  last = len(quotes)-1
  rnd = random.randint(0,last)
  f.close()
  print(quotes[rnd])

if __name__== "__main__":
  ain()
