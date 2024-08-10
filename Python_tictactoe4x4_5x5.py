import tkinter as tk
from tkinter import messagebox

#This is all 4x4 tic-tac-toe functions
current_player = "X"
board = [' ' for _ in range(16)]
def big4() :

    def make_move(position):
        global current_player
        row, col = position // 4, position % 4

        # Check if the current row is not the bottom row and if the cell below is not filled
        if row != 3 and board[position + 4] == ' ' and board[position] == ' ':
            messagebox.showinfo("Tic-Tac-Toe", "Cannot press here. You have to fill the cell below first.")
            return

        if board[position] == ' ':
            board[position] = current_player
            button = button_list[position]
            button.config(text=current_player, font=('Times New Roman', 20, 'bold'), bg='#F7E5E5', fg='#5E4343')
            check_winner()
            check_tie()
            current_player = "O" if current_player == "X" else "X"
            turn_tell()

    def turn_tell():
        tell_who_turn.config(text=f"{current_player}'s turn")

    def check_winner():
        for i in range(4):

            # Check rows4x4
            if board[i*4] == board[i*4 + 1] == board[i*4 + 2] != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f'Player {board[i*4]} wins!')
                reset_game()
                return
            elif (board[i*4 + 1] == board[i*4 + 2] == board[i*4 + 3] != ' '):
                messagebox.showinfo("Tic-Tac-Toe", f'Player {board[i*4+1]} wins!')
                reset_game()
                return

            # Check columns4x4
            if board[i] == board[i + 4] == board[i + 8]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board[i]} wins!")
                reset_game()
                return
            elif board[i+4] == board[i + 8] == board[i + 12]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board[i+4]} wins!")
                reset_game()
                return

            # Check diagonals4x4
            if board[0] == board[5] == board[10]  != ' ' :
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board[5]} wins!")  
                reset_game()
            if board[1] == board[6] == board[11]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board[6]} wins!")  
                reset_game()
            if board[12] == board[9] == board[6]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board[9]} wins!")  
                reset_game()
            if board[13] == board[10] == board[7]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board[10]} wins!")  
                reset_game()
            if board[2] == board[5] == board[8]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board[5]} wins!")  
                reset_game()
            if board[3] == board[6] == board[9]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board[6]} wins!")  
                reset_game()
            if board[4] == board[9] == board[14]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board[9]} wins!")  
                reset_game()
            if board[5] == board[10] == board[15]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board[10]} wins!")  
                reset_game()

    def check_tie():
        if ' ' not in board:
            messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            reset_game()

    def reset_game():
        global current_player, board
        current_player = "X"
        board = [" " for _ in range(16)]
        for button in button_list:
            button.config(text=' ', font=('Times New Roman', 20, 'bold'), bg='#D1AFAF', fg='#5E4343')
        turn_tell()

    root = tk.Tk()
    root.title("Tic-Tac-Toe")
    root.configure(bg='#F7E5E5')  # Background color

    button_list = []

    for i in range(16):
        row = i // 4
        col = i % 4
        button = tk.Button(
            root,
            text=' ',
            font=('Times New Roman', 20, 'bold'),
            width=6,
            height=3,
            command=lambda i=i: make_move(i),
            bg='#D1AFAF',  # Button color
            fg='#5E4343')  # Text color
        button.grid(row=row, column=col, padx=10, pady=10)
        button_list.append(button)

    tell_who_turn = tk.Label(root, text="Start !!", font=('Times New Roman', 16, 'bold'), bg='#F7E5E5', fg='#5E4343')
    tell_who_turn.grid(row=4, columnspan=4, pady=10)

    reset_button = tk.Button(root, text="Reset Game", command=reset_game, font=('Times New Roman', 16, 'bold'), bg='#5E4343', fg='#F7E5E5')
    reset_button.grid(row=5, columnspan=4, pady=10)

    root.mainloop()

