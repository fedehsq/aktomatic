class SeverityDTO:
    def __init__(self, _name):
        self._name = _name

    @classmethod
    def from_json(cls, json_data):
        return cls(json_data["_name"])
    
    def __repr__(self):
        return f"{self._name}"


class SubCategoryDTO:
    def __init__(
        self,
        issue_description,
        issue_details,
        issue_impact,
        issue_tags,
        test_name,
        references,
        cwe,
        cve,
        name,
        _name,
        content,
        template_source,
        updated_ts,
        super_category,
        inactive,
    ):
        self.issue_description = issue_description
        self.issue_details = issue_details
        self.issue_impact = issue_impact
        self.issue_tags = issue_tags
        self.test_name = test_name
        self.references = references
        self.cwe = cwe
        self.cve = cve
        self.name = name
        self._name = _name
        self.content = content
        self.template_source = template_source
        self.updated_ts = updated_ts
        self.super_category = super_category
        self.inactive = inactive

    @classmethod
    def from_json(cls, json_data):
        return cls(
            json_data["issueDescription"],
            json_data["issueDetails"],
            json_data["issueImpact"],
            json_data["issueTags"],
            json_data["testName"],
            json_data["references"],
            json_data["cwe"],
            json_data["cve"],
            json_data["name"],
            json_data["_name"],
            json_data["content"],
            json_data["templateSource"],
            json_data["updatedTs"],
            SuperCategoryDTO.from_json(json_data["superCategory"]),
            json_data["inactive"],
        )
    
    def __repr__(self):
        return f"{self.name}, {self._name}, {self.test_name}, {self.super_category}, {self.inactive}, {self.issue_description}, {self.issue_details}, {self.issue_impact}, {self.issue_tags}, {self.references}, {self.cwe}, {self.cve}, {self.content}, {self.template_source}, {self.updated_ts}"
    
    def beautify(self):
        return f"{self.name}"


class SuperCategoryDTO:
    def __init__(self, display_name, name, short_name, severity):
        self.display_name = display_name
        self.name = name
        self.short_name = short_name
        self.severity = SeverityDTO.from_json(severity)

    @classmethod
    def from_json(cls, json_data):
        return cls(
            json_data["displayName"],
            json_data["name"],
            json_data["shortName"],
            json_data["severity"],
        )
    
    def __repr__(self):
        return f"{self.display_name}, {self.name}, {self.short_name}, {self.severity}"
    
    def beautify(self):
        return f"{self.display_name}"


class CategoriesDTO:
    def __init__(
        self,
        categories,
        fetch_only_active,
        filter_collections_id,
        filter_severity,
        filter_status,
        filter_sub_category,
        ignore_reason,
        issue_id,
        issue_id_array,
        issues,
        limit,
        sample_data_vs_curl_map,
        similarly_affected_issues,
        skip,
        start_epoch,
        status_to_be_updated,
        sub_categories,
    ):
        self.categories = categories
        self.fetch_only_active = fetch_only_active
        self.filter_collections_id = filter_collections_id
        self.filter_severity = filter_severity
        self.filter_status = filter_status
        self.filter_sub_category = filter_sub_category
        self.ignore_reason = ignore_reason
        self.issue_id = issue_id
        self.issue_id_array = issue_id_array
        self.issues = issues
        self.limit = limit
        self.sample_data_vs_curl_map = sample_data_vs_curl_map
        self.similarly_affected_issues = similarly_affected_issues
        self.skip = skip
        self.start_epoch = start_epoch
        self.status_to_be_updated = status_to_be_updated
        self.sub_categories = sub_categories

    @classmethod
    def from_json(cls, json_data):
        return cls(
            [
                SuperCategoryDTO.from_json(category_data)
                for category_data in json_data["categories"]
            ],
            json_data["fetchOnlyActive"],
            json_data["filterCollectionsId"],
            json_data["filterSeverity"],
            json_data["filterStatus"],
            json_data["filterSubCategory"],
            json_data["ignoreReason"],
            json_data["issueId"],
            json_data["issueIdArray"],
            json_data["issues"],
            json_data["limit"],
            json_data["sampleDataVsCurlMap"],
            json_data["similarlyAffectedIssues"],
            json_data["skip"],
            json_data["startEpoch"],
            json_data["statusToBeUpdated"],
            [
                SubCategoryDTO.from_json(sub_category_data)
                for sub_category_data in json_data["subCategories"]
            ],
        )
    
    def __repr__(self):
        return f"{self.categories}, {self.sub_categories}, {self.filter_status}, {self.filter_severity}, {self.filter_sub_category}, {self.filter_collections_id}, {self.fetch_only_active}, {self.limit}, {self.skip}, {self.start_epoch}, {self.issue_id}, {self.issue_id_array}, {self.issues}, {self.status_to_be_updated}, {self.ignore_reason}, {self.sample_data_vs_curl_map}, {self.similarly_affected_issues}"
    
    def beautify(self):
        return '\n'.join([f"{index + 1}: {category.beautify()}" for index, category in enumerate(self.categories)])
    