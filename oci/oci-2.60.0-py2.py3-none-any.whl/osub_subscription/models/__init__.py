# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .commitment import Commitment
from .commitment_detail import CommitmentDetail
from .commitment_summary import CommitmentSummary
from .currency import Currency
from .product import Product
from .rate_card_summary import RateCardSummary
from .rate_card_tier import RateCardTier
from .subscribed_service_summary import SubscribedServiceSummary
from .subscription_product import SubscriptionProduct
from .subscription_summary import SubscriptionSummary

# Maps type names to classes for osub_subscription services.
osub_subscription_type_mapping = {
    "Commitment": Commitment,
    "CommitmentDetail": CommitmentDetail,
    "CommitmentSummary": CommitmentSummary,
    "Currency": Currency,
    "Product": Product,
    "RateCardSummary": RateCardSummary,
    "RateCardTier": RateCardTier,
    "SubscribedServiceSummary": SubscribedServiceSummary,
    "SubscriptionProduct": SubscriptionProduct,
    "SubscriptionSummary": SubscriptionSummary
}
