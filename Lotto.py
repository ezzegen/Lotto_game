import random


class LotoCard:
    """
    Класс для генерации чисел лото-карточки
    """
    def __init__(self):
        self.card_lst = []
        self.card_player = str
        self.card_computer = str

    def create_card(self):
        # Создание общего списка с элементами игровых карточек player[1] и computer[0]
        self.card_lst = [[random.sample([
            item for elem in [('  ', num)
                              for _, num in zip(range(5), random.sample(list(range(91)), 5))]
            for item in elem], 10) for _ in range(3)] for _ in range(2)]
        [self.card_lst[j].insert(i * 2, '\n') for j in range(len(self.card_lst)) for i in range(0, 3)]


class Computer(LotoCard):
    """
    Создание индивидуальной карточки компьютера
    """
    def __init__(self):
        super().__init__()
        LotoCard.create_card(self)
        self.card_lst_computer = [i for e in self.card_lst[0] for i in e]

    def create_card_computer(self):
        # Исключение повторяющихся элементов и добавление спец. символов для создания интерфейса карточки.
        for i in self.card_lst_computer:
            if self.card_lst_computer.count(i) > 1 and i not in ['  ', '\n']:
                self.card_lst_computer[self.card_lst_computer.index(i)] = random.randint(1, 91)
        self.card_lst_computer.insert(0, ('-' * 6 + 'Карточка компьютера' + '-' * 6))
        self.card_lst_computer.insert(34, '\n' + ('-' * 31))
        self.card_computer = ' '.join(list(map(str, self.card_lst_computer)))
        return self.card_computer


class Player(Computer):
    """
        Создание индивидуальной карточки игрока
    """
    def __init__(self):
        super().__init__()
        LotoCard.create_card(self)
        self.card_lst_gamer = [i for e in self.card_lst[0] for i in e]

    def create_card_player(self):
        # Исключение повторяющихся элементов и добавление спец. символов для создания интерфейса карточки.
        for i in self.card_lst_gamer:
            if self.card_lst_gamer.count(i) > 1 and i not in ['  ', '\n']:
                self.card_lst_gamer[self.card_lst_gamer.index(i)] = random.randrange(1, 91)
        for i in self.card_lst_gamer:
            if i in self.card_lst_computer and i not in ['  ', '\n']:
                self.card_lst_gamer[self.card_lst_gamer.index(i)] = random.randrange(1, 91)
        self.card_lst_gamer.insert(0, ('-' * 9 + 'Ваша карточка' + '-' * 9))
        self.card_lst_gamer.insert(34, '\n' + ('-' * 31))
        self.card_player = ' '.join(list(map(str, self.card_lst_gamer)))
        return self.card_player


class LottoGame(Player):
    """Игра"""
    @staticmethod
    def barrel_choice():
        # Функция-имитация случайного выбора бочонка
        bag = list(range(1, 91))
        random.shuffle(bag)
        for barrel in bag:
            yield barrel

    def game(self):
        # Создание карточек игроков.
        Computer.create_card_computer(self)
        Player.create_card_player(self)
        for num in LottoGame.barrel_choice():
            print(self.card_player)
            print(self.card_computer)
            anw = input(f'Номер бочонка: {num}\nВычеркиваем из карточки?\ny/n\n')
            if anw == 'y':
                if num in self.card_lst_gamer:
                    # Реализация вычеркивания номера бочонка из карточки
                    self.card_lst_gamer[self.card_lst_gamer.index(num)] = ' -'
                    self.card_player = ' '.join(list(map(str, self.card_lst_gamer)))
                    # Проверка есть ли еще числа в карточке игрока.
                    count_num = 0
                    for elem in self.card_player:
                        if elem.isdigit():
                            count_num += 1
                    if count_num == 0:
                        print('Вы выиграли!')
                        break
                else:
                    print('Вы проиграли!\nКомпьютер победил!')
                    break
            else:
                # Реализация хода компьютера
                if num in self.card_lst_computer:
                    self.card_lst_computer[self.card_lst_computer.index(num)] = ' -'
                    self.card_computer = ' '.join(list(map(str, self.card_lst_computer)))
                    # Проверка есть ли еще числа в карточке.
                    count_num = 0
                    for elem in self.card_computer:
                        if elem.isdigit():
                            count_num += 1
                    if count_num == 0:
                        print('Вы проиграли!\nКомпьютер победил!')
                        break
                if num in self.card_lst_gamer:
                    print('Вы проиграли!\nКомпьютер победил!')
                    break
                else:
                    pass


game = LottoGame()
game.game()
