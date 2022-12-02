# CSV to Excel table view

Using `pandas` and `XlxsWriter` to easily convert a csv file to a Excel human readable and FILTRABLE (table view) file, interesting with BIG files.

## Install dependencies

```
pip install -r requirements.txt
```

## Input file

```
ID,Date,FirstName,LastName,E-mail
H2NM4KQQ5VVPB7UC,1988-01-12,Angie,Barnett-Roy,demetrice.francis@jade.com
SY0GQK10VB6VOHLM,2022-03-25,Demetra,Montenegro,stephaine.santoro@hotmail.com
Y1P2P4FQN90NQCA8,2016-02-04,Elizebeth,Pack,gregoria3@gmail.com
E7RZEHYE6JBOZO39,1991-09-07,Damien,Utley,yoshiebreeden5935@ni.clan.rip
EVM2PXYDXUMUZVVQ,2019-08-28,Santo,Calvert,alidadoolittle@hotmail.com
RPE0GJQKZU52358C,1980-02-16,Leila,Beasley,cassie-avila8446@yahoo.com
ZPQLEOUL61ZZXSLU,1991-06-19,Ranae,Spears,veta.shook@yahoo.com
QRUHFSHPDBQR2QIG,2002-07-18,Tuyet,Creed,janise78@gmail.com
H8DBT8909LAT7MH1,2004-09-24,Tracy,Mcneal,abigail.connors@gmail.com
G3Z5C6QDXLIX5C0O,1977-12-19,Tyler,Himes,candice5708@hotmail.com
```

## Launch the script

```
python3 csv2exceltable.py -i sample.csv
```

## Output
![img](https://i.imgur.com/J9CX78I.png)

## Result

![img](https://i.imgur.com/oE1Wb1x.png)