from flask import Flask,render_template,request

import time,random
def evaluation(word):

  correct_guess = ''
  remaining_attempts=10
  victory = 0

  for i in range(0,10):
    no_of_fails = 0
    time.sleep(0.1)
    print('-'*50)
    print("You have",remaining_attempts,"more tries")
    guess = input("guess a character:")
    correct_guess+=guess
    print("Your entered characters are: ",correct_guess)
  
    for char in word:
      if char in correct_guess:
        print (char+"*")
      else:
        print ("_"+"*")
        no_of_fails += 1
    
    if no_of_fails == 0: 
      victory=1       
      print ('You won')
      break
    if remaining_attempts==0:
      victory=0
      print("You lose, all 10 tries are over")
      break
    
    if guess not in word:
      print("Wrong")
      remaining_attempts -= 1
      if remaining_attempts==0:
        victory=0
        print("You lose, all 10 tries are over")
        break
    else:
      remaining_attempts -= 1
  return victory

app=Flask(__name__)

app.jinja_env.add_extension('jinja2.ext.loopcontrols')

@app.route('/')
def index():
    global word
    words=["water","computer","pencil","birthday","pizza","surprise"]
    word = random.choice(words)
    return render_template("index1.html",word=word)

@app.route('/game',methods=['get','post'])
def game():
    
    username=request.form['username']
    output=evaluation(word)
    return render_template("hangman3.html",word=word,username=username,output=output)


  
if __name__=='__main__':
    app.run(host="0.0.0.0",debug=True)
