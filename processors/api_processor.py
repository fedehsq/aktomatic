import os
from dotenv import load_dotenv
import requests

from dto.test_request_dto import TestRequestDTO

load_dotenv()
X_API_KEY = os.environ.get("X_API_KEY")
SERVER_URL = os.environ.get("SERVER_URL")

class ApiProcessor:
    @staticmethod
    def import_collection(collection: str):
        try:
            return requests.post(
                f"{SERVER_URL}/api/importDataFromPostmanFile",
                json={"postmanCollectionFile": collection, "allowReplay": True},
                headers={"x-api-key": X_API_KEY},
            )
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def get_all_collections():
        try:
            return requests.post(
                f"{SERVER_URL}/api/getAllCollections",
                headers={"x-api-key": X_API_KEY},
            )
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def get_collection_endpoints(collection_id: int):
        try:
            return requests.post(
                f"{SERVER_URL}/api/fetchAPICollection",
                headers={"x-api-key": X_API_KEY},
                json={"apiCollectionId": collection_id},
            )
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def get_collection_endpoints_with_senstive_params(collection_id: int):
        try:
            return requests.post(
                f"{SERVER_URL}/api/loadSensitiveParameters",
                headers={"x-api-key": X_API_KEY},
                json={"apiCollectionId": collection_id},
            )
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def get_all_test_types():
        try:
            return requests.post(
                f"{SERVER_URL}/api/fetchAllSubCategories",
                headers={"x-api-key": X_API_KEY},
            )
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def test_collection(test: TestRequestDTO):
        try:
            return requests.post(
                f"{SERVER_URL}/api/startTest",
                headers={"x-api-key": X_API_KEY},
                json=test.to_json(),
            )
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def test_summary_result():
        try:
            return requests.post(
                f"{SERVER_URL}/api/retrieveAllCollectionTests",
                headers={"x-api-key": X_API_KEY},
            )
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def test_result(test_id: str):
        try:
            return requests.post(
                f"{SERVER_URL}/api/fetchTestingRunResults",
                headers={"x-api-key": X_API_KEY},
                json={
                    "testingRunResultSummaryHexId": test_id,
                    "fetchOnlyVulnerable": True,
                },
            )
        except Exception as e:
            print(e)
            return None
