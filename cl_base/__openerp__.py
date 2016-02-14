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
    'name': 'Base Module',
    'summary': 'Base Module needed for all CLVsol Solutions.',
    'version': '1.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'http://clvsol.com',
    'depends': [],
    'data': [
        'security/cl_base_security.xml',
        'menu/cl_base_menu_view.xml',
        'menu/cl_groupings_menu_view.xml',
        # 'menu/cl_agro_menu_view.xml',
        'menu/cl_community_menu_view.xml',
        'menu/cl_health_menu_view.xml',
        # 'menu/cl_insurance_menu_view.xml',
        # 'menu/cl_pharmacy_menu_view.xml',
        ],
    'test': [],
    'installable': True,
    'application': False,
    'active': False,
}
