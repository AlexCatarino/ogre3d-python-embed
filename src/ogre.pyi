﻿# coding: utf-8

import enum

class ColourValue:
    def __init__(self, r : float, g : float, b : float, a : float): ...

class Light:
    diffuse_colour : ColourValue = ...
    light_type : LightTypes = ...
    specular_colour : ColourValue = ...
    def set_attenuation(self, range : float, constant : float, linear : float, quadratic : float): ...

class Viewport:
    def set_background_colour(self, colour : ColourValue): ...

class SceneManager:
    def create_light(self, name : str): return Light()
    def set_ambient_light(self, colour : ColourValue): ...
    def set_fog(self, mode : FogMode, colour : ColourValue, density : float, expDensity : float, linearStart : float, linearEnd : float): ...
    def set_shadow_technique(self, technique : ShadowTechnique): ...
    def set_shadow_colour(self, colour : ColourValue): ...
    def set_shadow_texture_count(self, count : int): ...
    def set_shadow_texture_size(self, size : int): ...

# For enumerations, we define each value as its own type and assign '...' because
# we don't know/care about the value. In the future, we should imply this simply
# from specifying the name.

class FogMode(enum.Enum):
    EXP : FogMode = ...
    EXP2 : FogMode = ...
    LINEAR : FogMode = ...
    NONE : FogMode = ...

class LightTypes(enum.Enum):
    DIRECTIONAL : LightTypes = ...
    POINT : LightTypes = ...
    SPOTLIGHT : LightTypes = ...

class ShadowTechnique(enum.Enum):
    NONE : ShadowTechnique = ...
    TEXTURE_ADDITIVE :ShadowTechnique = ...
    TEXTURE_MODULATIVE : ShadowTechnique = ...