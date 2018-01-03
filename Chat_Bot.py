import telegram
import pygraphviz
from time import sleep
from transitions import State
from transitions.extensions import GraphMachine as Machine

states = ['open', 'year_done', 'month_done', 'day_done']
transitions = [['in_year', 'open', 'year_done'], ['in_month', 'year_done', 'month_done'], ['in_day', 'month_done', 'day_done']]
class Game(Machine):
	pass
machine = Game(states = states, transitions = transitions, initial = 'open')
print(machine.state)

BOT_TOKEN = "451025509:AAFHZWnDoB2bZuLpIn8u6hP01Slxd0mC0Ik"
bot = telegram.Bot(BOT_TOKEN)
machine.get_graph().draw('state.png', prog = 'dot')
status = bot.set_webhook()
def num_test(te):
    #print(te)
    if(te == '0' or te == '1' or te == '2' or te == '3' or te == '4' or te == '5' or te == '6' or te == '7' or te == '8' or te == '9'):
        return 1
    else:
        return -1
def year_test(ye):
    if(int(ye) % 400 == 0):
        return 1
    elif(int(ye) % 100 == 0):
        return -1
    elif(int(ye) % 4 == 0):
        return 1
    else:
        return -1
def main():
    state = 0
    lastmsgid = 0
    year = 0
    month = 0
    day = 0
    choice = 0
    Updates = bot.getUpdates()
    if(len(Updates) > 0):
        lastmsgid = Updates[-1]["update_id"]
    while(True):
        Updates = bot.getUpdates(offset=lastmsgid, timeout = 1)
        Updates = [Update for Update in Updates if Update["update_id"] > lastmsgid]
        for Update in Updates:
            is_right = 1
            text = Update["message"]["text"]
            msg_id = Update["update_id"]
            user_id = Update["message"]["from_user"]["id"]
            lastmsgid = msg_id
            print(msg_id, text);
            #bot.sendMessage(user_id, text)
            if(text == '/start'):
                machine.set_state('open')
                year = 0
                month = 0
                day = 0
                year_left = 0
                bot.sendMessage(user_id, '請輸入生日年份(西元1~2017)')
            else:
                if(machine.state == 'open'):
                    if(len(text) <= 4):
                        for num in range(0, len(text)):
                            if(num_test(text[num]) == -1):
                                is_right = 0
                        if(is_right == 1):
                            if(int(text) <= 2017 and int(text) >=1):
                                year = int(text)
                                machine.in_year()
                                bot.sendMessage(user_id, '請輸入生日月份(1~12)')
                            else:
                                bot.sendMessage(user_id, 'Too big or too small,please enter a number between 1 & 2017')
                        else:
                            bot.sendMessage(user_id, 'Please enter a [number] between 1 & 2017')
                    else:
                        bot.sendMessage(user_id, 'Too long, please enter a number between 1 & 2017')
                elif(machine.state == 'year_done'):
                    if(len(text) <= 2):
                        for num in range(0, len(text)):
                            if(num_test(text[num]) == -1):
                                is_right = 0
                        if(is_right == 1):
                            if(int(text) <= 12 and int(text) >= 1):
                                month = int(text)
                                machine.in_month()
                                bot.sendMessage(user_id, '請輸入生日日期')
                            else:
                                bot.sendMessage(user_id, 'Too big or too small,please enter a number between 1 & 12')
                        else:
                            bot.sendMessage(user_id, 'Please enter a [number] between 1 & 12')
                    else:
                        bot.sendMessage(user_id, 'Too long, please enter a number between 1 & 12')
                elif(machine.state == 'month_done'):
                    if(len(text) <= 2):
                        for num in range(0, len(text)):
                            if(num_test(text[num]) == -1):
                                is_right = 0
                        if(is_right == 1):
                            if(year_test(year) == 1):
                                if(month == 2):
                                    if(int(text) >=1 and int(text) <= 29):
                                        day = int(text)
                                        machine.in_day()
                                        bot.sendMessage(user_id, '輸入1看生肖，輸入2看星座')
                                    else:
                                        bot.sendMessage(user_id, 'Too big or too small,please enter right number')
                                elif(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
                                    if(int(text) >=1 and int(text) <= 31):
                                        day = int(text)
                                        machine.in_day()
                                        bot.sendMessage(user_id, '輸入1看生肖，輸入2看星座')
                                    else:
                                        bot.sendMessage(user_id, 'Too big or too small,please enter right number')
                                else:
                                    if(int(text) >=1 and int(text) <= 30):
                                        day = int(text)
                                        machine.in_day()
                                        bot.sendMessage(user_id, '輸入1看生肖，輸入2看星座')
                                    else:
                                        bot.sendMessage(user_id, 'Too big or too small,please enter right number')
                            else:
                                if(month == 2):
                                    if(int(text) >=1 and int(text) <= 28):
                                        day = int(text)
                                        machine.in_day()
                                        bot.sendMessage(user_id, '輸入1看生肖，輸入2看星座')
                                    else:
                                        bot.sendMessage(user_id, 'Too big or too small,please enter right number')
                                elif(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
                                    if(int(text) >=1 and int(text) <= 31):
                                        day = int(text)
                                        machine.in_day()
                                        bot.sendMessage(user_id, '輸入1看生肖，輸入2看星座')
                                    else:
                                        bot.sendMessage(user_id, 'Too big or too small,please enter right number')
                                else:
                                    if(int(text) >=1 and int(text) <= 30):
                                        day = int(text)
                                        machine.in_day()
                                        bot.sendMessage(user_id, '輸入1看生肖，輸入2看星座')
                                    else:
                                        bot.sendMessage(user_id, 'Too big or too small,please enter right number')
                        else:
                            bot.sendMessage(user_id, 'Too big or too small,please enter right number')
                    else:
                            bot.sendMessage(user_id, 'Too big or too small,please enter right number')
                elif(machine.state == 'day_done'):
                    #print(year, month, day)
                    if(len(text) == 1):
                        if(num_test(text) == -1):
                            is_right = 0
                        if(is_right == 1):
                            if(int(text) == 1 or int(text) == 2):
                                choice = int(text)
                                if(choice == 1):
                                    year_left = year % 12
                                    if(year_left == 0):
                                        bot.sendMessage(user_id, '您的生肖是 : 猴')
                                    elif(year_left == 1):
                                        bot.sendMessage(user_id, '您的生肖是 : 雞')
                                    elif(year_left == 2):
                                        bot.sendMessage(user_id, '您的生肖是 : 狗')
                                    elif(year_left == 3):
                                        bot.sendMessage(user_id, '您的生肖是 : 豬')
                                    elif(year_left == 4):
                                        bot.sendMessage(user_id, '您的生肖是 : 鼠')
                                    elif(year_left == 5):
                                        bot.sendMessage(user_id, '您的生肖是 : 牛')
                                    elif(year_left == 6):
                                        bot.sendMessage(user_id, '您的生肖是 : 虎')
                                    elif(year_left == 7):
                                        bot.sendMessage(user_id, '您的生肖是 : 兔')
                                    elif(year_left == 8):
                                        bot.sendMessage(user_id, '您的生肖是 : 龍')
                                    elif(year_left == 9):
                                        bot.sendMessage(user_id, '您的生肖是 : 蛇')
                                    elif(year_left == 10):
                                        bot.sendMessage(user_id, '您的生肖是 : 馬')
                                    elif(year_left == 11):
                                        bot.sendMessage(user_id, '您的生肖是 : 羊')
                                elif(choice == 2):
                                    if(month == 1):
                                        if(day < 21):
                                            bot.sendMessage(user_id, '您的星座是 : 摩羯座')
                                        else:
                                            bot.sendMessage(user_id, '您的星座是 : 水瓶座')
                                    elif(month == 2):
                                        if(day < 20):
                                            bot.sendMessage(user_id, '您的星座是 : 水瓶座')
                                        else:
                                            bot.sendMessage(user_id, '您的星座是 : 雙魚宮')
                                    elif(month == 3):
                                        if(day < 21):
                                            bot.sendMessage(user_id, '您的星座是 : 雙魚座')
                                        else:
                                            bot.sendMessage(user_id, '您的星座是 : 白羊座')
                                    elif(month == 4):
                                        if(day < 21):
                                            bot.sendMessage(user_id, '您的星座是 : 白羊座')
                                        else:
                                            bot.sendMessage(user_id, '您的星座是 : 金牛座')
                                    elif(month == 5):
                                        if(day < 22):
                                            bot.sendMessage(user_id, '您的星座是 : 金牛座')
                                        else:
                                            bot.sendMessage(user_id, '您的星座是 : 雙子座')
                                    elif(month == 6):
                                        if(day < 22):
                                            bot.sendMessage(user_id, '您的星座是 : 雙子座')
                                        else:
                                            bot.sendMessage(user_id, '您的星座是 : 巨蟹座')
                                    elif(month == 7):
                                        if(day < 24):
                                            bot.sendMessage(user_id, '您的星座是 : 巨蟹座')
                                        else:
                                            bot.sendMessage(user_id, '您的星座是 : 獅子座')
                                    elif(month == 8):
                                        if(day < 24):
                                            bot.sendMessage(user_id, '您的星座是 : 獅子座')
                                        else:
                                            bot.sendMessage(user_id, '您的星座是 : 處女座')
                                    elif(month == 9):
                                        if(day < 24):
                                            bot.sendMessage(user_id, '您的星座是 : 處女座')
                                        else:
                                            bot.sendMessage(user_id, '您的星座是 : 天秤座')
                                    elif(month == 10):
                                        if(day < 24):
                                            bot.sendMessage(user_id, '您的星座是 : 天秤座')
                                        else:
                                            bot.sendMessage(user_id, '您的星座是 : 天蠍座')
                                    elif(month == 11):
                                        if(day < 23):
                                            bot.sendMessage(user_id, '您的星座是 : 天蠍座')
                                        else:
                                            bot.sendMessage(user_id, '您的星座是 : 人馬座')
                                    elif(month == 12):
                                        if(day < 23):
                                            bot.sendMessage(user_id, '您的星座是 : 人馬座')
                                        else:
                                            bot.sendMessage(user_id, '您的星座是 : 摩羯座')
                            else:
                                bot.sendMessage(user_id, 'Too big or too small,please enter right number')
                        else:
                            bot.sendMessage(user_id, 'Too big or too small,please enter right number')
                    else:
                        bot.sendMessage(user_id, 'Too big or too small,please enter right number')
                    choice = 0
        sleep(0.5)
if __name__ == "__main__":
    main()
