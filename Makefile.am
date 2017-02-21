AUTOMAKE_OPTIONS = foreign

SUBDIRS = po utils

EXTRA_DIST = autogen.sh config.rpath exceptions.h gettext.h tconsole.h tconsole.spec thread.h util.h

sbin_PROGRAMS = tconsole
tconsole_SOURCES = tconsole.cpp thread.cpp util.cpp

ACLOCAL_AMFLAGS = -I m4
