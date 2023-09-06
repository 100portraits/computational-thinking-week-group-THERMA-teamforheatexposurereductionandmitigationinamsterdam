def solution_station_5(name):
    import pandas as pd
    members_dict = {1 : ['Mika', 'Maria', 'Isis', 'Rosa', 'Maja', 'Damaris'], 2 : ['Emily ', 'Celia', 'Carine', 'Sabrina', 'Maria', 'Gur'], 3 : ['Elisa', 'Sari', 'Dave', 'Dima', 'Jesper', 'Martyna'], 4 : ['Kelt', 'Sebastian', 'Quanpu', 'Ruben', 'Sofia', 'Gabriella'], 5 : ['Kian', 'Sahir', 'Tom', 'Gonzalo', 'Ameer', 'Teun'], 6 : ['Angelica', 'Matas', 'Caleb', 'Angeline', 'Raven', 'Paulina'], 7 : ['Martyna', 'Maja ', 'Mate', 'Vincent', 'Eryk', 'Emma'], 8 : ['Hielke', 'Liss', 'Beatris', 'Caio', 'Sally', 'Sanne'], 9 : ['Atlas', 'Elli', 'Felix', 'Diana', 'Yash'], 10 : ['Akanksha', 'Charlie', 'Andrey', 'Max', 'Hugo', 'Al-fatihi'], 11 : ['Misha', 'Ioanna', 'Ella', 'Cristian', 'Vanessa'], 12 : ['Luca', 'Rachna', 'Jelle', 'Karolina', 'Yuyue', 'Alexia']}
    ans=None
    for i in range(1, 13):
        if name in members_dict[i]:
            ans=i

    return ans
