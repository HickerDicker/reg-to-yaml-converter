import re
import yaml

def parse_reg_file(reg_file_path):
    with open(reg_file_path, 'r') as reg_file:
        reg_content = reg_file.read()
    
    reg_sections = re.split(r'\n(?=\[|\])', reg_content)
    
    reg_data = []
    
    for section in reg_sections:
        key_match = re.search(r'\[(.*?)\]', section)
        if not key_match:
            continue
        key_name = key_match.group(1)
        value_matches = re.findall(r'"{0,1}([^"\r\n]+)"\s*=\s*([^\r\n]+)', section)
        values_data = {}
        for value_match in value_matches:
            value_name = value_match[0]
            value_data = value_match[1]
            if value_data.startswith('"') and value_data.endswith('"'):
                value_data = value_data[1:-1]
            
            if value_data.startswith('dword:'):
                value_data = str(int(value_data.split(':')[1], 16))
            
            values_data[value_name] = value_data
        
        reg_data.append({'path': key_name, 'values': values_data})
    
    return reg_data

def convert_reg_to_yaml(reg_data, yaml_file_path):
    with open(yaml_file_path, 'w') as yaml_file:
        for entry in reg_data:
            key_name = entry['path']
            values_data = entry['values']
            
            for value_name, value_data in values_data.items():
                if value_data.isdigit():
                    value_data = int(value_data)
                    value_type = 'REG_DWORD'
                elif value_data.startswith("hex:"):
                    value_type = 'REG_BINARY'
                    value_data = bytes.fromhex(value_data.split(':')[1])
                else:
                    value_type = 'REG_SZ'
                
                yaml_entry = "- !registryValue: {path: '%s', value: '%s', type: %s, data: '%s'}\n" % (key_name, value_name, value_type, value_data)
                
                yaml_file.write(yaml_entry)
    
    print(f"YAML file '{yaml_file_path}' has been created.")

reg_file_path = r'add reg file here'
yaml_file_path = r'add where you want the yml file to be saved'
reg_data = parse_reg_file(reg_file_path)
convert_reg_to_yaml(reg_data, yaml_file_path)
