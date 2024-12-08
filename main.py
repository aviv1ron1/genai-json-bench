import json
from json import JSONDecodeError

from huggingface_hub import InferenceClient
from config import STORY_STRUCTURE_PATH, THEME_PATH, ERRORS_PATH
from generators import error_generator, json_schema_generator, json_generator, input_generator, \
    description_output_generator
from utils import insert_schemas_to_arr, SCHEMAS_ARRAY, JSON_ARR_OF_ARR, insert_all_to_dict, \
    insert_json_arr_to_arr, DICT_FOR_INPUT, INPUT_OUTPUT_DICT
from validation import json_validator

if __name__ == "__main__":
    client = InferenceClient()
    # creating JSON schema from story structure and theme, and insert to a array
    with open(STORY_STRUCTURE_PATH, 'r') as structure_file:
        for structure in structure_file:
            with open(THEME_PATH, 'r') as theme_file:
                for theme in theme_file:
                    schema = json_schema_generator(structure, theme)
                    insert_schemas_to_arr(schema)
    # iterate on the schmas array and create multiple jsons, and insert to an array of array of ksons
    seed_arr = 40
    num_of_jsons = 2

    for schema in SCHEMAS_ARRAY:
        json_arr = []
        for i in range(num_of_jsons):
            json_file = json_generator(schema, seed_arr + i)
            json_arr.append(json_file)
        insert_json_arr_to_arr(json_arr)

    # iterate on the schemas array and the json array and create for each json an error
    for i in range(len(SCHEMAS_ARRAY)):
        for json_file in JSON_ARR_OF_ARR[i]:
            with open(ERRORS_PATH, 'r') as error_file:
                for error in error_file:
                    desc, json_with_error = error_generator(json_file, error)
                    schema = SCHEMAS_ARRAY[i]

                    # checks if the description and the json with error is not None and insert to a dictionary

                    if desc is not None:
                        try:
                            json_instance_error = json.loads(json_with_error)
                        except JSONDecodeError as e:
                            insert_all_to_dict(schema, json_file, json_with_error, desc)

    # creating input for the user ond output of the model and insert it to a dictionary

    for key, val in DICT_FOR_INPUT.items():
        user_input = input_generator(key)
        model_output = description_output_generator(val[2], val[1])
        INPUT_OUTPUT_DICT[user_input] = [model_output, val[1]]
