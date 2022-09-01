class Erkin():
    def __init__(self, boy, yaş, meslek):
        self.boy = boy
        self.yaş = yaş
        self.meslek = meslek

    def ShowInfo(self):
        print("""Showing Infos
        boy={}
        yaş={}
        meslek={}






        """.format(self.boy, self.yaş, self.meslek))

    def mesleChanging(self, yenimeslek):
        self.meslek = yenimeslek

        print("Meslek Güncellendi... ")