#-------------------------------------------------------------------------------------------------------------------------------------------
#This is all 5x5 tic-tac-toe functions
current_player5x5 = "X"
board5x5 = [' ' for _ in range(25)]
def bigFive() :

    def make_movefive_five(position):
        global current_player5x5
        row, col = position // 5, position % 5

        # Check if the current row is not the bottom row and if the cell below is not filled
        if row != 4 and board5x5[position + 5] == ' ' and board5x5[position] == ' ':
            messagebox.showinfo("Tic-Tac-Toe", "Cannot press here. You have to fill the cell below first.")
            return

        if board5x5[position] == ' ':
            board5x5[position] = current_player5x5
            button = button_list5x5[position]
            button.config(text=current_player5x5, font=('Times New Roman', 20, 'bold'), bg='#F7E5E5', fg='#5E4343')
            check_winnerfive_five()
            check_tiefive_five()
            current_player5x5 = "O" if current_player5x5 == "X" else "X"
            turn_tellfive_five()

    def turn_tellfive_five():
        tell_who_turn5x5.config(text=f"{current_player5x5}'s turn")

    def check_winnerfive_five():
        for i in range(5):
            # Check rows 5x5
            if board5x5[i*5] == board5x5[i*5 + 1] == board5x5[i*5 + 2] != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f'Player {board5x5[i*5]} wins!')
                reset_game5x5()
                return
            elif (board5x5[i*5 + 1] == board5x5[i*5 + 2] == board5x5[i*5 + 3] != ' '):
                messagebox.showinfo("Tic-Tac-Toe", f'Player {board5x5[i*5+1]} wins!')
                reset_game5x5()
                return
            elif (board5x5[i*5 + 2] == board5x5[i*5 + 3] == board5x5[i*5 + 4] != ' '):
                messagebox.showinfo("Tic-Tac-Toe", f'Player {board5x5[i*5+2]} wins!')
                reset_game5x5()
                return

            # Check columns 5x5
            if board5x5[i] == board5x5[i + 5] == board5x5[i + 10]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board5x5[i]} wins!")
                reset_game5x5()
                return
            elif board5x5[i+5] == board5x5[i + 10] == board5x5[i + 15]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board5x5[i+5]} wins!")
                reset_game5x5()
                return
            elif board5x5[i+10] == board5x5[i + 15] == board5x5[i + 20]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board5x5[i+10]} wins!")
                reset_game5x5()
                return


            # Check diagonals 5x5
            if board5x5[0] == board5x5[6] == board5x5[12]  != ' ' :
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board5x5[6]} wins!")  
                reset_game5x5()
            if board5x5[1] == board5x5[7] == board5x5[13]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board5x5[7]} wins!")  
                reset_game5x5()
            if board5x5[2] == board5x5[8] == board5x5[14]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board5x5[8]} wins!")  
                reset_game5x5()
            if board5x5[5] == board5x5[11] == board5x5[17]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board5x5[11]} wins!")  
                reset_game5x5()
            if board5x5[6] == board5x5[12] == board5x5[18]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board5x5[12]} wins!")  
                reset_game5x5()
            if board5x5[7] == board5x5[13] == board5x5[19]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board5x5[13]} wins!")  
                reset_game5x5()
            if board5x5[10] == board5x5[16] == board5x5[22]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board5x5[16]} wins!")  
                reset_game5x5()
            if board5x5[11] == board5x5[17] == board5x5[23]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board5x5[17]} wins!")  
                reset_game5x5()
            if board5x5[12] == board5x5[18] == board5x5[24]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board5x5[18]} wins!")  
                reset_game5x5()
            if board5x5[2] == board5x5[6] == board5x5[10]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board5x5[6]} wins!")  
                reset_game5x5()
            if board5x5[3] == board5x5[7] == board5x5[11]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board5x5[7]} wins!")  
                reset_game5x5()
            if board5x5[4] == board5x5[8] == board5x5[12]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board5x5[8]} wins!")  
                reset_game5x5()
            if board5x5[7] == board5x5[11] == board5x5[15]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board5x5[11]} wins!")  
                reset_game5x5()
            if board5x5[8] == board5x5[12] == board5x5[16]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board5x5[12]} wins!")  
                reset_game5x5()
            if board5x5[9] == board5x5[13] == board5x5[17]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board5x5[13]} wins!")  
                reset_game5x5()
            if board5x5[12] == board5x5[16] == board5x5[20]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board5x5[16]} wins!")  
                reset_game5x5()
            if board5x5[13] == board5x5[17] == board5x5[21]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board5x5[17]} wins!")  
                reset_game5x5()
            if board5x5[14] == board5x5[18] == board5x5[22]  != ' ':
                messagebox.showinfo("Tic-Tac-Toe", f"Player {board5x5[18]} wins!")  
                reset_game5x5()
    def check_tiefive_five():
        if ' ' not in board5x5:
            messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            reset_game5x5()

    def reset_game5x5():
        global current_player5x5, board5x5
        current_player5x5 = "X"
        board5x5 = [" " for _ in range(25)]
        for button in button_list5x5:
            button.config(text=' ', font=('Times New Roman', 20, 'bold'), bg='#D1AFAF', fg='#5E4343')
        turn_tellfive_five()

    root5x5 = tk.Tk()
    root5x5.title("Tic-Tac-Toe")
    root5x5.configure(bg='#F7E5E5')  # Background color

    button_list5x5 = []

    for i in range(25):
        row = i // 5
        col = i % 5
        button = tk.Button(
            root5x5,
            text=' ',
            font=('Times New Roman', 20, 'bold'),
            width=6,
            height=3,
            command=lambda i=i: make_movefive_five(i),
            bg='#D1AFAF',  # Button color
            fg='#5E4343')  # Text color
        button.grid(row=row, column=col, padx=10, pady=10)
        button_list5x5.append(button)

    tell_who_turn5x5 = tk.Label(root5x5, text="Start !!", font=('Times New Roman', 18, 'bold'), bg='#F7E5E5', fg='#5E4343')
    tell_who_turn5x5.grid(row=5, columnspan=5, pady=10)

    reset_button5x5 = tk.Button(root5x5, text="Reset Game", command=reset_game5x5, font=('Times New Roman', 18, 'bold'), bg='#5E4343', fg='#F7E5E5')
    reset_button5x5.grid(row=6, columnspan=5, pady=10)

    root5x5.mainloop()

#This is Home page function

def open_4x4():
    root_main.destroy()
    big4() #When we press the button. It will start playing 4x4 tic-tac-toe

def open_5x5():
    root_main.destroy()
    bigFive() #When we press the button. It will start playing 5x5 tic-tac-toe

root_main = tk.Tk()
root_main.title("Tic-Tac-Toe")
root_main.configure(bg='#F7E5E5')  # Background color
root_main.geometry("600x300")

label_title = tk.Label(root_main, text="Tic-Tac-Toe", font=('Times New Roman', 24, 'bold'), bg='#F7E5E5', fg='#5E4343')
label_title.grid(row=0, column=0, columnspan=2, pady=20)

button_4x4 = tk.Button(root_main, text="Play 4x4 Tic-Tac-Toe", command=open_4x4, font=('Times New Roman', 18, 'bold'), bg='#D1AFAF', fg='#5E4343')
button_4x4.grid(row=1, column=1, padx=165, pady=20)

button_5x5 = tk.Button(root_main, text="Play 5x5 Tic-Tac-Toe", command=open_5x5, font=('Times New Roman', 18, 'bold'), bg='#D1AFAF', fg='#5E4343')
button_5x5.grid(row=2, column=1, padx=165, pady=20)

root_main.mainloop()