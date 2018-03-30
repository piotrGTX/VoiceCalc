import sys, os, glob, uuid

RANDOM_NAME = uuid.uuid4().hex

os.system("mkdir .\out")
os.system(f"E:\Programy\sox-14-4-2\sox.exe {sys.argv[1]} .\out\{RANDOM_NAME}.wav silence 1 0.15 0.8% 1 0.15 1% : newfile : restart")
os.system("mkdir .\outSilent")

for f in glob.glob(".\out\*.wav"):
	name = os.path.basename(f)
	os.system(f"E:\Programy\sox-14-4-2\sox.exe -m {f} ..\cisza.wav .\outSilent\{name}")

print("Nazwa: " + str(RANDOM_NAME))