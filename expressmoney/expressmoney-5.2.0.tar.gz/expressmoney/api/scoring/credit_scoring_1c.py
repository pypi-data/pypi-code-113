__all__ = ('Scoring1CPoint',)

from expressmoney.api import *


SERVICE_NAME = 'scoring'


class CreditScoring1CCreateContract(Contract):

    MALE = "0"
    FEMALE = "1"
    GENDER_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female")
    )
    first_name = serializers.CharField(min_length=1, max_length=32)
    last_name = serializers.CharField(min_length=1, max_length=32)
    middle_name = serializers.CharField(min_length=1, max_length=32)
    gender = serializers.ChoiceField(choices=GENDER_CHOICES)
    birth_date = serializers.DateField()
    passport_serial = serializers.CharField(min_length=4, max_length=4)
    passport_number = serializers.CharField(min_length=6, max_length=6)
    passport_date = serializers.DateField()
    score = serializers.DecimalField(5, 4, min_value=0, max_value=1, read_only=True)


class CreditScoring1CReadContract(CreditScoring1CCreateContract):
    pagination = PaginationContract()
    id = serializers.IntegerField(min_value=1)
    score = serializers.DecimalField(5, 4, min_value=0, max_value=1)


# Endpoints ID
scoring_credit_scoring_1c_scoring_1c = ID(SERVICE_NAME, 'credit_scoring_1c', 'scoring_1c')


# Endpoints handlers
class Scoring1CPoint(ListPointMixin, CreatePointMixin, ContractPoint):
    _point_id = scoring_credit_scoring_1c_scoring_1c
    _create_contract = CreditScoring1CCreateContract
    _read_contract = CreditScoring1CReadContract
