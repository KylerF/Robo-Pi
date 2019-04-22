from inputs import get_gamepad

def gamepad_update():
    # Code execution stops at the following line until gamepad event occurs.
    controller_input = {'ABS_X': 0, 'ABS_RZ': 0, 'BTN_SOUTH': 0, 'BTN_WEST': 0}
    events = get_gamepad()
    return_code = 'No Match'
                    
    for event in events:
        print(event.code, '\t', event.state)
        event_test = controller_input.get(event.code, 'No Match')
                                        
        if event_test != 'No Match':
            controller_input[event.code] = event.state
            return_code = event.code
                                                                                             
    return return_code

def main():
    while True:
        button = gamepad_update()

if __name__ == "__main__":
    main()
