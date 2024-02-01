class TestRequestDTO:
    def __init__(
        self,
        api_collection_id,
        selected_tests,
        test_name,
    ):
        self.api_collection_id = api_collection_id
        self.type = "COLLECTION_WISE"
        # self.start_timestamp = int((datetime.now() + timedelta(seconds=10)).timestamp() * 1000)
        self.recurring_daily = False
        self.selected_tests = selected_tests
        self.test_name = test_name
        self.test_run_time = -1
        self.max_concurrent_requests = -1
        self.overridden_test_app_url = ""

    def to_json(self):
        return {
            "apiCollectionId": self.api_collection_id,
            "type": self.type,
            # "startTimestamp": self.start_timestamp,
            "recurringDaily": self.recurring_daily,
            "selectedTests": self.selected_tests,
            "testName": self.test_name,
            "testRunTime": self.test_run_time,
            "maxConcurrentRequests": self.max_concurrent_requests,
            "overriddenTestAppUrl": self.overridden_test_app_url,
        }
