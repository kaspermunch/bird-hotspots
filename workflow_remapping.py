

from gwf import Workflow, AnonymousTarget
import os, sys
from pathlib import Path

gwf = Workflow()

data_path = Path('/project/Birds/faststorage/data')
composition_data_path = data_path / 'composition_cpg'
composition_data_path_remapped = data_path / 'composition_cpg_remapped'

if not composition_data_path_remapped.exists():
    os.makedirs(composition_data_path_remapped)

hotspot_data_file = '/project/Birds/faststorage/data/bed/hotspots.bed'
cgi_data_file = '/project/Birds/faststorage/data/bed/CGI-taeGut1.txt'
promoter_data_file = '/project/Birds/faststorage/data/bed/promoters.bed'
tss_data_file = '/project/Birds/faststorage/data/bed/tss_1bp.bed'
tes_data_file = '/project/Birds/faststorage/data/bed/tes_1bp.bed'

species_dirs = [x for x in composition_data_path.iterdir() if x.is_dir()]

for species_dir in species_dirs:
    
    input_files = list(species_dir.iterdir())

    outfile_hotspots = composition_data_path_remapped / species_dir.with_suffix('.hotspot_relative.txt').name
    outfile_cgi = composition_data_path_remapped / species_dir.with_suffix('.cgi_relative.txt').name

    outfile_promoters = composition_data_path_remapped / species_dir.with_suffix('.promoter_relative.txt').name
    outfile_tss = composition_data_path_remapped / species_dir.with_suffix('.tss_relative.txt').name
    outfile_tes = composition_data_path_remapped / species_dir.with_suffix('.tes_relative.txt').name

    gwf.target(f'remap_{species_dir.name}', 
    inputs=[hotspot_data_file, cgi_data_file, promoter_data_file, tss_data_file, tes_data_file] + input_files, 
    outputs=[outfile_hotspots, outfile_cgi, outfile_promoters, outfile_tss, outfile_tes],
    walltime='01:00:00', memory='10g') << f"""

    python scripts/remap_coordinates.py {species_dir} {hotspot_data_file} {cgi_data_file} {promoter_data_file} {tss_data_file} {tes_data_file} \
        {outfile_hotspots} {outfile_cgi} {outfile_promoters} {outfile_tss} {outfile_tes}
    """

outfile_hotspots_rel_cgi = composition_data_path_remapped / 'hotspot_rel_cgi.txt'
outfile_hotspots_rel_promoter = composition_data_path_remapped / 'hotspot_rel_promoter.txt'
outfile_hotspots_rel_tss = composition_data_path_remapped / 'hotspot_rel_tss.txt'
outfile_hotspots_rel_tes = composition_data_path_remapped / 'hotspot_rel_tes.txt'
    
gwf.target('remap_hotspots', 
inputs=[hotspot_data_file, cgi_data_file, promoter_data_file, tss_data_file, tes_data_file], 
outputs=[outfile_hotspots_rel_cgi, outfile_hotspots_rel_promoter, outfile_hotspots_rel_tss, outfile_hotspots_rel_tes],
walltime='01:00:00', memory='10g') << f"""

python scripts/remap_hotspots.py {hotspot_data_file} {cgi_data_file} {promoter_data_file} {tss_data_file} {tes_data_file} \
    {outfile_hotspots_rel_cgi} {outfile_hotspots_rel_promoter} {outfile_hotspots_rel_tss} {outfile_hotspots_rel_tes}
"""

#python scripts/remap_hotspots.py /project/Birds/faststorage/data/bed/hotspots.bed /project/Birds/faststorage/data/bed/CGI-taeGut1.txt /project/Birds/faststorage/data/bed/promoters.bed /project/Birds/faststorage/data/bed/tss_1bp.bed /project/Birds/faststorage/data/bed/tes_1bp.bed hotspot_rel_cgi.txt hotspot_rel_tss.txt hotspot_rel_tes.txt hotspot_rel_promoter.txt 