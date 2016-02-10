# -*- coding: utf-8 -*-
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


class cl_todo_task(models.Model):
    _name = 'cl_todo.task'
    _inherit = ['mail.thread']

    name = fields.Char('Description', required=True, help="What needs to be done?")
    user_id = fields.Many2one('res.users', 'Responsible')
    date_deadline = fields.Date('Deadline')
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)

    @api.one
    def do_toggle_done(self):
        if self.user_id != self.env.user:
            raise Exception('Only the responsible can do this!')
        else:
            self.is_done = not self.is_done
            return True

    @api.multi
    def do_clear_done(self):
        domain = [('is_done', '=', True),
                  '|', ('user_id', '=', self.env.uid),
                       ('user_id', '=', False)]
        done_recs = self.search(domain)
        done_recs.write({'active': False})
        return True
