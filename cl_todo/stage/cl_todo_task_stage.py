# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2016-Today  Carlos Eduardo Vercelino - CLVsol                  #
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

from openerp import models, fields, api
# from openerp.addons.base.res import res_request
from openerp.exceptions import ValidationError


# def referencable_models(self):
#     return res_request.referencable_models(
#         self, self.env.cr, self.env.uid, context=self.env.context)


class Stage(models.Model):
    _name = 'cl_todo.task.stage'
    _order = 'sequence,name'

    # name = fields.Char('Name', 40, translate=True)
    # Field attributes:
    name = fields.Char(
        string='Name',
        # Common field attributes:
        copy=False,
        default='New',
        groups="base.group_user,base.group_no_one",
        help='The title for the stage.',
        index=True,
        readonly=False,
        required=True,
        states={'done': [('readonly', False)]},
        # String only attributes:
        size=40,
        translate=True,
        )

    # Other string fields:
    desc = fields.Text('Description')
    state = fields.Selection(
        [('draft', 'New'),
         ('open', 'Started'),
         ('done', 'Closed')
         ], 'State',
        # selection_add= When extending a Model, adds items to selection list
        )
    docs = fields.Html('Documentation')

    # Numeric fields:
    sequence = fields.Integer('Sequence')
    perc_complete = fields.Float('% Complete', (3, 2))

    # Date fields:
    date_effective = fields.Date('Effective Date')
    date_changed = fields.Datetime('Last Changed')

    # Other fields:
    fold = fields.Boolean('Folded?')
    image = fields.Binary('Image')

    # One2many inverse relation:
    task_ids = fields.One2many('cl_todo.task', 'stage_id', 'Tasks in this stage')


class TodoTask(models.Model):
    _inherit = 'cl_todo.task'

    # Relational fields
    stage_id = fields.Many2one('cl_todo.task.stage', 'Stage')

    #     # Relational field attributes:
    #     auto_join=False,
    #     context="{}",
    #     domain="[]",
    #     ondelete='cascade',
    # )

    # Dynamic Reference fields:
    refers_to = fields.Reference(
        [('res.user', 'User'),
         ('res.partner', 'Partner')
         ], 'Refers to',
        )

    # Related fields:
    stage_state = fields.Selection(
        related='stage_id.state',
        string='Stage State',
        store=True,  # optional
        )

    # Calculated fields:
    stage_fold = fields.Boolean(
        string='Stage Folded?',
        compute='_compute_stage_fold',
        search='_search_stage_fold',
        inverse='_write_stage_fold',
        store=False,  # the default
        )

    @api.one
    @api.depends('stage_id.fold')
    def _compute_stage_fold(self):
        self.stage_fold = self.stage_id.fold

    def _search_stage_fold(self, operator, value):
        return [('stage_id.fold', operator, value)]

    def _write_stage_fold(self):
        self.stage_id.fold = self.stage_fold

    # Constraints
    _sql_constraints = [(
        'todo_task_name_unique',
        'UNIQUE (name, user_id, active)',
        'Task title must be unique!'
        )]

    @api.one
    @api.constrains('name')
    def _check_name_size(self):
        if len(self.name) < 5:
            raise ValidationError('Title must have 5 chars!')

    @api.one
    def compute_user_todo_count(self):
        self.user_todo_count = self.search_count(
            [('user_id', '=', self.user_id.id)])

    user_todo_count = fields.Integer(
        'User To-Do Count',
        compute='compute_user_todo_count'
    )
    effort_estimate = fields.Integer('Effort Estimate')
