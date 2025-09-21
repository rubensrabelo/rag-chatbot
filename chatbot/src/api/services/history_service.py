from sqlmodel import Session, select

from models.history import History


def save_history(
        session: Session,
        session_id: str,
        question: str,
        answer: str
) -> History:
    entry = History(session_id=session_id, question=question, answer=answer)
    session.add(entry)
    session.commit()


def get_history_context(session: Session, session_id: str) -> str:
    statement = (
        select(History)
        .where(History.session_id == session_id)
        .order_by(History.timestamp)
    )

    history = session.exec(statement).all()
    context = "\n".join(
        f"User: {h.question}\nBot: {h.answer}"
        for h in history
    )
    return context
