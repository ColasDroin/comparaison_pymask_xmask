import os


# Run all scripts in one go
os.system("python 000_build_collider_from_mad_model.py")
os.system("python 001_install_beambeam.py")
os.system("python 002_knobs_and_tuning.py")
os.system("python 003_lumi_level.py")
os.system("python 004_configure_beambeam.py")
os.system("python 005_footprint.py")
