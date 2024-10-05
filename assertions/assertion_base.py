import json
from jsonschema import validate, ValidationError
from logger_config import setup_logger
import os
logger = setup_logger()


class AssertionBase:

    @staticmethod
    def validate_status_code(response, expected_code):
        logger.info(f"Check the Response Status Code is {response.status_code}")
        assert response.status_code == expected_code, (
            f"Expected status code {expected_code}, but got {response.status_code}. "
            f"Response: {response.text}"
        )

    @staticmethod
    def validate_schema(response, model):
        schema_path = os.path.join(os.path.dirname(__file__), '..', 'models', model)
        with open(schema_path) as schema_file:
            user_schema = json.load(schema_file)
        try:
            validate(instance=response.json(), schema=user_schema)
            logger.info("Response is valid according to the schema.")
        except ValidationError as e:
            logger.error(f"Response validation error: {e.message}")
            assert False, f"Response did not match the expected schema: {e.message}"
