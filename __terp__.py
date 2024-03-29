# -*- encoding: utf-8 -*-
##############################################################################
#    
#    Copyright (C) 2009 Italian Community (http://www). 
#    All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'STAMPE PERSONALIZZATE PER CLIENTE',
    'version': '0.1',
    'category': 'Localisation/Italy',
    'description': "Questo modulo aggiunge le stampe personalizzate lanciando dei wizard parametrici che lanceranno poi la stampa di Jasper",
    'author': 'C & G Software sas',
    'website': 'http://www.cgsoftware.it',
    "depends" : ['base','sale','jasper_reports'],
    "update_xml" : ['report.xml','wizard/stampa_out.xml'],
    "active": False,
    "installable": True
}

