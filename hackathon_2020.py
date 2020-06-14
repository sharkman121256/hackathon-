print("Hi, I am Info_Bot, What would you like to know on COVID-19 or hear a joke?")
keywords = ["joke", "stats", "status", "covid-19", "covid", "thanks", "hospital", "symptoms", "symptom","hi"]
run = True
while(run):
  userInput = input()
  if userInput.lower() == "bye" :
    print("See ya later!")
    run = False
  else:
    inputValue = userInput.split(" ")
    printValue =""
    for inp in inputValue:
      match = next((value for value in keywords if inp.lower() == value), "")
      if match != "" :
        if(match == "joke"):
          print("Pick a number 1, 2, 3, ")
          joke_input = input()
          if joke_input == '1':
            printValue="Why do we tell actors to “break a leg?\nBecause every play has cast."
          elif joke_input == '2':
            printValue = "What do dentists call a astronaut\'s cavity\nA black hole!"
          if joke_input == '3':
            printValue = "What do you get when you cross a snowman with a vampire?\nA Frostbite"
          break
        elif(match == "hospital"):
          printValue = "One of the hopitals in Silicon Valley is the West Valley Center\nLink:\nsutterhealth.org/find-location/facility/west-valley-center "
          break
        elif(match == "symptoms" or match == "symptom"):
          printValue = "These are the symptoms of COVID-19:\n\nFever or chills\nCough\nShortness of breath or difficulty breathing\nFatigue\nMuscle or body aches\nHeadache\nNew loss of taste or smell\nSore throat\nCongestion or runny nose\nNausea or vomiting\nDiarrhea"
          break
        elif(match == "covid-19" or match == "covid"):
          printValue = "This link below will guide you to a CDC sheet on COVID-19:\n https://www.cdc.gov/coronavirus/2019-ncov/downloads/2019-ncov-factsheet.pdf"
          break
        elif(match == "thanks"):
          printValue = "Happy to help !"
        if(match == "stats" or match == "status"):
          printValue="You can find all the covid 19 stats in this website https://www.worldometers.info/coronavirus/"
        elif(match == 'hi'):
          printValue = "Hi, I am Info_Bot, What would you like to know on COVID-19 or hear a joke?"
          break
    if(printValue == ""):
      printValue = "Sorry, I do not know how to help at this moment."
    print(printValue)
