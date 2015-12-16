import sys
import chilkat

ftp = chilkat.CkFtp2()

#  Any string unlocks the component for the 1st 30-days.
success = ftp.UnlockComponent("Anything for 30-day trial")
if (success != True):
    print(ftp.lastErrorText())
    sys.exit()

ftp.put_Hostname("www.example-code.com")
ftp.put_Username("***")
ftp.put_Password("***")

#  Use Passive mode.
ftp.put_Passive(True)

#  Connect and login to the FTP server.
success = ftp.Connect()
if (success != True):
    print(ftp.lastErrorText())
    sys.exit()

#  Change to the remote directory where the file will be uploaded.
success = ftp.ChangeRemoteDir("junk")
if (success != True):
    print(ftp.lastErrorText())
    sys.exit()

#  Upload a file.
localFilename = "hamlet.xml"
remoteFilename = "hamlet.xml"

success = ftp.PutFile(localFilename,remoteFilename)
if (success != True):
    print(ftp.lastErrorText())
    sys.exit()

ftp.Disconnect()

print("File Uploaded!")