
class Point():
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

        if not (-90 <= latitude <= 90) or not (-90 <= longitude <= 90):
            raise ValueError("Invalid latitude or longitude")


    def get_lat_long(self):
        return (self.latitude, self.longitude)
