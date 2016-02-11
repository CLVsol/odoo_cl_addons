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

    annotation_ids = fields.Many2many(
        'cl_annotation',
        'cl_annotation_cl_tag_rel',
        'tag_id',
        'annotation_id',
        'Annotations'
        )


class cl_annotation(models.Model):
    _inherit = 'cl_annotation'

    tag_ids = fields.Many2many(
        'cl_tag',
        'cl_annotation_cl_tag_rel',
        'annotation_id',
        'tag_id',
        'Tags'
        )
