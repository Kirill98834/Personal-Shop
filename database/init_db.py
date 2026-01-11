import os
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from database.base import Base
from database.models import Users, Carts, FinallyCarts, Categories, Products, Orders
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

DB_USER=os.getenv("DB_USER")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_NAME=os.getenv("DB_NAME")
DB_HOST=os.getenv("DB_HOST")
DB_PORT=os.getenv("DB_PORT")

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal=sessionmaker(bind=engine, autoflush=False, autocommit=False)

def init_db():
    print("База данных создаётся")
    Base.metadata.create_all(engine)
    with SessionLocal() as session:

        categories = ["Торты", "Печенье", "Пирожные"]
        category_map = {}

        for name in categories:
            category = session.scalar(select(Categories).filter_by(category_name=name))
            if not category:
                category = Categories(category_name=name)
                session.add(category)
                session.flush()
            category_map[name] = category.id

        products = [
            ("Торты", "Медовик", 45, "мёд, мука, сахар, яйца, масло", "media/honey_cake.jpg"),
            ("Торты", "Наполеон", 55, "молоко, мука, сахар, яйца, масло", "media/cake_napoleon.jpg"),
            (
            "Печенье", "Шоколадное печенье", 20, "шоколад, мука, сахар, яйца, масло", "media/choco_cookie.jpg"),
            ("Печенье", "Кокосовое печенье", 25, "кокос, мука, сахар, яйца, масло", "media/kokos_cookie.jpg"),
            ("Пирожные", "Эклер", 30, "мука, яйца, масло, шоколад", "media/eclair.jpg"),
            ("Пирожные", "Картошка", 35, "печенье, сгущёнка, какао, масло", "media/kar-toshka.jpg"),
        ]
        for category_name, name, price, desc, image in products:
            product_exists = session.scalar(select(Products).filter_by(product_name=name))
            if not product_exists:
                product = Products(
                    category_id=category_map[category_name],
                    product_name=name,
                    price=price,
                    description=desc,
                    image=image
                )
                session.add(product)

        session.commit()

if __name__ == "__main__":
    init_db()

