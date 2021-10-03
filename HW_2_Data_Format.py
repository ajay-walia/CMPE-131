import csv
import json
import xml.etree.ElementTree as ET

#DISCLAIMER
#When opening the .txt file, there were some special characters that it couldn't comprehend.
#We tried to fix the errors as best as we could.
#Sometimes it would work on a Windows machine, but not a macOS machine.
#On the Windows machine, the best possible code is written below
#If attempting to open on macOS, lines 52, 62, and 90 can be interchangeable as follows
#with open(csvFile, encoding='utf-8')
#or
#with open(csvFile, encoding='windows-1252')
#or
#with open(csvFile, encoding='latin-1')
#or
#with open(csvFile, encoding='ISO-8859-1')


#NFL Offensive Player stats, 1999-2013.txt
txt_format = input(r"Please enter a .txt file to convert: ")

#Menu Loop
loop = True
while loop:
    print("\nHW #2 Data Format: Main Menu")
    print("\nEnter -c to convert to CSV format")
    print("\nEnter -j to convert to JSON format")
    print("\nEnter -x to convert to XML format")
    print("\nEnter -e to exit program")

    #User Input
    selection = input("\nEnter selection: ")

    #File Conversion
    if selection == "-c":
        #CSV Conversion (.txt -> .csv)
        csv_format = r"NFL Offensive Player stats, 1999-2013.csv"

        input_txt = csv.reader(open(txt_format, "r"), delimiter = '\t')
        output_csv = csv.writer(open(csv_format, 'w'))
    
        output_csv.writerows(input_txt)
        print("\nFile successfully converted to CSV\n")
    elif selection == "-j":
        #CSV Conversion (.txt -> .csv)
        csv_format = r"NFL Offensive Player stats, 1999-2013.csv"

        input_txt = csv.reader(open(txt_format, "r"), delimiter = '\t')
        output_csv = csv.writer(open(csv_format, 'w'))
    
        output_csv.writerows(input_txt)

        #JSON Conversion (.txt -> .csv -> .json)
        def to_json(csvFile, jsonFile):
            jsonList = []
      
            #Read csv file
            with open(csvFile, encoding='utf-8', errors = 'ignore') as csvf: 
                #Load csv file data using csv library's dictionary reader
                csvRead = csv.DictReader(csvf) 

                #Convert each csv row into py dict
                for row in csvRead: 
                    #Append py dict to json list
                    jsonList.append(row)
  
            #Convert py jsonList to JSON String and write to file
            with open(jsonFile, 'w', encoding='utf-8', errors = 'ignore') as jsonf: 
                jsonString = json.dumps(jsonList, indent=4)
                jsonf.write(jsonString)
          
        csvFile = r'NFL Offensive Player stats, 1999-2013.csv'
        jsonFile = r'NFL Offensive Player stats, 1999-2013.json'
        to_json(csvFile, jsonFile)
        print("\nFile successfully converted to JSON\n")
    elif selection == "-x":
        #XML Conversion (.txt -> .xml)
        def to_xml(d_list):
            with open('NFL Offensive Player stats, 1999-2013.xml', 'wb') as f:
                data = ET.Element('data')
                for data_d in d_list:
                    item1 = ET.SubElement(data, 'player')
                    for i, field in enumerate(data_d.keys()):
                        item2 = ET.SubElement(item1, 'field')
                        item2.set('name', field)
                        item2.text = data_d[field]

                # create a new XML file with the results
                mydata = ET.tostring(data)
                f.write(mydata)


        data_list = []

        try:
            with open("NFL Offensive Player stats, 1999-2013.txt", "r", encoding="utf-8", errors = 'ignore') as f:
                lines = f.read().split('\n')

                for line in lines[1:-1]:
                    data_dict = {}
                    data = line.split('\t')
                    for i, field in enumerate(lines[0].split('\t')):
                        data_dict[field] = data[i]
                    data_list.append(data_dict)

        except FileNotFoundError:
            print("File not found!")
            raise SystemExit

        to_xml(data_list)
        print("\nFile successfully converted to XML\n")
    elif selection == "-e":
        print("\nExiting program...")
        loop = False