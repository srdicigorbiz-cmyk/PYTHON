class PlayingState:
    def play(self, player):
        print("Already playing")
    
    def stop(self, player):
        print("Stopping music")
        player.state = StoppedState()


class StoppedState:
    def play(self, player):
        print("Starting music")
        player.state = PlayingState()
    
    def stop(self, player):
        print("Already stopped")


class MusicPlayer:
    def __init__(self):
        self.state = StoppedState()
    
    def play(self):
        self.state.play(self)
    
    def stop(self):
        self.state.stop(self)


player = MusicPlayer()
player.play()   # Starting music
player.play()   # Already playing
player.stop()   # Stopping music
player.stop()   # Already stopped
