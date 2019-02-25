class Gun:
    
    def __init__(self, name, fire_range, bullet_capacity):
        self.name = name
        self.fire_range = fire_range
        self.bullet_capacity = bullet_capacity
        self.ammo = 15

    def __repr__(self):
        return f'{self.name}, Range:{self.fire_range}, Capacity:{self.bullet_capacity}'

sip = Gun('Loader', '5cm', 12)
print(sip)
