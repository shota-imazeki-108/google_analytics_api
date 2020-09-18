# 一部処理は下記を参考にしています。
# - クイックスタートガイド: https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py
from src.config import key_file_location

class ServiceObjectForGa:
    """Service Object For Google Analytics"""
    service_name='analyticsreporting'
    version='v4'
    key_file_location=key_file_location
    scopes=['https://www.googleapis.com/auth/analytics.readonly']
    
    @classmethod
    def get_params(cls):
        return cls.service_name, cls.version, cls.key_file_location, cls.scopes
        
    

class ServiceObjectForGsc:
    """Service Object For Google Search Console"""
    service_name='webmasters'
    version='v3'
    key_file_location='client_secrets.json'
    scopes=['https://www.googleapis.com/auth/webmasters.readonly']
    
    @classmethod
    def get_params(cls):
        return cls.service_name, cls.version, cls.key_file_location, cls.scopes
