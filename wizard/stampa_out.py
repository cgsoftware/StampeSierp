# -*- encoding: utf-8 -*-

import wizard
import decimal_precision as dp
import pooler
import time
from tools.translate import _
from osv import osv, fields
from tools.translate import _



class stampa_stock_move(osv.osv_memory):
    _name = 'stampa.stock.move'
    _description = 'funzioni stampa ordini jasper'
    _columns = {
                #'dadata': fields.date('Da Data Documento', required=True ),
                #'adata': fields.date('A Data Documento', required=True),
                'danrv': fields.char('Da Documento',size=30,required=True),
                'anrv': fields.char('A Documento',size=30,required=True),
                #'anrv': fields.char('A Documento',size=30,required=True),
                #'prezzi':fields.boolean('Stampo i prezzi e gli sconti sull''ordine?')
    }
    
    def _build_contexts(self, cr, uid, ids, data, context=None):
        if context is None:
            context = {}
        result = {}
        result = {'danr':data['form']['danrv'],'anr':data['form']['anrv'],'name':data['form']['danrv']}
        
            
        return result
  
    def _print_report(self, cr, uid, ids, data, context=None):
        #import pdb;pdb.set_trace()
        if context is None:
            context = {}
        pool = pooler.get_pool(cr.dbname)
        fatture = pool.get('stock.move')
        active_ids = context and context.get('active_ids', [])
        Primo = True
        return {
                'type': 'ir.actions.report.xml',
                'report_name': 'scarico',
                'datas': data,
            }
 

    def check_report(self, cr, uid, ids, context=None):
        #import pdb;pdb.set_trace()
        if context is None:
            context = {}
            
        data = {}
        data['ids'] = context.get('active_ids', [])
        data['model'] = context.get('active_model', 'ir.ui.menu')
        data['form'] = self.read(cr, uid, ids, ['danrv', 'anrv'])[0]
        used_context = self._build_contexts(cr, uid, ids, data, context=context)
        data['form']['parameters'] = used_context
        return self._print_report(cr, uid, ids, data, context=context)
  
    def view_init(self, cr, uid, fields_list, context=None):
        # import pdb;pdb.set_trace()
        res = super(stampa_ordini, self).view_init(cr, uid, fields_list, context=context)

        return res
    
             
    def  default_get(self, cr, uid, fields, context=None):
        #import pdb;pdb.set_trace()
        pool = pooler.get_pool(cr.dbname)
        produzione = pool.get('stock.move')
        active_ids = context and context.get('active_ids', [])
        Primo = True
        if active_ids:
             for ordine in produzione.browse(cr, uid, active_ids, context=context):
                if Primo:
                    Primo = False
                    
                    NrIni = ordine.picking_id.name
                    danr = ordine['id']
                    name = NrIni
                

                NrFin = ordine.picking_id.name
                anr = ordine['id']                
        
        return{'danrv':NrIni,'anrv':NrFin, 'name':name }

    

    
stampa_stock_move()  


