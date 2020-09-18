# 一部処理は下記を参考にしています。
# - クイックスタートガイド: https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py

import pandas as pd
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


def initialize_service_object(service_name, version, key_file_location, scopes):
    """Initializes an service object.

    Returns:
    An authorized service object.
    """
    credentials = ServiceAccountCredentials.from_json_keyfile_name(key_file_location, scopes)

    # Build the service object.
    service = build(serviceName=service_name, version=version, credentials=credentials)
    return service
