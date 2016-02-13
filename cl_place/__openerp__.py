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

{
    'name': 'Place',
    'summary': 'Place Module used by all CLVsol Solutions.',
    'version': '1.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'http://clvsol.com',
    'depends': [
        'cl_base',
        'cl_tag',
        'cl_annotation',
        'cl_address',
        ],
    'data': [
        'security/cl_place_security.xml',
        # 'security/ir.model.access.csv',
        'cl_place_view.xml',
        'category/cl_place_category_view.xml',
        'tag/cl_tag_view.xml',
        'annotation/cl_annotation_view.xml',
        # 'seq/cl_place_seq_view.xml',
        # 'seq/cl_place_sequence.xml',
        # 'seq/cl_place_category_sequence.xml',
        # 'wkf/cl_place_workflow.xml',
        # 'wkf/cl_place_wkf_view.xml',
        # 'history/cl_place_history_view.xml',
        'menu/cl_place_menu_view.xml',
        ],
    'init_xml': [],
    'test': [],
    'update_xml': [],
    'installable': True,
    'application': False,
    'active': False,
}
