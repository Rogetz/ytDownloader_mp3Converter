from pytube import YouTube
import sys
import os


absolutePath = os.path.abspath(r".")
outputPath = os.path.join(absolutePath,"./downloads")

#perfectly worked, this if for video only though, I want to make one for choosing,audio,video and e.t.c
def highResolutionVideoDownload(linkReceived):
    try:
        videoObject = YouTube(linkReceived)
        print(f"Video title: {videoObject.title} \n")
        stream = videoObject.streams.get_highest_resolution()
        
        stream.download(output_path=outputPath)
    except:
        print("youtube link is invalid, or there's an error.sorry...")


def lowResolutionVideoDownload(linkReceived):
    try:
        videoObject = YouTube(linkReceived)
        print(f"Video title: {videoObject.title} \n ")
        stream = videoObject.streams.get_lowest_resolution()
        
        stream.download(output_path=outputPath)
    except:
        print("youtube link is invalid, or there's an error.sorry...")

# Get the video by the resolution e.g "720p" "360p" "240p" "480p" "144p"
def videoByResolution(linkReceived,resolution="360p"):
    try:
        videoObject = YouTube(linkReceived)
        print(f"Video title: {videoObject.title} \n ")
        # enable the user to choose the resolution
        stream = videoObject.streams.get_by_resolution(resolution)
        
        stream.download(output_path=outputPath)
    except:
        print("youtube link is invalid, or there's an error.sorry...")


# for downloading any video file type
def audioDownload(linkReceived):
    try:
        videoObject = YouTube(linkReceived)
        print(f"audio title: {videoObject.title} \n ")
        # by default subtype is mp4 and you can't change to mp3 since it won't work.
        # use ffmpeg to convert to audio there's a way to connect it directly using a subprocess in python
        #stream = videoObject.streams.get_audio_only()
        stream = videoObject.streams.filter(only_audio=True).first()
        stream.download(output_path=outputPath)
    except:
        print("youtube link is invalid, or there's an error.sorry...")


# This is meant to fetch data from the cmd
# use lenght of 2 to ensure that it doesn't take in the file name.
# length must be two.
"""
if len(sys.argv) == 2: 
    linkToUse = sys.argv[1]
    videoDownload(linkToUse)
else:
    print("ensure you've typed in the link or provide a valid link")
"""


# redesign it to be an interactive command line interface programm.

print("pops welcome to Rogetz youtube downloader,copy/type the youtube link to continue\n")
initialLink = input("youtube link:")
while len(initialLink) < 1:
    print("input a link please\n")
else:
    try:
        videoObject = YouTube(initialLink)
        print(f"video title: {videoObject.title}")
        print("streams available:")
        for stream in videoObject.streams:
            streamsFound = []
            print(f"mime_type {stream.mime_type} , {stream.resolution} resolution ")
            streamsFound.append(stream.resolution)

        print("\nchoose one resolution from the list above if in need of a specific video resolution e.g '360p'\n")
        print(f"if in need of a high/low resolution simply type 'high' or 'low'\n")
        print(f"if in need of audio type audio: only mp4 supported\n")
        answer = input("choice:")
        while answer == None:
            print("type your choice kindly for you to continue.")
        else:
            if answer == "high":
                highResolutionVideoDownload(initialLink)
            elif answer == "low":
                lowResolutionVideoDownload(initialLink)
            elif answer == "audio":
                audioDownload(initialLink)
            elif len(answer) > 3:
                # pass over the resolution
                videoByResolution(initialLink,answer)
    except:
        print("youtube link is invalid, or there's an error.sorry...")

    