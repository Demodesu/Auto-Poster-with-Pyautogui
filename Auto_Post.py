#https://www.youtube.com/watch?v=uWrcHArLLLM
#https://stackoverflow.com/questions/22745076/libpng-warning-iccp-known-incorrect-srgb-profile

import pyautogui, time, requests, random, sys
from bs4 import BeautifulSoup

def auto_post():
    group_list = [5969589316417037,567107234297571,930037904221621]

    for count, group in enumerate(group_list):
        wait = 5
        print(f'>Executing in {wait} seconds')
        time.sleep(wait)

        pyautogui.hotkey('ctrl', 't')   

        time.sleep(1)
        print(f'Entering group {count + 1} key {group}')
        pyautogui.typewrite(f'https://www.facebook.com/groups/{group}')
        pyautogui.press('enter')

        time.sleep(4)
        print('Loading group')

        time.sleep(2)
        print('Locating post box')           
        post_box_location = pyautogui.center(pyautogui.locateOnScreen('Image/Post_Box_Image.png', confidence=0.6))
        pyautogui.moveTo(post_box_location[0],post_box_location[1])
        pyautogui.click()

        time.sleep(2)
        print('Posting text')
        pyautogui.typewrite('This is a test')   

        time.sleep(2)
        print('Posting photos')
        photo_button_location = pyautogui.locateOnScreen('Image/Post_Photo_Box.png', confidence=0.6)
        pyautogui.moveTo(photo_button_location[0] + 25,photo_button_location[1] + 25)
        pyautogui.click()

        time.sleep(2)
        print('Finding photos')
        wanted_photo = pyautogui.center(pyautogui.locateOnScreen('Image/Duck.png', confidence=0.5))
        pyautogui.moveTo(wanted_photo[0] + 25,wanted_photo[1] + 25)  
        time.sleep(1)     
        pyautogui.click()
        pyautogui.press('enter')

        time.sleep(2)
        print('Posting')
        post_button_location = pyautogui.center(pyautogui.locateOnScreen('Image/Post_Button_Image.png', confidence=0.6))
        pyautogui.moveTo(post_button_location[0],post_button_location[1])
        pyautogui.click()

        time.sleep(4)
        pyautogui.hotkey('ctrl', 'w')    

if __name__ == '__main__':    
    opening = True
    while opening:
        print('>Make sure the shortcut to open google chrome is CTRL+ALT+C')
        print('>When running move mouse to top left corner to interrupt')
        open_webpage = input('>Start program? (yes/no) >')
        if open_webpage == 'yes':
            opening = False
            running = True
            time.sleep(2)
            pyautogui.hotkey('win', 'd')
            pyautogui.hotkey('ctrl', 'alt', 'c')             
            while running:
                auto_post()
                time_wait = 30
                print(f'>>End of posting')
                print(f'>>Waiting {time_wait} minutes to post again')
                time.sleep(time_wait * 60)
