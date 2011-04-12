#!/usr/bin/env python

#import pudb; pudb.set_trace()
import os,sys

SETUPFILECONST = 'from setuptools import setup,find_packages\n' + \
                 '\n' + \
                 'setup(\n' + \
                 '    name="{name}",\n' + \
                 '    version="0.1",\n' + \
                 '    description="",\n' + \
                 '    packages=find_packages(),\n'

ENTRYPOINTS = '    entry_points=\n' + \
              '        """\n' + \
              '        [console_scripts]\n' + \
              '        {script_str} = {script_main_str}\n' + \
              '        """\n'

ENDCONST = '    )'

def main():
    if len(sys.argv) != 2:
        print("please just tell me the name of the program")
    # find the main() function...
    script_main = None
    for root,dirs,files in os.walk(os.getcwd()):
        for source_file in files:
            f = open(os.path.join(root,source_file))
            a = f.read()
            f.close()
            if "def main():" in a:
                script_main = "{0}.{1}:main".format(root.split("/")[-1], source_file.split('.')[0]) 
    result = SETUPFILECONST.format(name=sys.argv[1])
    if script_main is not None:
        result += ENTRYPOINTS.format(script_str=sys.argv[1], script_main_str=script_main)
    result += ENDCONST
    f = open("setup.py", 'w')
    f.write(result)
    f.close()


if __name__=="__main__":
    main()
