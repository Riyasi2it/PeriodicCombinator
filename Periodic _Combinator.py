import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Periodic Combinator - Periodic Table")

BACKGROUND = (44, 44, 47)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 100, 100)
ELEMENT_FONT_COLOR = (82, 87, 93) 


ALKALI_METALS = (255, 204, 204)      
ALKALINE_EARTH_METALS = (255, 229, 204) 
TRANSITION_METALS = (255, 255, 204)  
POST_TRANSITION_METALS = (229, 255, 204)
METALLOIDS = (204, 255, 204)      
NONMETALS = (204, 255, 229)     
HALOGENS = (204, 229, 255)     
NOBLE_GASES = (229, 204, 255) 
LANTHANIDES = (255, 204, 229)      
ACTINIDES = (255, 229, 204)  


font = pygame.font.Font(None, 29)

large_font = pygame.font.Font(None, 36)

bold_font = pygame.font.Font(None, 33)
bold_font.set_bold(True) 

element_font = pygame.font.Font("//", 28)

popup_font = pygame.font.Font(None, 46)  


CELL_SIZE = 53  
GRID_PADDING = 4  
TABLE_OFFSET_X = 80 


ELEMENTS = {
    'H': {'name': 'Hydrogen', 'color': NONMETALS, 'atomic_number': 1, 'mass': 1.008, 'electron_config': '1s1', 'shells': [1]},
    'He': {'name': 'Helium', 'color': NOBLE_GASES, 'atomic_number': 2, 'mass': 4.003, 'electron_config': '1s2', 'shells': [2]},
    'Li': {'name': 'Lithium', 'color': ALKALI_METALS, 'atomic_number': 3, 'mass': 6.941, 'electron_config': '1s2 2s1', 'shells': [2, 1]},
    'Be': {'name': 'Beryllium', 'color': ALKALINE_EARTH_METALS, 'atomic_number': 4, 'mass': 9.012, 'electron_config': '1s2 2s2', 'shells': [2, 2]},
    'B': {'name': 'Boron', 'color': METALLOIDS, 'atomic_number': 5, 'mass': 10.811, 'electron_config': '1s2 2s2 2p1', 'shells': [2, 3]},
    'C': {'name': 'Carbon', 'color': NONMETALS, 'atomic_number': 6, 'mass': 12.011, 'electron_config': '1s2 2s2 2p2', 'shells': [2, 4]},
    'N': {'name': 'Nitrogen', 'color': NONMETALS, 'atomic_number': 7, 'mass': 14.007, 'electron_config': '1s2 2s2 2p3', 'shells': [2, 5]},
    'O': {'name': 'Oxygen', 'color': NONMETALS, 'atomic_number': 8, 'mass': 15.999, 'electron_config': '1s2 2s2 2p4', 'shells': [2, 6]},
    'F': {'name': 'Fluorine', 'color': HALOGENS, 'atomic_number': 9, 'mass': 18.998, 'electron_config': '1s2 2s2 2p5', 'shells': [2, 7]},
    'Ne': {'name': 'Neon', 'color': NOBLE_GASES, 'atomic_number': 10, 'mass': 20.180, 'electron_config': '1s2 2s2 2p6', 'shells': [2, 8]},
    'Na': {'name': 'Sodium', 'color': ALKALI_METALS, 'atomic_number': 11, 'mass': 22.990, 'electron_config': '1s2 2s2 2p6 3s1', 'shells': [2, 8, 1]},
    'Mg': {'name': 'Magnesium', 'color': ALKALINE_EARTH_METALS, 'atomic_number': 12, 'mass': 24.305, 'electron_config': '1s2 2s2 2p6 3s2', 'shells': [2, 8, 2]},
    'Al': {'name': 'Aluminum', 'color': POST_TRANSITION_METALS, 'atomic_number': 13, 'mass': 26.982, 'electron_config': '1s2 2s2 2p6 3s2 3p1', 'shells': [2, 8, 3]},
    'Si': {'name': 'Silicon', 'color': METALLOIDS, 'atomic_number': 14, 'mass': 28.086, 'electron_config': '1s2 2s2 2p6 3s2 3p2', 'shells': [2, 8, 4]},
    'P': {'name': 'Phosphorus', 'color': NONMETALS, 'atomic_number': 15, 'mass': 30.974, 'electron_config': '1s2 2s2 2p6 3s2 3p3', 'shells': [2, 8, 5]},
    'S': {'name': 'Sulfur', 'color': NONMETALS, 'atomic_number': 16, 'mass': 32.065, 'electron_config': '1s2 2s2 2p6 3s2 3p4', 'shells': [2, 8, 6]},
    'Cl': {'name': 'Chlorine', 'color': HALOGENS, 'atomic_number': 17, 'mass': 35.453, 'electron_config': '1s2 2s2 2p6 3s2 3p5', 'shells': [2, 8, 7]},
    'Ar': {'name': 'Argon', 'color': NOBLE_GASES, 'atomic_number': 18, 'mass': 39.948, 'electron_config': '1s2 2s2 2p6 3s2 3p6', 'shells': [2, 8, 8]},
    'K': {'name': 'Potassium', 'color': ALKALI_METALS, 'atomic_number': 19, 'mass': 39.098, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s1', 'shells': [2, 8, 8, 1]},
    'Ca': {'name': 'Calcium', 'color': ALKALINE_EARTH_METALS, 'atomic_number': 20, 'mass': 40.078, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2', 'shells': [2, 8, 8, 2]},
    'Sc': {'name': 'Scandium', 'color': TRANSITION_METALS, 'atomic_number': 21, 'mass': 44.956, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d1', 'shells': [2, 8, 9, 2]},
    'Ti': {'name': 'Titanium', 'color': TRANSITION_METALS, 'atomic_number': 22, 'mass': 47.867, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d2', 'shells': [2, 8, 10, 2]},
    'V': {'name': 'Vanadium', 'color': TRANSITION_METALS, 'atomic_number': 23, 'mass': 50.942, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d3', 'shells': [2, 8, 11, 2]},
    'Cr': {'name': 'Chromium', 'color': TRANSITION_METALS, 'atomic_number': 24, 'mass': 51.996, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s1 3d5', 'shells': [2, 8, 13, 1]},
    'Mn': {'name': 'Manganese', 'color': TRANSITION_METALS, 'atomic_number': 25, 'mass': 54.938, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d5', 'shells': [2, 8, 13, 2]},
    'Fe': {'name': 'Iron', 'color': TRANSITION_METALS, 'atomic_number': 26, 'mass': 55.845, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d6', 'shells': [2, 8, 14, 2]},
    'Co': {'name': 'Cobalt', 'color': TRANSITION_METALS, 'atomic_number': 27, 'mass': 58.933, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d7', 'shells': [2, 8, 15, 2]},
    'Ni': {'name': 'Nickel', 'color': TRANSITION_METALS, 'atomic_number': 28, 'mass': 58.693, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d8', 'shells': [2, 8, 16, 2]},
    'Cu': {'name': 'Copper', 'color': TRANSITION_METALS, 'atomic_number': 29, 'mass': 63.546, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s1 3d10', 'shells': [2, 8, 18, 1]},
    'Zn': {'name': 'Zinc', 'color': TRANSITION_METALS, 'atomic_number': 30, 'mass': 65.38, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10', 'shells': [2, 8, 18, 2]},
    'Ga': {'name': 'Gallium', 'color': POST_TRANSITION_METALS, 'atomic_number': 31, 'mass': 69.723, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p1', 'shells': [2, 8, 18, 3]},
    'Ge': {'name': 'Germanium', 'color': METALLOIDS, 'atomic_number': 32, 'mass': 72.63, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p2', 'shells': [2, 8, 18, 4]},
    'As': {'name': 'Arsenic', 'color': METALLOIDS, 'atomic_number': 33, 'mass': 74.922, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p3', 'shells': [2, 8, 18, 5]},
    'Se': {'name': 'Selenium', 'color': NONMETALS, 'atomic_number': 34, 'mass': 78.971, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p4', 'shells': [2, 8, 18, 6]},
    'Br': {'name': 'Bromine', 'color': HALOGENS, 'atomic_number': 35, 'mass': 79.904, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p5', 'shells': [2, 8, 18, 7]},
    'Kr': {'name': 'Krypton', 'color': NOBLE_GASES, 'atomic_number': 36, 'mass': 83.798, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6', 'shells': [2, 8, 18, 8]},
    'Rb': {'name': 'Rubidium', 'color': ALKALI_METALS, 'atomic_number': 37, 'mass': 85.468, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1', 'shells': [2, 8, 18, 8, 1]},
    'Sr': {'name': 'Strontium', 'color': ALKALINE_EARTH_METALS, 'atomic_number': 38, 'mass': 87.62, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2', 'shells': [2, 8, 18, 8, 2]},
    'Y': {'name': 'Yttrium', 'color': TRANSITION_METALS, 'atomic_number': 39, 'mass': 88.906, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d1', 'shells': [2, 8, 18, 9, 2]},
    'Zr': {'name': 'Zirconium', 'color': TRANSITION_METALS, 'atomic_number': 40, 'mass': 91.224, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d2', 'shells': [2, 8, 18, 10, 2]},
    'Nb': {'name': 'Niobium', 'color': TRANSITION_METALS, 'atomic_number': 41, 'mass': 92.906, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d4', 'shells': [2, 8, 18, 12, 1]},
    'Mo': {'name': 'Molybdenum', 'color': TRANSITION_METALS, 'atomic_number': 42, 'mass': 95.95, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d5', 'shells': [2, 8, 18, 13, 1]},
    'Tc': {'name': 'Technetium', 'color': TRANSITION_METALS, 'atomic_number': 43, 'mass': 98, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d5', 'shells': [2, 8, 18, 13, 2]},
    'Ru': {'name': 'Ruthenium', 'color': TRANSITION_METALS, 'atomic_number': 44, 'mass': 101.07, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d7', 'shells': [2, 8, 18, 15, 1]},
    'Rh': {'name': 'Rhodium', 'color': TRANSITION_METALS, 'atomic_number': 45, 'mass': 102.91, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d8', 'shells': [2, 8, 18, 16, 1]},
    'Pd': {'name': 'Palladium', 'color': TRANSITION_METALS, 'atomic_number': 46, 'mass': 106.42, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 4d10', 'shells': [2, 8, 18, 18]},
    'Ag': {'name': 'Silver', 'color': TRANSITION_METALS, 'atomic_number': 47, 'mass': 107.87, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d10', 'shells': [2, 8, 18, 18, 1]},
    'Cd': {'name': 'Cadmium', 'color': TRANSITION_METALS, 'atomic_number': 48, 'mass': 112.41, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10', 'shells': [2, 8, 18, 18, 2]},
    'In': {'name': 'Indium', 'color': POST_TRANSITION_METALS, 'atomic_number': 49, 'mass': 114.82, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p1', 'shells': [2, 8, 18, 18, 3]},
    'Sn': {'name': 'Tin', 'color': POST_TRANSITION_METALS, 'atomic_number': 50, 'mass': 118.71, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p2', 'shells': [2, 8, 18, 18, 4]},
    'Sb': {'name': 'Antimony', 'color': METALLOIDS, 'atomic_number': 51, 'mass': 121.76, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p3', 'shells': [2, 8, 18, 18, 5]},
    'Te': {'name': 'Tellurium', 'color': METALLOIDS, 'atomic_number': 52, 'mass': 127.60, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p4', 'shells': [2, 8, 18, 18, 6]},
    'I': {'name': 'Iodine', 'color': HALOGENS, 'atomic_number': 53, 'mass': 126.90, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p5', 'shells': [2, 8, 18, 18, 7]},
    'Xe': {'name': 'Xenon', 'color': NOBLE_GASES, 'atomic_number': 54, 'mass': 131.29, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6', 'shells': [2, 8, 18, 18, 8]},
    'Cs': {'name': 'Cesium', 'color': ALKALI_METALS, 'atomic_number': 55, 'mass': 132.91, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1', 'shells': [2, 8, 18, 18, 8, 1]},
    'Ba': {'name': 'Barium', 'color': ALKALINE_EARTH_METALS, 'atomic_number': 56, 'mass': 137.33, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2', 'shells': [2, 8, 18, 18, 8, 2]},
    'La': {'name': 'Lanthanum', 'color': LANTHANIDES, 'atomic_number': 57, 'mass': 138.91, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1', 'shells': [2, 8, 18, 18, 9, 2]},
    'Ce': {'name': 'Cerium', 'color': LANTHANIDES, 'atomic_number': 58, 'mass': 140.12, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f1 5d1', 'shells': [2, 8, 18, 19, 9, 2]},
    'Pr': {'name': 'Praseodymium', 'color': LANTHANIDES, 'atomic_number': 59, 'mass': 140.91, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f3', 'shells': [2, 8, 18, 21, 8, 2]},
    'Nd': {'name': 'Neodymium', 'color': LANTHANIDES, 'atomic_number': 60, 'mass': 144.24, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f4', 'shells': [2, 8, 18, 22, 8, 2]},
    'Pm': {'name': 'Promethium', 'color': LANTHANIDES, 'atomic_number': 61, 'mass': 145, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f5', 'shells': [2, 8, 18, 23, 8, 2]},
    'Sm': {'name': 'Samarium', 'color': LANTHANIDES, 'atomic_number': 62, 'mass': 150.36, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f6', 'shells': [2, 8, 18, 24, 8, 2]},
    'Eu': {'name': 'Europium', 'color': LANTHANIDES, 'atomic_number': 63, 'mass': 151.96, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f7', 'shells': [2, 8, 18, 25, 8, 2]},
    'Gd': {'name': 'Gadolinium', 'color': LANTHANIDES, 'atomic_number': 64, 'mass': 157.25, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f7 5d1', 'shells': [2, 8, 18, 25, 9, 2]},
    'Tb': {'name': 'Terbium', 'color': LANTHANIDES, 'atomic_number': 65, 'mass': 158.93, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f9', 'shells': [2, 8, 18, 27, 8, 2]},
    'Dy': {'name': 'Dysprosium', 'color': LANTHANIDES, 'atomic_number': 66, 'mass': 162.50, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f10', 'shells': [2, 8, 18, 28, 8, 2]},
    'Ho': {'name': 'Holmium', 'color': LANTHANIDES, 'atomic_number': 67, 'mass': 164.93, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f11', 'shells': [2, 8, 18, 29, 8, 2]},
    'Er': {'name': 'Erbium', 'color': LANTHANIDES, 'atomic_number': 68, 'mass': 167.26, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f12', 'shells': [2, 8, 18, 30, 8, 2]},
    'Tm': {'name': 'Thulium', 'color': LANTHANIDES, 'atomic_number': 69, 'mass': 168.93, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f13', 'shells': [2, 8, 18, 31, 8, 2]},
    'Yb': {'name': 'Ytterbium', 'color': LANTHANIDES, 'atomic_number': 70, 'mass': 173.05, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14', 'shells': [2, 8, 18, 32, 8, 2]},
    'Lu': {'name': 'Lutetium', 'color': LANTHANIDES, 'atomic_number': 71, 'mass': 174.97, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d1', 'shells': [2, 8, 18, 32, 9, 2]},
    'Hf': {'name': 'Hafnium', 'color': TRANSITION_METALS, 'atomic_number': 72, 'mass': 178.49, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d2', 'shells': [2, 8, 18, 32, 10, 2]},
    'Ta': {'name': 'Tantalum', 'color': TRANSITION_METALS, 'atomic_number': 73, 'mass': 180.95, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d3', 'shells': [2, 8, 18, 32, 11, 2]},
    'W': {'name': 'Tungsten', 'color': TRANSITION_METALS, 'atomic_number': 74, 'mass': 183.84, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d4', 'shells': [2, 8, 18, 32, 12, 2]},
    'Re': {'name': 'Rhenium', 'color': TRANSITION_METALS, 'atomic_number': 75, 'mass': 186.21, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d5', 'shells': [2, 8, 18, 32, 13, 2]},
    'Os': {'name': 'Osmium', 'color': TRANSITION_METALS, 'atomic_number': 76, 'mass': 190.23, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d6', 'shells': [2, 8, 18, 32, 14, 2]},
    'Ir': {'name': 'Iridium', 'color': TRANSITION_METALS, 'atomic_number': 77, 'mass': 192.22, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d7', 'shells': [2, 8, 18, 32, 15, 2]},
    'Pt': {'name': 'Platinum', 'color': TRANSITION_METALS, 'atomic_number': 78, 'mass': 195.08, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1 4f14 5d9', 'shells': [2, 8, 18, 32, 17, 1]},
    'Au': {'name': 'Gold', 'color': TRANSITION_METALS, 'atomic_number': 79, 'mass': 196.97, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1 4f14 5d10', 'shells': [2, 8, 18, 32, 18, 1]},
    'Hg': {'name': 'Mercury', 'color': TRANSITION_METALS, 'atomic_number': 80, 'mass': 200.59, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10', 'shells': [2, 8, 18, 32, 18, 2]},
    'Tl': {'name': 'Thallium', 'color': POST_TRANSITION_METALS, 'atomic_number': 81, 'mass': 204.38, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p1', 'shells': [2, 8, 18, 32, 18, 3]},
    'Pb': {'name': 'Lead', 'color': POST_TRANSITION_METALS, 'atomic_number': 82, 'mass': 207.2, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p2', 'shells': [2, 8, 18, 32, 18, 4]},
    'Bi': {'name': 'Bismuth', 'color': POST_TRANSITION_METALS, 'atomic_number': 83, 'mass': 208.98, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p3', 'shells': [2, 8, 18, 32, 18, 5]},
    'Po': {'name': 'Polonium', 'color': POST_TRANSITION_METALS, 'atomic_number': 84, 'mass': 209, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p4', 'shells': [2, 8, 18, 32, 18, 6]},
    'At': {'name': 'Astatine', 'color': HALOGENS, 'atomic_number': 85, 'mass': 210, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p5', 'shells': [2, 8, 18, 32, 18, 7]},
    'Rn': {'name': 'Radon', 'color': NOBLE_GASES, 'atomic_number': 86, 'mass': 222, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6', 'shells': [2, 8, 18, 32, 18, 8]},
    'Fr': {'name': 'Francium', 'color': ALKALI_METALS, 'atomic_number': 87, 'mass': 223, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s1', 'shells': [2, 8, 18, 32, 18, 8, 1]},
    'Ra': {'name': 'Radium', 'color': ALKALINE_EARTH_METALS, 'atomic_number': 88, 'mass': 226, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2', 'shells': [2, 8, 18, 32, 18, 8, 2]},
    'Ac': {'name': 'Actinium', 'color': ACTINIDES, 'atomic_number': 89, 'mass': 227, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 6d1', 'shells': [2, 8, 18, 32, 18, 9, 2]},
    'Th': {'name': 'Thorium', 'color': ACTINIDES, 'atomic_number': 90, 'mass': 232.04, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 6d2', 'shells': [2, 8, 18, 32, 18, 10, 2]},
    'Pa': {'name': 'Protactinium', 'color': ACTINIDES, 'atomic_number': 91, 'mass': 231.04, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f2 6d1', 'shells': [2, 8, 18, 32, 20, 9, 2]},
    'U': {'name': 'Uranium', 'color': ACTINIDES, 'atomic_number': 92, 'mass': 238.03, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f3 6d1', 'shells': [2, 8, 18, 32, 21, 9, 2]},
    'Np': {'name': 'Neptunium', 'color': ACTINIDES, 'atomic_number': 93, 'mass': 237, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f4 6d1', 'shells': [2, 8, 18, 32, 22, 9, 2]},
    'Pu': {'name': 'Plutonium', 'color': ACTINIDES, 'atomic_number': 94, 'mass': 244, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f6', 'shells': [2, 8, 18, 32, 24, 8, 2]},
    'Am': {'name': 'Americium', 'color': ACTINIDES, 'atomic_number': 95, 'mass': 243, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f7', 'shells': [2, 8, 18, 32, 25, 8, 2]},
    'Cm': {'name': 'Curium', 'color': ACTINIDES, 'atomic_number': 96, 'mass': 247, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f7 6d1', 'shells': [2, 8, 18, 32, 25, 9, 2]},
    'Bk': {'name': 'Berkelium', 'color': ACTINIDES, 'atomic_number': 97, 'mass': 247, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f9', 'shells': [2, 8, 18, 32, 27, 8, 2]},
    'Cf': {'name': 'Californium', 'color': ACTINIDES, 'atomic_number': 98, 'mass': 251, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f10', 'shells': [2, 8, 18, 32, 28, 8, 2]},
    'Es': {'name': 'Einsteinium', 'color': ACTINIDES, 'atomic_number': 99, 'mass': 252, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f11', 'shells': [2, 8, 18, 32, 29, 8, 2]},
    'Fm': {'name': 'Fermium', 'color': ACTINIDES, 'atomic_number': 100, 'mass': 257, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f12', 'shells': [2, 8, 18, 32, 30, 8, 2]},
    'Md': {'name': 'Mendelevium', 'color': ACTINIDES, 'atomic_number': 101, 'mass': 258, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f13', 'shells': [2, 8, 18, 32, 31, 8, 2]},
    'No': {'name': 'Nobelium', 'color': ACTINIDES, 'atomic_number': 102, 'mass': 259, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14', 'shells': [2, 8, 18, 32, 32, 8, 2]},
    'Lr': {'name': 'Lawrencium', 'color': ACTINIDES, 'atomic_number': 103, 'mass': 262, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 7p1', 'shells': [2, 8, 18, 32, 32, 8, 3]},
    'Rf': {'name': 'Rutherfordium', 'color': TRANSITION_METALS, 'atomic_number': 104, 'mass': 267, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d2', 'shells': [2, 8, 18, 32, 32, 10, 2]},
    'Db': {'name': 'Dubnium', 'color': TRANSITION_METALS, 'atomic_number': 105, 'mass': 268, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d3', 'shells': [2, 8, 18, 32, 32, 11, 2]},
    'Sg': {'name': 'Seaborgium', 'color': TRANSITION_METALS, 'atomic_number': 106, 'mass': 269, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d4', 'shells': [2, 8, 18, 32, 32, 12, 2]},
    'Bh': {'name': 'Bohrium', 'color': TRANSITION_METALS, 'atomic_number': 107, 'mass': 270, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d5', 'shells': [2, 8, 18, 32, 32, 13, 2]},
    'Hs': {'name': 'Hassium', 'color': TRANSITION_METALS, 'atomic_number': 108, 'mass': 269, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d6', 'shells': [2, 8, 18, 32, 32, 14, 2]},
    'Mt': {'name': 'Meitnerium', 'color': TRANSITION_METALS, 'atomic_number': 109, 'mass': 278, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d7', 'shells': [2, 8, 18, 32, 32, 15, 2]},
    'Ds': {'name': 'Darmstadtium', 'color': TRANSITION_METALS, 'atomic_number': 110, 'mass': 281, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d8', 'shells': [2, 8, 18, 32, 32, 16, 2]},
    'Rg': {'name': 'Roentgenium', 'color': TRANSITION_METALS, 'atomic_number': 111, 'mass': 282, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d9', 'shells': [2, 8, 18, 32, 32, 17, 2]},
    'Cn': {'name': 'Copernicium', 'color': TRANSITION_METALS, 'atomic_number': 112, 'mass': 285, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10', 'shells': [2, 8, 18, 32, 32, 18, 2]},
    'Nh': {'name': 'Nihonium', 'color': POST_TRANSITION_METALS, 'atomic_number': 113, 'mass': 286, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p1', 'shells': [2, 8, 18, 32, 32, 18, 3]},
    'Fl': {'name': 'Flerovium', 'color': POST_TRANSITION_METALS, 'atomic_number': 114, 'mass': 289, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p2', 'shells': [2, 8, 18, 32, 32, 18, 4]},
    'Mc': {'name': 'Moscovium', 'color': POST_TRANSITION_METALS, 'atomic_number': 115, 'mass': 290, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p3', 'shells': [2, 8, 18, 32, 32, 18, 5]},
    'Lv': {'name': 'Livermorium', 'color': POST_TRANSITION_METALS, 'atomic_number': 116, 'mass': 293, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p4', 'shells': [2, 8, 18, 32, 32, 18, 6]},
    'Ts': {'name': 'Tennessine', 'color': HALOGENS, 'atomic_number': 117, 'mass': 294, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p5', 'shells': [2, 8, 18, 32, 32, 18, 7]},
    'Og': {'name': 'Oganesson', 'color': NOBLE_GASES, 'atomic_number': 118, 'mass': 294, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p6', 'shells': [2, 8, 18, 32, 32, 18, 8]},
}

# Define compounds
COMPOUNDS = {
    'H2O': {'elements': ['H', 'H', 'O'], 'name': 'Water', 'uses': 'Essential for life, solvent', 'properties': 'Colorless, odorless liquid'},
    'CO2': {'elements': ['C', 'O', 'O'], 'name': 'Carbon Dioxide', 'uses': 'Carbonated drinks, plant photosynthesis', 'properties': 'Colorless gas, soluble in water'},
    'NaCl': {'elements': ['Na', 'Cl'], 'name': 'Sodium Chloride', 'uses': 'Food seasoning, de-icing', 'properties': 'Crystalline solid, highly soluble in water'},
    'CH4': {'elements': ['C', 'H', 'H', 'H', 'H'], 'name': 'Methane', 'uses': 'Fuel, organic synthesis', 'properties': 'Colorless, odorless gas'},
    'NH3': {'elements': ['N', 'H', 'H', 'H'], 'name': 'Ammonia', 'uses': 'Fertilizers, cleaning products', 'properties': 'Colorless gas with pungent odor'},
    'HCl': {'elements': ['H', 'Cl'], 'name': 'Hydrochloric Acid', 'uses': 'Industrial cleaning, pH control', 'properties': 'Strong, corrosive acid'},
    'H2SO4': {'elements': ['H', 'H', 'S', 'O', 'O', 'O', 'O'], 'name': 'Sulfuric Acid', 'uses': 'Battery acid, industrial processes', 'properties': 'Dense, colorless, oily liquid'},
    'CaCO3': {'elements': ['Ca', 'C', 'O', 'O', 'O'], 'name': 'Calcium Carbonate', 'uses': 'Antacid, construction material', 'properties': 'White, chalky solid'},
    'C6H12O6': {'elements': ['C', 'C', 'C', 'C', 'C', 'C', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'O', 'O', 'O', 'O', 'O', 'O'], 'name': 'Glucose', 'uses': 'Energy source for living organisms', 'properties': 'Sweet-tasting, crystalline solid'},
    'NaHCO3': {'elements': ['Na', 'H', 'C', 'O', 'O', 'O'], 'name': 'Sodium Bicarbonate', 'uses': 'Baking, antacid', 'properties': 'White crystalline solid'},
    'C2H5OH': {'elements': ['C', 'C', 'H', 'H', 'H', 'H', 'H', 'O', 'H'], 'name': 'Ethanol', 'uses': 'Alcoholic beverages, fuel, solvent', 'properties': 'Colorless, flammable liquid'},
    'H2O2': {'elements': ['H', 'H', 'O', 'O'], 'name': 'Hydrogen Peroxide', 'uses': 'Bleaching agent, disinfectant', 'properties': 'Pale blue liquid, strong oxidizer'},
    'CH3COOH': {'elements': ['C', 'H', 'H', 'H', 'C', 'O', 'O', 'H'], 'name': 'Acetic Acid', 'uses': 'Vinegar, chemical reagent', 'properties': 'Colorless liquid with pungent odor'},
    'NaOH': {'elements': ['Na', 'O', 'H'], 'name': 'Sodium Hydroxide', 'uses': 'Drain cleaner, soap making', 'properties': 'White, corrosive solid'},
    'KCl': {'elements': ['K', 'Cl'], 'name': 'Potassium Chloride', 'uses': 'Fertilizer, salt substitute', 'properties': 'Colorless crystals or white powder'},
    'MgO': {'elements': ['Mg', 'O'], 'name': 'Magnesium Oxide', 'uses': 'Antacid, refractory material', 'properties': 'White, hygroscopic solid'},
    'Fe2O3': {'elements': ['Fe', 'Fe', 'O', 'O', 'O'], 'name': 'Iron(III) Oxide', 'uses': 'Pigment, polishing compound', 'properties': 'Reddish-brown solid'},
    'CuSO4': {'elements': ['Cu', 'S', 'O', 'O', 'O', 'O'], 'name': 'Copper(II) Sulfate', 'uses': 'Fungicide, algicide', 'properties': 'Blue crystalline solid'},
    'AgNO3': {'elements': ['Ag', 'N', 'O', 'O', 'O'], 'name': 'Silver Nitrate', 'uses': 'Photography, silver plating', 'properties': 'Colorless crystals, light sensitive'},
    'ZnCl2': {'elements': ['Zn', 'Cl', 'Cl'], 'name': 'Zinc Chloride', 'uses': 'Deodorants, soldering flux', 'properties': 'White crystalline solid, highly soluble in water'},
}


PERIODIC_TABLE_LAYOUT = [
    ['H', '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  '', 'He'],
    ['Li','Be', '',  '',  '',  '',  '',  '',  '',  '',  '',  '', 'B', 'C', 'N', 'O', 'F','Ne'],
    ['Na','Mg', '',  '',  '',  '',  '',  '',  '',  '',  '',  '', 'Al','Si', 'P', 'S','Cl','Ar'],
    ['K','Ca','Sc','Ti', 'V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr'],
    ['Rb','Sr', 'Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te', 'I','Xe'],
    ['Cs','Ba','La','Hf','Ta', 'W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb','Bi','Po','At','Rn'],
    ['Fr','Ra','Ac','Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Cn','Nh','Fl','Mc','Lv','Ts','Og'],
    ['', '', '*', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '#', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '*La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu',''],
    ['', '', '#Ac','Th','Pa', 'U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr',''],
]
def draw_element(element, x, y, angle=0):

    if angle == 0:

        if element and element in ELEMENTS:

            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

            pygame.draw.rect(screen, ELEMENTS[element]['color'], rect)

            pygame.draw.rect(screen, BLACK, rect, 1)
            

            symbol = element_font.render(element, True, ELEMENT_FONT_COLOR)

            symbol_rect = symbol.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))

            screen.blit(symbol, symbol_rect)

def draw_periodic_table():

    for row, elements in enumerate(PERIODIC_TABLE_LAYOUT):

        for col, element in enumerate(elements):

            x = col * (CELL_SIZE + GRID_PADDING) + GRID_PADDING + TABLE_OFFSET_X

            y = row * (CELL_SIZE + GRID_PADDING) + GRID_PADDING

            draw_element(element, x, y)

def draw_electron_shells(element, x, y, width, height):

    shells = ELEMENTS[element]['shells']

    center_x, center_y = x + width // 2, y + height // 2

    for i, electrons in enumerate(shells):

        radius = (i + 1) * (min(width, height) // (2 * len(shells)))

        pygame.draw.circle(screen, WHITE, (center_x, center_y), radius, 1)

        angle_step = 360 / electrons

        for j in range(electrons):

            angle = math.radians(j * angle_step)

            ex = center_x + int(radius * math.cos(angle))

            ey = center_y + int(radius * math.sin(angle))

            pygame.draw.circle(screen, WHITE, (ex, ey), 2)


def create_tooltip(element):

    info = ELEMENTS[element]

    tooltip_text = f"{info['name']}"


    tooltip = font.render(tooltip_text, True, (44, 44, 47), (229, 229, 229))

    return tooltip

def draw_tooltip(screen, tooltip, pos):

    screen.blit(tooltip, (pos[0] + 15, pos[1] + 15))

def show_element_info(element):

    info = ELEMENTS[element]

    lines = [
        f"Name: {info['name']}",
        f"Atomic Number: {info['atomic_number']}",
        f"Mass: {info['mass']}",
        f"Electron Config: {info['electron_config']}"
    ]

    return lines

def show_compound_info(compound):

    info = COMPOUNDS[compound]

    lines = [
        f"Name: {info['name']}",
        f"Formula: {compound}",
        f"Uses: {info['uses']}",
        f"Properties: {info['properties']}"
    ]

    return lines

def check_compound(elements):

    elements.sort()

    for compound, data in COMPOUNDS.items():

        if elements == sorted(data['elements']):

            return compound, data['name']

    return None, None

def show_popup(message, color):

    popup = popup_font.render(message, True, color)

    popup_rect = popup.get_rect(center=(WIDTH // 2, HEIGHT - 260))

    screen.blit(popup, popup_rect)

    pygame.display.flip()

    pygame.time.wait(1500)

def get_element_at_pos(pos):

    x, y = pos

    col = (x - TABLE_OFFSET_X) // (CELL_SIZE + GRID_PADDING)

    row = y // (CELL_SIZE + GRID_PADDING)

    if 0 <= row < len(PERIODIC_TABLE_LAYOUT) and 0 <= col < len(PERIODIC_TABLE_LAYOUT[0]):

        return PERIODIC_TABLE_LAYOUT[row][col]

    return None

def main():

    clock = pygame.time.Clock()

    dragging = False
    

    dragged_element = None
    

    merge_area = []

    merge_area_rect = pygame.Rect(WIDTH - 200, HEIGHT - 150, 180, 100)
    electron_shell_rect = pygame.Rect(WIDTH - 200, HEIGHT - 260, 180, 100)
    merge_button = pygame.Rect(WIDTH - 200, HEIGHT - 40, 180, 30)
    

    info_area = []
    

    hover_element = None
    

    tooltip = None

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if merge_button.collidepoint(event.pos):
 
                    compound, name = check_compound(merge_area)
                    if compound:

                        show_popup(f"Created {name} ({compound})", WHITE)

                        info_area = show_compound_info(compound)
                    else:

                        show_popup("No compound formed", RED)

                    merge_area = []
                else:

                    element = get_element_at_pos(event.pos)
                    if element and element in ELEMENTS:

                        dragging = True
                        dragged_element = element

                        info_area = show_element_info(element)
            elif event.type == pygame.MOUSEBUTTONUP:
                if dragging:
                    dragging = False
                    if merge_area_rect.collidepoint(event.pos) and dragged_element:

                        merge_area.append(dragged_element)
                    else:

                        show_popup(f"{ELEMENTS[dragged_element]['name']}", WHITE)

                dragged_element = None


        screen.fill(BACKGROUND)

        draw_periodic_table()
        

        pygame.draw.rect(screen, WHITE, merge_area_rect, 2)
        for i, elem in enumerate(merge_area):

            draw_element(elem, merge_area_rect.x + 10 + i*40, merge_area_rect.y + 10)
        

        pygame.draw.rect(screen, WHITE, electron_shell_rect, 2)
        if merge_area:

            draw_electron_shells(merge_area[-1], electron_shell_rect.x, electron_shell_rect.y, 
                                 electron_shell_rect.width, electron_shell_rect.height)

        pygame.draw.rect(screen, WHITE, merge_button)
        merge_text = font.render("Merge", True, BLACK)
        screen.blit(merge_text, (merge_button.x + 70, merge_button.y + 8))


        info_rect = pygame.Rect(10, HEIGHT - 150, 300, 140)
        for i, line in enumerate(info_area):

            info_text = font.render(line, True, WHITE)

            screen.blit(info_text, (info_rect.x, info_rect.y + i*30))

        mouse_pos = pygame.mouse.get_pos()

        hover_element = get_element_at_pos(mouse_pos)
        if hover_element and hover_element in ELEMENTS:

            tooltip = create_tooltip(hover_element)
        else:

            tooltip = None

        if tooltip:

            draw_tooltip(screen, tooltip, mouse_pos)


        if dragging and dragged_element:

            x, y = pygame.mouse.get_pos()

            draw_element(dragged_element, x - CELL_SIZE // 2, y - CELL_SIZE // 2)


        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":

    main()