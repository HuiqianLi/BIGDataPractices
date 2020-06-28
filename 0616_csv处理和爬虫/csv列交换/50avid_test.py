import csv

file_path ='50avid.csv'
infile = open(file_path,'r', encoding='utf_8_sig')
file_out = '50avid_result.csv'
outfile = open(file_out,'w', encoding='utf_8_sig', newline = "")

fieldnames = ['UPname',
    'avid0',
    'avid1',
    'avid2',
    'avid3',
    'avid4',
    'avid5',
    'avid6',
    'avid7',
    'avid8',
    'avid9',
    'avid10',
    'avid11',
    'avid12',
    'avid13',
    'avid14',
    'avid15',
    'avid16',
    'avid17',
    'avid18',
    'avid19',
    'avid20',
    'avid21',
    'avid22',
    'avid23',
    'avid24',
    'avid25',
    'avid26',
    'avid27',
    'avid28',
    'avid29',
    'avid30',
    'avid31',
    'avid32',
    'avid33',
    'avid34' ,
    'avid35' ,
    'avid36' ,
    'avid37' ,
    'avid38' ,
    'avid39' ,
    'avid40' ,
    'avid41' ,
    'avid42' ,
    'avid43' ,
    'avid44' ,
    'avid45' ,
    'avid46' ,
    'avid47' ,
    'avid48' ,
    'avid49' ]
# reader2 = csv.reader(infile)
writer = csv.DictWriter(outfile, fieldnames=fieldnames)
writer.writeheader()
for row in csv.DictReader(infile):
    writer.writerow(row)