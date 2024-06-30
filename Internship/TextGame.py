import tkinter as tk
from tkinter import messagebox
from random import randint as rdt

class TextGame:
    def __init__(self, master):
        self.master = master
        master.title("Lost in Space Adventure")

        self.background_color = "#0D0D0D"  
        self.text_color = "#FFFFFF"        
        self.button_color = "#4B92CC"       
        self.font_style = ("Segoe UI", 10)  
        self.code_font_style = ("Consolas", 10)

        master.configure(bg=self.background_color)

        self.story_text = tk.StringVar()
        self.choice_text = tk.StringVar()
        self.rdchoice = 0

        self.create_widgets()

    def create_widgets(self):
        self.story_label = tk.Label(self.master, textvariable=self.story_text, wraplength=300, justify=tk.LEFT,bg=self.button_color,fg=self.text_color,font=self.font_style)
        self.story_label.pack(pady=10)

        self.choice_label = tk.Label(self.master, textvariable=self.choice_text, wraplength=300, justify=tk.LEFT,bg=self.button_color,fg=self.text_color,font=self.code_font_style)
        self.choice_label.pack(pady=10)

        self.choice_entry = tk.Entry(self.master)
        self.choice_entry.pack(pady=10)
        self.choice_entry.bind("<Return>",lambda event:self.handle_choice())

        self.submit_button = tk.Button(self.master, text="Submit", command=self.handle_choice,bg=self.button_color,fg=self.text_color,font=self.font_style)
        self.submit_button.pack(pady=10)

        self.page_number = 1
        self.update_story()

    def update_story(self):
        if self.page_number == 1:
            self.story_text.set("You wake up to the blaring sound of alarms. The navigation system of the MC Explorer has malfunctioned, "
                                "and you are now lost in an unknown region of space in a desolate-looking planet. \nThe control panel flickers with warning lights.\nYour mission was to find another hospitable planet that was under similar conditions as Earth.\nBut now you're at the mercy of the universe\nWhat will you do?")
            self.choice_text.set("1. Use a distress beacon in order to send a distress signal.\n2. Scan the terrain of the planet.\n3. Try using the navigation system to find your position")

        elif self.page_number == 2:
            self.story_text.set("Your Distress beacon pings another Starship in the vicinity."
                                "The distress beacon did not have enough power to send a message to the aforementioned starship.\nWhat will you do?")
            self.choice_text.set("1. Try unencrypted comms that can be easily intercepted and uses lesser power\n2. Send a simple 'SOS' message that is encrypted but takes more power")

        elif self.page_number == 3:
            self.story_text.set("Your scan reveals a structure of sorts and gives an approximate co-ordinate for the said structure.\nWhat will you do?")
            self.choice_text.set("1. Scan the terrain anomaly further and find out the exact location but loose some power doing so\n2. Try using the distress beacon instead\n3. Try establishing comms again")

        elif self.page_number == 4:
            self.story_text.set("Your navigation appears to have failed, but a glimmer of hope shines as an unknown entity relays a message providing you with assistance.\nWhat will you do?")
            self.choice_text.set("1. Accept the alien's help and allow yourself to be towed by them.\n2. Decline their help and continue to work on the nav system.")

        elif self.page_number == 5:
            self.story_text.set("Your unencrypted comms are picked up by the starship but they also draw the attention of an unknown life form's Starship.\nWhat will you do?")
            self.choice_text.set("1. Use your remaining power to enable stealth and hide from the alien starship\n2. Try urging the pinged starship to come to your help faster")
            self.rdchoice = rdt(1,2)

        elif self.page_number == 6:
            self.story_text.set("Your encrypted message is brodcasted to the starship but unfortunately the starship wasnt able to recieve the message\nWhat will you do?")
            self.choice_text.set("1. Try sending the message again but this time in an easier encryption\n2. Send a message in an unencrypted channel")

        elif self.page_number == 7:
            self.story_text.set("You come across an abandoned power facility, and have the equipment required to restore power to your ship.\nYou use the equipment in hopes of powering up your spaceship\nAll the power in your starship has been restored and all functionality has been restored.\nThe navigation suddenly pings a place of interest, a Goldilocks zone a couple of lightyears from your current planet\nWhat will you do?")
            self.choice_text.set("1. Use the comms along with stealth to avoid drawing any unwanted attention to yourselves\n2. Warp to the pinged Goldilocks zone in hopes of finding a planet with life")
            self.rdchoice = rdt(700,800)
        
        elif self.page_number == 8:
            self.story_text.set("You reject the help of the aliens and try to use the nav systems again and a Goldilocks zone gets pinged on your console.\nWhat will you do?")
            self.choice_text.set("1. Try to warp to the Goldilocks zone with barely any power and hope you make it there\n2. Try contacting the entities again")
            self.rdchoice = rdt(800,900)
        
        elif self.page_number == 9:
            self.story_text.set("The aliens take you to a facility of some sorts that looks like a trade center.\nAn alien places 2 items infront of you gesturing you to pick one\nWhat will you do?")
            self.choice_text.set("1. Pickup the item that looks like an earbud\n2. Pickup the item that looks like a remote")

        elif self.page_number == 10:
            self.story_text.set("The aliens find your location and tow it to a facility")
            self.choice_text.set("Click submit/ press enter to continue")

        elif self.page_number == 11:
            self.story_text.set("You use up almost all your power in order to send the encrypted message.\nWhat will you do?")
            self.choice_text.set("1. Try going to cryosleep in order to save oxygen and hope that someone can find you\n2. Use the last of your power to warp to a random location")
            self.rdchoice = rdt(1100,1200)
        
        elif self.page_number == 12:
            self.choice_label.pack_forget()
            self.choice_entry.pack_forget()
            self.submit_button.pack_forget()
            self.story_text.set("Your warping fails and you crash land on a moon of a dwarf planet\nThere is no hospitable zone in your current solar system\nYou end up succumbing to your bad luck, or your poor decisions\nThe End.")
        
        elif self.page_number == 13:
            self.choice_label.pack_forget()
            self.choice_entry.pack_forget()
            self.submit_button.pack_forget()
            self.story_text.set("Your warp fails and you are left drifting in space at near light speed with no power and limited rations\nAll is lost, there is nothing other than the void everywhere you look\nYou have no power to turn on cryosleep, all is lost\nThe End.")
        
        elif self.page_number == 14:
            self.choice_label.pack_forget()
            self.choice_entry.pack_forget()
            self.submit_button.pack_forget()
            self.story_text.set("The earbud turns out to be a universal translator. The aliens look at you expecting you to answer them. \nYou can understand them now. They are asking you to join their crew and help them till you earn enough credits to repair your ship and go home.\nYou go along with them and finally what seems to be years later repay them for the repairs and set your warp back home.\nThe End.")
        
        elif self.page_number == 15:
            self.choice_label.pack_forget()
            self.choice_entry.pack_forget()
            self.submit_button.pack_forget()
            self.story_text.set("The remote has a few buttons and you click the glowing button. And all of a sudden you're home! \nThe device that was lent to you appears to be a teleporter. A device that enables multidimensional travel. \nYou rejoice as a hero and statues are built of you in your hometown.\nScientists are grateful to you for bringing back the teleporter, everything has been peaceful for many years.\nBut then the sky goes dark, an Unidentified flying object appears in the sky and wipes the entire city clean with one ray\nThe aliens put your picture up everywhere and demand your head. Turns out the teleporter was priced universally and your disappearance meant that every planet that housed humans had to be destroyed.\nYou brought upon the end of humanity.\nThe End")
        
        elif self.page_number == 16:
            self.choice_label.pack_forget()
            self.choice_entry.pack_forget()
            self.submit_button.pack_forget()
            self.story_text.set("What appears to be a friendly starship comes to your rescue and you are taken back home.\nBut since you were failed the mission and you had wrecked your billion dollar spacecraft, \nyou were taken under trial and sentenced to prision under destruction of private property.\nThe End.")
        
        elif self.page_number == 17:
            self.choice_label.pack_forget()
            self.choice_entry.pack_forget()
            self.submit_button.pack_forget()
            self.story_text.set("You find what seems to be a Space Station orbiting a blue planet that looks similar like Earth.\nThis is the planet you've been searching for all this while.Youre overjoyed to see it.\nYou land on the space station to be greeted by another carbon based humanoid life form who look similar to humans.\nThey greet you and you have been presented with a universal translator.\nYou ask for repairs then set off to Earth to complete your task of finding friendly extraterrestrials.\nThe End")


    def handle_choice(self):
        user_choice = self.choice_entry.get()
        print(self.page_number)
        err = ("Invalid Choice, Please enter a valid choice.")

        if self.page_number == 1:
            if user_choice == "1":
                self.page_number = 2
            elif user_choice == "2":
                self.page_number = 3
            elif user_choice == "3":
                self.page_number = 4
            else:
                messagebox.showinfo("Error",err)

        elif self.page_number == 2:
            if user_choice == "1":
                self.page_number = 5
            elif user_choice == "2":
                self.page_number = 6
            else:
                messagebox.showinfo("Error",err)

        elif self.page_number == 3:
            if user_choice == "1":
                self.page_number = 7
            elif user_choice == "2":
                self.page_number = 2
            elif user_choice == "3":
                self.page_number = 4
            else:
                messagebox.showinfo("Error",err)

        elif self.page_number == 4:
            if user_choice == "1":
                self.page_number = 9
            elif user_choice == "2":
                self.page_number =  8
            else:
                messagebox.showinfo("Error",err)

        elif self.page_number == 5:
            if user_choice == "1":
                self.page_number = 16
            elif user_choice == "2":
                if self.rdchoice == 1:
                    self.page_number = 16
                elif self.rdchoice == 2:
                    self.page_number = 10
            else:
                messagebox.showinfo("Error",err)

        elif self.page_number == 6:
            if user_choice == "1":
                self.page_number = 11
            elif user_choice == "2":
                self.page_number =  5
            else:
                messagebox.showinfo("Error",err)

        elif self.page_number == 7:
            if user_choice == "1":
                self.page_number = 16
            elif user_choice == "2":
                if self.rdchoice in range(700,751):
                    self.page_number = 17
                elif self.rdchoice in range(750,776):
                    self.page_number = 12
                elif self.rdchoice in range(775,801):
                    self.page_number = 13
            else:
                messagebox.showinfo("Error",err)
        
        elif self.page_number == 8:
            if user_choice == "1":
                if self.rdchoice in range(800,826):
                    self.page_number = 17
                elif self.rdchoice in range(825,901):
                    self.page_number = 12
            elif user_choice == "2":
                self.page_number = 13
            else:
                messagebox.showinfo("Error",err)

        elif self.page_number == 9:
            if user_choice == "1":
                self.page_number = 14
            elif user_choice == "2":
                self.page_number = 15
            else:
                messagebox.showinfo("Error",err)
        
        elif self.page_number == 10:
            self.page_number = 9

        elif self.page_number == 11:
            if user_choice == "1":
                if self.rdchoice in range(1100,1146):
                    self.page_number = 16
                elif self.rdchoice in range(1145,1201):
                    self.page_number = 13
            if user_choice == "2":
                if self.rdchoice in range(1100,1111):
                    self.page_number = 17
                elif self.rdchoice in range(1110,1201):
                    self.page_number = 12


        self.update_story()
        self.choice_entry.delete(0,tk.END)


if __name__ == "__main__":
    root = tk.Tk()

    root.geometry("400x400")
    root.resizable(False,False)

    root.wm_attributes('-topmost', 1)

    game = TextGame(root)
    root.mainloop()
