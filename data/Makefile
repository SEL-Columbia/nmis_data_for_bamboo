DATA_DIR=$(HOME)/Dropbox/Nigeria/Nigeria\ 661\ Baseline\ Data\ Cleaning/in_process_data/nmis
E=Education
H=Health
W=Water
OF=_Facilities.csv
OL=_LGA.csv
NF=_661_NMIS_Facility.csv
NL=_LGA_level_661.csv
all: $(E)$(OF) $(H)$(OF) $(W)$(OF) $(E)$(OL) $(H)$(OL) $(W)$(OL) 
clean:
	rm *.csv
$(E)$(OF): $(DATA_DIR)/$(E)$(NF)
	cp $(DATA_DIR)/$(E)$(NF) $(E)$(OF) 
$(H)$(OF): $(DATA_DIR)/$(H)$(NF)
	cp $(DATA_DIR)/$(H)$(NF) $(H)$(OF) 
$(W)$(OF): $(DATA_DIR)/$(W)$(NF)
	cp $(DATA_DIR)/$(W)$(NF) $(W)$(OF) 

$(E)$(OL): $(DATA_DIR)/$(E)$(NL)
	cp $(DATA_DIR)/$(E)$(NL) $(E)$(OL) 
$(H)$(OL): $(DATA_DIR)/$(H)$(NL)
	cp $(DATA_DIR)/$(H)$(NL) $(H)$(OL) 
$(W)$(OL): $(DATA_DIR)/$(W)$(NL)
	cp $(DATA_DIR)/$(W)$(NL) $(W)$(OL) 
