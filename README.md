# AIIP_Python_summative
# THE PROBLEMS
You work for an oil company that has been struggling to identify problem areas in pipelines. The pipelines have recently had sensors installed to help address this situation. But there are two problems:

1. The sensors didn't ship with any kind of software. You get a data stream for 32 sensor clusters with 16 readings per cluster, but all you get is a streaming data object, that currently overwrites itself with each cycle.
2. The second problem is that when the sensors breakdown they no longer report any numbers and they return a string, 'err', with no further number readings being recorded until that sensor is fixed. And since they run in a circuit when one sensor fails no data is reported for the entire circuit until the sensors are working again.
# THE ASK
You are currently going through a down period where there is a sensor is out. While the sensor is out you have been asked to create solutions to these problems. 

# Problem 1:
Before they switch all the sensors back on they want to have a solution in place. However, right now there is no data for you to use. You have been asked to generate a dummy dataset that you can use to prove your solutions work with.

----------------------------------------------------------ACCEPTANCE CRITERIA--------------------------------------------------------

1. The order of the objects must be sequential, ( ie. 1,2,3...32. ) since each number references a different pipeline region.
2. Your generated dataset needs to return a single set of data, that has 32 entries, with each entry returning 16 floats. 
3. The 16 floats returned will be between 0 and 1
# Problem 2:
Once you have your dataset to work with you will need to show that you can store this data with every iteration of the data set so no data is lost.

----------------------------------------------------------ACCEPTANCE CRITERIA--------------------------------------------------------
1. Every time your data set is generated the output should be stored and saved
2. For a challenge you could try to write the data to a file
3. New data should not overwrite historical data
4. For an extra challenge you can try to date and time stamp each interval of data collection
# Problem 3:
Write a function that will test the incoming data for possible strings entries

----------------------------------------------------------ACCEPTANCE CRITERIA--------------------------------------------------------
1. Create a copy of a "corrupted" data set containing at least one entry where the value is "err"
2. Your function should check for this error
3. Convert the string to a numerical value that can be uniquely identified as the error
4. Create an error log that records that the error happened and which of the sensors the error occurred with
5. For a challenge you can try to date and time stamp the log entries
