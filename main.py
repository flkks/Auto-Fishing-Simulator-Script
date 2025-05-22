import pygetwindow as gw
import keyboard as kb
import pyautogui as ag
import time

def selectwindow():
    try:
        gameWindow = gw.getWindowsWithTitle('Roblox')
        return gameWindow
    except Exception as e:
        print(e)

def recovery():
    print("Performing recovery operations...")
    for i in range(6):
        kb.press_and_release('1')
        time.sleep(0.5)
    ag.click(button='left')
    checkforbubbles()

def checkforbubbles():
    bubblecolour = (68, 252, 234)
    magmabubblecolour = (178, 0, 209)
    last_action_time = time.time()
    timeout = 20  # timeout for inactivity

    while True:
        if time.time() - last_action_time > timeout:
            print("Timeout reached, initiating recovery...")
            recovery()
            return

        if kb.is_pressed(','):                                          # STOP HOTKEY
            print("Stopping bubble checks...")
            break

        s = ag.screenshot()
        bubble_found = False
        for i in range(300, 1620):
            for j in range(150, 750):
                if s.getpixel((i, j)) == bubblecolour or s.getpixel((i, j)) == magmabubblecolour:
                    print("Bubble found")
                    ag.click(button='left')
                    automatedfishing()
                    bubble_found = True
                    last_action_time = time.time()  # Reset the last action time
                    break
            if bubble_found:
                break

def automatedfishing():
    positioncolour = (255, 255, 255)
    barcolour = (83, 250, 83)
    position = (877, 815)
    print("Starting automated fishing...")
    last_action_time = time.time()
    timeout = 30

    while True:
        if time.time() - last_action_time > timeout:
            print("Timeout during fishing, initiating recovery...")
            recovery()
            return

        if kb.is_pressed(','):                                          # STOP HOTKEY
            print("Stopping colour checks...")
            break

        s = ag.screenshot()
        current_color = s.getpixel(position)
        print(f"Checking color at {position}: {current_color}")
        if current_color == positioncolour:
            print("White bar detected - clicking...")
            ag.click(button='left')
            last_action_time = time.time()
        elif current_color not in (positioncolour, barcolour):
            time.sleep(2)
            ag.click(button='left')
            checkforbubbles()

def startscript():
    kb.wait('*')                                                        # START HOTKEY
    ag.click(button='left')
    checkforbubbles()

def main():
    gamewindow = selectwindow()
    if not gamewindow is None:
        startscript()
    else:
        print("Failed to find the Roblox window.")

if __name__ == "__main__":
    main()
