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


class cl_tag(models.Model):
    _inherit = 'cl_tag'

    address_ids = fields.Many2many(
        'cl_address',
        'cl_address_cl_tag_rel',
        'tag_id',
        'address_id',
        'Addresses'
        )


class cl_address(models.Model):
    _inherit = 'cl_address'

    tag_ids = fields.Many2many(
        'cl_tag',
        'cl_address_cl_tag_rel',
        'address_id',
        'tag_id',
        'Tags'
        )
