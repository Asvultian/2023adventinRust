def main():
    print("Hello, World!")
    with open("puzzle_input.txt", "r") as file:
        data = file.read()
        data =data.split("\n")
        print(data)
        # Process the data here
        for i in range(len(data)):
            current_string=data[i]
            current_string=current_string.split(";")
            for char in (current_string):
                print(current_string[j])

if __name__ == '__main__':
    main()