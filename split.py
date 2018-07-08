import subprocess
import sys
import easygui

def main():
    """split a music track into specified sub-tracks by calling ffmpeg from the shell"""

    #Registering user input of files.
    #First is to select audio file for splitting, second is the text file with time and tracks.
    easygui.msgbox("Choose file to split")
    original_track = easygui.fileopenbox()
    easygui.msgbox("Choose text file that contains Start | End Times and titles")
    track_list = easygui.fileopenbox()

    # create a template of the ffmpeg call in advance
    cmd_string = 'ffmpeg -i {tr} -acodec copy -ss {st} -to {en} {nm}.m4a'

    # read each line of the track list and split into start, end, name
    with open(track_list, 'r') as f:
        for line in f:
            # skip comment and empty lines
            if line.startswith('#') or len(line) <= 1:
                continue

            # create command string for a given track
            start, end, name = line.strip().split()
            command = cmd_string.format(tr=original_track, st=start, en=end, nm=name)

            # use subprocess to execute the command in the shell
            subprocess.call(command, shell=True)

    return None


if __name__ == '__main__':
    main()
