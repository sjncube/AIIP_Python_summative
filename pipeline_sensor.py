# Python Sumnative Assessment
# author Sizwe Ncube
import random
import datetime

#function for Problem:1 and Problem:2
def Funct_Cluster():
    """
        create 32 clusters and 16 transducer
        sensors in each and every cluster
    """
    cluster = {}
    for cluster_counter in range(1, 33):
        sensor = []
        for sensor_counter in range(1, 17):
            randnum = random.uniform(0, 1)
            sensor.append(randnum)
        cluster[cluster_counter] = sensor
    file = open("sensor_data.txt", "a")
    file.write(str(datetime.datetime.now())+"\n" + 1024*"-" + "\n")
    file.write(str(cluster)+"\n" + 1024*"-" + "\n")
    file.close()


Funct_Cluster()