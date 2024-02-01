class TestResultSummaryDTO:
    def __init__(
        self,
        count_issues,
        end_timestamp,
        hex_id,
        identifier,
        metadata,
        start_timestamp,
        state,
        test_id_config,
        test_results_count,
        testing_run_hex_id,
        testing_run_id,
        total_apis,
    ):
        self.count_issues = count_issues
        self.end_timestamp = end_timestamp
        self.hex_id = hex_id
        self.identifier = identifier
        self.metadata = metadata
        self.start_timestamp = start_timestamp
        self.state = state
        self.test_id_config = test_id_config
        self.test_results_count = test_results_count
        self.testing_run_hex_id = testing_run_hex_id
        self.testing_run_id = testing_run_id
        self.total_apis = total_apis

    @classmethod
    def from_json(cls, json):
        data = json.get("latestTestingRunResultSummaries")
        for key, summary_data in data.items():
            count_issues = summary_data.get("countIssues", {})
            identifier = summary_data.get("id", {})
            testing_run_id = summary_data.get("testingRunId", {})

            summary = cls(
                count_issues=count_issues,
                end_timestamp=summary_data.get("endTimestamp"),
                hex_id=summary_data.get("hexId"),
                identifier={
                    "date": identifier.get("date"),
                    "timestamp": identifier.get("timestamp"),
                },
                metadata=summary_data.get("metadata"),
                start_timestamp=summary_data.get("startTimestamp"),
                state=summary_data.get("state"),
                test_id_config=summary_data.get("testIdConfig"),
                test_results_count=summary_data.get("testResultsCount"),
                testing_run_hex_id=summary_data.get("testingRunHexId"),
                testing_run_id={
                    "date": testing_run_id.get("date"),
                    "timestamp": testing_run_id.get("timestamp"),
                },
                total_apis=summary_data.get("totalApis"),
            )

            return summary

    def __repr__(self):
        return f"TestResultSummaryDTO({self.identifier}, {self.state}, {self.test_results_count}, {self.count_issues}, {self.total_apis}, {self.start_timestamp}, {self.end_timestamp}, {self.testing_run_id}, {self.testing_run_hex_id}, {self.hex_id}, {self.test_id_config}, {self.metadata})"
