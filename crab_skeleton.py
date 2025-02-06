"""
This is a crab configuration skeleton

Here is a useful page on crab:
https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#CRAB_configuration_file

"""

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")

config.General.requestName = 'crab_job_name'
config.General.workArea = config.General.requestName

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runForestAOD_pp_DATA_94X.py'

