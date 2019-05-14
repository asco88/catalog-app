from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


category1 = Category(name="Home Audio")
session.add(category1)
session.commit()

Item2 = Item(title="Home Theater Systems", description="Home Theater Systems", category=category1, creator_email="admin@mail.com")
session.add(Item2)
session.commit()

Item1 = Item(title="Receivers & Amplifiers", description="Receivers & Amplifiers", category=category1, creator_email="admin@mail.com")
session.add(Item1)
session.commit()

Item2 = Item(title="Speakers", description="Speakers", category=category1, creator_email="admin@mail.com")
session.add(Item2)
session.commit()

Item3 = Item(title="Turntables", description="Turntables", category=category1, creator_email="admin@mail.com")
session.add(Item3)
session.commit()

Item4 = Item(title="CD Players", description="CD Players", category=category1, creator_email="admin@mail.com")
session.add(Item4)
session.commit()

Item5 = Item(title="Stereo Shelf Systems", description="Stereo Shelf Systems", category=category1, creator_email="admin@mail.com")
session.add(Item5)
session.commit()

Item6 = Item(title="Sound Bars", description="Sound Bars", category=category1, creator_email="admin@mail.com")
session.add(Item6)
session.commit()

Item7 = Item(title="Wireless & Multiroom Audio", description="Wireless & Multiroom Audio", category=category1, creator_email="admin@mail.com")
session.add(Item7)
session.commit()

Item8 = Item(title="Magnolia Audio", description="Magnolia Audio", category=category1, creator_email="admin@mail.com")
session.add(Item8)
session.commit()

Item9 = Item(title="Home Audio Accessories", description="Home Audio Accessories", category=category1, creator_email="admin@mail.com")
session.add(Item9)
session.commit()


category2 = Category(name="Headphones")
session.add(category2)
session.commit()

Item1 = Item(title="Over-Ear & On-Ear Headphones", description="Over-Ear & On-Ear Headphones", category=category2, creator_email="admin@mail.com")
session.add(Item1)
session.commit()

Item2 = Item(title="Earbud & In-Ear Headphones", description="Earbud & In-Ear Headphones", category=category2, creator_email="admin@mail.com")
session.add(Item2)
session.commit()

Item3 = Item(title="Wireless Headphones", description="Wireless Headphones", category=category2, creator_email="admin@mail.com")
session.add(Item3)
session.commit()

Item4 = Item(title="Noise-Canceling Headphones", description="Noise-Canceling Headphones", category=category2, creator_email="admin@mail.com")
session.add(Item4)
session.commit()


category1 = Category(name="Bluetooth Speakers")
session.add(category1)
session.commit()

Item1 = Item(title="Portable Speakers", description="Portable Speakers", category=category1, creator_email="admin@mail.com")
session.add(Item1)
session.commit()

Item2 = Item(title="Smart Speakers", description="Smart Speakers", category=category1, creator_email="admin@mail.com")
session.add(Item2)
session.commit()


category1 = Category(name="More Audio")
session.add(category1)
session.commit()

Item1 = Item(title="iPod & MP3 Players", description="iPod & MP3 Players", category=category1, creator_email="admin@mail.com")
session.add(Item1)
session.commit()

Item2 = Item(title="Docks, Radios & Boomboxes", description="Docks, Radios & Boomboxes", category=category1, creator_email="admin@mail.com")
session.add(Item2)
session.commit()

Item3 = Item(title="Car Audio", description="Car Audio", category=category1, creator_email="admin@mail.com")
session.add(Item3)
session.commit()

Item4 = Item(title="Marine Audio", description="Marine Audio", category=category1, creator_email="admin@mail.com")
session.add(Item4)
session.commit()

Item5 = Item(title="Musical Instruments", description="Musical Instruments", category=category1, creator_email="admin@mail.com")
session.add(Item5)
session.commit()


print("added items!")
