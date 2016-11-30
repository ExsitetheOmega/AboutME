"""
 __      __       .__                                  __             __  .__                                                                              .__  .__          ___.                  __                  ._.
/  \    /  \ ____ |  |   ____  ____   _____   ____   _/  |_  ____   _/  |_|  |__   ____   _____________  ____   ________________    _____   _____   _____  |  | |  |   _____ \_ |__   ____  __ ___/  |_    _____   ____| |
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \  \   __\/  _ \  \   __\  |  \_/ __ \  \____ \_  __ \/  _ \ / ___\_  __ \__  \  /     \ /     \  \__  \ |  | |  |   \__  \ | __ \ /  _ \|  |  \   __\  /     \_/ __ \ |
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/   |  | (  <_> )  |  | |   Y  \  ___/  |  |_> >  | \(  <_> ) /_/  >  | \// __ \|  Y Y  \  Y Y  \  / __ \|  |_|  |__  / __ \| \_\ (  <_> )  |  /|  |   |  Y Y  \  ___/\|
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >  |__|  \____/   |__| |___|  /\___  > |   __/|__|   \____/\___  /|__|  (____  /__|_|  /__|_|  / (____  /____/____/ (____  /___  /\____/|____/ |__|   |__|_|  /\___  >_
       \/       \/          \/            \/     \/                            \/     \/  |__|               /_____/            \/      \/      \/       \/                 \/    \/                           \/     \/\/
"""
# Imports:
import time
import datetime
# Info: 
job = "Albert Heijn Employee"
age = "15"
future = "I want to be a developer and I'm going to study Computer Science."
school = "High School: CSB"
country = "The Netherlands, Amsterdam"


# Beginning:
print("Welcome to my programm, this programm is based on me.\nIt concludes some information about me. \n-=Created by: Exsite=-\n")
# actual programm:
while True:
    do = input("What would you like to know?\nChoose one of the following:\n%s, %s, %s, %s, %s, %s: " % ("job", "age", "future", "school", "country", "exit"))
    if do == "job":
        print(job)
    elif do == "age":
        print(age)
    elif do == "future":
        print(future)
    elif do == "school":
        print(school)
    elif do == "country":
        print(country)
    elif do == "exit":
        break
    else:
        print("You typed it wrong try again")
    time.sleep(2)
print("programm is closing...")
time.sleep(1.5)
exit()
