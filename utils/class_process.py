################################################################################
# PROCESS CLASS
#
# This class stores the infromation about the process that the memory is being
# generated in. Every memory has a pointer to a process object. The information
# for the process comes from the json configuration file (typically before the
# "sram" list section).
################################################################################
import os
import sys
import math
class Process:

  def __init__(self, json_data):

    # From JSON configuration file
    self.tech_nm        = int(json_data['tech_nm'])
    self.voltage        = str(json_data['voltage'])
    self.metal_prefix    = str(json_data['metal_prefix'])
    self.metal_layer     = str(json_data['metal_layer'])
    self.pin_width_nm    = int(json_data['pin_width_nm'])
    self.pin_pitch_nm    = int(json_data['pin_pitch_nm'])
    self.metal_track_pitch_nm =  int(json_data['metal_track_pitch_nm'])
    self.contacted_poly_pitch_nm = int(json_data['contacted_poly_pitch_nm'])
    self.fin_pitch_nm = int(json_data['fin_pitch_nm'])
    self.manufacturing_grid_nm = int(json_data['manufacturing_grid_nm'])
    self.column_mux_factor = int(json_data['column_mux_factor'])
    
    # Optional keys
    self.snap_width_nm   = int(json_data['snap_width_nm']) if 'snap_width_nm' in json_data else 1
    self.snap_height_nm  = int(json_data['snap_height_nm']) if 'snap_height_nm' in json_data else 1
    
    # Converted values
    self.tech_um     = self.tech_nm / 1000.0
    self.pin_width_um = self.pin_width_nm / 1000.0
    self.pin_pitch_um = self.pin_pitch_nm / 1000.0
    self.metal_track_pitch_um = self.metal_track_pitch_nm / 1000.0
    self.manufacturing_grid_um = self.manufacturing_grid_nm / 1000.0

    if (self.pin_pitch_nm % self.metal_track_pitch_nm != 0):
      print("Pin Pitch %d not a multiple of Metal Track Pitch %d" %(self.pin_pitch_nm,self.metal_track_pitch_nm))
      sys.exit(1)
    if (self.pin_pitch_nm % self.manufacturing_grid_nm != 0):
      print("Pin Pitch %d not a multiple of Manufacturing Grid %d" %(self.pin_pitch_nm, self.manufacturing_grid_nm))
      sys.exit(1) 
