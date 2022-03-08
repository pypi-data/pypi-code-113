from typing import Any, cast, Dict, Optional, Type, TypeVar, Union

import attr

from ..extensions import NotPresentError
from ..models.scalar_config_types import ScalarConfigTypes
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManifestScalarConfig")


@attr.s(auto_attribs=True, repr=False)
class ManifestScalarConfig:
    """  """

    _type: Union[Unset, ScalarConfigTypes] = UNSET
    _description: Union[Unset, None, str] = UNSET
    _name: Union[Unset, str] = UNSET

    def __repr__(self):
        fields = []
        fields.append("type={}".format(repr(self._type)))
        fields.append("description={}".format(repr(self._description)))
        fields.append("name={}".format(repr(self._name)))
        return "ManifestScalarConfig({})".format(", ".join(fields))

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, int] = UNSET
        if not isinstance(self._type, Unset):
            type = self._type.value

        description = self._description
        name = self._name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def get_type() -> Union[Unset, ScalarConfigTypes]:
            type = None
            _type = d.pop("type")
            if _type is not None and _type is not UNSET:
                try:
                    type = ScalarConfigTypes(_type)
                except ValueError:
                    type = ScalarConfigTypes.of_unknown(_type)

            return type

        type = get_type() if "type" in d else cast(Union[Unset, ScalarConfigTypes], UNSET)

        def get_description() -> Union[Unset, None, str]:
            description = d.pop("description")
            return description

        description = get_description() if "description" in d else cast(Union[Unset, None, str], UNSET)

        def get_name() -> Union[Unset, str]:
            name = d.pop("name")
            return name

        name = get_name() if "name" in d else cast(Union[Unset, str], UNSET)

        manifest_scalar_config = cls(
            type=type,
            description=description,
            name=name,
        )

        return manifest_scalar_config

    @property
    def type(self) -> ScalarConfigTypes:
        if isinstance(self._type, Unset):
            raise NotPresentError(self, "type")
        return self._type

    @type.setter
    def type(self, value: ScalarConfigTypes) -> None:
        self._type = value

    @type.deleter
    def type(self) -> None:
        self._type = UNSET

    @property
    def description(self) -> Optional[str]:
        if isinstance(self._description, Unset):
            raise NotPresentError(self, "description")
        return self._description

    @description.setter
    def description(self, value: Optional[str]) -> None:
        self._description = value

    @description.deleter
    def description(self) -> None:
        self._description = UNSET

    @property
    def name(self) -> str:
        if isinstance(self._name, Unset):
            raise NotPresentError(self, "name")
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @name.deleter
    def name(self) -> None:
        self._name = UNSET
