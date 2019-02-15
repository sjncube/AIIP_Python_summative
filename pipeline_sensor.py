# Python Summative
# author Sizwe Ncube

def Funct_Cluster():
    """ create 32 clusters and 16 transducer
        sensors in each and every cluster
    """
    import random
    cluster = {}
    for cluster_counter in range(1, 33):
        sensor = []
        for sensor_counter in range(1, 17):
            randNum = random.uniform(0, 1)
            sensor.append(randNum)
        cluster[cluster_counter] = sensor
    return cluster
#print(Funct_Cluster())
