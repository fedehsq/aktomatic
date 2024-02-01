class IdDataDTO:
    def __init__(self, api_collection_id, url, method, tags):
        self.api_collection_id = api_collection_id
        self.url = url
        self.method = method
        self.tags = tags

    @classmethod
    def from_dict(cls, id_dict):
        return cls(
            id_dict.get("apiCollectionId", None),
            id_dict.get("url", None),
            id_dict.get("method", None),
            id_dict.get("tags", []),
        )

    def __repr__(self):
        return f"{self.api_collection_id}, {self.url}, {self.method}, {self.tags}"

    def beautify(self):
        return f"{self.url}"


class EndpointDataDTO:
    def __init__(self, _id, start_ts, changes_count):
        self._id = _id
        self.start_ts = start_ts
        self.changes_count = changes_count

    @classmethod
    def from_dict(cls, endpoint_dict):
        _id = IdDataDTO.from_dict(endpoint_dict["_id"])
        start_ts = endpoint_dict["startTs"]
        changes_count = endpoint_dict["changesCount"]
        return cls(_id, start_ts, changes_count)

    def __repr__(self):
        return f"{self._id}, {self.start_ts}, {self.changes_count}"

    def beautify(self):
        return self._id.beautify()


class EndpointsDTO:
    def __init__(self, endpoints, unused_endpoints):
        self.endpoints = endpoints
        self.unused_endpoints = unused_endpoints

    @classmethod
    def from_json(cls, json_data):
        data = json_data.get("data", {})
        endpoints_data = data.get("endpoints", [])
        unused_endpoints_data = json_data.get("unusedEndpoints", [])

        endpoints = [
            EndpointDataDTO.from_dict(endpoint_data) for endpoint_data in endpoints_data
        ]

        return cls(endpoints, unused_endpoints_data)

    def __repr__(self):
        return f"{self.endpoints, self.unused_endpoints}"

    def beautify(self):
        return "\n".join(
            [
                f"{index + 1}: {endpoint.beautify()}"
                for index, endpoint in enumerate(self.endpoints)
            ]
        )
