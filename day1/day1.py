juicy_array_of_numbers = []
finished_array = []
def main():
    total_sum = 0
    with open("file.txt", "r") as file:
        data = file.read()
        data =data.split("\n")
        for i in range(len(data)):
            for char in data[i]:
                if char.isdigit():
                    
                    juicy_array_of_numbers.append((char))
            #-1 indexes the last element in the list
            concatenated = juicy_array_of_numbers[0] + juicy_array_of_numbers[-1]
            total_sum = total_sum + int(concatenated)
            finished_array.append(int(concatenated)) 
            #clear the list for the next iteration
            juicy_array_of_numbers.clear()   
        # Process the data here
    print(total_sum)
    with open("output.txt", "w") as file:
        for i in range(len(finished_array)):
            file.write(f"{finished_array[i]}\n")

        # Write the results to the output file

if __name__ == '__main__':
    main()