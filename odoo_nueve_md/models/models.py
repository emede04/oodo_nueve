# -*- coding: utf-8 -*-
from odoo import models, fields, api


# class odoo_nueve_md(models.Model):
#     _name = 'odoo_nueve_md.odoo_nueve_md'
#     _description = 'odoo_nueve_md.odoo_nueve_md'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100



class pelicula(models.Model):
     _name = 'odoo_nueve_md.pelicula'
     _description = 'model pelicula'

     name = fields.Char('ID', required=True)
     titulo = fields.Char(String = 'titulo', required = True)
     director = fields.Many2many('odoo_nueve_md.director', string='director')
     resumen = fields.Many2many('odoo_nueve_md.resumen', string='breve resumen')
     estudio= fields.Many2one('odoo_nueve_md.estudios', string='a que estudio pertenece')
     tipo = fields.Many2many('odoo_nueve_md.tipo_pelicula', string='tipo de pelicula')
     galardones= fields.Many2many('odoo_nueve_md.galardones', string='galardones')
     encartelera= fields.Many2one('odoo_nueve_md.encartelera', string='encartelera')
     online= fields.Many2one('odoo_nueve_md.online', string='online')
     taquillazo= fields.Many2many('odoo_nueve_md.taquillazo', string='taquillazo')
     franquicia= fields.Many2one('odoo_nueve_md.franquicia', string='franquicia')
     trilogia= fields.Many2one('odoo_nueve_md.trilogias', string='Trilogia')


class director(models.Model):
     _name = 'odoo_nueve_md.director'
     _description = 'model director'

     
     name = fields.Char('ID', required = True)
     nombre = fields.Char(String = 'nombre', required = True)
     apellido = fields.Char(String = 'apellido', required = True)

     origen = fields.Char(String = 'origen')
     pelicula = fields.Many2many('odoo_nueve_md.pelicula', 'director', string='pelicula')

class estudios(models.Model):
     _name = 'odoo_nueve_md.estudios'
     _description = 'model estudios'

     
     name = fields.Char('ID', required=True)
     nombre = fields.Char(String='nombre', required=True)
     fundador = fields.Char(String='fundador', required = True)
     pais = fields.Char(String='pais')
     estilo = fields.Char(String='estilo')
     budget = fields.Char(String='budget')

     pelicula = fields.One2many('odoo_nueve_md.pelicula', 'estudio', string='pelicula')


class galardones(models.Model):
     _name='odoo_nueve_md.galardones'
     _descripcion = 'model galardones'

     
     name = fields.Char('ID', required = True)
     nombre_premio = fields.Char(String = 'nombre_premio', required = True)
     anio = fields.Char(String = 'anio', required = True)

     pelicula = fields.Many2many('odoo_nueve_md.pelicula', 'galardones', string='pelicula')
class taquillazo(models.Model):
     _name='odoo_nueve_md.taquillazo'
     _descripcion = 'model taquillazo'

     
     name = fields.Char('ID', required = True)
     anio = fields.Char(String = 'año', required = True)
     dinero = fields.Char(String = 'dinero recaudado', required = True)
     dinerosemana = fields.Char(String = 'dinero de primera semana', required = True)

     pelicula = fields.Many2many('odoo_nueve_md.pelicula', 'taquillazo', string='pelicula')

class franquicia(models.Model):
     _name='odoo_nueve_md.franquicia'
     _descripcion = 'model franquicia'

     
     name = fields.Char('ID', required = True)
     franquicia = fields.Char(String = 'franquicia', required = True)
     pelicula = fields.One2many('odoo_nueve_md.pelicula', 'franquicia', string='pelicula')

class trilogias(models.Model):
     _name='odoo_nueve_md.trilogias'
     _descripcion = 'model trilogias'

     
     name = fields.Char('ID', required = True)
     trilogia = fields.Char(String = 'trilogia', required = True)
     basada  = fields.Char(String = 'basada en algun libro', required = True)
     pelicula = fields.One2many('odoo_nueve_md.pelicula', 'trilogia', string='pelicula')

class encartelera(models.Model):
     _name='odoo_nueve_md.encartelera'
     _descripcion = 'model encartelera'

     
     name = fields.Char('ID', required = True)
     encartelera = fields.Char(String = 'encartelera', required = True)
     cines = fields.Char(String = 'cines en los que esta ', required = True)
     independiente = fields.Char(String = 'se encuentra en teatros independientes', required = True)

     pelicula = fields.One2many('odoo_nueve_md.pelicula', 'encartelera', string='pelicula')

class online(models.Model):
     _name='odoo_nueve_md.online'
     _descripcion = 'model online'

     
     name = fields.Char('ID', required = True)
     online = fields.Char(String = 'online', required = True)
     torrent = fields.Char(String = 'es pirateable', required = True)

     pelicula = fields.One2many('odoo_nueve_md.pelicula', 'online', string='pelicula')

class tipo_pelicula(models.Model):
     _name='odoo_nueve_md.tipo_pelicula'
     _descripcion = 'model tipo_pelicula'

     name = fields.Char('ID', required = True)
     tipo = fields.Char(String = 'tipo', required = True)
     subgenero = fields.Char(String = 'subgenero', required = True)

     pelicula = fields.Many2many('odoo_nueve_md.pelicula', 'tipo', string='pelicula')
