########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

from .test_base import CliCommandTest
from cloudify_cli.exceptions import CloudifyValidationError


class SecretsTest(CliCommandTest):
    def setUp(self):
        super(SecretsTest, self).setUp()
        self.use_manager()

    def test_get_secrets_missing_key(self):
        outcome = self.invoke(
            'cfy secrets get',
            err_str_segment='2',  # Exit code
            exception=SystemExit
        )
        self.assertIn('Missing argument "key"', outcome.output)

    def test_get_secrets_invalid_key(self):
        self.invoke(
            "cfy secrets get ' ' ",
            err_str_segment='ERROR: The `key` argument contains illegal '
                            'characters',
            exception=CloudifyValidationError
        )

    def test_create_secrets_missing_value(self):
        outcome = self.invoke(
            'cfy secrets create key',
            err_str_segment='2',  # Exit code
            exception=SystemExit
        )
        self.assertIn('Missing option "-s" / "--secret-value"', outcome.output)
