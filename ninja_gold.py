from flask import Flask, render_template, request, redirect, session
from random import randint

app = Flask(__name__)
app.secret_key = 'coolio'



@app.route("/")
def index():
    
    gold_count = request.args.get('gold_count')
    isMessage = request.args.get('isMessage')

    if not isMessage:
        session['activitiesLog'] = ''

  
    if not gold_count:
        session['gold_counter'] = 0

    print(session['activitiesLog'])
    print(isMessage)

    return render_template('index.html')

@app.route("/process_money", methods=["POST"])
def change_gold():
    location = request.form["location"]

    if location == 'farm':
        win = True
        farmGold = randint(10, 20)
        farmGoldMessage = f'You gained {farmGold} amount of gold'
        session['gold_counter'] += farmGold 
        session['activitiesLog'] = session['activitiesLog'] + farmGoldMessage
        print(session['activitiesLog'])
        

    elif location == 'cave':
        win = True
        caveGold = randint(5, 10)
        caveGoldMessage = f'You gained {caveGold} gold'
        session['gold_counter'] += caveGold
        session['activitiesLog'] += caveGoldMessage

    elif location == 'house':
        win = True
        houseGold = randint(2, 5)
        houseGoldMessage = f'You gained {houseGold} gold'
        session['gold_counter'] += houseGold
        session['activitiesLog'] += houseGoldMessage
        

    elif location == 'casino':
        casinoGold = randint(-50,50)
        casinoGainGoldMessage = f' You gained {casinoGold}  of gold'
        casinoLoseGoldMessage = f'You lost {casinoGold *-1}  of gold'
        session['gold_counter'] += casinoGold
        if casinoGold >= 0:
            session['activitiesLog'] += casinoGainGoldMessage
            win = False
        else:
            session['activitiesLog'] += casinoLoseGoldMessage 
            win = True   
    if len(session['activitiesLog']) > 0:
        isMessage = 'True'
      
        

       
    gold_count = session['gold_counter']
        
    return redirect("/?gold_count={}&isMessage={}".format(gold_count, isMessage))    



if __name__ == '__main__':
    app.run(debug=True)