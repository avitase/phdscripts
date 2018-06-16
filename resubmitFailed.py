from sys import argv

if len(argv) != 2:
    print 'Usage:', argv[0], '[jobID]' 
    exit(-1)

assert len(argv) == 2
job = jobs(argv[1])

print 'Job: {} ({})'.format(job.id, job.name)
def getFailedLFNs(job):
    for sj in filter(lambda j: j.status == 'failed', job.subjobs):
        for lfn in [x.lfn for x in sj.inputdata.files]:
            yield lfn

failedLFNs = ['LFN:' + lfn for lfn in getFailedLFNs(job)]

print 'found {} LFNs ...'.format(len(failedLFNs))
yesno = raw_input('Do you want to continue? (yes/no): ')
if yesno.strip() != 'yes':
    exit(-1)

job2name = job.name + '_failed'
print 'preparing new job \'{}\' ...'.format(job2name)

job2 = job.copy()
job2.name = job2name

job2.inputdata = LHCbDataset(failedLFNs)
job2.splitter.filesPerJob = max(1, len(failedLFNs) / 100)
job2.submit()
