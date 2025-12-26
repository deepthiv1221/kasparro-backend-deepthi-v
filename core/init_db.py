from core.db import engine, Base
import core.models  # 👈 forces model registration

def init_db():
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully")

if __name__ == "__main__":
    init_db()
