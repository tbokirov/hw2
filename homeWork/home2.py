class Hero:
    head = 1
    ability = True

    def __init__(self,name,nickname,heatpoint,damage):
      self.name=name
      self.hp=heatpoint
      self.nickname=nickname
      self.damage=damage

    def heal(self,hp):
      print(self.hp + 100)

    def two_damage(self, x2):
      print(self.damage * x2)

    def greetings(self):
        print('my name is ' + self.nickname)

    def brand_phrase(self):
        print('good will win')

player1 = Hero(name = 'Paladin', nickname = 'Pd', heatpoint = 100 , damage = 70 )
player1.heal(100)
print(player1.name,player1.nickname,player1.hp,player1.damage)

player2 = Hero(name = 'Tbokirov', nickname = 'tbkrv', heatpoint= 50, damage = 50)
print(player2.name , player2.nickname , player2.hp , player2.damage)
player2.two_damage(2)

player3 = Hero(name = 'Big', nickname = 'Mike', heatpoint = 10, damage = 90)
print(player3.name , player3.nickname , player3.hp , player3.damage)
player3.greetings()

player4 = Hero(name = 'Palash', nickname = 'Bocman', heatpoint = 5 , damage = 10)
print(player4.name , player4.nickname , player4.hp , player4.damage)
player4.brand_phrase()
class Air(Hero):
    wings = 2
    def __init__(self, name, nickname, hp, damage, fly=False):
        super().__init__(name, nickname, hp, damage)
        self.fly = fly
    def brand_phrase(self):
        self.fly = True
        print('fly in the True_phrase')
    def _gutenmorgen(self):
        pass
class Space(Hero):
    hands = 12
    def __init__(self, name, nickname, hp, damage, fly=False):
        super().__init__(name, nickname, hp, damage)
        self.fly = fly
    def brand_phrase(self):
        self.fly = True
        print('fly in the True_phrase')
    def __gutentak(self):
        pass
class Earthly(Hero):
    ankles = 2
    def __init__(self, name, nickname, hp, damage, fly=False):
        super().__init__(name, nickname, hp, damage)
        self.fly = fly
    def brand_phrase(self):
        self.fly = True
        print('fly in the True_phrase')
    def __gutenabend(self):
        pass
h1 = Air(name='soap', nickname='maktvish', hp=780, damage=60)
h2 = Space(name='ghost', nickname='...', hp=800, damage=90)
h3 = Earthly(name='gas', nickname='goose', hp=1000, damage=200)
h1.brand_phrase()