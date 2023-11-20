class MusicTracker():
    def __init__(self):
        self.tracks = []

    def add(self, track):
        if track == '':
            raise Exception("Track must be at least one character long")
        self.tracks.append(track)

    def history(self):
        return self.tracks