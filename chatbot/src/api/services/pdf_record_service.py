from sqlmodel import Session, select
from models.pdf_record import PDFRecord


def save_pdf_record(
    session: Session,
    filename: str,
    session_id: str,
    description: str | None = None
) -> PDFRecord:
    """
    Salva um registro de upload de PDF no banco de dados
    """
    record = PDFRecord(
        filename,
        session_id,
        description
    )
    session.add(record)
    session.commit()
    session.refresh(record)
    return record


def list_pdf_records(
    session: Session
) -> list[PDFRecord]:
    """
    Lista todos os registros de PDFs armazenados.
    """
    return session.exec(select(PDFRecord)).all()


def delete_pdf_record(
    session: Session,
    pdf_id: int
) -> bool:
    """
    Remove um registro de PDF pelo ID.
    """
    pdf = session.get(PDFRecord, pdf_id)
    if not pdf:
        return False
    session.delete(pdf)
    session.commit()
    return True
