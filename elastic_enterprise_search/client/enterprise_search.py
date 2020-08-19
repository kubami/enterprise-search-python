#  Licensed to Elasticsearch B.V. under one or more contributor
#  license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright
#  ownership. Elasticsearch B.V. licenses this file to you under
#  the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

from .base import BaseClient
from ..utils import (  # noqa: F401
    make_path,
    make_params,
    SKIP_IN_PATH,
)


class EnterpriseSearch(BaseClient):
    def get_health(
        self, params=None, headers=None, http_auth=None,
    ):
        """
        Get information on the health of a deployment and basic statistics around
        resource usage
        :arg params: Additional query params to send with the request
        :arg headers: Additional headers to send with the request
        :arg http_auth: Access token or HTTP basic auth username
            and password to send with the request
        :raises elastic_enterprise_search.Unauthorized:
        """
        return self._perform_request(
            "GET",
            make_path("api", "ent", "v1", "internal", "health"),
            params=params,
            headers=headers,
            http_auth=http_auth,
        )

    def get_read_only(
        self, params=None, headers=None, http_auth=None,
    ):
        """
        Get the read-only flag's state
        :arg params: Additional query params to send with the request
        :arg headers: Additional headers to send with the request
        :arg http_auth: Access token or HTTP basic auth username
            and password to send with the request
        :raises elastic_enterprise_search.Unauthorized:
        """
        return self._perform_request(
            "GET",
            make_path("api", "ent", "v1", "internal", "read_only_mode"),
            params=params,
            headers=headers,
            http_auth=http_auth,
        )

    def put_read_only(
        self, body, params=None, headers=None, http_auth=None,
    ):
        """
        Update the read-only flag's state

        :arg body: HTTP request body
        :arg params: Additional query params to send with the request
        :arg headers: Additional headers to send with the request
        :arg http_auth: Access token or HTTP basic auth username
            and password to send with the request
        :raises elastic_enterprise_search.Unauthorized:
        """
        return self._perform_request(
            "PUT",
            make_path("api", "ent", "v1", "internal", "read_only_mode"),
            body=body,
            params=params,
            headers=headers,
            http_auth=http_auth,
        )

    def get_stats(
        self, include=None, params=None, headers=None, http_auth=None,
    ):
        """
        Get information about the resource usage of the application, the state of
        different internal queues, etc.

        :arg include: Comma-separated list of stats to return
        :arg params: Additional query params to send with the request
        :arg headers: Additional headers to send with the request
        :arg http_auth: Access token or HTTP basic auth username
            and password to send with the request
        :raises elastic_enterprise_search.Unauthorized:
        """
        params = make_params(params, {"include": include})
        return self._perform_request(
            "GET",
            make_path("api", "ent", "v1", "internal", "stats"),
            params=params,
            headers=headers,
            http_auth=http_auth,
        )

    def get_version(
        self, params=None, headers=None, http_auth=None,
    ):
        """
        Get version information for this server
        :arg params: Additional query params to send with the request
        :arg headers: Additional headers to send with the request
        :arg http_auth: Access token or HTTP basic auth username
            and password to send with the request
        :raises elastic_enterprise_search.Unauthorized:
        """
        return self._perform_request(
            "GET",
            make_path("api", "ent", "v1", "internal", "version"),
            params=params,
            headers=headers,
            http_auth=http_auth,
        )