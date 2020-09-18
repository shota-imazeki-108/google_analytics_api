import pandas as pd
from src.body.base import BaseBody


# Google Analytics
class BodyForGaUserActivity(BaseBody):
    
    def get_body(self, client_id):
        self.client_id = client_id
        body={
            'viewId': self.view_id,
            'user': {'type': "CLIENT_ID",'userId': None},
            'dateRange':{'startDate': self.start_date, 'endDate': self.end_date}
        }
        body['user']['userId'] = client_id
        return body
    
    def sessions_to_df(self, sessions):
        """中身複雑すぎて挫折しましたので、やけくそコーディングです"""
        dfs = []
        for session in sessions:
            df = self._session_to_df(session)
            dfs.append(df)
        concat_df = pd.concat(dfs)
        concat_df['client_id'] = self.client_id
        return df
    
    def _session_to_df(self, session):
        activities_df = self._activites_explosion(session['activities'])
        session_df = pd.DataFrame(session).drop('activities', axis=1)
        return pd.concat([activities_df, session_df], axis=1)
    
    def _activites_explosion(self, activites):
        keys = []
        outs = []
        for activity in activites:
            out = self._dict_explosion(activity)
            outs.append(out)
        return pd.DataFrame(outs)
    
    def _dict_explosion(self, session):
        out = {}
        for k, v in session.items():
            if isinstance(v, dict):
                out.update(self._dict_explosion(v))
            else:
                out[k] = v

        return out
