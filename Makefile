# Makefile for source rpm: rdesktop
# $Id$
NAME := rdesktop
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
