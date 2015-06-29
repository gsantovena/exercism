class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        return round(self.seconds / 31557600.0, 2)

    def on_mercury(self):
        return round(self.on_earth() / 0.2408467, 2)

    def on_venus(self):
        return round(self.on_earth() / 0.61519726, 2)

    def on_mars(self):
        return round(self.on_earth() / 1.8808158, 2)

    def on_jupiter(self):
        return round(self.on_earth() / 11.862615, 2)

    def on_saturn(self):
        return round(self.on_earth() / 29.447498, 2)

    def on_uranus(self):
        return round(self.on_earth() / 84.016846, 2)

    def on_neptune(self):
        return round(self.on_earth() / 164.79132, 2)

if __name__ == '__main__':
    age = SpaceAge(1e9)
    print(age.on_earth())

    age = SpaceAge(31557600)
    print(age.on_earth())

    age = SpaceAge(2134835688)
    print(age.on_earth()) # 67.65
    print(age.on_mercury()) # 280.88


