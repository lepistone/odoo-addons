# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015  ADHOC SA  (http://www.adhoc.com.ar)
#    All Rights Reserved.
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
#######################################################s#######################
{
    'name': 'Portal Distributor Stock',
    'version': '0.1',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
Portal Stock Distributor Sale
=======================
    """,
    'author': 'ADHOC SA',
    'depends': [
        'portal_sale_distributor',
        'portal_stock',
        ],
    'demo': [
    ],
    'data': [
        'security/portal_security.xml',
        'security/ir.model.access.csv',
        'portal_sale_view.xml',
    ],
    'auto_install': True,
    'category': 'Hidden',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
