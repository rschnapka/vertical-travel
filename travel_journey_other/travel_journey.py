# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2013 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, orm


class travel_journey(orm.Model):
    _inherit = 'travel.journey'
    _columns = {
        'other_from': fields.char('Origin', 256),
        'other_to': fields.char('Destination', 256),
        'other_departure': fields.datetime('Departure',
                                           help='Date and time of the '
                                                'departure of the special '
                                                'transportation type.'),
        'other_arrival': fields.datetime('Arrival',
                                         help='Date and time of the '
                                              'arrival of the special '
                                              'transportation type.'),
        'other_capacity': fields.integer('Capacity',
                                         help='Number of passengers who can '
                                              'take this mode of transport'),
        'other_description': fields.text('Description'),
    }


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
