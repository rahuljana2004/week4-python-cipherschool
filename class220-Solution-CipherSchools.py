with open("class219-Ex1-CipherSchools.py","r") as rf:
    with open("output.txt","a") as wf:
        for line in rf.readlines():
            name,salary = line.split('')
            wf.write(f'{name}\'s salary is {salary}')

        