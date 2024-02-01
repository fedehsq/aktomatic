from colorama import Fore, Style


class SubType:
    def __init__(
        self,
        name,
        sensitive_always,
        sensitive_position,
        super_type,
        swagger_schema_class,
    ):
        self.name = name
        self.sensitive_always = sensitive_always
        self.sensitive_position = sensitive_position
        self.super_type = super_type
        self.swagger_schema_class = swagger_schema_class

    @classmethod
    def from_json(cls, sub_type_data):
        return cls(
            name=sub_type_data.get("name"),
            sensitive_always=sub_type_data.get("sensitiveAlways"),
            sensitive_position=sub_type_data.get("sensitivePosition"),
            super_type=sub_type_data.get("superType"),
            swagger_schema_class=sub_type_data.get("swaggerSchemaClass"),
        )

    def __repr__(self):
        return f"{self.name}, {self.sensitive_always}, {self.sensitive_position}, {self.super_type}, {self.swagger_schema_class}"

    def beautify(self):
        return f"{Fore.YELLOW}{self.name}{Style.RESET_ALL}"



class Endpoint:
    def __init__(
        self,
        api_collection_id,
        collection_ids,
        count,
        domain,
        duration,
        examples,
        is_header,
        is_private,
        is_url_param,
        last_seen,
        max_value,
        method,
        min_value,
        param,
        public_count,
        response_code,
        sensitive,
        sub_type,
        sub_type_string,
        timestamp,
        unique_count,
        url,
        user_ids,
        values,
    ):
        self.api_collection_id = api_collection_id
        self.collection_ids = collection_ids
        self.count = count
        self.domain = domain
        self.duration = duration
        self.examples = examples
        self.is_header = is_header
        self.is_private = is_private
        self.is_url_param = is_url_param
        self.last_seen = last_seen
        self.max_value = max_value
        self.method = method
        self.min_value = min_value
        self.param = param
        self.public_count = public_count
        self.response_code = response_code
        self.sensitive = sensitive
        self.sub_type = sub_type
        self.sub_type_string = sub_type_string
        self.timestamp = timestamp
        self.unique_count = unique_count
        self.url = url
        self.user_ids = user_ids
        self.values = values

    @classmethod
    def from_json(cls, endpoint_data):
        return cls(
            api_collection_id=endpoint_data.get("apiCollectionId"),
            collection_ids=endpoint_data.get("collectionIds"),
            count=endpoint_data.get("count"),
            domain=endpoint_data.get("domain"),
            duration=endpoint_data.get("duration"),
            examples=endpoint_data.get("examples"),
            is_header=endpoint_data.get("isHeader"),
            is_private=endpoint_data.get("isPrivate"),
            is_url_param=endpoint_data.get("isUrlParam"),
            last_seen=endpoint_data.get("lastSeen"),
            max_value=endpoint_data.get("maxValue"),
            method=endpoint_data.get("method"),
            min_value=endpoint_data.get("minValue"),
            param=endpoint_data.get("param"),
            public_count=endpoint_data.get("publicCount"),
            response_code=endpoint_data.get("responseCode"),
            sensitive=endpoint_data.get("sensitive"),
            sub_type=SubType.from_json(endpoint_data.get("subType")),
            sub_type_string=endpoint_data.get("subTypeString"),
            timestamp=endpoint_data.get("timestamp"),
            unique_count=endpoint_data.get("uniqueCount"),
            url=endpoint_data.get("url"),
            user_ids=endpoint_data.get("userIds"),
            values=endpoint_data.get("values"),
        )

    def __repr__(self):
        return f"{self.url}, {self.method}, {self.api_collection_id}, {self.count}, {self.duration}, {self.is_private}, {self.is_url_param}, {self.last_seen}, {self.max_value}, {self.min_value}, {self.param}, {self.response_code}, {self.sensitive}, {self.sub_type}, {self.sub_type_string}, {self.timestamp}, {self.unique_count}, {self.user_ids}, {self.values}"

    def beautify(self):
        return f"{self.url} exposes {self.sub_type.beautify()} with '{self.param.split('#')[-1]}'"


class Endpoints:
    @classmethod
    def from_json(cls, endpoints_data):
        return [Endpoint.from_json(endpoint_data) for endpoint_data in endpoints_data]

    def __repr__(self):
        return f"{self.endpoints}"

    def beautify(self):
        return "\n".join(
            [
                f"{i+1}. {endpoint.beautify()}"
                for i, endpoint in enumerate(self.endpoints)
            ]
        )


class SensitiveParams:
    def __init__(self, endpoints):
        self.endpoints = endpoints

    @classmethod
    def from_json(cls, json_data):
        endpoints_data = json_data.get("data", {}).get("endpoints", [])
        endpoints = Endpoints.from_json(endpoints_data)
        return cls(endpoints)

    def __repr__(self):
        return f"{self.endpoints}"

    def beautify(self):
        return "\n".join(
            [
                f"{i+1}. {endpoint.beautify()}"
                for i, endpoint in enumerate(self.endpoints)
            ]
        )
