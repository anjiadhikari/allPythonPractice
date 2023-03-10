# importing the module  
#pytube used for downloading videos from youtube

from pytube import YouTube

# link of the video to be downloaded 
link = input("Enter The Link of video : ")

try: 
    # object creation using YouTube 
    yt = YouTube(link)

    #Title of video
    print("The Title of video is: ", yt.title)

    #Number of views of video
    print("Number of views: ",yt.views)

    #Length of the video
    print(f"Length of video: {yt.length} seconds")

    #Description of video
    print("Description: ",yt.description)

    #get the video highest resolution
    ys = yt.streams.get_highest_resolution()

    # downloading the video 
    ys.download('')
    print('Download Completed!') 
except: 
    print("Try again") #to handle exception 