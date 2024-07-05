import xml.etree.ElementTree as ET

output_xml_path =  "/home/einfochips/Desktop/Project/Robot_Frame_Work/Data_Parsing/output.xml"
def get_test_case_counts(output_xml_path):
    tree = ET.parse(output_xml_path)
    root = tree.getroot()

    pass_count = 0
    fail_count = 0
    skip_count = 0

    for test in root.findall('.//test'):
        status = test.find('status').attrib['status']
        if status == 'PASS':
            pass_count += 1
        elif status == 'FAIL':
            fail_count += 1
        elif status == 'SKIP':
            skip_count += 1
    print(f"Pass count: {pass_count}, Fail count: {fail_count}, Skip count: {skip_count}")
    return pass_count, fail_count, skip_count

get_test_case_counts(output_xml_path)