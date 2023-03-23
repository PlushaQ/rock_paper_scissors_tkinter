import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random


window = tk.Tk()

class Img:
  """Class to load and resize images"""
  def __init__(self):
    self.starting_image = None
    self.rock_image = None
    self.scissors_image = None
    self.paper_image = None

  def load_and_resize_images(self):
    self.starting_image = ImageTk.PhotoImage(Image.open('sign.png').resize((50, 50)))
    
    rock_img_open = Image.open('rock.png').resize((50,50))
    self.rock_image = ImageTk.PhotoImage(rock_img_open)
    
    scissors_img_open = Image.open('scissors.png').resize((50,50))
    self.scissors_image = ImageTk.PhotoImage(scissors_img_open)
    
    paper_img_open= Image.open('paper.png').resize((50,50))
    self.paper_image = ImageTk.PhotoImage(paper_img_open)

image = Img()
    
# Create the main window
class GameGUI:
  """Class to create GUI"""
  def __init__(self, window):
    self.window = window
    self.window.title("Rock Paper Scissors")
    self.window.geometry("450x450")
    self.label_frame = None
    self.image_frame = None
    self.result_text = None
    self.choices_frame = None

  def create_title_label(self):
    title_label = ttk.Label(master=self.window, text="ROCK PAPER SCISSORS", font='normal 20 bold')
    title_label.pack(padx=10, pady=10)
      
  def create_labels(self):
    # Create the labels for the player and computer choices
    self.label_frame = ttk.Frame(master=window)
    self.label_frame.pack(pady=20)
    
    self.player_label = ttk.Label(master=self.label_frame, text="Player", font='normal 12 bold')
    self.player_label.pack(side=tk.LEFT, padx=10, pady=10)
    
    self.vs_label = ttk.Label(master=self.label_frame, text="    vs    ", font='normal 12 bold')
    self.vs_label.pack(side=tk.LEFT, padx=10, pady=10)
    
    self.computer_label = ttk.Label(master=self.label_frame, text="Computer", font='normal 12 bold')
    self.computer_label.pack(side=tk.LEFT, padx=10, pady=10)

  def create_options_display(self):
    # Create a frame to hold the images
    self.image_frame = ttk.Frame(master=window)
    self.image_frame.pack(pady=20)
    
    # Create the labels for the player and computer images
    self.player_image = ttk.Label(master=self.image_frame, image=image.starting_image)
    self.player_image.pack(side=tk.LEFT, padx=40, pady=10)
    self.computer_image = ttk.Label(master=self.image_frame, image=image.starting_image)
    self.computer_image.pack(side=tk.RIGHT, padx=40, pady=10)

  def create_result_labels(self):
    # Define the label for the game result
    self.result_text = tk.StringVar()
    self.result_label = ttk.Label(master=window, textvariable=self.result_text, font='normal 16 bold')
    self.result_label.pack(padx=10, pady=10)

  def create_buttons(self):
    # Create the buttons for the player's choices
    self.choices_frame = ttk.Frame(master=window)
    self.choices_frame.pack(pady=20)
    
    
    self.rock_button = ttk.Button(master=self.choices_frame, image=image.rock_image)
    self.rock_button.pack(side=tk.LEFT, padx=10, pady=10)
    
    
    self.paper_button = ttk.Button(master=self.choices_frame, image=image.paper_image)
    self.paper_button.pack(side=tk.LEFT, padx=10, pady=10)
    
   
    self.scissors_button = ttk.Button(master=self.choices_frame, image=image.scissors_image)
    self.scissors_button.pack(side=tk.LEFT, padx=10, pady=10)


gui = GameGUI(window)


class Game:
  '''Define the game function'''
  def __init__(self):
      self.choices = ["rock", "paper", "scissors"]
      image.load_and_resize_images()
      gui.create_title_label()
      gui.create_labels()
      gui.create_options_display()
      gui.create_result_labels()
      gui.create_buttons()
      gui.scissors_button.configure(command=lambda: self.play_game("scissors"))
      gui.rock_button.configure(command=lambda: self.play_game("rock"))
      gui.paper_button.configure(command=lambda: self.play_game("paper"))
    
  def play_game(self, player_choice):
      computer_choice = random.choice(self.choices)
  
      if player_choice == computer_choice:  
        gui.result_text.set("Tie!")
      elif (player_choice == "rock" and computer_choice == "scissors") \
    or (player_choice == "paper" and computer_choice == "rock") \
    or (player_choice == "scissors" and computer_choice == "paper"):
          gui.result_text.set("You win!")
      else:
          gui.result_text.set("Computer wins!")
        
      # Update the images
      player_choice_image = ImageTk.PhotoImage(Image.open(f"{player_choice}.png").resize((75,75)))
      computer_choice_image = ImageTk.PhotoImage(Image.open(f'{computer_choice}.png').resize((75,75)))
      gui.player_image.configure(image=player_choice_image)
      gui.player_image.image = player_choice_image
      gui.computer_image.configure(image=computer_choice_image)
      gui.computer_image.image = computer_choice_image

  # Start the main loop
  def start_game(self):
    gui.window.mainloop()

game = Game()
game.start_game()
