from datetime import date
from sqlalchemy.orm import Session
from model import Users, Profiles, Publishers, Games, UserGames, Reviews, Gender, AgeRating


def init(session: Session) -> bool:
    publishers = [
        Publishers(name="Valve", country="USA"),
        Publishers(name="CD Projekt Red", country="Poland"),
        Publishers(name="Ubisoft", country="France"),
        Publishers(name="Electronic Arts", country="USA"),
        Publishers(name="Bethesda", country="USA"),
    ]
    session.add_all(publishers)
    session.flush()

    games = [
        # Valve
        Games(title="Counter-Strike 2", price=0.0, release_date=date(2023, 9, 27), age_rating=AgeRating.PEGI_16, publisher=publishers[0]),
        Games(title="Dota 2", price=0.0, release_date=date(2013, 7, 9), age_rating=AgeRating.PEGI_12, publisher=publishers[0]),
        Games(title="Team Fortress 2", price=0.0, release_date=date(2007, 10, 10), age_rating=AgeRating.PEGI_12, publisher=publishers[0]),
        Games(title="Portal 2", price=9.99, release_date=date(2011, 4, 19), age_rating=AgeRating.PEGI_7, publisher=publishers[0]),
        # CD Projekt Red
        Games(title="The Witcher 3", price=29.99, release_date=date(2015, 5, 19), age_rating=AgeRating.PEGI_18, publisher=publishers[1]),
        Games(title="Cyberpunk 2077", price=59.99, release_date=date(2020, 12, 10), age_rating=AgeRating.PEGI_18, publisher=publishers[1]),
        Games(title="The Witcher 2", price=19.99, release_date=date(2011, 5, 17), age_rating=AgeRating.PEGI_18, publisher=publishers[1]),
        Games(title="Gwent", price=0.0, release_date=date(2017, 10, 24), age_rating=AgeRating.PEGI_12, publisher=publishers[1]),
        # Ubisoft
        Games(title="Assassin's Creed Valhalla", price=49.99, release_date=date(2020, 11, 10), age_rating=AgeRating.PEGI_18, publisher=publishers[2]),
        Games(title="Far Cry 6", price=39.99, release_date=date(2021, 10, 7), age_rating=AgeRating.PEGI_18, publisher=publishers[2]),
        Games(title="Rainbow Six Siege", price=19.99, release_date=date(2015, 12, 1), age_rating=AgeRating.PEGI_18, publisher=publishers[2]),
        Games(title="For Honor", price=29.99, release_date=date(2017, 2, 14), age_rating=AgeRating.PEGI_12, publisher=publishers[2]),
        Games(title="Anno 1800", price=39.99, release_date=date(2019, 4, 16), age_rating=AgeRating.PEGI_7, publisher=publishers[2]),
        # Electronic Arts
        Games(title="FIFA 23", price=59.99, release_date=date(2022, 9, 30), age_rating=AgeRating.PEGI_3, publisher=publishers[3]),
        Games(title="Mass Effect Legendary Edition", price=59.99, release_date=date(2021, 5, 14), age_rating=AgeRating.PEGI_16, publisher=publishers[3]),
        Games(title="The Sims 4", price=0.0, release_date=date(2014, 9, 2), age_rating=AgeRating.PEGI_12, publisher=publishers[3]),
        Games(title="Apex Legends", price=0.0, release_date=date(2019, 2, 4), age_rating=AgeRating.PEGI_16, publisher=publishers[3]),
        # Bethesda
        Games(title="The Elder Scrolls V: Skyrim", price=39.99, release_date=date(2011, 11, 11), age_rating=AgeRating.PEGI_18, publisher=publishers[4]),
        Games(title="Fallout 4", price=19.99, release_date=date(2015, 11, 10), age_rating=AgeRating.PEGI_18, publisher=publishers[4]),
        Games(title="Doom Eternal", price=39.99, release_date=date(2020, 3, 20), age_rating=AgeRating.PEGI_18, publisher=publishers[4]),
    ]
    session.add_all(games)
    session.flush()

    users = [
        Users(username="alice",   email="alice@mail.com",   gender=Gender.Female),
        Users(username="bob",     email="bob@mail.com",     gender=Gender.Male),
        Users(username="charlie", email="charlie@mail.com", gender=Gender.Male),
        Users(username="diana",   email="diana@mail.com",   gender=Gender.Female),
        Users(username="evan",    email="evan@mail.com",    gender=Gender.Other),
        Users(username="fiona",   email="fiona@mail.com",   gender=Gender.Female),
        Users(username="greg",    email="greg@mail.com",    gender=Gender.Male),
        Users(username="helen",   email="helen@mail.com",   gender=Gender.Female),
        Users(username="ivan",    email="ivan@mail.com",    gender=Gender.Male),
        Users(username="julia",   email="julia@mail.com",   gender=Gender.Female),
    ]
    session.add_all(users)
    session.flush()

    profiles = [
        Profiles(user=users[0], bio="FPS and RPG lover",            country="Belgium",     birthdate=date(1995, 3, 15),  avatar_url="https://avatar.com/alice.png"),
        Profiles(user=users[1], bio="Competitive gamer",             country="France",      birthdate=date(1992, 7, 22),  avatar_url="https://avatar.com/bob.png"),
        Profiles(user=users[2], bio="Sports game enthusiast",        country="UK",          birthdate=date(1998, 11, 5),  avatar_url="https://avatar.com/charlie.png"),
        Profiles(user=users[3], bio="RPG addict",                    country="Germany",     birthdate=date(1997, 4, 28),  avatar_url="https://avatar.com/diana.png"),
        Profiles(user=users[4], bio="MOBA and shooter player",       country="Netherlands", birthdate=date(2000, 8, 12),  avatar_url="https://avatar.com/evan.png"),
        Profiles(user=users[5], bio="Casual gamer",                  country="Spain",       birthdate=date(1999, 1, 30),  avatar_url="https://avatar.com/fiona.png"),
        Profiles(user=users[6], bio="FPS pro",                       country="Belgium",     birthdate=date(1993, 6, 17),  avatar_url="https://avatar.com/greg.png"),
        Profiles(user=users[7], bio="Open world games fan",          country="Italy",       birthdate=date(1996, 9, 8),   avatar_url="https://avatar.com/helen.png"),
        Profiles(user=users[8], bio="Old school RPG player",         country="Poland",      birthdate=date(1994, 12, 20), avatar_url="https://avatar.com/ivan.png"),
        Profiles(user=users[9], bio="Strategy and simulation fan",   country="France",      birthdate=date(2001, 5, 3),   avatar_url="https://avatar.com/julia.png"),
    ]
    session.add_all(profiles)
    session.flush()

    # 30 purchases — 3 per user
    user_games = [
        # alice — CS2, Witcher3, Skyrim
        UserGames(user=users[0], game=games[0],  purchase_date=date(2023, 10, 1),  hours_played=120),
        UserGames(user=users[0], game=games[4],  purchase_date=date(2022, 5, 15),  hours_played=300),
        UserGames(user=users[0], game=games[17], purchase_date=date(2021, 11, 11), hours_played=200),
        # bob — CS2, AC Valhalla, Fallout4
        UserGames(user=users[1], game=games[0],  purchase_date=date(2023, 10, 5),  hours_played=450),
        UserGames(user=users[1], game=games[8],  purchase_date=date(2021, 1, 3),   hours_played=80),
        UserGames(user=users[1], game=games[18], purchase_date=date(2022, 8, 20),  hours_played=60),
        # charlie — TF2, FIFA23, Mass Effect
        UserGames(user=users[2], game=games[2],  purchase_date=date(2020, 3, 10),  hours_played=500),
        UserGames(user=users[2], game=games[13], purchase_date=date(2023, 9, 30),  hours_played=40),
        UserGames(user=users[2], game=games[14], purchase_date=date(2021, 6, 1),   hours_played=150),
        # diana — Witcher3, Cyberpunk, Doom
        UserGames(user=users[3], game=games[4],  purchase_date=date(2020, 7, 12),  hours_played=400),
        UserGames(user=users[3], game=games[5],  purchase_date=date(2021, 2, 28),  hours_played=90),
        UserGames(user=users[3], game=games[19], purchase_date=date(2022, 4, 5),   hours_played=70),
        # evan — Dota2, R6Siege, Apex
        UserGames(user=users[4], game=games[1],  purchase_date=date(2019, 8, 15),  hours_played=1200),
        UserGames(user=users[4], game=games[10], purchase_date=date(2020, 12, 25), hours_played=300),
        UserGames(user=users[4], game=games[16], purchase_date=date(2022, 3, 8),   hours_played=85),
        # fiona — Portal2, Gwent, Anno1800
        UserGames(user=users[5], game=games[3],  purchase_date=date(2021, 7, 4),   hours_played=25),
        UserGames(user=users[5], game=games[7],  purchase_date=date(2023, 1, 15),  hours_played=60),
        UserGames(user=users[5], game=games[12], purchase_date=date(2022, 6, 20),  hours_played=110),
        # greg — Dota2, FarCry6, Fallout4
        UserGames(user=users[6], game=games[1],  purchase_date=date(2018, 5, 10),  hours_played=800),
        UserGames(user=users[6], game=games[9],  purchase_date=date(2021, 11, 25), hours_played=45),
        UserGames(user=users[6], game=games[18], purchase_date=date(2023, 2, 14),  hours_played=30),
        # helen — Cyberpunk, FIFA23, Sims4
        UserGames(user=users[7], game=games[5],  purchase_date=date(2021, 3, 1),   hours_played=120),
        UserGames(user=users[7], game=games[13], purchase_date=date(2022, 10, 1),  hours_played=55),
        UserGames(user=users[7], game=games[15], purchase_date=date(2023, 4, 10),  hours_played=200),
        # ivan — TF2, Witcher2, R6Siege
        UserGames(user=users[8], game=games[2],  purchase_date=date(2015, 6, 5),   hours_played=600),
        UserGames(user=users[8], game=games[6],  purchase_date=date(2019, 9, 18),  hours_played=180),
        UserGames(user=users[8], game=games[10], purchase_date=date(2021, 4, 30),  hours_played=250),
        # julia — Portal2, ForHonor, Apex
        UserGames(user=users[9], game=games[3],  purchase_date=date(2022, 11, 8),  hours_played=15),
        UserGames(user=users[9], game=games[11], purchase_date=date(2023, 5, 22),  hours_played=90),
        UserGames(user=users[9], game=games[16], purchase_date=date(2022, 12, 25), hours_played=130),
    ]
    session.add_all(user_games)
    session.flush()

    # 15 reviews — only for games the user owns
    reviews = [
        Reviews(user=users[0], game=games[0],  rating=4, comment="Great tactical shooter!"),
        Reviews(user=users[0], game=games[4],  rating=5, comment="Best RPG ever made."),
        Reviews(user=users[1], game=games[0],  rating=3, comment="Good but too competitive."),
        Reviews(user=users[1], game=games[8],  rating=4, comment="Beautiful open world."),
        Reviews(user=users[2], game=games[13], rating=3, comment="Same as last year."),
        Reviews(user=users[2], game=games[14], rating=5, comment="A trilogy worth revisiting."),
        Reviews(user=users[3], game=games[4],  rating=5, comment="Absolutely masterful storytelling."),
        Reviews(user=users[3], game=games[5],  rating=4, comment="Rough launch, great now."),
        Reviews(user=users[4], game=games[1],  rating=4, comment="Steep learning curve, worth it."),
        Reviews(user=users[4], game=games[10], rating=5, comment="Best tactical shooter on the market."),
        Reviews(user=users[5], game=games[3],  rating=5, comment="Brilliant puzzle design."),
        Reviews(user=users[5], game=games[12], rating=4, comment="Relaxing city builder."),
        Reviews(user=users[6], game=games[1],  rating=3, comment="Too complex for newcomers."),
        Reviews(user=users[7], game=games[5],  rating=4, comment="Night City is stunning."),
        Reviews(user=users[8], game=games[6],  rating=4, comment="Great predecessor to Witcher 3."),
    ]
    session.add_all(reviews)
    session.flush()
    return True
