import sqlite3
from discord.ext import commands

class Database_Commands(commands.Cog):
    """
    Commands related to database stuff
    """
    def __init__(self, client):
        self.client = client
        self.connection = None
        self.cursor = None

        self.schema = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            discord_id TEXT NOT NULL UNIQUE
        );

        CREATE TABLE IF NOT EXISTS characters (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );

        CREATE TABLE IF NOT EXISTS places (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT
        );

        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT
        );
        """

        # self.initialize()

    def initialize(self, db_name="dnd_stuff.db"):
        try:
            self.connection = sqlite3.connect(db_name)
            self.cursor = self.connection.cursor()
            self.cursor.executescript(self.schema)
        except Exception as e:
            print(f"[ERROR] {e}")

    


async def setup(client):
    await client.add_cog(Database_Commands(client))