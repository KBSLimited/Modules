#Task 1: Custom Module with Aliases

def reverse_string(s):
    return s[::-1]

def capitalize_string(s):
    return s.capitalize()

def main():
    input_string = input("Enter a string: ")

    reversed_string = reverse_string(input_string)
    print(f"Reversed string: {reversed_string}")

    capitalized_string = capitalize_string(input_string)
    print(f"Capitalized string: {capitalized_string}")

if __name__ == "__main__":
    main()