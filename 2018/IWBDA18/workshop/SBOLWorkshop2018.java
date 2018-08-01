package org.sbolstandard.core2.examples;

import java.io.IOException;
import java.net.URI;
import java.util.ArrayList;

import org.sbolstandard.core2.Activity;
import org.sbolstandard.core2.Collection;
import org.sbolstandard.core2.Component;
import org.sbolstandard.core2.ComponentDefinition;
import org.sbolstandard.core2.Implementation;
import org.sbolstandard.core2.Plan;
import org.sbolstandard.core2.RestrictionType;
import org.sbolstandard.core2.SBOLConversionException;
import org.sbolstandard.core2.SBOLDocument;
import org.sbolstandard.core2.SBOLReader;
import org.sbolstandard.core2.SBOLValidate;
import org.sbolstandard.core2.SBOLValidationException;
import org.sbolstandard.core2.Sequence;
import org.sbolstandard.core2.SequenceAnnotation;
import org.sbolstandard.core2.SequenceOntology;
import org.sbolstandard.core2.TopLevel;
import org.synbiohub.frontend.IdentifiedMetadata;
import org.synbiohub.frontend.SynBioHubException;
import org.synbiohub.frontend.SynBioHubFrontend;

public class SBOLWorkshop2018 {
	
	public static String version = "1";
	
	public static int len(SBOLDocument sbolDocument) {
		int length = 0;
		length += sbolDocument.getActivities().size();
		length += sbolDocument.getAgents().size();
		length += sbolDocument.getAttachments().size();
		length += sbolDocument.getCollections().size();
		length += sbolDocument.getCombinatorialDerivations().size();
		length += sbolDocument.getComponentDefinitions().size();
		length += sbolDocument.getImplementations().size();
		length += sbolDocument.getModels().size();
		length += sbolDocument.getModuleDefinitions().size();
		length += sbolDocument.getPlans().size();
		length += sbolDocument.getSequences().size();

		return length;
	}

	public static void printCounts(SBOLDocument sbolDocument) {
		System.out.println("Activity......................" + sbolDocument.getActivities().size());
		System.out.println("Agents........................" + sbolDocument.getAgents().size());
		System.out.println("Attachment...................." + sbolDocument.getAttachments().size());
		System.out.println("Collection...................." + sbolDocument.getCollections().size());
		System.out.println("CombinatorialDerivation......." + sbolDocument.getCombinatorialDerivations().size());
		System.out.println("ComponentDefinition..........." + sbolDocument.getComponentDefinitions().size());
		System.out.println("Implementation................" + sbolDocument.getImplementations().size());
		System.out.println("Model........................." + sbolDocument.getModels().size());
		System.out.println("ModuleDefinition.............." + sbolDocument.getModuleDefinitions().size());
		System.out.println("Plans........................." + sbolDocument.getPlans().size());
		System.out.println("Sequence......................" + sbolDocument.getSequences().size());
		System.out.println("---");
		System.out.println("Total........................." + len(sbolDocument));
	}

	public static void compile(SBOLDocument sbolDocument,ComponentDefinition componentDefinition) throws SBOLValidationException {
		for (Component component : componentDefinition.getComponents()) {
			SequenceAnnotation sa = componentDefinition.getSequenceAnnotation(component);
			if (sa==null) {
				sa = componentDefinition.createSequenceAnnotation(component.getDisplayId()+"_annot", "location");
				sa.setComponent(component.getIdentity());
			}
		}
		int start = 1;
		String elements = "";
		for (Component component : componentDefinition.getSortedComponents()) {
			Sequence seq = component.getDefinition().getSequenceByEncoding(Sequence.IUPAC_DNA);
			int end = start + seq.getElements().length()-1;
			SequenceAnnotation sa = componentDefinition.getSequenceAnnotation(component);
			componentDefinition.removeSequenceAnnotation(sa);
			sa = componentDefinition.createSequenceAnnotation(component.getDisplayId()+"_annot", "range", 
					start, end);
			start = end + 1;
			sa.setComponent(component.getIdentity());
			elements += seq.getElements();
		}
		Sequence seq = sbolDocument.createSequence(componentDefinition.getDisplayId()+"_seq", version, elements, Sequence.IUPAC_DNA);
		componentDefinition.addSequence(seq);
	}

