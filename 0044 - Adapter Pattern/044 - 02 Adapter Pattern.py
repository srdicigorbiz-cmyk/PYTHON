class Mp3Player:
    def play_mp3(self, filename):
        return f"Playing MP3: {filename}"


class Mp4Player:
    def play_mp4(self, filename):
        return f"Playing MP4: {filename}"


class MediaAdapter:
    def __init__(self, player, audio_type):
        self.player = player
        self.audio_type = audio_type
    
    def play(self, filename):
        if self.audio_type == "mp3":
            return self.player.play_mp3(filename)
        elif self.audio_type == "mp4":
            return self.player.play_mp4(filename)

class AudioPlayer:
    def play(self, audio_type, filename):
        if audio_type == "mp3":
            return Mp3Player().play_mp3(filename)
        else:
            adapter = MediaAdapter(Mp4Player(), audio_type)
            return adapter.play(filename)


player = AudioPlayer()
print(player.play("mp3", "song.mp3"))
print(player.play("mp4", "video.mp4"))
