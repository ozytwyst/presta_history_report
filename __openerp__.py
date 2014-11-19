# -*- coding: utf-8 -*-
##############################################################################
#
#    presta_history_report module for OpenERP, Get PrestaShop Connection History
#    Copyright (C) 2014 ozytwyst Julien Thomazeau <ozydev@julienthomazeau.fr>
#
#    This file is a part of product_brands
#
#    product_brands is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    product_brands is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Presta History Report',
    'version': '1.0',
    'category': 'Synchro',
    'description': """ Connection history report""",
    'author': 'Julien Thomazeau',
    'depends': [
        'product',
        ],
    'data': [
	'presta_history_report_view.xml',
	]
}
