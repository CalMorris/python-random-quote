import random 

def main_function():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1

  i = 0
  quotes_to_print = []

  while i < 3:
    i+=1
    rnd = random.randint(0, last)
    quotes_to_print.append(quotes[rnd][:-1])

  print(quotes_to_print)



def addQuote (file, quote):
  with open(file, 'a') as f:
    f.write(quote)

addQuote('quotes.txt', 'this is a test quote to add to the document')
if __name__== "__main__":
  main_function()