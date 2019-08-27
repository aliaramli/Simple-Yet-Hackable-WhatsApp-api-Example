from whatsapp import WhatsApp
import time
import pandas
import argparse
import numpy
import glob
parser = argparse.ArgumentParser(description='Send anonymous message to clients')

parser.add_argument('csv_file', type=str, help='CSV file')
args = parser.parse_args()

app = WhatsApp(100)
app.override_timeout(30)

old_numbers=[]

# get all csv with numbers 
all_csv = glob.glob('fb_group_number*.csv')
for x in all_csv:
    if x != args.csv_file:
        print(x)
        try:
            csv = pandas.read_csv(x)
            for index, row in csv.iterrows():
                if row['Mobile'] == "":
                    continue
                if row['Mobile'] == "6":
                    continue
                if pandas.isna(row['Mobile']):
                    continue
                if not row['Mobile'].isdigit():
                    continue
                old_numbers.append(row['Mobile'])
        except Exception as e:
            print(e)
    
# append all phone numbers in csv file

try:
    csv = pandas.read_csv(args.csv_file)
    for index, row in csv.iterrows():       
        if row['Mobile'] == "":
            continue
        if row['Mobile'] == "6":
            continue
        if pandas.isna(row['Mobile']):
            continue
        try:
            if not len(row['Mobile']) > 6:
                continue
        except:
            pass
        
        try:
            if not len(str(row['Mobile'])) > 6:
                continue
        except:
            pass

        try:
            if not row['Mobile'].isdigit():
                continue
        except Exception as e:
            pass
        if row['Mobile'] in old_numbers:
            print("number contacted %s" % row['Mobile'])
            continue
        try:
            app.send_anon_message(row['Mobile'], "Hi, nak tanya skit boleh?\nSaya Alia dari foodah.my\nBerminat nak iklan makan secara percuma di foodah.my? percuma sahaja. takder sebarang charge akan dikenakan\nApa itu foodah.my ?? Platform yang mudah, professional & FREE untuk business makanan anda.FREE website iklan untuk iklankan makanan anda. :D\nConcept macam mudah.my . Anda berminat?")
        except Exception as e:
            print(e)
        time.sleep(10)
except Exception as e:
    print(e)
app.goto_main()
