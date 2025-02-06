"""
This is a crab configuration skeleton

Here is a useful page on crab:
https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#CRAB_configuration_file

"""

from WMCore.Configuration import Configuration
config = Configuration()

###########################
config.section_("General")

config.General.requestName = 'crab_job_name'
config.General.workArea = config.General.requestName

###########################
config.section_("JobType")

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'psetName.py'
config.JobType.maxMemoryMB = 4000
config.JobType.maxJobRuntimeMin = 2700
config.JobType.allowUndistributedCMSSW = True

###########################
config.section_("Data")

config.Data.inputDataset = '/SingleMuon/Run2017G-17Nov2017-v1/AOD'
config.Data.inputDBS = 'global'
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/5TeV/ReReco/Cert_306546-306826_5TeV_EOY2017ReReco_Collisions17_JSON.txt'
config.Data.partialDataset = True;

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False

config.Data.outLFNDirBase = '/store/group/phys_heavyions/cbennett/'+config.General.requestName

###########################
config.section_("Site")

config.Site.storageSite = 'T2_CH_CERN'



