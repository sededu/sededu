import os
import json

'''
this script is run as part of the build to parse out the README.md file into
usable information for the about page in the module.

A file called _readme.txt is generated in the /sededu/ folder for inclusion in
the deployment.
'''


class _ReadmeFileReader(object):
    # parse the SedEdu readme
    def __init__(self, rootPath):
        raw, lines = self.extract_from_file(rootPath)
        self.summary = self.make_summary(lines)
        self.license = self.make_license(lines)
        self.contributors = self.make_contributors(lines)
        
    def extract_from_file(self, path):
        # get the raw data into iterable lines
        readmePath = os.path.join(path, 'README.md')
        raw = open(readmePath, 'rt')
        lines = [ln.replace('\n', '').replace('*', '') for ln in raw]
        return raw, lines

    def strip_and_join(self, lines_raw):
        # utility to remove end whitespace and cat lines
        lines_rstripped = [ln.rstrip() for ln in lines_raw]
        lines = ' '.join(lines_rstripped)
        return lines

    def make_summary(self, lines):
        # the main summary text
        summaryIdx = lines.index('<!-- # SedEdu -->') + 1
        imageIdx = [i for i, s in enumerate(lines) 
                    if 'sededu_demo.png' in s]
        imageIdx = imageIdx[0]
        summary_raw = lines[summaryIdx:imageIdx]
        summary = self.strip_and_join(summary_raw)
        return summary

    def make_license(self, lines):
        # the license text
        licenseIdx = lines.index('# License') + 2
        acknowledgeIdx = lines.index('# Acknowledgments')
        license_raw = lines[licenseIdx:acknowledgeIdx]
        license = self.strip_and_join(license_raw)
        return license

    def make_contributors(self, lines):
        # the list of contributors
        contributorsIdx = lines.index('# Authors') + 2
        licenseIdx = lines.index('# License')
        contributors_raw = lines[contributorsIdx:licenseIdx]
        contributors = contributors_raw
        return contributors


class _ReadmeFileWriter(object):
    # write out the SedEdu readme to new
    def __init__(self, rootPath, data):
        self.data = data
        self.rootPath = rootPath

    def processData(self):
        self.dataDict = {'summary': self.data.summary,
                         'license': self.data.license,
                         'contributors': self.data.contributors}
        self.filePath = os.path.join(self.rootPath, 'sededu', '_readme.json')

    def jsonWrite(self):
        with open(self.filePath, 'w') as outfile:
            json.dump(self.dataDict, outfile)


if __name__ == '__main__':

    rootPath = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
    print('Parsing data from the README.md file:')
    print('\t', os.path.join(rootPath, 'README.md'))
    data = _ReadmeFileReader(rootPath)

    print('Data parsed from the README.md file:')
    print('\tSummary:')
    print('\t\t', data.summary)
    print('\tLicense:')
    print('\t\t', data.license)
    print('\tContributors:')
    print('\t\t', data.contributors)

    print('Writing data into new file:')
    writer = _ReadmeFileWriter(rootPath, data)
    writer.processData()
    writer.jsonWrite()
