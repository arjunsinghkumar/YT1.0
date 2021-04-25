def combine_audio(vidname, audname, outname, fps=25):
    import moviepy.editor as mpe
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname,fps=fps)

combine_audio('C:/poems/output_video.mp4','C:/poems/rsc/Poem0.mp3' , 'C:/poems/pls_work.mp4', fps=25)