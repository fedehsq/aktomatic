from colorama import Fore, Style


class ApiInfoKeyDTO:
    def __init__(self, api_collection_id, method, url):
        self.api_collection_id = api_collection_id
        self.method = method
        self.url = url

    @classmethod
    def from_json(cls, json_data):
        api_collection_id = json_data.get("apiCollectionId", 0)
        method = json_data.get("method", "")
        url = json_data.get("url", "")

        return cls(api_collection_id, method, url)
    
    def __repr__(self):
        return f"{self.url}, {self.method}, {self.api_collection_id}"
    
    def beautify(self):
        return f" {self.method}: {self.url}"


class TestResultDTO:
    def __init__(self, api_info_key, test_sub_type, test_super_type):
        self.api_info_key = api_info_key
        self.test_sub_type = test_sub_type
        self.test_super_type = test_super_type

    @classmethod
    def from_json(cls, json_data):
        api_info_key_data = json_data.get("apiInfoKey", {})
        api_info_key = ApiInfoKeyDTO.from_json(api_info_key_data)
        test_sub_type = json_data.get("testSubType", "")
        test_super_type = json_data.get("testSuperType", "")

        return cls(api_info_key, test_sub_type, test_super_type)
    
    def __repr__(self):
        return f"{self.api_info_key}, {self.test_sub_type}, {self.test_super_type}"
    
    def beautify(self):
        return f"{self.api_info_key.beautify()}, {Fore.RED}{self.test_sub_type}{Style.RESET_ALL}, {self.test_super_type}"


class TestsResultsDTO:
    def __init__(self, test_results):
        self.test_results = test_results

    @classmethod
    def from_json(cls, json_data):
        test_results_data = json_data.get("testingRunResults", [])
        test_results = [
            TestResultDTO.from_json(test_result_data)
            for test_result_data in test_results_data
        ]

        return cls(test_results)

    def __repr__(self):
        return f"{self.test_results}"

    def beautify(self):
        return "\n".join(
            [
                f"{index + 1}: {test_result.beautify()}"
                for index, test_result in enumerate(self.test_results)
            ]
        )
