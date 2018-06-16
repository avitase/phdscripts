import config as configFile

j = Job(name = configFile.name)

myApp = GaudiExec()
myApp.directory = '/afs/cern.ch/user/n/nmeinert/phdthesis/analysis/DaVinciDev_v42r6p1'

j.application = myApp
j.application.options = ['options.py']

if configFile.debug:
    j.application.readInputData(configFile.bkk)
    j.backend = Local()
else:
    data = BKQuery(configFile.bkquery).getDataset()
    assert len(data.files) > 0
    j.inputdata = data
    j.backend = Dirac()

j.splitter = SplitByFiles(filesPerJob = configFile.filesPerJob)
j.outputfiles = [LocalFile(configFile.name + '.root')]

j.submit()
