class Athlete:
    def __init__(self, full_name, years_old, role):
        self.full_name = full_name
        self.years_old = years_old
        self.role = role

    def __str__(self):
        return f"ФИО: {self.full_name}\nВозраст: {self.years_old}\nАмплуа: {self.role}"

class Club:
    def __init__(self, club_title, head_coach):
        self.club_title = club_title
        self.head_coach = head_coach
        self.roster = []

    def add_athlete(self, athlete):
        self.roster.append(athlete)
        print(f"Атлет {athlete.full_name} добавлен в клуб {self.club_title}")

    def remove_athlete(self, athlete):
        if athlete in self.roster:
            self.roster.remove(athlete)
            print(f"Атлет {athlete.full_name} удален из клуба {self.club_title}")
        else:
            print(f"Атлет {athlete.full_name} не найден в клубе {self.club_title}")

    def show_roster(self):
        print(f"\nКлуб: {self.club_title}")
        print(f"Главный тренер: {self.head_coach}")
        print("Состав клуба:")
        for athlete in self.roster:
            print(athlete)
            print("-" * 20)

# Пример использования
if __name__ == "__main__":
    # Создаем атлетов
    athlete1 = Athlete("Иванов И.И.", 25, "Нападающий")
    athlete2 = Athlete("Петров П.П.", 30, "Полузащитник")
    athlete3 = Athlete("Сидоров С.С.", 28, "Защитник")

    # Создаем клубы
    club1 = Club("Алые", "Краснов А.")
    club2 = Club("Лазурные", "Синёв С.")

    # Добавляем атлетов в клубы
    club1.add_athlete(athlete1)
    club1.add_athlete(athlete2)
    club2.add_athlete(athlete3)

    # Показываем составы клубов
    club1.show_roster()
    club2.show_roster()

    # Удаляем атлета из клуба
    club1.remove_athlete(athlete2)

    # Показываем обновленный состав
    club1.show_roster()