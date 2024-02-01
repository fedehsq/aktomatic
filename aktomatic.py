#!/usr/bin/env python3

from time import sleep
import argparse

from dto.collection_dto import CollectionsDTO
from dto.sensitive_param import SensitiveParams
from dto.test_category_dto import CategoriesDTO
from dto.test_request_dto import TestRequestDTO
from dto.test_result_dto import TestsResultsDTO
from dto.test_result_summary_dto import TestResultSummaryDTO
from processors.api_processor import ApiProcessor



def check_response(response, error_message: str):
    if response is None:
        print(error_message)
        exit(1)
    if response.status_code != 200:
        print(response.text)
        exit(1)


def import_postman_collection(collection_file_path):
    print(f"Importing Postman collection from file: {collection_file_path}")
    collection = open(collection_file_path, "r").read()
    response = ApiProcessor.import_collection(collection)
    check_response(response, "importing Postman collection")
    print("Postman collection imported successfully")


def list_all_collections():
    print("Listing all collections")
    response = ApiProcessor.get_all_collections()
    check_response(response, "Error listing collections")
    collections = CollectionsDTO.from_json(response.json())
    print(collections.beautify())


def read_endpoints_from_collection(collection_name):
    print(f"Reading endpoints from collection: {collection_name}")
    response = ApiProcessor.get_all_collections()
    check_response(response, "Error listing collections")
    collections = CollectionsDTO.from_json(response.json())
    collection = collections.get_collection_by_name(collection_name)
    if collection is None:
        print(f"Collection {collection_name} not found")
        return
    # response = ApiProcessor.get_collection_endpoints(collection.id)
    # check_response(response, "Error fetching collection")
    # endpoints = EndpointsDTO.from_json(response.json())
    # print(endpoints.beautify())
    response = ApiProcessor.get_collection_endpoints_with_senstive_params(collection.id)
    check_response(response, "Error fetching collection")
    endpoints = SensitiveParams.from_json(response.json())
    print(endpoints.beautify())


def list_all_tests():
    print("Listing all tests")
    response = ApiProcessor.get_all_test_types()
    check_response(response, "Error listing tests")
    categories = CategoriesDTO.from_json(response.json())
    print(categories.beautify())


def run_test(collection_name):
    print(f"Testing collection: {collection_name}", flush=True, end="")
    response = ApiProcessor.get_all_collections()
    check_response(response, "Error listing collections")
    collections = CollectionsDTO.from_json(response.json())
    collection = collections.get_collection_by_name(collection_name)
    if collection is None:
        print(f"Collection {collection_name} not found")
        return
    response = ApiProcessor.get_all_test_types()
    check_response(response, "Error listing tests")
    categories = CategoriesDTO.from_json(response.json())
    test_request = TestRequestDTO(
        collection.id,
        [test.name for test in categories.sub_categories],
        collection_name,
    )
    response = ApiProcessor.test_collection(test_request)
    check_response(response, "Error running tests")
    response = ApiProcessor.test_summary_result()
    check_response(response, "Error getting test summary result")
    response = TestResultSummaryDTO.from_json(response.json())
    dummy_wait()
    response = ApiProcessor.test_result(response.hex_id)
    check_response(response, "Error getting test result")
    tests = TestsResultsDTO.from_json(response.json())
    print(f"{tests.beautify()}")
    print("Tests run successfully")


def dummy_wait():
    for _ in range(30):
        print(".", end="", flush=True)
        sleep(1)
    print()


def run():
    parser = argparse.ArgumentParser(
        description="Aktomatic is a tool to manage Akto API."
    )

    parser.add_argument(
        "-i",
        "--import",
        dest="import_file",
        metavar="FILE",
        help="Import a collection from Postman. Specify the path of the Postman collection file.",
    )
    parser.add_argument(
        "-l",
        "--list",
        type=str,
        choices=["collections", "tests"],
        metavar="ITEM",
        help="Specify the type of item to list (e.g., collections, tests).",
    )
    parser.add_argument(
        "-r",
        "--read",
        metavar="COLLECTION",
        help="Read endpoints from the collection. Specify collection name.",
    )
    parser.add_argument(
        "-t",
        "--test",
        metavar="COLLECTION",
        help="Test all endpoints in a collection. Specify collection name.",
    )

    args = parser.parse_args()

    if args.import_file:
        import_postman_collection(args.import_file)
    elif args.list:
        if args.list == "collections":
            list_all_collections()
        elif args.list == "tests":
            list_all_tests()
    elif args.test:
        run_test(args.test)
    elif args.read:
        read_endpoints_from_collection(args.read)
    elif args.test:
        list_all_tests(args.test)
    else:
        print("Error: Please provide a valid option. Use --help for usage information.")


if __name__ == "__main__":
    run()
