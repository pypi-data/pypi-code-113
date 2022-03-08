from random import randint
from urllib.parse import urlencode
from pydantic.utils import get_model

import pytest
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from starlette.testclient import TestClient

from datetime import datetime
from maggma.api.query_operator.core import QueryOperator

from maggma.api.resource import SubmissionResource, post_resource
from maggma.api.query_operator import PaginationQuery

from maggma.stores import MemoryStore


class Owner(BaseModel):
    name: str = Field(..., title="Owner's name")
    age: int = Field(None, title="Owne'r Age")
    weight: float = Field(None, title="Owner's weight")
    last_updated: datetime = Field(None, title="Last updated date for this record")


owners = (
    [Owner(name=f"Person{i}", age=i + 3, weight=100 + i) for i in list(range(10))]
    + [Owner(name="PersonAge9", age=9, weight=float(randint(155, 195)))]
    + [Owner(name="PersonWeight150", age=randint(10, 15), weight=float(150))]
    + [Owner(name="PersonAge20Weight200", age=20, weight=float(200))]
)

total_owners = len(owners)


@pytest.fixture
def owner_store():
    store = MemoryStore("owners", key="name")
    store.connect()
    store.update([d.dict() for d in owners])
    return store


@pytest.fixture
def post_query_op():
    class PostQuery(QueryOperator):
        def query(self, name):
            return {"criteria": {"name": name}}

    return PostQuery()


def test_init(owner_store, post_query_op):
    resource = SubmissionResource(
        store=owner_store,
        get_query_operators=[PaginationQuery()],
        post_query_operators=[post_query_op],
        model=Owner,
    )
    assert len(resource.router.routes) == 4


def test_msonable(owner_store, post_query_op):
    owner_resource = SubmissionResource(
        store=owner_store,
        get_query_operators=[PaginationQuery()],
        post_query_operators=[post_query_op],
        model=Owner,
    )
    endpoint_dict = owner_resource.as_dict()

    for k in ["@class", "@module", "store", "model"]:
        assert k in endpoint_dict

    assert isinstance(endpoint_dict["model"], str)
    assert endpoint_dict["model"] == "tests.api.test_submission_resource.Owner"


def test_submission_search(owner_store, post_query_op):
    endpoint = SubmissionResource(
        store=owner_store,
        get_query_operators=[PaginationQuery()],
        post_query_operators=[post_query_op],
        calculate_submission_id=True,
        model=Owner,
    )
    app = FastAPI()
    app.include_router(endpoint.router)

    client = TestClient(app)

    assert client.get("/").status_code == 200
    assert client.post("/?name=test_name").status_code == 200


def test_key_fields(owner_store, post_query_op):
    endpoint = SubmissionResource(
        store=owner_store,
        get_query_operators=[PaginationQuery()],
        post_query_operators=[post_query_op],
        calculate_submission_id=False,
        model=Owner,
    )
    app = FastAPI()
    app.include_router(endpoint.router)

    client = TestClient(app)

    assert client.get("/Person1/").status_code == 200
    assert client.get("/Person1/").json()["data"][0]["name"] == "Person1"
