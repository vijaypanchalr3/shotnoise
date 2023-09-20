from pyinstro import SR830


import time


new_instance = SR830()

new_instance.ping()
time.sleep(2)
new_instance.reset()
time.sleep(2)

while True:
    if input('n'):
        break
    try:
        freq = float(input())
        new_instance.set_frequency(freq)
        for i in range(10):
            time.sleep(2)
            data = new_instance.get_data_explicitly(data_variable=3)
            new_instance.writerow(data)
            print(str(i)+")  ", "data taken: ", str(data))
    except:
        print("give proper frequency")
    time.sleep(2)
    
SR830.close()
exit()
