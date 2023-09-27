from os import read
import random
import re

username = input("Enter your username:")

def show_selector():
    '''randomly selects a show for the user to watch'''
    begin = input("Are you ready to begin Master [Y]/[N]:")
    while(True):
        if begin == "Y" or begin == "y" or begin =="yes" or begin == "Yes":
            print("Right away Master",username)
            break
        else:
            print("Goodbye Master",username)
            exit()
    select = input("What genre would you like to watch between: \n Anime, Cartoons, Comedy, Documentary, Movies, Podcast, SciFi, or Romance:")
    if select == "Anime" or select == "anime":
        with open("animeGenre.txt","r") as file:
            allText  = file.read()
            words = list(map(str,allText.split()))
            print("Master",username,"Here's something I've selected for you:",random.choice(words))
    elif select == "Cartoon" or  select == "cartoon" or select == "cartoons" or select == "Cartoons":
        with open ("cartoonGenre.txt","r") as file:
            allText = file.read()
            words = list(map(str,allText.split()))
            print("Master",username,"Here's something I've selected for you:",random.choice(words))
    elif select == "Comedy" or select == "comedy" :
        with open ("comedyGenre.txt","r") as file:
            allText  = file.read()
            words = list(map(str,allText.split()))
            print("Master",username,"Here's something I've selected for you:",random.choice(words))
    elif select == "Documentary" or select == "documentary" or select == "Documentaries" or select == "documentaries":
        with open("documentaryGenre.txt","r") as file:
            allText = file.read()
            words = list(map(str,allText.split()))            
            print("Master",username,"Here's something I've selected for you:",random.choice(words))
    elif select == "Podcast" or select == "podcast":
        with open("podcastGenre.txt","r") as file:
            allText = file.read()
            words = list(map(str,allText.split()))
            print("Master",username,"Here's something I've selected for you:",random.choice(words))
    elif select == "SciFi" or select == "scifi" or select == "Science Fiction" or select == "ScienceFiction" or select == "Scifi":
        with open("scifiGenre.txt","r") as file:
            allText = file.read()
            words = list(map(str,allText.split()))
            print("Master",username,"Here's something I've selected for you:",random.choice(words))
    elif select == "Movie" or select == "Movies" or select == "movie" or select == "movies":
        with open("movieGenre.txt","r") as file:
            allText = file.read()
            words = list(map(str,allText.split()))
            print("Master",username,"Here's something I've selected for you:",random.choice(words))
    elif select == "Romance" or select == "romance" or select == "romcom" or select == "Romcom":
        with open("romanceGenre.txt","r") as file:
            allText = file.read()
            words = list(map(str,allText.split()))
            print("Master",username,"Here's something I've selected for you:",random.choice(words))
    else:
        lastQ = ("Are you sure Master: [Y]/[N]:")
        if lastQ == "Yes" or lastQ == "yes" or lastQ == "Y" or lastQ == "y":
            print("Goodbye Master",username)
            exit()


def adding_prompt():
    '''Asks user if they want to add a file'''
    appendPrompt = input("Do you want to add a file Master?:[Y]/[N]")
    for i in appendPrompt:
        if i == "Y" or i == "y" or i == "Yes" or i == "yes":
            print("Right away Master")
            appending_file()
        elif i == "N" or i == "n" or i =="No" or i == "no":
            print(f'Goodbye Master {username}')
        exit()
        

