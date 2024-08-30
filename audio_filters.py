"""
Module: audio_filters

Authors:
1) Name - USD Email Address
2) Name - USD Email Address
"""

import sound

def remove_vocals(original_sound):
    """
    Creates a new sound object that is the same as the given sound, but with
    the vocals having been removed.

    Parameters:
    original_sound (type: Sound) - The original Sound object

    Returns:
    Sound object - Same sound as the original, but with vocals removed
    """

    pass  # Remove this "do nothing" statement when you start implementing.


def fade_in(original_sound, fade_length):
    """
    Replace this with a good docstring comment.

    Parameters:

    Returns:
    """

    pass  # Remove this "do nothing" statement when you start implementing.


def fade_out(original_sound, fade_length):
    """
    Replace this with a good docstring comment.

    Parameters:

    Returns:
    """

    pass  # Remove this "do nothing" statement when you start implementing.


def fade(original_sound, fade_length):
    """
    Replace this with a good docstring comment.

    Parameters:

    Returns:
    """

    pass  # Remove this "do nothing" statement when you start implementing.


def left_to_right(original_sound, pan_length):
    """
    Replace this with a good docstring comment.

    Parameters:

    Returns:
    """

    pass  # Remove this "do nothing" statement when you start implementing.


# Your final submission should NOT contain any global code.
# In other words, all your code should be contained in the functions defined
# above.



# WARNING: DO NOT MODIFY ANYTHING BELOW THIS LINE!!!

def main():
    '''
    The main function allows for selections to be made to test the sound functions.
    '''
    import os.path

    options = {
                1: ("remove_vocals", None),
                2: ("fade_in", "fade_length"),
                3: ("fade_out", "fade_length"),
                4: ("fade", "fade_length"),
                5: ("left_to_right", "pan_length")
            }

    print("The following functions are available.\n")
    print("(1) remove_vocals")
    print("(2) fade_in")
    print("(3) fade_out")
    print("(4) fade")
    print("(5) left_to_right")

    selection = int(input("\nEnter the number of the function to test: "))

    if selection not in range(1, 6):
        print("Invalid selection. Please run the tester again.")
        return

    wav_file = input("Enter the name of the wav file to test with: ")

    # Make sure the file exists so we don't get an error trying to open a
    # file that isn't there.
    if not os.path.isfile(wav_file):
        print("\nTest Failed: The file you typed does not exist. Try again.")
        return

    # create a sound object then call the selected function
    original_sound = sound.load_sound(wav_file)
    test_function_name = options[selection][0]
    test_function = globals()[test_function_name]

    # Have user enter value for the parameter if one exists
    has_parameter = options[selection][1] is not None

    while has_parameter:
        param_name = options[selection][1]
        param_value = int(input("Enter a value for %s: " % param_name))

        # TODO: check that it is not greater than sound's length?
        if param_value < 1:
            print("Invalid selection.", param_name, "must be a positive integer.")
        else:
            break
    

    # TODO: run this in a try-catch 
    if has_parameter:
        filtered_sound = test_function(original_sound, param_value)
    else:
        filtered_sound = test_function(original_sound)

    # Check that the function gave back a sound
    if filtered_sound is None:
        print("\nTest Failed:", test_function_name, "does not return a sound. Did you forget the return statement?")
        return

    # Allow the user to play or display the original or filtered sounds
    while True:
        print("\nThe following options are available:\n")
        print("(1) Play original sound.")
        print("(2) Play filtered sound.")
        print("(3) Display original sound waveforms.")
        print("(4) Display filtered sound waveforms.")
        print("(5) Exit this program.")

        selection = int(input("\nEnter your selection: "))
        if selection not in range(1, 6):
            print("Invalid selection. Enter a number between 1 and 5.")
        elif selection == 1:
            original_sound.play()
            sound.wait_until_played()
        elif selection == 2:
            filtered_sound.play()
            sound.wait_until_played()
        elif selection == 3:
            original_sound.display()
        elif selection == 4:
            filtered_sound.display()
        elif selection == 5:
            break

if __name__ == "__main__":
    main()
