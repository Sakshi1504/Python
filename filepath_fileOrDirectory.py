import os
checkfor="automate_whatsapp_msg.py"

if(os.path.isdir(checkfor)):
    print("Path")
elif(os.path.isfile(checkfor)):
    print("File")
else:
    print("None")