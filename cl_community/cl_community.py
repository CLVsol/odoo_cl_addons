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

from openerp.osv import fields, osv
from datetime import datetime


class cl_community(osv.osv):
    _name = "cl_community"

    def name_get(self, cr, uid, ids, context=None):
        """Return the community's display name, including their direct
           parent by default.

        :param dict context: the ``community_display`` key can be
                             used to select the short version of the
                             community (without the direct parent),
                             when set to ``'short'``. The default is
                             the long version."""
        if context is None:
            context = {}
        if context.get('community_display') == 'short':
            return super(cl_community, self).name_get(cr, uid, ids, context=context)
        if isinstance(ids, (int, long)):
            ids = [ids]
        reads = self.read(cr, uid, ids, ['name', 'parent_id'], context=context)
        res = []
        for record in reads:
            name = record['name']
            if record['parent_id']:
                name = record['parent_id'][1] + ' / ' + name
            res.append((record['id'], name))
        return res

    def name_search(self, cr, uid, name, args=None, operator='ilike', context=None, limit=100):
        if not args:
            args = []
        if not context:
            context = {}
        if name:
            name = name.split(' / ')[-1]
            ids = self.search(cr, uid, [('name', operator, name)] + args, limit=limit, context=context)
        else:
            ids = self.search(cr, uid, args, limit=limit, context=context)
        return self.name_get(cr, uid, ids, context)

    def _name_get_fnc(self, cr, uid, ids, prop, unknow_none, context=None):
        res = self.name_get(cr, uid, ids, context=context)
        return dict(res)

    _columns = {
        'name': fields.char('Community', required=True, size=64, translate=False),
        'alias': fields.char('Alias', size=64, help='Common name that the Community is referred'),
        'parent_id': fields.many2one('cl_community', 'Parent Community', select=True, ondelete='restrict'),
        'code': fields.char(size=64, string='Community Code', required=False),
        'address_id': fields.many2one('res.partner', 'Community Address', ondelete='restrict'),
        'comm_phone': fields.char('Community Phone', size=32),
        'mobile_phone': fields.char('Community Mobile', size=32),
        'comm_email': fields.char('Community Email', size=240),
        'notes': fields.text(string='Notes'),
        'complete_name': fields.function(_name_get_fnc, type="char", string='Name', store=False),
        'child_ids': fields.one2many('cl_community', 'parent_id', 'Child Communities'),
        'comm_location': fields.char('Community Location', size=32),
        'date_inclusion': fields.datetime("Inclusion Date", required=False, readonly=False),
        'active': fields.boolean('Active',
                                 help="If unchecked, it will allow you to hide the community without removing it."),
        'parent_left': fields.integer('Left parent', select=True),
        'parent_right': fields.integer('Right parent', select=True),
    }

    _constraints = [
        (osv.osv._check_recursion, 'Error! You can not create recursive communities.', ['parent_id'])
        ]

    _defaults = {
        'date_inclusion': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'active': 1,
    }

    _parent_store = True
    _parent_order = 'name'
    _order = 'parent_left'

    def onchange_address_id(self, cr, uid, ids, address, context=None):
        if address:
            address = self.pool.get('res.partner').browse(cr, uid, address, context=context)
            return {'value': {'comm_phone': address.phone,
                              'mobile_phone': address.mobile,
                              'comm_email': address.email
                              }}
        return {'value': {}}
