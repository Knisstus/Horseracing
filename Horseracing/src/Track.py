
class Track:    # this class is used for the tracks

    def __init__(self, name, segments, lanes, quality):
        self.name = name
        self.segments = segments  # segments are the length of the track
        self.lanes = lanes  # lanes determine the amount of horses that can race on the track
        self.quality = quality  # quality affects the speed of the horse
        self.map = []  # the map is used to  visually represent the tack
        for la in range(self.lanes):  # this loop dynamically generates a map using lanes and segments
            lane = []
            for se in range(self.segments):
                lane.append("_")

            self.map.append(lane)

    def print_track(self):  # her the map is printed in the output
        cur_lane = ""
        print("-" * self.segments)
        for x in range(self.lanes):
            for y in range(self.segments):
                cur_lane += self.map[x][y]

            print(cur_lane)
            cur_lane = ""
        print("-" * self.segments)
