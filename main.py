import os
import re

GQL_IMPORT = r'#import \"(.*\.gql|.*\.graphql)\"'
S = 'chema.gql'

# assert os.path.exists(S), f'Bad import path {S}'

with open(S, 'r') as schema:
  schema_string = schema.read()

imports = re.findall(GQL_IMPORT, schema_string)
print(imports)