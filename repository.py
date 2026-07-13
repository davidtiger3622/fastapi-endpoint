from abc import ABC, abstractmethod
from models import Note, NoteCreate


class NoteRepository(ABC):
    @abstractmethod
    def list_notes(self) -> list[Note]:
        ...

    @abstractmethod
    def create_note(self, note: NoteCreate) -> Note:
        ...


class InMemoryNoteRepository(NoteRepository):
    def __init__(self):
        self._notes: dict[int, Note] = {}
        self._next_id = 1

    def list_notes(self) -> list[Note]:
        return list(self._notes.values())

    def create_note(self, note: NoteCreate) -> Note:
        new_note = Note(id=self._next_id, **note.model_dump())
        self._notes[self._next_id] = new_note
        self._next_id += 1
        return new_note
