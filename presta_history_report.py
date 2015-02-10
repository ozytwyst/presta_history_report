# -*- coding: utf-8 -*-
##############################################################################
#
#    presta_history_report module for OpenERP, Display connections
#    Copyright (C) 2014 ozytwyst Julien Thomazeau <ozydev@julienthomazeau.fr>
#
#    This file is a part of presta_history_report
#
#    presta_history_report is free software: you can redistribute it and/or modify
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


from openerp.osv import fields
from openerp.osv import orm
from openerp.tools.sql import drop_view_if_exists

class presta_history_report(orm.Model):
    _name = 'presta.history.report'
    _auto = False
    _rec_name = 'email'
    _columns = {
	'date_connection':fields.datetime('Date',readonly=True),
	'email':fields.char('Email',size=240, readonly=True),
	'society_id':fields.many2one('res.partner','Society',readonly=True,relate=True),
	'pricelist_id':fields.many2one('product.pricelist','Price list',readonly=True,relate=True)
    }
    def init(self, cr):
        drop_view_if_exists(cr,'presta_history_report')
        cr.execute("""
	    CREATE OR REPLACE VIEW public.presta_history_report AS (	
                SELECT
                    presta.id as id,
		    presta.connection_date as date_connection,
                    presta.email as email,
		    case when (SELECT id from res_partner WHERE email like '%'||presta.email||'%' and parent_id is null and active = true limit 1) is null then (SELECT id from res_partner WHERE id = (SELECT parent_id FROM res_partner WHERE email like '%'||presta.email||'%' limit 1))
else (SELECT id from res_partner WHERE email like '%'||presta.email||'%' and parent_id is null and active = true limit 1)
end as society_id,
		    (SELECT get_ir_property_many2one('res.partner',case when (SELECT id from res_partner WHERE email like '%'||presta.email||'%' and parent_id is null and active = true limit 1) is null then (SELECT id from res_partner WHERE id = (SELECT parent_id FROM res_partner WHERE email like '%'||presta.email||'%' limit 1))
else (SELECT id from res_partner WHERE email like '%'||presta.email||'%' and parent_id is null and active = true limit 1)
end,'property_product_pricelist',3)) as pricelist_id
                FROM
                    prestashop.connection as presta
	    )""")
