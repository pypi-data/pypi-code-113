# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['graphene_django_filter']

package_data = \
{'': ['*']}

install_requires = \
['Django>=3,<4',
 'anytree>=2.8.0,<3.0.0',
 'django-filter>=21.1,<22.0',
 'django-seed>=0.3.1,<0.4.0',
 'graphene-django>=2.15.0,<3.0.0',
 'graphene==2.1.9',
 'psycopg2-binary>=2.9.3,<3.0.0',
 'stringcase>=1.2.0,<2.0.0',
 'wrapt>=1.13.3,<2.0.0']

setup_kwargs = {
    'name': 'graphene-django-filter',
    'version': '0.6.2',
    'description': 'Advanced filters for Graphene',
    'long_description': '# Graphene-Django-Filter\n[![CI](https://github.com/devind-team/graphene-django-filter/workflows/CI/badge.svg)](https://github.com/devind-team/graphene-django-filter/actions)\n[![Coverage Status](https://coveralls.io/repos/github/devind-team/graphene-django-filter/badge.svg?branch=main)](https://coveralls.io/github/devind-team/graphene-django-filter?branch=main)\n[![PyPI version](https://badge.fury.io/py/graphene-django-filter.svg)](https://badge.fury.io/py/graphene-django-filter)\n[![License: MIT](https://img.shields.io/badge/License-MIT-success.svg)](https://opensource.org/licenses/MIT)\n\nThis package contains advanced filters for [graphene-django](https://github.com/graphql-python/graphene-django).\nThe standard filtering feature in graphene-django relies on the [django-filter](https://github.com/carltongibson/django-filter)\nlibrary and therefore provides the flat API without the ability to use logical operators such as\n`and`, `or` and `not`. This library makes the API nested and adds logical expressions by extension\nof the `DjangoFilterConnectionField` field and the `FilterSet` class.\nAlso, the library provides some other convenient filtering features.\n\n# Installation\n```shell\n# pip\npip install graphene-django-filter\n# poetry\npoetry add graphene-django-filter\n```\n\n# Requirements\n* Python (3.7, 3.8, 3.9, 3.10)\n* Graphene-Django (2.15)\n\n# Features\n\n## Nested API with the ability to use logical operators\nTo use, simply replace all `DjangoFilterConnectionField` fields with\n`AdvancedDjangoFilterConnectionField` fields in your queries.\nAlso,if you create custom FilterSets, replace the inheritance from the `FilterSet` class\nwith the inheritance from the `AdvancedFilterSet` class.\nFor example, the following task query exposes the old flat API.\n```python\nimport graphene\nfrom django_filters import FilterSet\nfrom graphene_django import DjangoObjectType\nfrom graphene_django.filter import DjangoFilterConnectionField\n\nclass TaskFilter(FilterSet):\n    class Meta:\n        model = Task\n        fields = {\n            \'name\': (\'exact\', \'contains\'),\n            \'user__email\': (\'exact\', \'contains\'),\n            \'user__first_name\': (\'exact\', \'contains\'),\n            \'user__last_name\': (\'exact\', \'contains\'),\n        }\n\nclass UserType(DjangoObjectType):\n    class Meta:\n        model = User\n        interfaces = (graphene.relay.Node,)\n        fields = \'__all__\'\n\nclass TaskType(DjangoObjectType):\n    user = graphene.Field(UserType)\n\n    class Meta:\n        model = Task\n        interfaces = (graphene.relay.Node,)\n        fields = \'__all__\'\n        filterset_class = TaskFilter\n\nclass Query(graphene.ObjectType):\n    tasks = DjangoFilterConnectionField(TaskType)\n```\nThe flat API in which all filters are applied using the `and` operator looks like this.\n```graphql\n{\n  tasks(\n    name_Contains: "important"\n    user_Email_Contains: "john"\n    user_FirstName: "John"\n    user_LastName: "Dou"\n  ){\n    edges {\n      node {\n        id\n        name\n      }\n    }\n  }\n}\n```\nAfter replacing the field class with the `AdvancedDjangoFilterConnectionField`\nand the `FilterSet` class with the `AdvancedFilterSet`\nthe API becomes nested with support for logical expressions.\n```python\nimport graphene\nfrom graphene_django_filter import AdvancedDjangoFilterConnectionField, AdvancedFilterSet\n\nclass TaskFilter(AdvancedFilterSet):\n    class Meta:\n        model = Task\n        fields = {\n            \'name\': (\'exact\', \'contains\'),\n            \'user__email\': (\'exact\', \'contains\'),\n            \'user__first_name\': (\'exact\', \'contains\'),\n            \'user__last_name\': (\'exact\', \'contains\'),\n        }\n\nclass Query(graphene.ObjectType):\n    tasks = AdvancedDjangoFilterConnectionField(TaskType)\n```\nFor example, the following query returns tasks which names contain the word "important"\nor the user\'s email address contains the word "john" and the user\'s last name is "Dou"\nand the first name is not "John".\nNote that the operators are applied to lookups\nsuch as `contains`, `exact`, etc. at the last level of nesting.\n```graphql\n{\n  tasks(\n    filter: {\n      or: [\n        {name: {contains: "important"}}\n        {\n            and: [\n              {user: {email: {contains: "john"}}}\n              {user: {lastName: {exact: "Dou"}}}\n            ]\n        }\n      ]\n      not: {\n        user: {firstName: {exact: "John"}}\n      }\n    }\n  ) {\n    edges {\n      node {\n        id\n        name\n      }\n    }\n  }\n}\n```\nThe same result can be achieved with an alternative query structure\nbecause within the same object the `and` operator is always used.\n```graphql\n{\n  tasks(\n    filter: {\n      or: [\n        {name: {contains: "important"}}\n        {\n          user: {\n            email: {contains: "john"}\n            lastName: {exact: "Dou"}\n          }\n        }\n      ]\n      not: {\n        user: {firstName: {exact: "John"}}\n      }\n    }\n  ){\n    edges {\n      node {\n        id\n        name\n      }\n    }\n  }\n}\n```\nThe filter input type has the following structure.\n```graphql\ninput FilterInputType {\n  and: [FilterInputType]\n  or: [FilterInputType]\n  not: FilterInputType\n  ...FieldLookups\n}\n```\nFor more examples, see [tests](https://github.com/devind-team/graphene-django-filter/blob/06ed0af8def8a4378b4c65a5d137ef17b6176cab/tests/test_queries_execution.py#L23).\n\n## Full text search\nDjango provides the [API](https://docs.djangoproject.com/en/3.2/ref/contrib/postgres/search/)\nfor PostgreSQL full text search. Graphene-Django-Filter inject this API into the GraphQL filter API.\nTo use, add `full_text_search` lookup to fields for which you want to enable full text search.\nFor example, the following type has full text search for\n`first_name` and `last_name` fields.\n```python\nimport graphene\nfrom graphene_django import DjangoObjectType\nfrom graphene_django_filter import AdvancedDjangoFilterConnectionField\n\nclass UserType(DjangoObjectType):\n    class Meta:\n        model = User\n        interfaces = (graphene.relay.Node,)\n        fields = \'__all__\'\n        filter_fields = {\n            \'email\': (\'exact\', \'startswith\', \'contains\'),\n            \'first_name\': (\'exact\', \'contains\', \'full_text_search\'),\n            \'last_name\': (\'exact\', \'contains\', \'full_text_search\'),\n        }\n\nclass Query(graphene.ObjectType):\n    users = AdvancedDjangoFilterConnectionField(UserType)\n```\nSince this feature belongs to the AdvancedFilterSet,\nit can be used in a custom FilterSet.\nThe following example will work exactly like the previous one.\n```python\nimport graphene\nfrom graphene_django import DjangoObjectType\nfrom graphene_django_filter import AdvancedDjangoFilterConnectionField, AdvancedFilterSet\n\nclass UserFilter(AdvancedFilterSet):\n    class Meta:\n        model = User\n        fields = {\n            \'email\': (\'exact\', \'startswith\', \'contains\'),\n            \'first_name\': (\'exact\', \'contains\', \'full_text_search\'),\n            \'last_name\': (\'exact\', \'contains\', \'full_text_search\'),\n        }\n\nclass UserType(DjangoObjectType):\n    class Meta:\n        model = User\n        interfaces = (graphene.relay.Node,)\n        fields = \'__all__\'\n        filterset_class = UserFilter\n\nclass Query(graphene.ObjectType):\n    users = AdvancedDjangoFilterConnectionField(UserType)\n```\nFull text search API includes SearchQuery, SearchRank, and Trigram filters.\nSearchQuery and SearchRank filters are at the top level.\nIf some field has been enabled for full text search then it can be included in the field array.\nThe following queries show an example of using the SearchQuery and SearchRank filters.\n```graphql\n{\n  users(\n    filter: {\n      searchQuery: {\n        vector: {\n          fields: ["first_name"]\n        }\n        query: {\n          or: [\n            {value: "Bob"}\n            {value: "Alice"}\n          ]\n        }\n      }\n    }\n  ){\n    edges {\n      node {\n        id\n        firstName\n        lastName  \n      }\n    }\n  }\n}\n```\n```graphql\n{\n  users(\n    filter: {\n      searchRank: {\n        vector: {fields: ["first_name", "last_name"]}\n        query: {value: "John Dou"}\n        lookups: {gte: 0.5}\n      }\n    }\n  ){\n    edges {\n      node {\n        id\n        firstName\n        lastName  \n      }\n    }\n  }\n}\n```\nTrigram filter belongs to the corresponding field.\nThe following query shows an example of using the Trigram filter.\n```graphql\n{\n  users(\n    filter: {\n      firstName: {\n        trigram: {\n          value: "john"\n          lookups: {gte: 0.85}\n        }\n      }\n    }\n  ){\n    edges {\n      node {\n        id\n        firstName\n        lastName  \n      }\n    }\n  }\n}\n```\nInput types have the following structure.\n```graphql\ninput SearchConfigInputType {\n  value: String!\n  isField: Boolean\n}\nenum SearchVectorWeight {\n  A\n  B\n  C\n  D\n}\ninput SearchVectorInputType {\n  fields: [String!]!\n  config: SearchConfigInputType\n  weight: SearchVectorWeight\n}\nenum SearchQueryType {\n  PLAIN\n  PHRASE\n  RAW\n  WEBSEARCH\n}\ninput SearchQueryInputType {\n  value: String\n  config: SearchConfigInputType\n  and: [SearchQueryInputType]\n  or: [SearchQueryInputType]\n  not: SearchQueryInputType\n}\ninput SearchQueryFilterInputType {\n  vector: SearchVectorInputType!\n  query: SearchQueryInputType!\n}\ninput FloatLookupsInputType {\n  exact: Float\n  gt: Float\n  gte: Float\n  lt: Float\n  lte: Float\n}\ninput SearchRankWeightsInputType {\n  D: Float\n  C: Float\n  B: Float\n  A: Float\n}\ninput SearchRankFilterInputType {\n  vector: SearchVectorInputType!\n  query: SearchQueryInputType!\n  lookups: FloatLookupsInputType!\n  weights: SearchRankWeightsInputType\n  coverDensity: Boolean\n  normalization: Int\n}\nenum TrigramSearchKind {\n  SIMILARITY\n  DISTANCE\n}\ninput TrigramFilterInputType {\n  kind: TrigramSearchKind\n  lookups: FloatLookupsInputType!\n  value: String!\n}\n```\nFor more examples, see [tests](https://github.com/devind-team/graphene-django-filter/blob/06ed0af8def8a4378b4c65a5d137ef17b6176cab/tests/test_queries_execution.py#L134).\n\n## Settings\nThe library can be customised using settings.\nTo add settings, create a dictionary\nwith name `GRAPHENE_DJANGO_FILTER` in the project’s `settings.py`.\nThe default settings are as follows.\n```python\nGRAPHENE_DJANGO_FILTER = {\n    \'FILTER_KEY\': \'filter\',\n    \'AND_KEY\': \'and\',\n    \'OR_KEY\': \'or\',\n    \'NOT_KEY\': \'not\',\n}\n```\nTo read the settings, import them from the `conf` module.\n```python\nfrom graphene_django_filter.conf import settings\n\nprint(settings.FILTER_KEY)\n```\nThe `settings` object also includes fixed settings, which depend on the user\'s environment.\n`IS_POSTGRESQL` determinate that current database is PostgreSQL\nand `HAS_TRIGRAM_EXTENSION` that `pg_trgm` extension is installed.\n',
    'author': 'devind-team',
    'author_email': 'team@devind.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/devind-team/graphene-django-filter',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
