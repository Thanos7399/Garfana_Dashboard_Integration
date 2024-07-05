import mysql.connector
import xml.etree.ElementTree as ET

# Function to parse XML and extract data
def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    pass_cases = []
    fail_cases = []
    skip_cases = []

    # Iterate through each <test> element
    for test in root.findall('.//test'):
        test_name = test.get('name')
        test_result = test.find('.//status').get('status')

        if test_result == 'PASS':
            pass_cases.append(test_name)
        elif test_result == 'FAIL':
            fail_cases.append(test_name)
        elif test_result == 'SKIP':
            skip_cases.append(test_name)

    return pass_cases, fail_cases, skip_cases

# Function to insert data into MySQL database
def insert_into_mysql(pass_cases, fail_cases, skip_cases):
    # Connect to MySQL (replace with your connection details)
    conn = mysql.connector.connect(
        host='localhost',
        user='einfochips',
        password='Einfochips@123',
        database='Demo'
    )
    cursor = conn.cursor()

    # Insert pass cases
    for test_name in pass_cases:
        insert_query = "INSERT INTO test_results (test_name, result) VALUES (%s, %s)"
        cursor.execute(insert_query, (test_name, 'PASS'))

    # Insert fail cases
    for test_name in fail_cases:
        insert_query = "INSERT INTO test_results (test_name, result) VALUES (%s, %s)"
        cursor.execute(insert_query, (test_name, 'FAIL'))

    # Insert skip cases
    for test_name in skip_cases:
        insert_query = "INSERT INTO test_results (test_name, result) VALUES (%s, %s)"
        cursor.execute(insert_query, (test_name, 'SKIP'))

    # Commit changes and close connection
    conn.commit()
    cursor.close()
    conn.close()

# Main function to execute parsing and insertion
def main():
    xml_file = '/home/einfochips/Desktop/Project/Robot_Frame_Work/Data_Parsing/output.xml'
    pass_cases, fail_cases, skip_cases = parse_xml(xml_file)
    insert_into_mysql(pass_cases, fail_cases, skip_cases)
    print("Data inserted into MySQL database successfully!")

if __name__ == "__main__":
    main()
