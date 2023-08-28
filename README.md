# Password Manager GUI

## Project Overview
The Password Manager Graphic User Interface is to provide the user with strong and unique passwords that simplify the process of managing numerous online accounts.

## Objectives
- Create a Simple GUI.
- Generate Complex & Unique Passwords.
- Create Password Storage Functionality

## Results
Should the fields for the number of letters, digits and symbols are empty. 


The password generator would automatically create a strong password with 8 of each character type. 

![image](https://github.com/frantzalexander/password_manager_gui/assets/128331579/4b4575c1-1ad5-4b90-90bd-592b09becad7)

## Process
```mermaid
flowchart TD
start(((START)))
ui_setup[User Interface Setup]
labels[Create Labels]
text[Create Text Entry Fields]
buttons[Create Buttons]
password[Password Generator Setup]
import[Import data from Text Entry Fields]
create_pass[Create password]
copy[Copy Password to Clipboard]
save[Save Functionality Setup]
warning[Warning Prompt: Empty Website Name Field]
error[Error Prompt: Empty Password Field]
save_button[Save Button Prompt: Asks user Whether Info Is Correct]
save_pass[Save Password to Data File]
finish(((END)))
start --> ui_setup
ui_setup --> labels
labels --> text
text --> buttons
start --> password
password --> import
import --> create_pass
create_pass --> copy
start --> save
save --> warning
warning --> error
error --> save_button
save_button --> save_pass
buttons --> finish
copy --> finish
save_pass --> finish
 
