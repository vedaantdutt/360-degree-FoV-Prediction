#We are obtaining 10 frames from FoV n/w
#Make the necessary changes such as the name of the output binary file accordingn to each video
#and name of the reconstructed file in the cfg of both 360ConvertApp and EncoderApp to avoid
#overwriting and losing data
import os

choice = int(input("Choose a mode (0: with FoV prediction, 1: without FoV prediction ): "))

while(choice > 1):
    print("Invalid choice, please choose 0 or 1")
    choice = int(input("Choose a mode (0: with FoV prediction, 1: without FoV prediction ): "))

if (choice == 0):
    print("Using FoV prediction")
    os.system("Path to main.py script in your laptop")
    os.system(r"E:\VVC-clone\vcc\VTM-5.0\VTM-5.0\bin\vs16\msvc-19.28\x86_64\release\360ConvertApp.exe -c E:\VVC-clone\vcc\VTM-5.0\VTM-5.0\cfg-360Lib\custom_vid_1.cfg && E:\VVC-clone\vcc\VTM-5.0\VTM-5.0\bin\vs16\msvc-19.28\x86_64\release\EncoderApp.exe -c E:\VVC-clone\vcc\VTM-5.0\VTM-5.0\cfg\custom.cfg")


if (choice == 1):
    print("Without using FoV prediction")
    os.system(r"E:\VVC-clone\vcc\VTM-5.0\VTM-5.0\bin\vs16\msvc-19.28\x86_64\release\360ConvertApp.exe -c E:\VVC-clone\vcc\VTM-5.0\VTM-5.0\cfg-360Lib\custom_vid_1.cfg")
    os.system(r" E:\VVC-clone\vcc\VTM-5.0\VTM-5.0\bin\vs16\msvc-19.28\x86_64\release\EncoderApp.exe -c E:\VVC-clone\vcc\VTM-5.0\VTM-5.0\cfg\custom.cfg")