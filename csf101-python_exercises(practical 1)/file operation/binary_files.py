def create_binary_file(filename):
    data = bytes([0, 1, 2, 3, 4, 5])
    with open(filename, "wb") as file:
        file.write(data)

        create_binary_file("binary_sample.bin")
        print("binary file created successfully.")