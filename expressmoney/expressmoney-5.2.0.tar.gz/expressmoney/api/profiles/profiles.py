__all__ = ('UserProfilePoint', 'UserProfileObjectPoint', 'RussianProfilePoint', 'RussianProfileObjectPoint')

from expressmoney.api import *


SERVICE_NAME = 'profiles'


class UserProfileCreateContract(Contract):
    user_id = serializers.IntegerField(min_value=1)
    ip = serializers.IPAddressField(protocol='ipv4')
    http_referer = serializers.URLField()


class UserProfileUpdateContract(Contract):
    last_password = serializers.CharField(max_length=8, allow_blank=True)


class ProfileUpdateContract(Contract):
    first_name = serializers.CharField(max_length=32)
    last_name = serializers.CharField(max_length=32)
    middle_name = serializers.CharField(max_length=32)


class ProfileCreateContract(ProfileUpdateContract):
    NONE = 'NONE'
    PASSPORT = "PP"
    DRIVING_LICENCE = "DL"
    INSURANCE = "INSURANCE"
    TAX_ID = "TAX_ID"
    GOVERNMENT_ID_TYPE_CHOICES = (
        (NONE, gettext_lazy('None')),
        (PASSPORT, gettext_lazy("Passport")),
        (DRIVING_LICENCE, gettext_lazy("Driving licence")),
        (TAX_ID, gettext_lazy("Tax ID")),
        (INSURANCE, gettext_lazy('SNILS')),
    )

    birth_date = serializers.DateField()
    # Address
    postal_code = serializers.CharField(max_length=16, allow_blank=True)
    state = serializers.CharField(max_length=32, allow_blank=True)
    city = serializers.CharField(max_length=32, allow_blank=True)
    street = serializers.CharField(max_length=32, allow_blank=True)
    street_house = serializers.CharField(max_length=8, allow_blank=True)
    street_building = serializers.CharField(max_length=4, allow_blank=True)
    street_lane = serializers.CharField(max_length=16, allow_blank=True)
    street_apartment = serializers.CharField(max_length=8, allow_blank=True)
    address = serializers.CharField(max_length=256, allow_blank=True)
    address_optional = serializers.CharField(max_length=64, allow_blank=True)
    po_box = serializers.CharField(max_length=8, allow_blank=True)
    # Government ID
    government_id_type = serializers.ChoiceField(choices=GOVERNMENT_ID_TYPE_CHOICES)
    government_id_number = serializers.CharField(max_length=16, allow_blank=True)
    government_id_date = serializers.DateField(allow_null=True)


class ProfileReadContract(ProfileCreateContract):
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()
    # Underwriting
    is_identified = serializers.BooleanField()
    is_verified = serializers.BooleanField()
    # Address
    address_code = serializers.CharField(max_length=64, allow_blank=True)
    address_coordinates = serializers.CharField(max_length=64, allow_blank=True)


class RussianProfileUpdateContract(ProfileUpdateContract):
    passport_serial = serializers.CharField(max_length=4)
    passport_number = serializers.CharField(max_length=6)


class RussianProfileCreateContract(ProfileCreateContract):
    passport_serial = serializers.CharField(max_length=4)
    passport_number = serializers.CharField(max_length=6)
    passport_issue_name = serializers.CharField(max_length=256, allow_blank=True)
    passport_code = serializers.CharField(max_length=16)
    passport_date = serializers.DateField()
    income = serializers.IntegerField(allow_null=True)


class RussianProfileReadContract(ProfileReadContract,):
    passport_serial = serializers.CharField(max_length=4)
    passport_number = serializers.CharField(max_length=6)
    passport_issue_name = serializers.CharField(max_length=256, allow_blank=True)
    passport_code = serializers.CharField(max_length=16)
    passport_date = serializers.DateField()
    income = serializers.IntegerField(allow_null=True)
    income_region = serializers.IntegerField(allow_null=True)
    court_address = serializers.CharField(max_length=256, allow_blank=True)
    fias_region = serializers.CharField(max_length=256, allow_blank=True)


profiles_profiles_russian_profile = ID(SERVICE_NAME, 'profiles', 'russian_profile')
profiles_profiles_user_profile = ID(SERVICE_NAME, 'profiles', 'user_profile')


class UserProfilePoint(CreatePointMixin, ContractPoint):
    _point_id = profiles_profiles_user_profile
    _create_contract = UserProfileCreateContract


class UserProfileObjectPoint(UpdatePointMixin, ContractObjectPoint):
    _point_id = profiles_profiles_user_profile
    _update_contract = UserProfileUpdateContract


class RussianProfilePoint(CreatePointMixin, ContractPoint):
    _point_id = profiles_profiles_russian_profile
    _create_contract = RussianProfileCreateContract


class RussianProfileObjectPoint(RetrievePointMixin, UpdatePointMixin, ContractObjectPoint):
    _point_id = profiles_profiles_russian_profile
    _read_contract = RussianProfileReadContract
    _update_contract = RussianProfileUpdateContract
