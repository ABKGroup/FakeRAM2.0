import os
import sys
import math 

def get_macro_dimensions(process, sram_data):
  contacted_poly_pitch_um = process.contacted_poly_pitch_nm / 1000
  column_mux_factor       = process.column_mux_factor
  fin_pitch_um            = process.fin_pitch_nm / 1000
  width_in_bits           = int(sram_data['width'])
  depth                   = int(sram_data['depth'])
  num_banks               = int(sram_data['banks'])

  # Corresponds to the recommended 122 cell in asap7
  bitcell_height = 10 * fin_pitch_um
  bitcell_width = 2 * contacted_poly_pitch_um

  all_bitcell_height =  bitcell_height * depth
  all_bitcell_width =  bitcell_width * width_in_bits

  if num_banks == 2 or num_banks == 4:
    all_bitcell_height = all_bitcell_height / num_banks
    all_bitcell_width = all_bitcell_width * num_banks
  elif num_banks != 1:
    raise Exception("Unsupported number of banks: {}".format(num_banks))

  all_bitcell_height = all_bitcell_height / column_mux_factor
  all_bitcell_width = all_bitcell_width * column_mux_factor

  total_height = all_bitcell_height * 1.2
  total_width = all_bitcell_width * 1.2

  return total_height, total_width
