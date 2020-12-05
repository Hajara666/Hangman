from flask import Flask,render_template,request
#import flask for flask,render_template for jinja2 and request for form details

import time,random
def evaluation(word):

  correct_guess = ''
  remaining_attempts=10
  victory = 0

  for i in range(0,10):#allows the user for maximum 10 times only
    no_of_fails = 0
    time.sleep(0.1)
    print('-'*50)
    print("You have",remaining_attempts,"more tries")
    guess = input("guess a character:")#get user input
    correct_guess+=guess
    print("Your entered characters are: ",correct_guess)#prints the sofar entered letters

    for char in word:#loops for the length of the word
      if char in correct_guess:
        print (char+"*")
      else:
        print ("_"+"*")
        no_of_fails += 1

    if no_of_fails == 0:#it means all the letters are correctly guessed
      victory=1
      print ('You won')
      break
    if remaining_attempts==0:#all 10 attempts are finished and exits the for loop
      victory=0
      print("You lose, all 10 tries are over")
      break

    if guess not in word:#print wrong message whenever user enters a wrong guess
      print("Wrong")
      remaining_attempts -= 1
      if remaining_attempts==0:#all 10 attempts are finished and exits the for loop
        victory=0
        print("You lose, all 10 tries are over")/c/Users/Redi/Hangman

        break
    else:
      remaining_attempts -= 1
  return victory

app=Flask(__name__)


@app.route('/',methods=['get','post'])
def index():
    global word#global ,because going to use in another function
    words=["water","computer","pencil","birthday","pizza","surprise"]
    word = random.choice(words)#randomly creates a word every time in index site
    no_of_letters=len(word)#length of the word
    return render_template("index1.html",word=word,no_of_letters=no_of_letters)

@app.route('/game',methods=['get','post'])
def game():

    username=request.form['username']
    output=evaluation(word)#calls fn evaluation() with argument word
    return render_template("hangman3.html",word=word,username=username,output=output)



if __name__=='__main__':
    app.run(host="0.0.0.0",debug=True)
