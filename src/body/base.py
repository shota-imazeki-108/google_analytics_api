from src.config import view_id

class BaseBody:
    def __init__(self, start_date, end_date):
        """
        parameters
        --------------
        start_date: YYYY-MM-DD
        end_date: YYYY-MM-DD
        """
        self.start_date = start_date
        self.end_date = end_date
        self.view_id = view_id