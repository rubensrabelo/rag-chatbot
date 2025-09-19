from sqlmodel import Session
from models.history import History


def save_history(
        session: Session,
        session_id: str,
        question: str,
        answer: str
):
    entry = History(session_id=session_id, question=question, answer=answer)
    session.add(entry)
    session.commit()


def get_history_context(session: Session, session_id: str):
    # Está errado aqui
    history = (
        session.exec(History)
        .filter(History.session_id == session_id)
        .order_by(History.timestamp).all()
    )
    context = "\n".join(
        f"User: {h.question}\nBot: {h.question}"
        for h in history
    )
    return context
