# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol                  #
#                                                                              #
# This program is free software: you can redistribute it and/or modify         #
# it under the terms of the GNU Affero General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or            #
# (at your option) any later version.                                          #
#                                                                              #
# This program is distributed in the hope that it will be useful,              #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU Affero General Public License for more details.                          #
#                                                                              #
# You should have received a copy of the GNU Affero General Public License     #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.        #
################################################################################

from openerp.osv import fields, osv
from datetime import *


class cl_person_address(osv.Model):
    _name = 'cl_person.address'

    _columns = {
        'address_id': fields.many2one('cl_address', 'Address', required=False),
        'person_id': fields.many2one('cl_person', string='Person', help='Person'),
        'sign_in_date': fields.datetime("Sign in date", required=False),
        'sign_out_date': fields.datetime("Sign out date", required=False),
        'notes': fields.text(string='Notes'),
        'active': fields.boolean(
            'Active',
            help="If unchecked, it will allow you to hide the person address without removing it."
            ),
    }

    _order = "sign_in_date desc"

    _defaults = {
        'sign_in_date': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'active': 1,
    }


class cl_person(osv.osv):
    _inherit = 'cl_person'

    _columns = {
        'person_address_ids': fields.one2many(
            'cl_person.address',
            'person_id',
            'Person Addresses'
            ),
    }


# class cl_address(osv.osv):
#     _inherit = 'cl_address'

#     _columns = {
#         'person_address_ids': fields.one2many(
#             'cl_person.address',
#             'address_id',
#             'Person Addresses'
#             ),
#     }
