import os
import psycopg
from dotenv import load_dotenv

from models import Note, NoteCreate
from repository import NoteRepository

load_dotenv()


class PostgresNoteRepository(NoteRepository):
    def __init__(self):
        self._dsn = os.environ["DATABASE_URL"]

    def list_notes(self) -> list[Note]:
        with psycopg.connect(self._dsn) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, title, content FROM notes ORDER BY id")
                rows = cur.fetchall()
        return [Note(id=row[0], title=row[1], content=row[2]) for row in rows]

    def create_note(self, note: NoteCreate) -> Note:
        with psycopg.connect(self._dsn) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO notes (title, content) VALUES (%s, %s) RETURNING id",
                    (note.title, note.content),
                )
                new_id = cur.fetchone()[0]
            conn.commit()
        return Note(id=new_id, title=note.title, content=note.content)
