import re
import logging
from datetime import datetime
from file_utiles import read, write


class MergeRequires(object):
    BUILDREQUIRES_RE = 'BuildRequires:'
    REQUIRES_RE = 'Requires:'

    def __init__(self, filename):
        self.f = filename
        self.content = read(self.f)
        self.flag_build_require = False
        self.flag_require = False
        self.content_fix = ''

    def handle(self):
        content_list = self.content.split('\n')
        for i in content_list:
            if re.match(self.BUILDREQUIRES_RE, i):
                if self.flag_build_require is True:
                    line_content = i.split(':')[1]
                else:
                    if self.flag_require is True:
                        line_content = '\n'+ i
                    else:
                        line_content = i
                self.flag_build_require = True
                self.flag_require = False
            elif re.match(self.REQUIRES_RE, i):
                if self.flag_require is True:
                    line_content = i.split(':')[1]
                else:
                    if self.flag_build_require is True:
                        line_content = '\n'+ i
                    else:
                        line_content = i
                self.flag_build_require = False
                self.flag_require = True
            else:
                if self.flag_require is True or self.flag_build_require is True:
                    if i == '':
                        line_content = i
                    else:
                        line_content = '\n' + i + '\n'
                        self.flag_require = False
                        self.flag_build_require = False
                else:
                    line_content = i + '\n'
            logging.debug(line_content)
            l = ['Name', 'Version', 'Release', 'Summary', 'License', 'URL', 'Source0', 'BuildRequires']
            if line_content.split(':')[0] in l:
                line_content = self.format_spec_key_value(self.split_spec_key_value(i)[0],
                                                          self.split_spec_key_value(i)[1])
                if line_content.split(':')[0] != 'BuildRequires' and line_content.split(':')[0] != 'Requires':
                    line_content += '\n'
            # logging.warn(line_content)
            if line_content.lstrip().startswith('%descr'):
                logging.debug(line_content)
                line_content = '\n' + line_content
            self.content_fix += line_content

    def write_spec(self):
        write(self.f, self.content_fix)

    def setup(self):
        self.handle()
        self.write_spec()

    @staticmethod
    def format_spec_key_value(k, v, width=16):
        hex_k = (k + ':').ljust(width)
        return hex_k + v

    @staticmethod
    def split_spec_key_value(s):
        ns = s.split(':', maxsplit=1)
        return ns[0], ns[1].lstrip()
