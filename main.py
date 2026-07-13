from fastapi import FastAPI, Depends

from models import Note, NoteCreate
from repository import NoteRepository
from db_repository import PostgresNoteRepository

app = FastAPI()

_repository = PostgresNoteRepository()


def get_repository() -> NoteRepository:
    return _repository


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/greet")
def greet():
    return {"message": "Hello Good start"}


@app.get("/notes")
def list_notes(repo: NoteRepository = Depends(get_repository)) -> list[Note]:
    return repo.list_notes()


@app.post("/notes")
def create_note(note: NoteCreate, repo: NoteRepository = Depends(get_repository)) -> Note:
    return repo.create_note(note)
