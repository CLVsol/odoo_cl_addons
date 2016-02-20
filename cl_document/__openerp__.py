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
    'name': 'Document',
    'summary': 'Document Module used by CLVsol Solutions.',
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
        ],
    'data': [
        'security/cl_document_security.xml',
        # 'security/ir.model.access.csv',
        'cl_document_view.xml',
        # 'doc_type/cl_document_type_view.xml',
        # # 'category/cl_document_category_view.xml',
        # 'cl_tag/cl_tag_view.xml',
        # 'cl_annotation/cl_annotation_view.xml',
        # 'seq/cl_document_sequence.xml',
        # # 'seq/cl_document_category_sequence.xml',
        # 'wkf/cl_document_workflow.xml',
        # 'wkf/cl_document_wkf_view.xml',
        # 'history/cl_document_history_view.xml',
        # # 'question/cl_document_question_view.xml',
        # # 'question/cl_document_document_question_view.xml',
        # # 'question/cl_document_question_answer_view.xml',
        'menu/cl_document_menu_view.xml',
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
