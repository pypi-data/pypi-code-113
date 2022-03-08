# (C) Copyright 2004-2022 Enthought, Inc., Austin, TX
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license included in LICENSE.txt and may be redistributed only under
# the conditions described in the aforementioned license. The license
# is also available online at http://www.enthought.com/licenses/BSD.txt
#
# Thanks for using Enthought open source!

from traits.api import HasStrictTraits, Instance, Int, List, Regex, Str
from traitsui.api import InstanceEditor, InstanceFactoryChoice, Item, View

# -------------------------------------------------------------------------
#  'Person' class:
# -------------------------------------------------------------------------


class Person(HasStrictTraits):

    # -------------------------------------------------------------------------
    #  Trait definitions:
    # -------------------------------------------------------------------------

    name = Str()
    age = Int()
    phone = Regex(value='000-0000', regex=r'\d\d\d[-]\d\d\d\d')

    # -------------------------------------------------------------------------
    #  Traits view definition:
    # -------------------------------------------------------------------------

    traits_view = View('name', 'age', 'phone', buttons=['OK', 'Cancel'])


# -------------------------------------------------------------------------
#  Sample data:
# -------------------------------------------------------------------------

people = [
    Person(name='Dave', age=39, phone='555-1212'),
    Person(name='Mike', age=28, phone='555-3526'),
    Person(name='Joe', age=34, phone='555-6943'),
    Person(name='Tom', age=22, phone='555-7586'),
    Person(name='Dick', age=63, phone='555-3895'),
    Person(name='Harry', age=46, phone='555-3285'),
    Person(name='Sally', age=43, phone='555-8797'),
    Person(name='Fields', age=31, phone='555-3547'),
]

# -------------------------------------------------------------------------
#  'Team' class:
# -------------------------------------------------------------------------


class Team(HasStrictTraits):

    # -------------------------------------------------------------------------
    #  Trait definitions:
    # -------------------------------------------------------------------------

    name = Str()
    captain = Instance(Person)
    roster = List(Person)

    # -------------------------------------------------------------------------
    #  Traits view definitions:
    # -------------------------------------------------------------------------

    traits_view = View(
        [
            'name',
            '_',
            Item(
                'captain',
                editor=InstanceEditor(
                    name='roster',
                    label='Edit...',
                    values=[
                        InstanceFactoryChoice(
                            klass=Person, name='Non player', view='edit_view'
                        )
                    ],
                ),
            ),
        ],
        buttons=['OK', 'Cancel'],
    )


# -------------------------------------------------------------------------
#  Run the test:
# -------------------------------------------------------------------------

if __name__ == '__main__':
    Team(name='Vultures', captain=people[0], roster=people).configure_traits()
