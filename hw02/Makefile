# Assignment data
## TA's CSID
TAID = benself
## assignment number
ASGN = CS345-HW2
## files to submit
SUBM = hw2.zip

SOURCES = hw2.1.lisp \
          hw2.2.lisp \
          hw2.3.lisp \
          hw2.4.lisp \
          hw2.5.lisp \
          ec.lisp

# Normal make rules
.PHONY: all submit clean

all: hw2.zip submit

hw2.zip: $(SOURCES)
	zip $@ $^

clean:
	rm -f hw2.zip

# Don't change this part between assignments
submit: $(SUBM)
	turnin --submit $(TAID) $(ASGN) $(SUBM)