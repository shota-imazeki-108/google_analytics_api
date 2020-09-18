import pandas as pd
from src.body.base import BaseBody

page_size = 100000
sampling_level = 'LARGE'


# Google Analytics
class BodyForGaReports(BaseBody):

    def get_body(self, m_list, d_list):
        self.m_list = m_list
        self.d_list = d_list
        metrics = [{'expression': 'ga:' + m} for m in self.m_list]
        dimensions = [{'name': 'ga:' + d} for d in self.d_list]
        body = {
            'reportRequests': [
                {
                    'viewId': self.view_id,
                    'dateRanges': [{'startDate': self.start_date, 'endDate': self.end_date}],
                    'metrics': metrics,
                    'dimensions': dimensions,
                    'pageSize': page_size,
                    'samplingLevel': sampling_level
                }
            ]
        }
        return body
    
    def report_rows_to_df(self, rows):
        df = pd.io.json.json_normalize(rows)

        for i, d in enumerate(self.d_list):
            df[d] = df['dimensions'].apply(lambda x: x[i])
        for i, m in enumerate(self.m_list):
            df[m] = df['metrics'].apply(lambda x: x[0]['values'][i])
        df.drop(columns=['dimensions', 'metrics'], inplace=True)

        return df