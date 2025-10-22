# errors.py

class DivisionError(Exception):
    """Sıfıra bölünme durumunda fırlatılır."""
    pass

class InvalidOperationError(Exception):
    """Geçersiz işlem seçildiğinde fırlatılır."""
    pass
