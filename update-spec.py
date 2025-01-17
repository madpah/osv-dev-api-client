#
# Copyright 2019-Present Sonatype Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import requests
from yaml import dump as yaml_dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

OSS_DEV_SPEC_PATH = 'https://osv.dev/docs/osv_service_v1.swagger.json'

json_spec_response_v2 = requests.get(OSS_DEV_SPEC_PATH)
json_spec_v2 = json_spec_response_v2.json()

# We need to convert from Swagger 2.0 to OpenAPI 3
json_spec_response = requests.post('https://converter.swagger.io/api/convert', json=json_spec_v2)
json_spec = json_spec_response.json()

with open('./spec/openapi.yaml', 'w') as output_yaml_specfile:
    output_yaml_specfile.write(yaml_dump(json_spec))
