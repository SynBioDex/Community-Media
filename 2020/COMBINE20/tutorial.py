import sbol3

# ----------------------------------------------------------------------
# COMBINE 2020 SBOL 3 Tutorial
# October, 2020
#
# This tutorial code goes with the slides at:
#
# https://github.com/SynBioDex/Community-Media/blob/master/2020/IWBDA20/SBOL3-IWBDA-2020.pptx
# ----------------------------------------------------------------------

# TODO: Slide 30 connect to sequence info
# TODO: Slide 32 for interactions
# TODO: Slide 34 for constraints

# Define a constant that is not defined in pySBOL3
SO_ENGINEERED_REGION = sbol3.SO_NS + '0000804'


# Preamble
sbol3.set_homespace('https://synbiohub.org/public/igem/')
doc = sbol3.Document()

# --------------------------------------------------
# Slide 26: GFP expression cassette
# --------------------------------------------------
# Component
# identity: iGEM#I13504
# name: "iGEM 2016 interlab reporter"
# description: "GFP expression cassette used for 2016 iGEM interlab"
# type: SBO:0000251 (DNA)
# role: SO:0000804 (Engineered Region)
print('Creating GFP expression cassette')
i13504 = sbol3.Component('I13504', sbol3.SBO_DNA)
i13504.name = 'iGEM 2016 interlab reporter'
i13504.description = 'GFP expression cassette used for 2016 iGEM interlab'
i13504.roles.append(SO_ENGINEERED_REGION)

# Add the GFP expression cassette to the document
doc.add(i13504)
print(f'Created GFP expression cassette {i13504.identity}')

# --------------------------------------------------
# Slide 28: expression cassette parts
# --------------------------------------------------
# Add the RBS subcomponent
rbs = sbol3.Component('B0034', sbol3.SBO_DNA)
rbs.name = 'RBS (Elowitz 1999)'
rbs.roles.append(sbol3.SO_RBS)
doc.add(rbs)
i13504.features.append(sbol3.SubComponent(rbs))
print(f'Added RBS SubComponent {rbs.identity}')

# Add the GFP subcomponent
gfp = sbol3.Component('E0040', sbol3.SBO_DNA)
gfp.name = 'GFP'
gfp.roles.append(sbol3.SO_CDS)
doc.add(gfp)
i13504.features.append(sbol3.SubComponent(gfp))
print(f'Added GFP SubComponent {gfp.identity}')

# Add the terminator
term = sbol3.Component('B0015', sbol3.SBO_DNA)
term.name = 'double terminator'
term.roles.append(sbol3.SO_TERMINATOR)
doc.add(term)
i13504.features.append(sbol3.SubComponent(term))
print(f'Added Terminator SubComponent {term.identity}')

doc.write('gfp.nt', sbol3.SORTED_NTRIPLES)
