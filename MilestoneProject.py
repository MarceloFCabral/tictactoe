#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Display the board

from IPython.display import clear_output

def display_board(board):
    clear_output()# Clears previously printed boards
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


# In[2]:


test_board = [' ']*10
display_board(test_board)


# In[3]:


# Make player input possible
def player_input():
    marker = ''
    
    # Keep asking player 1 to choose X or O:
    
    # Assign player 2 the opposite marker.
    
    while marker != 'X' and marker != 'O':
        marker = input('Do you want to be X or O?: ')
    
    player1 = marker
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1,player2)


# In[10]:


def playing():
    player1_marker , player2_marker = player_input()
    
    answer = ''
    while answer != 'Yes':
        answer = str(input('Are you ready to play? Yes or No? '))
    
    if player1_marker == 'X':
        marker_list = ['X','O','X','O','X','O','X','O','X']
    else:
        marker_list = ['O','X','O','X','O','X','O','X','O']
    
    board = [' ']*10
    display_board(board)
    
    playing = True
    
    while playing:
        index = 0
        while index not in list(range(1,10)):
            index = int(input("Please choose your placement position (from 1 to 9): "))
            
        board[index] = marker_list.pop()
        display_board(board)
        
        if board[1]==board[2]==board[3]==player1_marker:
            print("Player 1 wins!")
            break
        elif board[4]==board[5]==board[6]==player1_marker:
            print("Player 1 wins!")
            break
        elif board[7]==board[8]==board[9]==player1_marker:
            print("Player 1 wins!")
            break
        elif board[1]==board[2]==board[3]==player2_marker:
            print("Player 2 wins!")
            break
        elif board[4]==board[5]==board[6]==player2_marker:
            print("Player 2 wins!")
            break
        elif board[7]==board[8]==board[9]==player2_marker:
            print("Player 2 wins!")
            break
        elif board[1]==board[5]==board[9]==player1_marker:
            print("Player 1 wins!")
            break
        elif board[3]==board[5]==board[7]==player1_marker:
            print("Player 1 wins!")
            break
        elif board[1]==board[5]==board[9]==player2_marker:
            print("Player 2 wins!")
            break
        elif board[3]==board[5]==board[7]==player2_marker:
            print("Player 2 wins!")
            break
        elif board[1]==board[4]==board[7]==player1_marker:
            print("Player 1 wins!")
            break
        elif board[2]==board[5]==board[8]==player1_marker:
            print("Player 1 wins!")
            break
        elif board[3]==board[6]==board[9]==player1_marker:
            print("Player 1 wins!")
            break
        elif board[1]==board[4]==board[7]==player2_marker:
            print("Player 2 wins!")
            break
        elif board[2]==board[5]==board[8]==player2_marker:
            print("Player 2 wins!")
            break
        elif board[3]==board[6]==board[9]==player2_marker:
            print("Player 2 wins!")
            break
            
    answer2 = ''
    while answer2 not in ('Yes','No'):
        answer2 = input('Thank you for playing! Do you wish to play again? Yes or No? ')
        
    if answer2 == 'Yes':
        clear_output()
        play_ttt()
    else:
        print('Goodbye!')


# In[ ]:


def play_ttt():
    print('Welcome to this Tic Tac Toe Game!')
    playing()


# In[ ]:


play_ttt(


# In[ ]:





# In[ ]:





# In[ ]:





# In[8]:





# In[9]:





# In[ ]:




