# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['benchling_api_client',
 'benchling_api_client.api',
 'benchling_api_client.api.aa_sequences',
 'benchling_api_client.api.apps',
 'benchling_api_client.api.assay_results',
 'benchling_api_client.api.assay_runs',
 'benchling_api_client.api.authentication',
 'benchling_api_client.api.batches',
 'benchling_api_client.api.blobs',
 'benchling_api_client.api.boxes',
 'benchling_api_client.api.containers',
 'benchling_api_client.api.custom_entities',
 'benchling_api_client.api.dna_alignments',
 'benchling_api_client.api.dna_oligos',
 'benchling_api_client.api.dna_sequences',
 'benchling_api_client.api.dropdowns',
 'benchling_api_client.api.entries',
 'benchling_api_client.api.events',
 'benchling_api_client.api.exports',
 'benchling_api_client.api.feature_libraries',
 'benchling_api_client.api.folders',
 'benchling_api_client.api.inventory',
 'benchling_api_client.api.lab_automation',
 'benchling_api_client.api.label_templates',
 'benchling_api_client.api.legacy_workflows',
 'benchling_api_client.api.legacy_workflows_deprecated',
 'benchling_api_client.api.locations',
 'benchling_api_client.api.mixtures',
 'benchling_api_client.api.oligos',
 'benchling_api_client.api.organizations',
 'benchling_api_client.api.plates',
 'benchling_api_client.api.printers',
 'benchling_api_client.api.projects',
 'benchling_api_client.api.registry',
 'benchling_api_client.api.requests',
 'benchling_api_client.api.rna_oligos',
 'benchling_api_client.api.schemas',
 'benchling_api_client.api.tasks',
 'benchling_api_client.api.teams',
 'benchling_api_client.api.users',
 'benchling_api_client.api.warehouse',
 'benchling_api_client.api.workflow_outputs',
 'benchling_api_client.api.workflow_task_groups',
 'benchling_api_client.api.workflow_tasks',
 'benchling_api_client.api.workflows',
 'benchling_api_client.models',
 'benchling_api_client.v2',
 'benchling_api_client.v2.alpha',
 'benchling_api_client.v2.alpha.api',
 'benchling_api_client.v2.alpha.api.aa_sequences',
 'benchling_api_client.v2.alpha.api.access_policies',
 'benchling_api_client.v2.alpha.api.apps',
 'benchling_api_client.v2.alpha.api.codon_usage_tables',
 'benchling_api_client.v2.alpha.api.custom_entities',
 'benchling_api_client.v2.alpha.api.dna_oligos',
 'benchling_api_client.v2.alpha.api.dna_sequences',
 'benchling_api_client.v2.alpha.api.entities',
 'benchling_api_client.v2.alpha.api.entries',
 'benchling_api_client.v2.alpha.api.enzymes',
 'benchling_api_client.v2.alpha.api.legacy_workflows',
 'benchling_api_client.v2.alpha.api.molecules',
 'benchling_api_client.v2.alpha.api.projects',
 'benchling_api_client.v2.alpha.api.rna_oligos',
 'benchling_api_client.v2.alpha.api.schemas',
 'benchling_api_client.v2.alpha.api.workflow_flowchart_config_versions',
 'benchling_api_client.v2.alpha.api.workflow_outputs',
 'benchling_api_client.v2.alpha.api.workflow_task_groups',
 'benchling_api_client.v2.alpha.api.workflow_tasks',
 'benchling_api_client.v2.alpha.api.worklists',
 'benchling_api_client.v2.alpha.models',
 'benchling_api_client.v2.auth',
 'benchling_api_client.v2.beta',
 'benchling_api_client.v2.beta.api',
 'benchling_api_client.v2.beta.api.aa_sequences',
 'benchling_api_client.v2.beta.api.access_policies',
 'benchling_api_client.v2.beta.api.dna_sequences',
 'benchling_api_client.v2.beta.api.entries',
 'benchling_api_client.v2.beta.api.organizations',
 'benchling_api_client.v2.beta.api.projects',
 'benchling_api_client.v2.beta.api.teams',
 'benchling_api_client.v2.beta.api.users',
 'benchling_api_client.v2.beta.api.worklists',
 'benchling_api_client.v2.beta.models',
 'benchling_api_client.v2.stable',
 'benchling_api_client.v2.stable.api',
 'benchling_api_client.v2.stable.api.aa_sequences',
 'benchling_api_client.v2.stable.api.apps',
 'benchling_api_client.v2.stable.api.assay_results',
 'benchling_api_client.v2.stable.api.assay_runs',
 'benchling_api_client.v2.stable.api.authentication',
 'benchling_api_client.v2.stable.api.batches',
 'benchling_api_client.v2.stable.api.blobs',
 'benchling_api_client.v2.stable.api.boxes',
 'benchling_api_client.v2.stable.api.containers',
 'benchling_api_client.v2.stable.api.custom_entities',
 'benchling_api_client.v2.stable.api.dna_alignments',
 'benchling_api_client.v2.stable.api.dna_oligos',
 'benchling_api_client.v2.stable.api.dna_sequences',
 'benchling_api_client.v2.stable.api.dropdowns',
 'benchling_api_client.v2.stable.api.entries',
 'benchling_api_client.v2.stable.api.events',
 'benchling_api_client.v2.stable.api.exports',
 'benchling_api_client.v2.stable.api.feature_libraries',
 'benchling_api_client.v2.stable.api.folders',
 'benchling_api_client.v2.stable.api.inventory',
 'benchling_api_client.v2.stable.api.lab_automation',
 'benchling_api_client.v2.stable.api.label_templates',
 'benchling_api_client.v2.stable.api.legacy_workflows',
 'benchling_api_client.v2.stable.api.legacy_workflows_deprecated',
 'benchling_api_client.v2.stable.api.locations',
 'benchling_api_client.v2.stable.api.mixtures',
 'benchling_api_client.v2.stable.api.oligos',
 'benchling_api_client.v2.stable.api.organizations',
 'benchling_api_client.v2.stable.api.plates',
 'benchling_api_client.v2.stable.api.printers',
 'benchling_api_client.v2.stable.api.projects',
 'benchling_api_client.v2.stable.api.registry',
 'benchling_api_client.v2.stable.api.requests',
 'benchling_api_client.v2.stable.api.rna_oligos',
 'benchling_api_client.v2.stable.api.schemas',
 'benchling_api_client.v2.stable.api.tasks',
 'benchling_api_client.v2.stable.api.teams',
 'benchling_api_client.v2.stable.api.users',
 'benchling_api_client.v2.stable.api.warehouse',
 'benchling_api_client.v2.stable.api.workflow_outputs',
 'benchling_api_client.v2.stable.api.workflow_task_groups',
 'benchling_api_client.v2.stable.api.workflow_tasks',
 'benchling_api_client.v2.stable.models']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=20.1.0,<22.0',
 'backoff>=1.10.0,<2.0.0',
 'dataclasses-json>=0.5.2,<0.6.0',
 'httpx>=0.15.0,<0.16.0',
 'python-dateutil>=2.8.0,<3.0.0',
 'typing-extensions>=3.7.4,<4.0.0']

setup_kwargs = {
    'name': 'benchling-api-client',
    'version': '1.1.0a8',
    'description': 'Autogenerated Python client from OpenAPI Python Client generator',
    'long_description': "# benchling-api-client\nA client generated from Benchling's OpenAPI definition files, using openapi-python-client.\n\nRather than using this package directly, we recommend using the\n[Benchling SDK](https://pypi.org/project/benchling-sdk/), which has extra scaffolding to make some endpoints easier to\nuse, and has been released to general availability.",
    'author': 'Benchling Support',
    'author_email': 'support@benchling.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
