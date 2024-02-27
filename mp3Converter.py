from moviepy.editor import *

#path to mp4 file
def mp3Converter(mp4,mp3Path="audio.mp3"):
    videoClip = VideoFileClip(mp4)
    audioClip = videoClip.audio
    audioClip.write_audiofile(mp3Path)
    audioClip.close()
    videoClip.close()

# worked perfectly
#mp3Converter("./LAGOS LAWYER 🤣😭🙆🏾‍♂️.mp4","./downloads/lagos_lawyer.mp3")

print("pops welcome to Rogetz mp3Converter,follow the simple instructions to convert your file to audio\n")
initial_path = input("path to file to convert and file as one:")
while len(initial_path) < 1:
    print("input a file please\n")
else:
    try:
        print(f"input the path and file you want to store as one\n")
        final_path = input("path to file:")
        while final_path == None:
            print("type your path to file kindly for you to continue.")
        else:
            mp3Converter(initial_path,final_path)
    except:
        print("error while converting.sorry...")
