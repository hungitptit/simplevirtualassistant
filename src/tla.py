import speech_recognition
import pyttsx3
from datetime import date, datetime

import os

# Initialize
vi_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An"
birthdaySong = "C:/Users/Lenovo/Desktop/study/Machine_learning/VA/Secret Folder/HappyBirthday-VA_9ey.mp3"
while True:
    
    robot_ear = speech_recognition.Recognizer()
    robot_mouth = pyttsx3.init()
    robot_mouth.setProperty('voice', vi_voice_id)
    robot_brain = ""
    # Listening
    
    with speech_recognition.Microphone() as mic:
        print("Robot: Tôi đang nghe")
        audio = robot_ear.listen(mic)
    print("Robot:...")
    try:
        you = robot_ear.recognize_google(audio,language='vi-VN')
    except:
        continue
        you = ""

    print("Bạn: "+you)
    

    # Understanding
    if you == "":
        robot_brain = "Xin lỗi, tôi không nghe rõ"
    elif "Chào " in you or "chào" in you :
        robot_brain="Chào ông chủ"
    elif "nay" in you and "ngày" in you:
        today = date.today()
        robot_brain = today.strftime("%d/%m/%Y")
    
    elif "giờ" in you:
        now = datetime.now()  
        robot_brain = now.strftime("%H:%M:%S") 
    elif "tạm biệt" in you:
        robot_brain = "Tạm biệt, hẹn gặp lại"
        print("Robot: "+robot_brain)    
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    elif "đợi" in you or "chờ" in you or "Đợi" in you or "Chờ" in you:
        
        print("Robot: "+"Bấm phím bất kì khi nào bạn cần gọi tôi nhé")

        robot_mouth.say("Bấm phím bất kì khi nào bạn cần gọi tôi nhé")
        robot_mouth.runAndWait() 
        os.system("pause")
    
    elif "nghe" in you and "không" in you:
        robot_brain = "Có, tôi nghe rồi ạ"
   
    elif "học" in you or "thư mục học tập" in you:
        robot_brain = "Được bạn ơi, cố gắng vì tương lai nhé"
        path = "C:/Users/Lenovo/Desktop/study"
        path = os.path.realpath(path)
        os.startfile(path)

    
        #os.system("pause")
    
    elif "sẵn sàng chưa" in you:
        robot_brain = "Tôi sẵn sàng"   
    elif "thư mục bí mật" in you:
        robot_brain = "Đợi tí nhé, bạn cần mật khẩu cử chỉ tay"
        print("Robot: "+robot_brain)

        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        os.system("python src/detection.py >Output")
        f = open("Output", "r")
        password = f.read()
        #print (password)
        if("V"in password):
            robot_brain = "Đúng mật khẩu, mở khóa thành công"
        else:
            robot_brain = "Mày không phải bạn Hưng tao, cút, đánh chết cha mày giờ"
            print("Robot: "+robot_brain)

            robot_mouth.say(robot_brain)
            robot_mouth.runAndWait()
            os.system("pause")
            break
    elif "khỏe không" in you or "Khỏe không" in you:
        robot_brain = "Tôi lúc nào chả khỏe, bạn cứ hỏi thừa" 
    elif "không dây" in you or "wi-fi" in you:
        
        print("Robot: "+"Vâng, Dưới đây là danh sách mật khẩu wifi đã lưu của bạn ạ")

        robot_mouth.say("Vâng, Dưới đây là danh sách mật khẩu wifi đã lưu của bạn ạ")
        robot_mouth.runAndWait()
        os.system("python src/saved_wifi.py")
    elif "dịch" in you or "Dịch" in you:
                
        print("Robot: "+"Vâng, bạn nhập văn bản cần dịch đi ạ, khi nào muốn dừng thì bạn nhập 'x' nhé")

        robot_mouth.say("Vâng, bạn nhập văn bản cần dịch đi ạ, khi nào muốn dừng thì bạn nhập 'x' nhé")
        robot_mouth.runAndWait()
        os.system("python src/dich.py")
    elif "thông tin" in you:
        print("Robot: "+"Được bạn, Đây là thông tin về hệ thống, thời điểm khởi động máy, CPU, bộ nhớ, ổ đĩa, mạng và GPU. Mời bạn xem ")

        robot_mouth.say("Được bạn, Đây là thông tin về hệ thống, thời điểm khởi động máy, CPU, bộ nhớ, ổ đĩa, mạng và GPU. Mời bạn xem ")
        robot_mouth.runAndWait()
        os.system("python src/information.py")
    
    elif "ngủ " in you or "Ngủ" in you:
        print("Robot: "+"Vâng, tôi ngủ đây ")
        robot_mouth.say("Vâng, tôi ngủ đây ")
        robot_mouth.runAndWait() 
        os.system("rundll32.exe Powrprof.dll,SetSuspendState Sleep")
    elif "khởi động lại" in you or "Khởi động lại" in you:
        print("Robot: "+"Vâng, tôi khởi động lại đây ")
        robot_mouth.say("Vâng, tôi khởi động lại đây ")
        robot_mouth.runAndWait() 
        os.system("shutdown /r /t 1")
    elif "tắt" in you or "Tắt" in you or "nghỉ ngơi" in you or "Nghỉ ngơi" in you:
        print("Robot: "+"Vâng, tôi nghỉ đây, gặp lại sau nhé ")
        robot_mouth.say("Vâng, tôi nghỉ đây, gặp lại sau nhé ")
        robot_mouth.runAndWait() 
        os.system("shutdown /s /t 1") 
    elif "Thời tiết" in you or "thời tiết" in you or "thông tin thời tiết"in you:
        print("Robot: "+"Vâng, đây là thông tin thời tiết ngày hôm nay: ")
        robot_mouth.say("Vâng, đây là thông tin thời tiết ngày hôm nay")
        robot_mouth.runAndWait()
        os.system("python src/thoitiet.py ")
    elif "thay bạn" in you or "mua máy mới" in you or "thay máy"in you:
        print("Robot: "+"Đừng bạn ơi, tôi còn hữu dụng lắm")
        robot_mouth.say("Đừng bạn ơi, tôi còn hữu dụng lắm")
        robot_mouth.runAndWait()
    elif "hack Facebook" in you or "hack facebook" in you :
        print("Robot: "+"Tôi không biết")
        robot_mouth.say("Tôi không biết")
        robot_mouth.runAndWait()       
    
    else:
        robot_brain="Chúc bạn một ngày vui vẻ"
    print("Robot: "+robot_brain)

    # Speaking
    
    robot_mouth.say(robot_brain)


    robot_mouth.runAndWait()

  