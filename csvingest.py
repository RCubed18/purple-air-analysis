import csv, os, datetime

#Constants
VERSION = '1.0'     #Changed from Sensor Name to GPS Coordinates

OUTPUTFILE = './finaldataset2.csv'
DATAPATH = './final_data_set/'

#Global Variables
OutputHeaders = ['T'+str(x) for x in range(61*48)]
NumSensors = 0


#Main Program
Epoch = datetime.datetime(2020,8,1,0,0,0)

#look for files in current directory
allfiles = os.listdir(DATAPATH)                #creates a python list of all filename in directory
allfiles.sort()

#creating a csv file
f = open(OUTPUTFILE, 'w')

#Create column headers in row 0
#f.write('Sensor')                   #Row 0, Column 0
f.write('Coordinates')

#row 0 column 1 to end
for i in range (len(OutputHeaders)):
    f.write(', '+OutputHeaders[i])

f.write('\n')

for filename in allfiles:
    if filename.endswith('.csv'):
        #parse filename
        sname = filename.split('(')

        #extract GPS coordinates from filename
        gpscoordinates = sname[2].split(')')[0]
        f.write(gpscoordinates)

        #Determine column location based on date
        fname = DATAPATH+filename
        with open(fname) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            rownum = 0
            for row in csv_reader:
                #throw away headers of input file
                if rownum == 0:
                    rownum += 1

                #compute start location
                elif rownum == 1:
                    csvrow = row.copy()

                    #Determine date
                    starttime = datetime.datetime.strptime(csvrow[0], '%Y-%m-%d %H:%M:%S UTC')
                    timediff = starttime - Epoch

                    print(f'Time Offset: {timediff}')

                    missedsamples = int((timediff.days * 48) + (timediff.seconds/1800))
                    print(f'Missed Samples: {missedsamples}')
                    for _ in range(missedsamples):
                        f.write(', 0.0')

                    #First PM2.5 data
                    if csvrow[1] != '':
                        f.write(', '+csvrow[1])
                    else:
                        f.write(', 0.0')

                    NumSensors += 1
                    rownum += 1
                else:
                    csvrow = row.copy()

                    #PM2.5 data
                    if csvrow[1] != '':
                        f.write(', '+csvrow[1])
                    else:
                        f.write(', 0.0')

                    rownum += 1

            f.write('\n')

        #Add PM2.5 data over time

f.close()
