#!/usr/bin/env python3

import pytest
import os, os.path
import shutil

def run_and_compare(bash, chapter=None, script=None, output=None, timeout=None, skip_indexes=None, subdir=None):

    if chapter:
        # need to load sitecustomize.py which disables matplotlib, need to overwrite PYTHONPATH temporarily
        script = "PYTHONPATH=%s:tests ./PFTLS_Chapter_%s.py" % (os.environ['PYTHONPATH'], chapter)
        output = "tests/Chapter_%s.stdout" % chapter

    if not script or not output:
        print("Error")

    # change the working directory if set
    if subdir:
        working_dir = os.path.join(os.getcwd(), subdir)
    else:
        working_dir = os.getcwd()
        
    with bash(pwd=working_dir) as shell:
        # get output of script
        if timeout:
            run_output = shell.connection.send(script, timeout=timeout)
        else:
            run_output = shell.connection.send(script)

    # get previously saved contents, remove trailing carriage return
    saved_output = (open(output, 'r').read()).strip()

    # skip specified indexes output comparison
    # FIXME: this is a bit of a hack, needed because we are comparing stdout
    if skip_indexes:
        run_list = run_output.rsplit('\n')
        saved_list = saved_output.rsplit('\n')

        skip_indexes.reverse()
        # delete the lines to avoid
        for index in skip_indexes:
            del run_list[index]
            del saved_list[index]

        # compare the re-joined strings
        assert '\n'.join(run_list) == '\n'.join(saved_list)
        
    else:
        assert run_output == saved_output

def test_Chapter_02(bash):
    run_and_compare(bash, chapter='02')

def test_Chapter_03(bash):
    run_and_compare(bash, chapter='03')
    
def test_Chapter_04(bash):
    run_and_compare(bash, chapter='04')

def test_Chapter_05_01(bash):
    run_and_compare(bash, chapter='05_01')

def test_Chapter_05_02(bash):
    run_and_compare(bash, chapter='05_02')

def test_Chapter_07(bash):
    # skip the line printing the object (changes from run to run)
    # FIXME: this is fragile, could break with code change
    run_and_compare(bash, chapter='07', skip_indexes=[19])

@pytest.mark.skipif(shutil.which("bwa") == None, reason="bwa not installed")
@pytest.mark.skipif(shutil.which("samtools") == None, reason="samtools not installed")
def test_Chapter_08(bash):
    # script needs to run as a command in the "genomes" subdirectory
    run_and_compare(bash, script="../PFTLS_Chapter_08.py -o final.bam -c 'gi|110640213|ref|NC_008253.1|' -s 20 -e 200 e_coli_10000snp.fq", subdir="genomes", output="tests/Chapter_08.stdout")

def test_Chapter_09(bash):
    run_and_compare(bash, chapter='09')

def test_Chapter_10(bash):
    run_and_compare(bash, chapter='10')

def test_Chapter_11(bash):
    run_and_compare(bash, chapter='11')

def test_Chapter_12(bash):
    run_and_compare(bash, chapter='12')

def test_Chapter_13(bash):
    run_and_compare(bash, chapter='13')

def test_Chapter_14_01(bash):
    run_and_compare(bash, chapter='14_01')

def test_Chapter_14_02(bash):
    run_and_compare(bash, chapter='14_02')

def test_Chapter_15(bash):
    run_and_compare(bash, chapter='15')

def test_Chapter_16(bash):
    run_and_compare(bash, chapter='16', timeout=100.0)

def test_Chapter_17(bash):
    run_and_compare(bash, chapter='17')

def test_Chapter_18(bash):
    run_and_compare(bash, chapter='18')

def test_Chapter_19(bash):
    run_and_compare(bash, chapter='18')
    
def test_Chapter_06(bash):
    # run test last, longest-running
    # skip line 6 (object printing)
    # and also last 5 lines in comparison because they are timings which will vary
    run_and_compare(bash, chapter='06', timeout=1000.0, skip_indexes=[6, slice(-5,None)])


    
