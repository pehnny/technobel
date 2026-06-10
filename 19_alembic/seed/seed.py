from sqlalchemy.orm import Session

def init(session: Session) -> bool:
    
    session.commit()
    return True