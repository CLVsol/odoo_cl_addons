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
    'name': 'Community',
    'summary': 'Community Module used by the CLVsol Solutions.',
    'version': '1.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'http://clvsol.com',
    'images': [],
    'depends': [
        'cl_base',
        # 'cl_tag',
        # 'cl_annotation',
        # 'cl_person',
        # 'cl_family',
        # 'hr',
        ],
    'data': [
        'security/cl_community_security.xml',
        # 'security/ir.model.access.csv',
        'cl_community_view.xml',
        'category/cl_community_category_view.xml',
        # 'cl_tag/cl_tag_view.xml',
        # 'cl_annotation/cl_annotation_view.xml',
        # 'seq/cl_community_sequence.xml',
        # 'seq/cl_community_category_sequence.xml',
        # 'wkf/cl_community_workflow.xml',
        # 'wkf/cl_community_wkf_view.xml',
        # 'history/cl_community_history_view.xml',
        # 'cl_person/cl_community_person_view.xml',
        # 'cl_person/cl_community_person_role_view.xml',
        # 'cl_family/cl_community_family_view.xml',
        # 'cl_family/cl_community_family_role_view.xml',
        # 'hr_employee/cl_community_employee_view.xml',
        # 'hr_employee/cl_community_employee_role_view.xml',
        'menu/cl_community_menu_view.xml',
        ],
    'demo': [],
    'test': [],
    'init_xml': [],
    'test': [],
    'update_xml': [],
    'installable': True,
    'application': False,
    'active': False,
    'css': [],
}
