<!--

    Copyright (c) 2023-present Paul Horton. All Rights Reserved.
 
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
 
        http://www.apache.org/licenses/LICENSE-2.0
 
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
 
    SPDX-License-Identifier: Apache-2.0

-->

# osv.dev API Client in Go

[![CI](https://github.com/madpah/osv-dev-api-client/actions/workflows/build.yaml/badge.svg?branch=main)](https://github.com/madpah/osv-dev-api-client/actions/workflows/build.yaml)
[![GitHub license](https://img.shields.io/github/license/madpah/osv-dev-api-client)](https://github.com/madpah/osv-dev-api-client/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/madpah/osv-dev-api-client)](https://github.com/madpah/osv-dev-api-client/issues)
[![GitHub forks](https://img.shields.io/github/forks/madpah/osv-dev-api-client)](https://github.com/madpah/osv-dev-api-client/network)
[![GitHub stars](https://img.shields.io/github/stars/madpah/osv-dev-api-client)](https://github.com/madpah/osv-dev-api-client/stargazers)

----

This repository is use to generate API Clients for `https://osv.dev` in different langauges using their [OpenAPI Specification](https://google.github.io/osv.dev/api/) 
and the OpenAPI Generator.

- [Supported Languages \& Frameworks](#supported-languages--frameworks)
- [Getting the latest OpenAPI Schema](#getting-the-latest-openapi-schema)
- [Generation of API Client](#generation-of-api-client)
- [Releasing](#releasing)
- [Copyright \& License](#copyright--license)

## Supported Languages & Frameworks

| Language / Framework | Since | Public Package Link |
| -------------------- | ---------------------- | ------------------- |
| Go | 2025-01-17 | [![go.dev reference](https://img.shields.io/badge/dynamic/json?color=blue&label=tag&query=name&url=https://api.razonyang.com/v1/github/tag/madpah/osv-dev-api-client-go)](https://pkg.go.dev/github.com/madpah/osv-dev-api-client-go) |

## Getting the latest OpenAPI Schema

Create a Python Virtual Environment with Poetry and then run:

```
poetry install
python update-spec.py
```

This will download the current Swagger 2.0 specification, convert to OpenAPI 3 and put it into the `spec` folder.

## Generation of API Client

```
docker run --rm -v "$(PWD):/local" openapitools/openapi-generator-cli batch --clean /local/go.yaml
```

## Releasing

We use SemVer. Creating a tag, will kick off a release.

## Copyright & License

Copyright (c) 2025 Paul Horton. All Rights Reserved.  

Permission to modify and redistribute is granted under the terms of the Apache 2.0 license.  

See the [LICENSE](./LICENSE) file for the full license.