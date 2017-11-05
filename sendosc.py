import time
import schedule
import random
from pythonosc import osc_message_builder
from pythonosc import udp_client


client = udp_client.SimpleUDPClient("127.0.0.1",12000)

def job():
    print("I'm working...")
    output = "hello world  " + str(random.randint(1, 100))
    client.send_message("/filter", output)
    print(output)


schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)