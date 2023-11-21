class MusicLibrary:
    # Public properties:
    #   tracks: a list of strings representing tracks

    def __init__(self):
        self.tracks = []

    def add(self, track):
        # Parameters:
        #   track: an instance of Track
        # Returns:
        #   Nothing
        self.tracks.append(track)
    
    def search_by_title(self, keyword):
        # Parameters:
        #   keyword: a string
        # Returns:
        #   a list of Track instances with titles that include the keyword
        search_results = []
        for track in self.tracks:
            if keyword in track.title:
                search_results.append(track)
        return search_results
        # Alternative code:
        # return [
        #   track
        #   for track in self.tracks
        #   if keyword in track.title
        # ]