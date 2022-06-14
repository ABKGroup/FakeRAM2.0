import os
import sys
import math 

def get_macro_dimensions(process, sram_data):
  contacted_poly_pitch_nm        = process.contacted_poly_pitch_nm
  contacted_poly_pitch_um        = process.contacted_poly_pitch_nm / 1000
  column_mux_factor   = process.column_mux_factor
  fin_pitch_nm        = process.fin_pitch_nm
  fin_pitch_um        = process.fin_pitch_nm / 1000
  name                = str(sram_data['name'])
  width_in_bits       = int(sram_data['width'])
  depth               = int(sram_data['depth'])
  num_banks           = int(sram_data['banks'])
  total_size          = width_in_bits * depth
  single_bitcell_area = 8 * fin_pitch_um * 2 * contacted_poly_pitch_um
  if num_banks == 1:
    all_bitcell_height = 8 * fin_pitch_um * depth
    all_bitcell_width = 2 * contacted_poly_pitch_um * width_in_bits
  elif num_banks == 2:
    all_bitcell_height = 8 * fin_pitch_um * ( depth / 2 )
    all_bitcell_width = 2 * contacted_poly_pitch_um * 2 * width_in_bits
  all_bitcell_height = all_bitcell_height / column_mux_factor
  all_bitcell_width = all_bitcell_width * column_mux_factor
  total_height = all_bitcell_height * 1.2
  total_width = all_bitcell_width * 1.2

  return total_height, total_width
