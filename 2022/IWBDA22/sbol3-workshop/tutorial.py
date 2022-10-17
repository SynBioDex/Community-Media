import sbol3

# ----------------------------------------------------------------------
# COMBINE 2020 SBOL 3 Tutorial
# October, 2020
#
# This tutorial code goes with the slides at:
#
# https://github.com/SynBioDex/Community-Media/blob/master/2020/COMBINE20/SBOL3-COMBINE-2020.pptx
# ----------------------------------------------------------------------

# Define a constant that is not defined in pySBOL3
SO_ENGINEERED_REGION = sbol3.SO_NS + '0000804'
SO_ASSEMBLY_SCAR = sbol3.SO_NS + '0001953'

# Set the default namespace for new objects and create a document


# --------------------------------------------------
# Slide 26: GFP expression cassette
# --------------------------------------------------
# Component
# identity: iGEM#I13504
# name: "iGEM 2016 interlab reporter"
# description: "GFP expression cassette used for 2016 iGEM interlab"
# type: SBO:0000251 (DNA)
# role: SO:0000804 (Engineered Region)


# Add the GFP expression cassette to the document


# --------------------------------------------------
# Slide 28: expression cassette parts
# --------------------------------------------------
# Add the RBS subcomponent


# Add the GFP subcomponent


# Add the terminator



# --------------------------------------------------
# Slide 30: Location of a SubComponent
# --------------------------------------------------

# BBa_I13504_sequence (875 bp)
# See https://synbiohub.org/public/igem/BBa_I13504_sequence/1



# BBa_B0015_sequence (129 bp)
# From https://synbiohub.org/public/igem/BBa_B0015_sequence/1


# Add the location on to the B0015 SubComponent


# pySBOL3 does not yet have an easy way to locate features based on
# arbitrary criteria so we have to loop over the list to find the
# SubComponent we are looking for



# --------------------------------------------------
# Slide 32: GFP production from expression cassette
# --------------------------------------------------


# Make a SubComponent referencing i13504


# pySBOL3 does not yet have an easy way to locate features based on
# arbitrary criteria so we have to loop over the list to find the
# SubComponent we are looking for


# Make a component reference for the GFP in i13504


# GFP Protein


# Make the template participation


# Make the product participation


# Make the interaction



# --------------------------------------------------
# Slide 34: Example: concatenating & reusing components
# --------------------------------------------------

# Left hand side of slide: interlab16device1


# Right hand side of slide: interlab16device2


# --------------------------------------------------
# Finally, write the data out to a file
# --------------------------------------------------
