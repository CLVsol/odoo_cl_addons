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
    'name': 'Medicament',
    'summary': 'Medicament Module used by the CLVsol Solutions.',
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
        # 'product',
        ],
    'data': [
        'security/cl_medicament_security.xml',
        # 'security/ir.model.access.csv',
        # 'product_product_view.xml',
        'cl_medicament_view.xml',
        'uom/cl_medicament_uom_view.xml',
        'form/cl_medicament_form_view.xml',
        'category/cl_medicament_category_view.xml',
        # 'manufacturer/cl_medicament_manufacturer_view.xml',
        # 'active_component/cl_medicament_active_component_view.xml',
        # 'cl_tag/cl_tag_view.xml',
        # 'cl_annotation/cl_annotation_view.xml',
        # 'seq/cl_medicament_sequence.xml',
        # 'seq/cl_medicament_category_sequence.xml',
        # 'wkf/cl_medicament_workflow.xml',
        # 'wkf/cl_medicament_wkf_view.xml',
        # 'history/cl_medicament_history_view.xml',
        # 'therapeutic_class/cl_medicament_therapeutic_class_view.xml',
        # 'route/cl_medicament_route_view.xml',
        # 'template/cl_medicament_template_view.xml',
        # 'seq/cl_medicament_template_sequence.xml',
        'menu/cl_medicament_menu_view.xml',
        # 'seq/cl_medicament_manufacturer_sequence.xml',
        # 'seq/cl_medicament_active_component_sequence.xml',
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
