import speech_recognition
import pyttsx3
from datetime import date, datetime
import os
# Initialize

while True:
    
    robot_ear = speech_recognition.Recognizer()
    robot_mouth = pyttsx3.init()
    robot_brain = "" 
     
    # Listening
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.listen(mic)
    print("Robot:...")
    
    try:
        you = robot_ear.recognize_google(audio)
        
    except:
        continue
        you = ""
    print("You: "+you)
    
    # Understanding
    if you == "":
        robot_brain = "I can't hear you, please talk again"
    elif "hello" in you or "Hello" in you or "hey computer" in you:
        robot_brain="Hello boss"
    elif "today" in you and "date" in you :
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()  
        robot_brain = now.strftime("%H hours %M minutes %S seconds") 
    elif "wait" in you:
        
        print("Robot: "+"OK boss, press any key when you are ready")

        robot_mouth.say("OK boss, press any key when you are ready")
        robot_mouth.runAndWait() 
        os.system("pause")
    elif "bye" in you:
        robot_brain = "Good bye boss, see you later"
        print("Robot: "+robot_brain)

        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()        
        break
    elif "can you hear" in you:
        robot_brain = "Yeah, I can hear you"
    elif "study" in you or "My Study folder" in you:
        robot_brain = "OK boss, let try hard for your future"
        path = "C:/Users/Lenovo/Desktop/study"
        path = os.path.realpath(path)
        os.startfile(path)
    elif "music" in you:
        
        print("Robot: "+"OK boss, be relax")
        robot_mouth.say("OK boss, be relax")
        robot_mouth.runAndWait()
        path = "C:/Users/Lenovo/Desktop/study/Relax/Đen - Cô Gái Bàn Bên ft Lynk Lee (Official audio w-lyrics).mp4"
        path = os.path.realpath(path)
        os.startfile(path)
        #os.system("pause")
    elif "are you ready" in you:
        robot_brain = "yes, Im ready"   
    elif "secret folder" in you:
        robot_brain = "OK, wait a minutes, you need a password"
        print("Robot: "+robot_brain)

        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        os.system("python src/detection.py >Output")
        f = open("Output", "r")
        password = f.read()
        #print (password)
        if("V"in password):
            robot_brain = "Secret Folder opened successfully"
        else:
            robot_brain = "You are not my boss, bye"
            print("Robot: "+robot_brain)

            robot_mouth.say(robot_brain)
            robot_mouth.runAndWait()
            break
    elif "how are you" in you or "are you okay" in you:
        robot_brain = "I'm fine, thanks"
    elif "Wi-Fi password" in you or "wifi password" in you or "Wifi password" in you:
        
        print("Robot: "+"OK boss, here is the list of your saved wifi passwords")

        robot_mouth.say("OK boss, here is the list of your saved wifi passwords")
        robot_mouth.runAndWait()
        os.system("python src/saved_wifi.py")
    elif "your name" in you:
        computerName = os.environ['COMPUTERNAME']
        robot_brain="My name is " + computerName
    elif "information" in you and "system" in you:
        print("Robot: "+"OK boss, here are informations about system, boot time, CPU, memory, disk, network and GPU. Let see ")

        robot_mouth.say("OK boss, here are informations about system, boot time, CPU, memory, disk, network and GPU. Let see ")
        robot_mouth.runAndWait()
        os.system("python src/information.py")
    elif "translate" in you or "Translate" in you:
                
        print("Robot: "+"Yeah, please enter the text you need to translate, press 'x' when you want to stop")

        robot_mouth.say("Yeah, please enter the text you need to translate, press 'x' when you want to stop")
        robot_mouth.runAndWait()
        os.system("python src/translate.py")
    elif "weather" in you or "Weather" in you:
        print("Robot: "+"Here are informations about the weather today: ")

        robot_mouth.say("Here are informations about the weather today")
        robot_mouth.runAndWait()
        os.system("python src/weather.py >weather.txt")
        f = open("weather.txt", "r")
        weather = f.read()
        print(weather)
        robot_mouth.say(weather)
        robot_mouth.runAndWait()
    elif "sleep" in you or "Sleep" in you:
        print("Robot: "+"Yes, I will go to sleep ")
        robot_mouth.say("Yes, I will go to sleep")
        robot_mouth.runAndWait() 
    elif "restart" in you or "Restart" in you:
        print("Robot: "+"Yes, I will restart, see you later")
        robot_mouth.say("Yes, I will restart, see you later")
        robot_mouth.runAndWait() 
        os.system("shutdown /r /t 1")
    elif "shutdown" in you or "Shutdown" in you or"shut down"in you or "Shut down" in you:
        print("Robot: "+"Yes, I will shutdown, see you later")
        robot_mouth.say("Yes, I will shutdown, see you later")
        robot_mouth.runAndWait() 
        os.system("shutdown /s /t 1")
    else:
        robot_brain="Have a good day"

    print("Robot: "+robot_brain)

    # Speaking
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()