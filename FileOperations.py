def check_file():
    word="learning"
    with open("Sample.txt","w") as f:
        data=f.write("This is my learning lesson of python file.\nI will learn deep learning after this.")

    with open("Sample.txt","r") as f:
       data1=f.read(data)

    new_data=data1.replace("Python","Java")
    print(new_data)

    with open("Sample.txt","w") as f:
        data=f.write(new_data)
    
    
        