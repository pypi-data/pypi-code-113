__all__ = ('LoanIssuePoint', 'LoanPaymentBodyPoint', 'LoanInterestsChargePoint', 'LoanPaymentInterestsPoint')

from expressmoney.api import *

SERVICE_NAME = 'accounting'


class LoanIssueCreateContract(Contract):
    amount = serializers.DecimalField(max_digits=16, decimal_places=0, min_value=1, max_value=1000000000)
    department = serializers.IntegerField(min_value=1)
    analytical = serializers.IntegerField(min_value=1)


class LoanPaymentBodyCreateContract(LoanIssueCreateContract):
    pass


class LoanInterestsChargeCreateContract(LoanIssueCreateContract):
    pass


class LoanPaymentInterestsCreateContract(LoanIssueCreateContract):
    pass


accounting_operations_loan_issue = ID(SERVICE_NAME, 'operations', 'loan_issue')
accounting_operations_loan_payment_body = ID(SERVICE_NAME, 'operations', 'loan_payment_body')
accounting_operations_loan_interests_charge = ID(SERVICE_NAME, 'operations', 'loan_interests_charge')
accounting_operations_loan_payment_interests = ID(SERVICE_NAME, 'operations', 'loan_payment_interests')


class LoanIssuePoint(CreatePointMixin, ContractPoint):
    """Issue loan body (Dt48801 Kt47422)"""
    _point_id = accounting_operations_loan_issue
    _create_contract = LoanIssueCreateContract


class LoanPaymentBodyPoint(CreatePointMixin, ContractPoint):
    """Payment loan body (Dt47423 Kt48801)"""
    _point_id = accounting_operations_loan_payment_body
    _create_contract = LoanPaymentBodyCreateContract


class LoanInterestsChargePoint(CreatePointMixin, ContractPoint):
    """Charge loan interests (Dt48802 Kt71001)"""
    _point_id = accounting_operations_loan_interests_charge
    _create_contract = LoanInterestsChargeCreateContract


class LoanPaymentInterestsPoint(CreatePointMixin, ContractPoint):
    """Payment loan interests (Dt47423 Kt48809)"""
    _point_id = accounting_operations_loan_payment_interests
    _create_contract = LoanPaymentInterestsCreateContract
