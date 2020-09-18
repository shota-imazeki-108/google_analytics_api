import pandas as pd
from src.body.base import BaseBody

# Google Search Console
class BodyForGsc(BaseBody):
    
    def get_body(self, d_list, row_limit=25000):
        self.d_list = d_list # ['query', 'page']
        body = {
            'startDate': self.start_date,
            'endDate': self.end_date,
            'dimensions': d_list,
            'rowLimit': row_limit
        }
        return body
