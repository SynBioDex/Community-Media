#!/usr/bin/env python
# coding: utf-8

# # IWBDA 2022 SBOL 3 Tutorial
# 
# ### October 2022
# This tutorial code goes with the slides at:
# 
# https://github.com/SynBioDex/Community-Media/blob/master/2022/IWBDA22/sbol3-workshop/pySBOL3-IWBDA-2022.pptx

# Import the modules

# In[ ]:


from sbol3 import *
from sbol_utilities.calculate_sequences import compute_sequence
from sbol_utilities.component import *
import tyto


# Set the default namespace for new objects and create a document

# In[ ]:


set_namespace('https://synbiohub.org/public/igem/')
doc = Document()


# # Slide 26: GFP expression cassette
# Construct a simple part and add it to the Document.
# 
# Component  
# identity: iGEM#I13504  
# name: "iGEM 2016 interlab reporter"  
# description: "GFP expression cassette used for 2016 iGEM interlab"  
# type: SBO:0000251 (DNA)  
# role: SO:0000804 (Engineered Region)  
# 
# Which properties are required?  Which properties behave as lists?

# In[ ]:


i13504 = Component('i13504', SBO_DNA)
i13504.name = 'iGEM 2016 interlab reporter'
i13504.description = 'GFP expression cassette used for 2016 iGEM interlab study'
i13504.roles.append(tyto.SO.engineered_region)


# Add the GFP expression cassette to the document

# In[ ]:


doc.add(i13504)


# # Slide 28: expression cassette parts
# Here we will create a part-subpart hierarchy. We will also start using (SBOL-Utilities)[https://github.com/synbiodex/sbol-utilities] to make it easier to create parts and to assemble those parts into a hierarchy.
# 
# First, create the RBS component...
# 
# Component  
# identity: B0034  
# name: RBS (Elowitz 1999)

# In[ ]:


b0034, b0034_seq = doc.add(rbs('B0034', sequence='aaagaggagaaa', name='RBS (Elowitz 1999)'))


# Next, create the GFP component
# 
# identity: E0040  
# name: GFP

# In[ ]:


e0040_sequence = 'atgcgtaaaggagaagaacttttcactggagttgtcccaattcttgttgaattagatggtgatgttaatgggcacaaattttctgtcagtggagagggtgaaggtgatgcaacatacggaaaacttacccttaaatttatttgcactactggaaaactacctgttccatggccaacacttgtcactactttcggttatggtgttcaatgctttgcgagatacccagatcatatgaaacagcatgactttttcaagagtgccatgcccgaaggttatgtacaggaaagaactatatttttcaaagatgacgggaactacaagacacgtgctgaagtcaagtttgaaggtgatacccttgttaatagaatcgagttaaaaggtattgattttaaagaagatggaaacattcttggacacaaattggaatacaactataactcacacaatgtatacatcatggcagacaaacaaaagaatggaatcaaagttaacttcaaaattagacacaacattgaagatggaagcgttcaactagcagaccattatcaacaaaatactccaattggcgatggccctgtccttttaccagacaaccattacctgtccacacaatctgccctttcgaaagatcccaacgaaaagagagaccacatggtccttcttgagtttgtaacagctgctgggattacacatggcatggatgaactatacaaataataa'
e0040, _ = doc.add(cds('E0040', sequence=e0040_sequence, name='GFP'))


# Finally, create the terminator
# 
# identity: B0015  
# name: double terminator

# In[ ]:


b0015_sequence = 'ccaggcatcaaataaaacgaaaggctcagtcgaaagactgggcctttcgttttatctgttgtttgtcggtgaacgctctctactagagtcacactggctcaccttcgggtgggcctttctgcgtttata'
b0015, _ = doc.add(terminator('B0015', sequence=b0015_sequence, name='double terminator'))


# Now construct the part-subpart hierarchy and order the parts: RBS before CDS, CDS before terminator

# In[ ]:


order(b0034, e0040, i13504)
order(e0040, b0015, i13504)


# # Slide 30: Location of a SubComponent
# 
# Here we add base coordinates to SubComponents.
# 
# But first, use `compute_sequence` to get the full sequence for the BBa_I13504 device 
# 
# See http://parts.igem.org/Part:BBa_I13504

# In[ ]:


i13504_seq = compute_sequence(i13504)


# `compute_sequence` added `Range`s to the subcomponents. Check one of those ranges to see that the values are what we expect.
# 
# The expected range of the terminator is (733, 861).

# In[ ]:


b0015_subcomponent = next(f for f in i13504.features if f.instance_of == b0015.identity)
b0015_range = b0015_subcomponent.locations[0]
print(f'Range of {b0015.display_name}: ({b0015_range.start}, {b0015_range.end})')


# # Slide 32: GFP production from expression cassette
# In this example, we will create a system representation that includes DNA, proteins, and interactions.
# 
# First, create the system representation.  `functional_component` creates this for us.
# 
# Component  
# identity: i13504_system

# In[ ]:


i13504_system = functional_component('i13504_system')
doc.add(i13504_system)


# The system has two physical subcomponents, the expression construct and the expressed GFP protein. We already created the expression construct. Now create the GFP protein.
# `ed_protein` creates an "externally defined protein"

# In[ ]:


gfp = add_feature(i13504_system, ed_protein('https://www.fpbase.org/protein/gfpmut3/', name='GFP'))


# Now create the part-subpart hierarchy.

# In[ ]:


i13504_subcomponent = add_feature(i13504_system, i13504)


# Use a ComponentReference to link SubComponents in a multi-level hierarchy

# In[ ]:


e0040_subcomponent = next(f for f in i13504.features if f.instance_of == e0040.identity)
e0040_reference = ComponentReference(i13504_subcomponent, e0040_subcomponent)
i13504_system.features.append(e0040_reference)


# Make the Interaction.
# 
# Interaction:  
# type: SBO:0000589 (genetic production)
# 
# Participation:  
# role: SBO:0000645 (template)  
# participant: e0040_reference  
# 
# Participation:  
# role: SBO:0000011 (product)  
# participant: gfp_subcomponent  

# In[ ]:


add_interaction(tyto.SBO.genetic_production,
                participants={gfp: tyto.SBO.product, e0040_reference: tyto.SBO.template})


# ## Validate the document
# `Document.validate` returns a validation report. If the report is empty, the document is valid.

# In[ ]:


report = doc.validate()
if report:
    print('Document is not valid')
    print(f'Document has {len(report.errors)} errors')
    print(f'Document has {len(report.warnings)} warnings')
else:
    print('Document is valid')


# # Finally, write the data out to a file

# In[ ]:


doc.write('i13504.nt', file_format=SORTED_NTRIPLES)

