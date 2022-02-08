spring_festivals = ["Egg Festival", "Flower Dance"]
summer_festivals = ["Luau", "Dance of the Moonlight Jellies"]
fall_festivals = ["Stardew Valley Fair", "Spirit's Eve"]
winter_festivals = ["Festival of Ice", "Night Market", "Feast of the Winter Star"]

bday_dict_from_season = {'Spring 4 (Thurs)':'Kent', 'Spring 7 (Sun)':'Lewis', 'Spring 10 (Wed)':'Vincent',
                         'Spring 14 (Sun)':'Haley', 'Spring 18 (Thurs)':'Pam', 'Spring 20 (Sat)':'Shane',
                         'Spring 26 (Fri)':'Pierre', 'Spring 27 (Sat)':'Emily',
                 
                         'Summer 4 (Thurs)':'Jas', 'Summer 8 (Mon)':'Gus', 'Summer 10 (Wed)':'Maru',
                         'Summer 13 (Sat)': 'Alex', 'Summer 17 (Wed)':'Sam', 'Summer 19 (Fri)':'Demetrius',
                         'Summer 22 (Mon)':'Dwarf', 'Summer 24 (Wed)':'Willy'}

bday_dict_from_name = {'Kent':'Spring 4 (Thurs)', 'Lewis':'Spring 7 (Sun)', 'Vincent':'Spring 10 (Wed)',
                       'Haley':'Spring 14 (Sun)', 'Pam':'Spring 18 (Thurs)', 'Shane':'Spring 20 (Sat)',
                       'Pierre':'Spring 26 (Fri)', 'Emily':'Spring 27 (Sat)', 'Jas':'Summer 4 (Thurs)', 
                       'Gus':'Summer 8 (Mon)', 'Maru':'Summer 10 (Wed)', 'Alex':'Summer 13 (Sat)', 
                       'Sam':'Summer 17 (Wed)', 'Demetrius':'Summer 19 (Fri)', 'Dwarf': 'Summer 22 (Mon)',
                       'Willy':'Summer 24 (Wed)'}

def festival(): 
    festival_inquiry = input("Which season of festivals are you interested in? Your options are 'spring,' 'summer,' 'fall' or 'winter:' ")
    if (festival_inquiry.lower() == "spring"): #the .lower() ignores case 
        print("Spring festivals: ")
        print(spring_festivals)
       
    if (festival_inquiry.lower() == "summer"): 
        print("Summer festivals: ") 
        print(summer_festivals)
    
    if (festival_inquiry.lower() == "fall"): 
        print("Fall festivals: ")
        print(fall_festivals)
        
    if (festival_inquiry.lower() == "winter"): 
        print("Winter festivals: ") 
        print(winter_festivals)
    
def birthday_from_name():
    inquiry = input("Whose birthday are you looking for?: ")
    for i in bday_dict_from_name: 
        if inquiry in i: 
            print(bday_dict_from_name[i])

def birthday_from_season(): 
   inquiry = input("Which season's birthdays do you want to see?: ")
   #if inquiry in bday_dict_from_season:
   for i in bday_dict_from_season: 
       if inquiry in i: 
           print(bday_dict_from_season[i])

   more_info = input("Do you want to find the bdays of any specific chracters? enter 'y' or 'n': ")
   if more_info == 'y': 
       birthday_from_name()
   
    
greetings = input("enter what you want to learn more about (ex: festivals, bdays, etc.)")
if greetings == "festivals": 
    festival()
elif greetings == "bdays": 
    name_or_season = input("Do you have their name or season?")
    if name_or_season == "name": 
        birthday_from_name()
    elif name_or_season == "season": 
        birthday_from_season()
