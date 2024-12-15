from Translator import Translator

def test_parse(creation_text):
    translator = Translator()
    format = {
    "objects": [
        {
            "type": "extract",
            "name": "<unique_name>",
            "source": "<data_source>",
            "data": "<data_entity>"
        },
        {
            "type": "transform",
            "name": "<unique_name>",
            "operation": "<operation_description>"
        },
        {
            "type": "load",
            "name": "<unique_name>",
            "destination": "<target_destination>"
        }
    ],
    "relationships": [
        {
            "name": "<current_step_name>",
            "next": "<next_step_name>"
        }
        ]
    }
    translator.add_format(format)
    formatted_text = translator.parse(creation_text)
    expected_formatted_text = {'graph': [{'name': 'extract_sales', 'next': 'transform_sales_by_regions'},
           {'name': 'extract_customer_regions',
            'next': 'transform_sales_by_regions'},
           {'name': 'transform_sales_by_regions',
            'next': 'load_to_azure_warehouse'}],
 'objects': [{'data': 'sales table',
              'name': 'extract_sales',
              'source': 'mysql server',
              'type': 'extract'},
             {'data': 'customers regions',
              'name': 'extract_customer_regions',
              'source': 'SAP tables',
              'type': 'extract'},
             {'name': 'transform_sales_by_regions',
              'operation': 'show sales by customers regions',
              'type': 'transform'},
             {'destination': 'Azure warehouse',
              'name': 'load_to_azure_warehouse',
              'type': 'load'}]}
    print(formatted_text)
    assert formatted_text == expected_formatted_text
