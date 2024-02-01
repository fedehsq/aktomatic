class CollectionDTO:
    def __init__(
        self,
        display_name,
        host_name,
        collection_id,
        name,
        start_ts,
        urls,
        urls_count,
        vxlan_id,
    ):
        self.display_name = display_name
        self.host_name = host_name
        self.id = collection_id
        self.name = name
        self.start_ts = start_ts
        self.urls = urls
        self.urls_count = urls_count
        self.vxlan_id = vxlan_id

    @classmethod
    def from_json(cls, json_data):
        return cls(
            json_data.get("displayName"),
            json_data.get("hostName"),
            json_data.get("id"),
            json_data.get("name"),
            json_data.get("startTs"),
            json_data.get("urls", []),
            json_data.get("urlsCount", 0),
            json_data.get("vxlanId", 0),
        )

    def __repr__(self):
        return f"{self.display_name}, {self.host_name}, {self.id}, {self.name}, {self.start_ts}, {self.urls}, {self.urls_count}, {self.vxlan_id}"

    def beautify(self):
        return f"{self.display_name}"


class CollectionsDTO:
    def __init__(
        self,
        collection_id,
        api_collections,
        critical_endpoints_count,
        last_traffic_seen_map,
        risk_score_of_collections_map,
        sensitive_subtypes_in_collection,
        sensitive_urls_in_response,
        severity_info,
        tested_endpoints_maps,
        timer_info,
    ):
        self.api_collection_id = collection_id
        self.api_collections = api_collections
        self.critical_endpoints_count = critical_endpoints_count
        self.last_traffic_seen_map = last_traffic_seen_map
        self.risk_score_of_collections_map = risk_score_of_collections_map
        self.sensitive_subtypes_in_collection = sensitive_subtypes_in_collection
        self.sensitive_urls_in_response = sensitive_urls_in_response
        self.severity_info = severity_info
        self.tested_endpoints_maps = tested_endpoints_maps
        self.timer_info = timer_info

    @classmethod
    def from_json(cls, json_data):
        return cls(
            json_data.get("apiCollectionId", 0),
            [
                CollectionDTO.from_json(api_data)
                for api_data in json_data.get("apiCollections", [])
            ],
            json_data.get("criticalEndpointsCount", 0),
            json_data.get("lastTrafficSeenMap", {}),
            json_data.get("riskScoreOfCollectionsMap", {}),
            json_data.get("sensitiveSubtypesInCollection", {}),
            json_data.get("sensitiveUrlsInResponse", 0),
            json_data.get("severityInfo", {}),
            json_data.get("testedEndpointsMaps", {}),
            json_data.get("timerInfo"),
        )

    def get_collection_by_name(self, collection_name):
        return next(
            (
                collection
                for collection in self.api_collections
                if collection.display_name == collection_name
            ),
            None,
        )

    def __repr__(self):
        return f"{self.api_collection_id}, {self.api_collections}, {self.critical_endpoints_count}, {self.last_traffic_seen_map}, {self.risk_score_of_collections_map}, {self.sensitive_subtypes_in_collection}, {self.sensitive_urls_in_response}, {self.severity_info}, {self.tested_endpoints_maps}, {self.timer_info}"

    def beautify(self):
        return "\n".join(
            [
                f"{index + 1}: {collection.beautify()}"
                for index, collection in enumerate(self.api_collections)
            ]
        )
