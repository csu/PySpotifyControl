import subprocess

scripts = {
    "volumeUp": 'tell application "Spotify" to set sound volume to (sound volume + 10)',
    "volumeDown": 'tell application "Spotify" to set sound volume to (sound volume - 10)',
    "setVolume": 'tell application "Spotify" to set sound volume to %s',
    "play": 'tell application "Spotify" to play',
    "playTrack": 'tell application "Spotify" to play track "%s"',
    "playPause": 'tell application "Spotify" to playpause',
    "pause": 'tell application "Spotify" to pause',
    "next": 'tell application "Spotify" to next track',
    "previous": 'tell application "Spotify" to previous track',
    "jumpTo": 'tell application "Spotify" to set player position to %s',
    "getSongId": 'tell application "Spotify" to current track\'s id',
    "getSongDuration": 'tell application "Spotify"  to current track\'s duration',
    "getSongName": 'tell application "Spotify"  to current track\'s name',
    "getSongArtist": 'tell application "Spotify"  to current track\'s artist'
}

def run(ascript):
  osa = subprocess.Popen(['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
  return osa.communicate(ascript)[0]

def getSongId():
    return run(scripts["getSongId"]).rstrip()

def getSongName():
    return run(scripts["getSongName"]).rstrip()

def getSongArtist():
    return run(scripts["getSongArtist"]).rstrip()

def getSongDuration():
    return int(run(scripts["getSongDuration"]).rstrip())

def volumeUp():
    run(scripts["volumeUp"])

def volumeDown():
    run(scripts["volumeDown"])

def play():
    run(scripts["play"])

def playPause():
    run(scripts["playPause"])

def pause():
    run(scripts["pause"])

def next():
    run(scripts["next"])

def previous():
    run(scripts["previous"])

def setVolume(volume):
    run(scripts["setVolume"] % volume)

def jumpTo(position):
    run(scripts["jumpTo"] % position)

def playTrack(track_uri):
    run(scripts["playTrack"] % track_uri)