class SpaceAge:
    earth_year = 31557600
    mercury_year = earth_year * 0.2408467
    venus_year = earth_year * 0.61519726
    mars_year = earth_year * 1.8808158
    jupiter_year = earth_year * 11.862615
    saturn_year = earth_year * 29.447498
    uranus_year = earth_year * 84.016846
    neptune_year = earth_year * 164.79132
    
    def __init__(self, seconds):
        self.seconds = seconds
        
    def on_earth(self):
        self.seconds = round(self.seconds / SpaceAge.earth_year, 2)
        return self.seconds
    def on_mercury(self):
        self.seconds = round(self.seconds / SpaceAge.mercury_year, 2)
        return self.seconds
    def on_venus(self):
        self.seconds = round(self.seconds / SpaceAge.venus_year, 2)
        return self.seconds
    def on_mars(self):
        self.seconds = round(self.seconds / SpaceAge.mars_year, 2)
        return self.seconds
    def on_jupiter(self):
        self.seconds = round(self.seconds / SpaceAge.jupiter_year, 2)
        return self.seconds
    def on_saturn(self):
        self.seconds = round(self.seconds / SpaceAge.saturn_year, 2)
        return self.seconds
    def on_uranus(self):
        self.seconds = round(self.seconds / SpaceAge.uranus_year, 2)
        return self.seconds
    def on_neptune(self):
        self.seconds = round(self.seconds / SpaceAge.neptune_year, 2)
        return self.seconds