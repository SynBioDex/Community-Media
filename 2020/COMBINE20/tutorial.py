import sbol3

# ----------------------------------------------------------------------
# COMBINE 2020 SBOL 3 Tutorial
# October, 2020
#
# This tutorial code goes with the slides at:
#
# https://github.com/SynBioDex/Community-Media/blob/master/2020/IWBDA20/SBOL3-IWBDA-2020.pptx
# ----------------------------------------------------------------------

# TODO: Slide 34 for constraints

# Define a constant that is not defined in pySBOL3
SO_ENGINEERED_REGION = sbol3.SO_NS + '0000804'
SO_ASSEMBLY_SCAR = sbol3.SO_NS + '0001953'

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


# --------------------------------------------------
# Slide 30: Location of a SubComponent
# --------------------------------------------------

# BBa_I13504_sequence (875 bp)
# See https://synbiohub.org/public/igem/BBa_I13504_sequence/1
seq_13504 = ('aaagaggagaaatactagatgcgtaaaggagaagaacttttcactggagttgtcccaattcttgttgaat'
             'tagatggtgatgttaatgggcacaaattttctgtcagtggagagggtgaaggtgatgcaacatacggaaa'
             'acttacccttaaatttatttgcactactggaaaactacctgttccatggccaacacttgtcactactttc'
             'ggttatggtgttcaatgctttgcgagatacccagatcatatgaaacagcatgactttttcaagagtgcca'
             'tgcccgaaggttatgtacaggaaagaactatatttttcaaagatgacgggaactacaagacacgtgctga'
             'agtcaagtttgaaggtgatacccttgttaatagaatcgagttaaaaggtattgattttaaagaagatgga'
             'aacattcttggacacaaattggaatacaactataactcacacaatgtatacatcatggcagacaaacaaa'
             'agaatggaatcaaagttaacttcaaaattagacacaacattgaagatggaagcgttcaactagcagacca'
             'ttatcaacaaaatactccaattggcgatggccctgtccttttaccagacaaccattacctgtccacacaa'
             'tctgccctttcgaaagatcccaacgaaaagagagaccacatggtccttcttgagtttgtaacagctgctg'
             'ggattacacatggcatggatgaactatacaaataataatactagagccaggcatcaaataaaacgaaagg'
             'ctcagtcgaaagactgggcctttcgttttatctgttgtttgtcggtgaacgctctctactagagtcacac'
             'tggctcaccttcgggtgggcctttctgcgtttata')

i13504_seq = sbol3.Sequence('I13504_sequence')
i13504_seq.elements = seq_13504
i13504_seq.encoding = sbol3.SBOL_IUPAC_DNA
i13504.sequences.append(i13504_seq)

loc = sbol3.Range(i13504_seq, 738, 745)
i13504_seq_feat = sbol3.SequenceFeature([loc])
i13504_seq_feat.roles = [SO_ASSEMBLY_SCAR]
i13504.features.append(i13504_seq_feat)


# BBa_B0015_sequence (129 bp)
# From https://synbiohub.org/public/igem/BBa_B0015_sequence/1
seq_B0015 = ('ccaggcatcaaataaaacgaaaggctcagtcgaaagactgggcctttcgttttatctgttgtttgtcggt'
             'gaacgctctctactagagtcacactggctcaccttcgggtgggcctttctgcgtttata')

term_seq = sbol3.Sequence('B0015_sequence')
term_seq.elements = seq_B0015
term_seq.encoding = sbol3.SBOL_IUPAC_DNA
term.sequences.append(term_seq)

# Add the location on to the B0015 SubComponent
loc = sbol3.Range(i13504_seq, 746, 875)
for feature in i13504.features:
    if isinstance(feature, sbol3.SubComponent) and feature.instance_of == term.identity:
        feature.locations.append(loc)


# --------------------------------------------------
# Slide 32: GFP production from expression cassette
# --------------------------------------------------

# TODO: Is the type really SBO_FUNCTIONAL_ENTITY? It is not specified on the slide
i13504_system = sbol3.Component('i13504_system', sbol3.SBO_FUNCTIONAL_ENTITY)
doc.add(i13504_system)

# Make a SubComponent referencing i13504
subcomp1 = sbol3.SubComponent(i13504)
i13504_system.features.append(subcomp1)

# Make a component reference for the GFP in i13504
gfp_feature = None
for feature in i13504.features:
    if isinstance(feature, sbol3.SubComponent) and feature.instance_of == gfp.identity:
        gfp_feature = feature
if gfp_feature is None:
    raise Exception('Could not find GFP subcomponent')
compref1 = sbol3.ComponentReference(subcomp1, gfp_feature)
i13504_system.features.append(compref1)

# GFP Protein
gfp_protein = sbol3.Component('gfp_protein', sbol3.SBO_PROTEIN)
i13504_system.features.append(sbol3.SubComponent(gfp_protein))

# Make the template participation
participation1 = sbol3.Participation([sbol3.SBO_TEMPLATE], compref1)

# Make the product participation
participation2 = sbol3.Participation([sbol3.SBO_PRODUCT], gfp_protein)

# Make the interaction
interaction1 = sbol3.Interaction([sbol3.SBO_GENETIC_PRODUCTION])
interaction1.participations = [participation1, participation2]

i13504_system.interactions.append(interaction1)


# --------------------------------------------------
# Finally, write the data out to a file
# --------------------------------------------------
doc.write('gfp.nt', sbol3.SORTED_NTRIPLES)
