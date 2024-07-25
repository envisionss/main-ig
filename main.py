import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Gradient colors
gradient_blue_to_cyan = (0, 0, 255), (0, 255, 255)
gradient_neon_purple_to_white = (255, 0, 255), (255, 255, 255)  # Neon purple to white

def print_gradient(text, start_color, end_color):
    num_chars = len(text)
    
    def rgb_to_foreground(r, g, b):
        return f'\033[38;2;{r};{g};{b}m'

    def interpolate_color(start, end, factor):
        return tuple(int(start[i] + (end[i] - start[i]) * factor) for i in range(3))
    
    for i in range(num_chars):
        factor = i / (num_chars - 1) if num_chars > 1 else 0
        r, g, b = interpolate_color(start_color, end_color, factor)
        color = rgb_to_foreground(r, g, b)
        print(f"{color}{text[i]}", end='', flush=True)
    
    print(Style.RESET_ALL)

def print_options():
    # The text to display as options
    text_lines = [
        "Option 1: Webhook Spam",
        "Option 2: Exit",
        "[More Coming Soon]"
    ]
    
    # Print each line with the gradient
    for line in text_lines:
        print_gradient(line, gradient_blue_to_cyan[0], gradient_blue_to_cyan[1])

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_options()
        
        print()
        print_gradient("Choose an option (1 or 2):", gradient_neon_purple_to_white[0], gradient_neon_purple_to_white[1])
        choice = input().strip()
        if choice == '1':
            print_gradient("You chose: Webhook Spam", gradient_blue_to_cyan[0], gradient_blue_to_cyan[1])
            input("Press Enter to continue...")
        elif choice == '2':
            print_gradient("Exiting...", gradient_blue_to_cyan[0], gradient_blue_to_cyan[1])
            break
        else:
            print_gradient("Invalid choice, please try again.", gradient_blue_to_cyan[0], gradient_blue_to_cyan[1])
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
