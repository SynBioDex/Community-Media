
# coding: utf-8

# --Introduction--
# 
# 1. Create an account on SynBioHub
# 2. Make sure you've downloaded `parts.xml` and it is placed somewhere convenient on your computer.
# 3. Make sure you've downloaded `results.txt` and it is placed somewhere convenient on your computer.
# 4. Install SBOL library in language of choice

# --Getting a Device from an SBOL Compliant XML--


from sbol import *

# Set the default namespace (e.g. “http://my_namespace.org”)

# Create a new SBOL document

# Load some generic parts from `parts.xml` into another Document

# Copy the parts from `parts.xml` into your document. 
# Be sure to specify the original namespace `http://examples.org`


# --Getting a Device from Synbiohub--



# Start an interface to igem’s public part shop on SynBioHub. Located at `https://synbiohub.org/public/igem`

# Search the part shop for parts from the iGEM interlab study using the search term `interlab`

# Import the medium strength device into your document


# --Extracting ComponentDefinitions from a Pre-existing Device--




# Extract the medium strength promoter `BBa_J23106` from your document.

# Extract the ribosomal binding site (rbs) `Q2` from your document. 

# Extract the coding region (cds) `LuxR` from your document.

# Extract the terminator `ECK120010818` from your document.


# --Creating a New Device--




# Create a new empty device named `my_device`

# Assemble the new device from the promoter, rbs, cds, and terminator from above.

# Set the role of the device with the Sequence Ontology term `gene`

# Compile the sequence for the new device


# --Managing a Design-Build-Test-Learn Workflow--




# Create a new design in your document called `my_design`. 

# Set the structure of the design to `my_device` from above, and the function of the device to
# `None` (not covered in this tutorial)

# Create three Activities [‘build`, `test`, `analysis`]

# Create Plans for each Activity: set the`build` plan to `transformation`, the `test` plan
# to `promoter_characterization`, and the `analysis` plan to `parameter_optimization`

# Temporarily disable auto-construction of URIs (For setting Agent URIs)

# Set Agents for each Activity: set the `build` agent to `mailto:jdoe@example.com`, the `test` agent
# to `http://sys-bio.org/plate_reader_1`, and the `analysis` agent to `http://tellurium.analogmachine.org`

# Re-enable auto-construction of URIs

# Add the three activities to your document.

# Generate a build for your design out of your `build` activity. Name the result of the build step `transformed_cells`.

# Generate a test for your build out of your `test` activity. Name the test `my_experiment`.

# Generate an analysis of your test out of your `analysis` activity. Name the analysis `my_analysis`.


# --Uploading the Device Back to SynBioHub--



# Connect to your account on SynBioHub

# Give your document a displayId, name, and description
# (e.g. `my_device`, `my device`, `a newly characterized device`)

# Submit the document to the part shop


# Your document will now be available on your account at
# `https://synbiohub.org/user/<USERNAME>/<DOC.DISPLAYID>/<DOC.DISPLAYID>_collection`

# Attach the experimental results file `results.txt` to `my_experiment` from above

