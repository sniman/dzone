import ftplib

ftp = ftplib.FTP('172.23.183.149', 'desktop1', 'Letmein01')

print("File List: ")

files = ftp.dir()

print(files)

ftp.cwd("/pub/unix") #changing to /pub/unix