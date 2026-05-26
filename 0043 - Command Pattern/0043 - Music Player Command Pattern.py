# Van: MusicPlayer osztály - play(), pause(), next_track() metódusokkal
# Van: PlayCommand, PauseCommand, NextTrackCommand – execute() és undo()
# Van: SmartRemote – execute_command(), undo()
class MusicPlayer:
    def play(self):
        print("PLAY")
    def pause(self):
        print("PAUSE")
    def next_track(self):
        print("NEXT TRACK")


class PlayCommand:
    def __init__(self, player):
        self.player = player
    def execute(self):
        self.player.play()
    def undo(self):
        self.player.pause()

class PauseCommand:
    def __init__(self, player):
        self.player = player
    def execute(self):
        self.player.pause()
    def undo(self):
        self.player.play()

class NextTrackCommand:
    def __init__(self, player):
        self.player = player
    def execute(self):
        self.player.next_track()
    def undo(self):
        self.player.play()


class SmartRemote:
    def execute_command(self, command):
        self.command = command
        self.command.execute()
    def undo(self):
        self.command.undo()



player = MusicPlayer()
remote = SmartRemote()

remote.execute_command(PlayCommand(player))
remote.execute_command(NextTrackCommand(player))
remote.undo()  # visszamegy az előző trackre
remote.execute_command(PauseCommand(player))