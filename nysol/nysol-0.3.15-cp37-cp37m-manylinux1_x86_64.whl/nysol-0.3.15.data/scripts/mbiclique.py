#!python
# -*- coding: utf-8 -*-
import sys
import nysol.util.margs as margs
import nysol.take as nt

args=margs.Margs(sys.argv,"ei=,ef=,o=,l=,u=,-edge,-rp","ei=")
nt.mbiclique(**args.kvmap()).run(msg="on")

