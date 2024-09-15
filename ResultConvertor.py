import xml.etree.ElementTree as ET


# Function to convert NUnit XML to a custom XML format
def convert_nunit_to_custom(nunit_xml_path, output_xml_path):
    # Parse the NUnit XML file
    tree = ET.parse(nunit_xml_path)
    root = tree.getroot()

    # Create a new root for the custom XML format
    new_root = ET.Element('CustomTestResults')

    # Traverse through NUnit test cases in the XML and extract relevant data
    for test_case in root.findall('.//test-case'):
        # Create a new element in the custom XML structure for each test case
        custom_test_case = ET.Element('TestCase')

        # Map NUnit XML attributes to new XML structure
        test_name = test_case.get('fullname')
        result = test_case.get('result')
        duration = test_case.get('duration')

        # Add elements or attributes as per the required format
        name_element = ET.SubElement(custom_test_case, 'Name')
        name_element.text = test_name

        result_element = ET.SubElement(custom_test_case, 'Result')
        result_element.text = result

        duration_element = ET.SubElement(custom_test_case, 'Duration')
        duration_element.text = duration

        # Append this custom test case to the new root
        new_root.append(custom_test_case)

    # Create the tree and write it to the output file
    new_tree = ET.ElementTree(new_root)
    new_tree.write(output_xml_path, encoding="utf-8", xml_declaration=True)

    print(f"Converted XML saved to {output_xml_path}")


# Usage
nunit_xml_path = '/Users/apple/Library/CloudStorage/OneDrive-Personal/Development/Python-Learning/TestResultConversion/NunitTestResult.xml'  # Input NUnit XML file path
output_xml_path = '/Users/apple/Library/CloudStorage/OneDrive-Personal/Development/Python-Learning/TestResultConversion/NewTestResult.xml' # Output XML file path

convert_nunit_to_custom(nunit_xml_path, output_xml_path)
