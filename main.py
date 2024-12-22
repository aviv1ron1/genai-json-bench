import json
import os
from json import JSONDecodeError

from dotenv import load_dotenv
from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate

from config import STORY_STRUCTURE_PATH, THEME_PATH, ERRORS_PATH
from generators import error_generator, json_schema_generator, json_generator, input_generator, \
    description_output_generator
from prompts import JSON_SCHEMA_EXAMPLE, SIMPLE_JSON_SCHEMA
from utils import insert_schemas_to_arr, SCHEMAS_ARRAY, JSON_ARR_OF_ARR, insert_all_to_dict, \
    insert_json_arr_to_arr, ARRAY_OF_DICTS, INPUT_OUTPUT_DICT
from validation import json_validator
import inflect

if __name__ == "__main__":

    # creating JSON schema from story structure and theme, and insert to a array
    with open(STORY_STRUCTURE_PATH, 'r') as structure_file:
        for structure in structure_file:
            with open(THEME_PATH, 'r') as theme_file:
                for theme in theme_file:
                    schema = json_schema_generator(structure, theme.replace("\n", ""))
                    #print(f"schema: {schema}")
                    insert_schemas_to_arr(schema)
    # iterate on the schmas array and create multiple jsons, and insert to an array of array of ksons
    seed_arr = 40
    num_of_jsons = 2
    # Create an inflect engine instance
    p = inflect.engine()

    for schema in SCHEMAS_ARRAY:
        json_arr = []
        for i in range(num_of_jsons):
            json_file = json_generator(schema, p.ordinal(i+1))
            # print(f"json_before {i}:")

            json_arr.append(json_file)
        insert_json_arr_to_arr(json_arr)
    m = 0
    # # iterate on the schemas array and the json array and create for each json an error
    for i in range(len(SCHEMAS_ARRAY)):
        for json_file in JSON_ARR_OF_ARR[i]:
            with open(ERRORS_PATH, 'r') as error_file:
                if json_file is not None:
                    # print(f"json after {i}")
                    print(f"{i+1} is valid")
                    for error in error_file:
                        desc, json_with_error = error_generator(json_file, error)
                        schema = SCHEMAS_ARRAY[i]

                    # checks if the description and the json with error is not None and insert to a dictionary

                        if desc is not None:
                            try:
                                json_instance_error = json.loads(json_with_error)
                                validate(json_with_error, schema)
                            except (JSONDecodeError, ValidationError, TypeError) as e:
                                insert_all_to_dict(schema, json_file, json_with_error, desc)
                else:
                    print(f"{i+1} not valid")
    # # creating input for the user ond output of the model and insert it to a dictionary
    k = 0
    for arr_dict in ARRAY_OF_DICTS:

        user_input = input_generator(arr_dict['json with error'])
        model_output = description_output_generator(arr_dict['error description'], arr_dict["json instance"])
        INPUT_OUTPUT_DICT.append(
            {"user input": f"{user_input} {arr_dict['json with error']}", "model output": f'{model_output} {arr_dict["json instance"]}'})
        # print("JSON SCHEMA:" + dict['schema'])
        # print(f"JSON: {dict['json instance']}")
        print(f"{k})USER INPUT: {INPUT_OUTPUT_DICT[k]['user input']}")
        print(f"MODEL OUTPUT: {INPUT_OUTPUT_DICT[k]['model output']}")
        k += 1