def appending_file():
    '''lets user choose where they want to append the file to and it appends it if not it exits'''
    folderSelection = input("Choose folder you want to append to: Anime,Cartoon,Comedy,Documentary,Movie,Podcast,Romance,Sci-Fi:")
    if folderSelection == "Anime" or folderSelection == "anime":
        appender = "animeGenre.txt"
        file = open(appender, "a")
        title = input("Enter the anime you want to add to your list: ")
        file.write(title + "\n")
        file.close()
        print(f'Great addition to the file Master {username} Goodbye')
    elif folderSelection == "Cartoon" or  folderSelection == "cartoon" or folderSelection == "cartoons" or folderSelection == "Cartoons":
        appender = "cartoonGenre.txt"
        file = open(appender, "a")
        title = input("Enter the cartoon you want to add to your list: ")
        file.write(title + "\n")
        file.close()
        print(f'Great addition to the file Master {username} Goodbye')
    elif folderSelection == "Comedy" or folderSelection == "comedy" :
        appender = "comedyGenre.txt"
        file = open(appender, "a")
        title = input("Enter the comedy you want to add to your list: ")
        file.write(title + "\n")
        file.close()
        print(f'Great addition to the file Master {username} Goodbye')
    elif folderSelection == "Documentary" or folderSelection == "documentary" or folderSelection == "Documentaries" or folderSelection == "documentaries":
        appender = "documentaryGenre.txt"
        file = open(appender, "a")
        title = input("Enter the documentary you want to add to your list: ")
        file.write(title + "\n")
        file.close()
        print(f'Great addition to the file Master {username} Goodbye')
    elif folderSelection == "Podcast" or folderSelection == "podcast":
        appender = "podcastGenre.txt"
        file = open(appender, "a")
        title = input("Enter the podcast you want to add to your list: ")
        file.write(title + "\n")
        file.close()
        print(f'Great addition to the file Master {username} Goodbye')
    elif folderSelection == "SciFi" or folderSelection == "scifi" or folderSelection == "Science Fiction" or folderSelection == "ScienceFiction" or folderSelection == "Scifi":
        appender = "scifiGenre.txt"
        file = open(appender, "a")
        title = input("Enter the Sci-Fi you want to add to your list: ")
        file.write(title + "\n")
        file.close()
        print(f'Great addition to the file Master {username} Goodbye')
    elif folderSelection == "Movie" or folderSelection == "Movies" or folderSelection == "movie" or folderSelection == "movies":
        appender = "movieGenre.txt"
        file = open(appender, "a")
        title = input("Enter the Movie you want to add to your list: ")
        file.write(title + "\n")
        file.close()
        print(f'Great addition to the file Master {username} Goodbye')
    elif folderSelection == "Romance" or folderSelection == "romance" or folderSelection == "romcom" or folderSelection == "Romcom":
        appender = "romanceGenre.txt"
        file = open(appender, "a")
        title = input("Enter the Romance you want to add to your list: ")
        file.write(title + "\n")
        file.close()
        print(f'Great addition to the file Master {username} Goodbye')
    else:
        print("Oh was that a mistake?")
        adding_prompt()


show_selector()
adding_prompt()
appending_file()



# A feature I'm still working on...
# deleting_item()
# def deleting_item():
#     deletion_prompt = input(f'Do you want to delete anything Master {username}')
#     if deletion_prompt == "Y" or deletion_prompt == "y" or deletion_prompt =="yes" or deletion_prompt == "Yes":
#         folderSelection = input("Choose folder you want to delete from: Anime,Cartoon,Comedy,Documentary,Movie,Podcast,Romance,Sci-Fi:")
#         if folderSelection == "Anime" or "anime":
#             specific_item = input("What do you specifically want to delelte from your list?") 
#             with open("animeGenre.txt" ,"r") as f:
#                 lines = f.readlines()
#             with open("animeGenre.txt" ,"w") as f:
#                 for line  in lines:
#                     if line.strip("\n" != specific_item):
#                         f.write(line)
# def deleting_item():
#     deletion_prompt = input(f'Do you want to delete anything Master {username}: ')
#     if deletion_prompt == "Y" or deletion_prompt == "y" or deletion_prompt =="yes" or deletion_prompt == "Yes":
#         folderSelection = input("Choose folder you want to delete from: Anime,Cartoon,Comedy,Documentary,Movie,Podcast,Romance,Sci-Fi:")
#         if folderSelection == "Anime" or "anime":
#             #specific_item = input("What do you specifically want to delelte from your list?")
#             animeGenre = r'C:\Users\pc\Documents\CODING\Randomiser\animeGenre.txt'
#             string = open(animeGenre).read()
#             new_str = re.sub('!','', string)
#             open(animeGenre,'w').write(new_str)
#         if folderSelection == "Cartoon" or "cartoon":
#             cartoonGenre = r'C:\Users\pc\Documents\CODING\Randomiser\cartoonGenre.txt'
            
#     else:
#         # print("Alright Master",username)
#         print(f'Alright Master{username}')
#         adding_prompt()


        
   


    
