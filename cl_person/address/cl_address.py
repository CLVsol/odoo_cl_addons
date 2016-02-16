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

from openerp import models, fields


class cl_address(models.Model):
    _inherit = 'cl_address'

    person_ids = fields.One2many(
        'cl_person',
        'address_id',
        'Persons'
        )


class cl_person(models.Model):
    _inherit = 'cl_person'

    address_id = fields.Many2one('cl_address', 'Person Address', ondelete='restrict')
    person_phone = fields.Char('Person Phone', size=32)
    mobile_phone = fields.Char('Person Mobile', size=32)
    person_email = fields.Char('Person Email', size=240)

    def onchange_address_id(self, cr, uid, ids, address, context=None):
        if address:
            address = self.pool.get('cl_address').browse(cr, uid, address, context=context)
            return {'value': {'person_phone': address.phone,
                              'mobile_phone': address.mobile,
                              'person_email': address.email
                              }}
        return {'value': {}}
