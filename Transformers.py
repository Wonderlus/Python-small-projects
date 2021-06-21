import random
import time
aunames = ["Cliffjumper", "Ratchet", "Ironhide", "Wheeljack"]
decnames = ["Starscream", "Thundercracker", "Skywarp", "Sunstorm"]
auto_uses = []  # Имена
dec_uses = []  # Имена


class Transformer:

    def __init__(self, name, power):
        self.name = name
        self.power = power
        print("\nCreated: '{}' with power: {}\n".format(self.name, self.power))

    def watch(self):
        print("Name: {} | Power: {}".format(self.name, self.power))

    def getName(self):
        return self.name

    def getPow(self):
        return self.power


class Autobot(Transformer):
    count = 0

    def __init__(self, name, power):
        Transformer.__init__(self, name, power)
        Autobot.count += 1


class AutobotLeader(Autobot):
    st = 0

    def __init__(self, power):
        self.name = "Optimus Prime"
        self.power = power
        Autobot.count += 1
        print("\nCreated: '{}' with power: {}\n".format(self.name, self.power))

    @staticmethod
    def status():
        if "Optimus Prime" not in auto_uses:
            if AutobotLeader.st == 2:
                optimus = AutobotLeader(random.randint(80, 100))
                auto.insert(0, optimus)
                auto_uses.append(optimus.getName())
                AutobotLeader.st = 0
            else:
                print("Optimus Prime ready on {}%\n".format(AutobotLeader.st*50))
            AutobotLeader.st += 1


class Decepticon(Transformer):
    count = 0

    def __init__(self, name, power):
        Transformer.__init__(self, name, power)
        Decepticon.count += 1


class DecepticonLeader(Decepticon):
    st = 0

    def __init__(self, power):
        self.name = "Megatron"
        self.power = power
        Decepticon.count += 1
        print("\nCreated: '{}' with power: {}\n".format(self.name, self.power))

    @staticmethod
    def status():
        if "Megatron" not in dec_uses:
            if DecepticonLeader.st == 2:
                megatron = DecepticonLeader(random.randint(80, 100))
                dec.insert(0, megatron)
                dec_uses.append(megatron.getName())
                DecepticonLeader.st = 0
            else:
                print("Megatron ready on {}%\n".format(DecepticonLeader.st*50))
            DecepticonLeader.st += 1


def choose():
    for_fight = {}
    while True:
        print("Select an action:\n1 - create Autobot\n2 - create Decepticon\n\
        3 - see Autobots\n4 - see Decepticons\n"
              "5 - Form teams for fight\n6 - Start battle\n7 - Watch teams")
        n = str(input())
        if n == "1":
            incr = False
            if opt in auto:
                incr = True
                auto.remove(opt)
            if len(auto) < 4:
                inc(auto, aunames, auto_uses, Autobot)
            else:
                print("\nMaximum of Autobots\n")
            if incr:
                auto.insert(0, opt)
        elif n == "2":
            incr = False
            if meg in dec:
                incr = True
                dec.remove(meg)
            if len(dec) < 4:
                inc(dec, decnames, dec_uses, Decepticon)
            else:
                print("\nMaximum of Decepticons\n")
            if incr:
                dec.insert(0, meg)
        elif n == "3":
            print("\nAutobots")
            for_watch(auto)
            print("")
        elif n == "4":
            print("\nDecepticons")
            for_watch(dec)
            print("")
        elif n == "5":
            for_fight = {}
            try:
                for_watch(auto)
                print("")
                for_watch(dec)
                auto_unused = auto[:]
                dec_unused = dec[:]
                print("")
                while dec_unused != [] and auto_unused != []:
                    z = auto_unused[int(
                        input("Write number of Autobot or write something to\
                              exit and save teams: ")) - 1]
                    x = dec_unused[int(
                        input("Write number of Decepticon: ")) - 1]
                    for_fight[z] = x
                    auto_unused.remove(z)
                    dec_unused.remove(x)
                    print("")
                    if auto_unused:
                        i = 0
                        print("Unused Autobots:")
                        for elem in auto_unused:
                            i += 1
                            print(i, "-", elem.getName())
                    print("")
                    if dec_unused:
                        i = 0
                        print("Unused Decepticons:")
                        for elem in dec_unused:
                            i += 1
                            print(i, "-", elem.getName())
                    print('')
                    for a, b in for_fight.items():
                        print(a.getName(), "versus", b.getName())
                    print("")
            except IndexError:
                for_fight = {}
                print("Wrong Number\nStart again")
            except ValueError:
                pass

        elif n == "6" and for_fight != {}:
            fight(for_fight)
            for_fight = {}
        elif n == "6" and for_fight == {}:
            print("You have not formed teams")
        elif n == "7":
            if for_fight == {}:
                print("You have not formed teams")
            else:
                for a, b in for_fight.items():
                    print(a.getName(), "versus", b.getName())


def inc(list_obj, names, uses, clas):
    index = random.randint(0, 3)
    while True:
        if names[index] not in uses:
            list_obj.append(clas(names[index], random.randint(40, 80)))
            uses.append(names[index])
            break
        else:
            index = random.randint(0, 3)


def for_watch(list_obj):
    for elem in list_obj:
        elem.watch()


def fight(dictionary):
    for a, d in dictionary.items():
        print("\nFighting...")
        time.sleep(3)
        if a.getPow() > d.getPow():
            print("{} destroyes {}".format(a.getName(), d.getName()))
            loser = d
            dec.remove(loser)  # Объект
            loser = d.getName()
            dec_uses.remove(loser)  # Имя
        elif a.getPow() < d.getPow():
            print("{} destroyes {}".format(d.getName(), a.getName()))
            loser = a
            auto.remove(loser)  # Объект
            loser = a.getName()
            auto_uses.remove(loser)  # Имя
        else:
            print("Powers are equal")
    print("\nEnd fight...")
    time.sleep(3)
    opt.status()
    meg.status()


auto_uses.append("Optimus Prime")
dec_uses.append("Megatron")
opt = AutobotLeader(random.randint(80, 100))
meg = DecepticonLeader(random.randint(80, 100))
auto = [AutobotLeader(random.randint(80, 100))]  # Объекты
dec = [meg]  # Объекты
choose()