	public static void main(String[] args) throws SBOLValidationException, IOException, SBOLConversionException, SynBioHubException {	

		/* Getting a Device from an SBOL Compliant XML */

		// Start a new SBOL Document to hold the device
		// TODO: create a new SBOLDocument and set create defaults to true

		// Set your default URI prefix. All new SBOL objects will be created in this namespace
		// TODO

		// Create a new device
		// TODO
		
		// Load some genetic parts taken from the Cello paper
		// TODO: read parts.xml

		// Explore document contents. Notice it is composed of
		// componentDefinitions and sequences
		// TODO: loop over all top-levels and print their identities

		// Import these objects into your Document
		// TODO: copy these parts into your document

		// Retrieve an object from the Document using its uniform resource identifier (URI)
		// TODO: get the promoters collection

		// A Collection contains a list of URI references to objects, not the object themselves
		// TODO: print the identities of all members of the collection

		// Retrieve a component, using its full URI
		// TODO: get the pPhlF promoter from your document

		// Review the BioPAX and Sequence Ontology terms that describe this component
		// TODO: print this promoters types and roles

		/* Getting a Device from Synbiohub */

		// Start an interface to the part shop
		// TODO: create a SynBioHubFrontend for https://synbiohub.org

		// Search for records from the interlab study
		// TODO: get all matching component definitions that include "interlab" in the name

		// Import the medium device into the user's Document
		// TODO: get the Medium_2016Interlab and copy it into your document

		// Explore the new parts
		// TODO: print all top-level identities

		/* Extracting a ComponentDefinition from a Pre-existing Device */

		// Extract the medium strength promoter
		// TODO: get the BBa_J23106 promoter from your document

		// Get parts for a new circuit
		// TODO: Q2 rbs, LuxR cds, and ECK120010818 terminator

		// Assemble a new gene
		my_device.createSequenceConstraint("constraint1", RestrictionType.PRECEDES, medium_strength_promoter.getIdentity(), rbs.getIdentity());
		// TODO: add sequence constraints from rbs to cds AND cds to terminator

		// Annotate the target construct with a Sequence Ontology term
		// TODO: add role of Engineered Region

		// Explore the newly assembled gene
		// TODO: print the displayIds of all your components

		compile(doc,my_device);
		Sequence seq = my_device.getSequenceByEncoding(Sequence.IUPAC_DNA);
		System.out.println(seq.getElements());
		System.out.println("");

		/* Managing a Design-Build-Test-Learn workflow */

		Activity workflow_step_1 = doc.createActivity("build_1",version);
		// TODO: create a build_2, test_1, and analysis_1 activity

		Plan workflow_step_1_plan = doc.createPlan("gibson_assembly",version);
		// TODO: create a transformation, a promoter_characterization, and a parameter_optimization plan

		workflow_step_1.createAssociation("association",URI.create("mailto:jdoe@my_namespace.org")).setPlan(workflow_step_1_plan.getIdentity());
		// TODO: associate agent "mailto:jdoe@my_namespace.org" and "transformation" plan to step_2 
		// TODO: associate agent "http://sys-bio.org/plate_reader_1" and "promoter_characterization" plan to step_3 
		// TODO: associate agent "http://tellurium.analogmachine.org" and "parameter_optimization" plan to step_4 

		Implementation gibson_mix = doc.createImplementation("gibson_mix", version);
		gibson_mix.setBuilt(my_device);
		gibson_mix.addWasGeneratedBy(workflow_step_1.getIdentity());
		workflow_step_1.createUsage("usage", my_device.getIdentity());

		Collection clones = doc.createCollection("clones",version);
		Implementation clone1 = doc.createImplementation("clone1", version);
		clone1.setBuilt(my_device);
		clones.addMember(clone1.getIdentity());
		Implementation clone2 = doc.createImplementation("clone2", version);
		clone2.setBuilt(my_device);
		clones.addMember(clone2.getIdentity());
		Implementation clone3 = doc.createImplementation("clone3", version);
		clone3.setBuilt(my_device);
		clones.addMember(clone3.getIdentity());
		clones.addWasGeneratedBy(workflow_step_2.getIdentity());
		workflow_step_2.createUsage("usage", gibson_mix.getIdentity());

		// TODO: create a collection "experiment1" that is generated by step_3, using clones collection

		// TODO: create a collection "analysis1" that is generated by step_4 using experiment1 collection

		// Validate the Document
		// TODO: validate the document and print any errors found

		/* Uploading the Device back to SynBioHub */

		// TODO: Need to provide your credentials
		String user_name = "<USERNAME>";
		String password = "<PASSWORD>";
		// TODO: login to SynBioHub

		// Upon submission, the Document will be converted to a Collection with the following properties
		// The new Collection will have a URI that conforms to the following pattern:
		// https://synbiohub.org/user/<USERNAME>/<DOC.DISPLAYID>/<DOC.DISPLAYID>_collection
		String displayId = "my_device";
		String name = "my device";
		String description = "a description of the cassette";
		// TODO: create a collection on SynBioHub

		// TODO: need to fill in your path
		String attachment_path = "<PATH>/results.txt";

		// Attach raw experimental data to the Test object here. Note the pattern
		// TODO: attach this file to "experiment1" on SynBioHub 

		// Attach processed experimental data here
		// TODO: need to fill in your path
		String other_attachement_path = "<PATH>/results.txt";
		// TODO: attach this file to "analysis1" on SynBioHub 

		System.out.println("Successfully uploaded");

	}
}
