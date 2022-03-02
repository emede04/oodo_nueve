# -*- coding: utf-8 -*-

from odoo import models, fields, api


class director(models.Model):
    _name = 'nueve.director'
    -description = 'modelo director'
    name = fields.Char('nombre', required=True)
    edad = fields.Char('edad', required=True)


class actor(models.Model):
    _name = 'nueve.actor'
    -description = 'modelo actor'
    name = fields.Char('nombre', required=True)
    edad = fields.Char('edad', required=True)


class pelicula(models.Model):
    _name = 'nueve.pelicula'
    -description = 'modelo pelicula'


    name = fields.Char('nombre', required=True)
    edad = fields.Char('año', required=True)
        

class estudio(models.Model):
    _name = 'nueve.estudio'
    -description = 'modelo estudio'
    name = fields.Char('nombre', required=True)
    edad = fields.Char('edad', required=True)

    localizacion = fields.Char('localizacion',required=True)

class escritores(models.Model):
    _name = 'nueve.escritores'
    -description = 'modelo escritores'
    name = fields.Char('nombre', required=True)
    edad = fields.Char('edad', required=True)


class productor(models.Model):
    _name = 'nueve.productor'
    -description = 'modelo productor'
    name = fields.Char('nombre', required=True)
    edad = fields.Char('edad', required=True)


class compositor(models.Model):
    _name = 'nueve.compositor'
    -description = 'modelo compositor'
    name = fields.Char('nombre', required=True)
    edad = fields.Char('edad', required=True)


class editor(models.Model):
    _name = 'nueve.editor'
    -description = 'modelo editor'
    name = fields.Char('nombre', required=True)
    edad = fields.Char('edad', required=True)


class cinematografia(models.Model):
    _name = 'nueve.cinematografia'
    -description = 'modelo cinematografia'
    name = fields.Char('nombre', required=True)
    edad = fields.Char('edad', required=True)
