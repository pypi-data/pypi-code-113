# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2022 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2022 GNU Solidario <health@gnusolidario.org>
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from trytond.pool import Pool
from . import health_nursing
from . import sequences

def register():
    Pool.register(
        health_nursing.PatientRounding,
        health_nursing.RoundingProcedure,
        health_nursing.PatientAmbulatoryCare,
        health_nursing.AmbulatoryCareProcedure,
        sequences.GnuHealthSequences,
        sequences.AmbulatoryCareSequence,
        sequences.PatientRoundingSequence,
        module='health_nursing', type_='model')
