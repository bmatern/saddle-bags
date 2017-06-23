# This file is part of EMBL-HLA-Submission.
#
# EMBL-HLA-Submission is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# EMBL-HLA-Submission is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with EMBL-HLA-Submission. If not, see <http://www.gnu.org/licenses/>.

import os

import Tkinter, Tkconstants, tkFileDialog, tkMessageBox
from Tkinter import *
from ttk import *

from AlleleSubCommon import *
from ScrolledWindow import VerticalScrolledFrame

# I am using this ScrolledWindow class instead of a Frame.
# This interface is too big for one screen, need a scrollbar.

class AlleleGuiIMGTInputForm(VerticalScrolledFrame):
        
    # Initialize the GUI
    def __init__(self, root):
        
        
        VerticalScrolledFrame.__init__(self, root)
        #Tkinter.Frame.__init__(self, root)
        #super(500, 500)
        root.title("Choose IMGT Submission Options")
        self.parent = root

        button_opt = {'fill': Tkconstants.BOTH, 'padx': 35, 'pady': 5}
        
        # To define the exit behavior.  Save and exit.
        self.parent.protocol('WM_DELETE_WINDOW', self.saveOptions)
        
        self.instructionsFrame = Tkinter.Frame(self.interior)  
        self.instructionText = Tkinter.StringVar()       
        self.instructionText.set('\nThese options are required for an IMGT allele submission.\n'
            + 'Login Credentials will not be stored, but they will be sent to IMGT via\n'
            + 'secure https connection.\n')        
        Tkinter.Label(self.instructionsFrame, width=85, height=6, textvariable=self.instructionText).pack()
        self.instructionsFrame.pack()
        
        #Standard Inputs widths for the form elements
        formInputWidth = 35
        labelInputWidth = 35
                
        # Make a frame to contain the input variables
        # self.interior is defined in the ScrolledWindow class
        self.submissionDetailsInputFrame = Tkinter.Frame(self.interior)

        self.usernameInstrText = Tkinter.StringVar()
        self.usernameInstrText.set('IMGT Username:')
        self.usernameInstrLabel = Tkinter.Label(self.submissionDetailsInputFrame, width=labelInputWidth, height=1, textvariable=self.usernameInstrText).grid(row=0, column=0)
        self.inputUsername = Tkinter.StringVar()
        self.inputUsernameEntry = Tkinter.Entry(self.submissionDetailsInputFrame, width=formInputWidth, textvariable=self.inputUsername).grid(row=0, column=1)

        self.passwordInstrText = Tkinter.StringVar()
        self.passwordInstrText.set('IMGT Password:')
        self.passwordInstrLabel = Tkinter.Label(self.submissionDetailsInputFrame, width=labelInputWidth, height=1, textvariable=self.passwordInstrText).grid(row=1, column=0)
        self.inputPassword = Tkinter.StringVar()
        self.inputPasswordEntry = Tkinter.Entry(self.submissionDetailsInputFrame, width=formInputWidth, textvariable=self.inputPassword, show="*").grid(row=1, column=1)
  
        self.sampleIDInstrText = Tkinter.StringVar()
        self.sampleIDInstrText.set('Sample ID:')
        self.sampleIDinstrLabel = Tkinter.Label(self.submissionDetailsInputFrame, width=labelInputWidth, height=1, textvariable=self.sampleIDInstrText).grid(row=2, column=0)
        self.inputSampleID = Tkinter.StringVar()
        self.inputSampleIDEntry = Tkinter.Entry(self.submissionDetailsInputFrame, width=formInputWidth, textvariable=self.inputSampleID).grid(row=2, column=1)

        self.geneInstrStringVar = Tkinter.StringVar()
        self.geneInstrStringVar.set('Gene:')
        self.geneInstrLabel = Tkinter.Label(self.submissionDetailsInputFrame, width=labelInputWidth, height=1, textvariable=self.geneInstrStringVar).grid(row=3, column=0)
        self.inputGene = Tkinter.StringVar()        
        self.inputGeneEntry = Tkinter.Entry(self.submissionDetailsInputFrame, width=formInputWidth, textvariable=self.inputGene).grid(row=3, column=1)

        self.chooseClassIntVar = IntVar()
        self.chooseClassIntVar.set(1)
        Radiobutton(self.submissionDetailsInputFrame, text="HLA Class I ", variable=self.chooseClassIntVar, value=1).grid(row=4, column=0)
        Radiobutton(self.submissionDetailsInputFrame, text="HLA Class II", variable=self.chooseClassIntVar, value=2).grid(row=4, column=1)

        self.alleleInstrText = Tkinter.StringVar()
        self.alleleInstrText.set('Allele Local Name:')
        self.alleleInstrLabel = Tkinter.Label(self.submissionDetailsInputFrame, width=labelInputWidth, height=1, textvariable=self.alleleInstrText).grid(row=5, column=0)
        self.inputAllele = Tkinter.StringVar() 
        self.inputAlleleEntry = Tkinter.Entry(self.submissionDetailsInputFrame, width=formInputWidth, textvariable=self.inputAllele).grid(row=5, column=1)
        
        
        
        
        # New form stuff
        # Gotta add this to the load/save config nonsense below.
        
        
        # TODO: Can I just load an EMBL accession? I think that is possible.  Easier than filling it in here
        
        
        # TODO: Do I need to specify if it is EMBL / Genbank / The other one?  Probably not.
        # I can require an EMBL code and disregard Genbank.  
        # Radio Buttons?  
        # EMBL / Genbank Accession #
        self.emblAccInstrText = Tkinter.StringVar()
        self.emblAccInstrText.set('EMBL Sequence Accession #:')
        self.emblAccInstrLabel = Tkinter.Label(self.submissionDetailsInputFrame, width=labelInputWidth, height=1, textvariable=self.emblAccInstrText).grid(row=6, column=0)
        self.inputEmblAcc = Tkinter.StringVar() 
        self.inputEmblAccEntry = Tkinter.Entry(self.submissionDetailsInputFrame, width=formInputWidth, textvariable=self.inputEmblAcc).grid(row=6, column=1)

        
        # Release Date
        self.releaseDateInstrText = Tkinter.StringVar()
        self.releaseDateInstrText.set('Release Date:')
        self.releaseDateInstrLabel = Tkinter.Label(self.submissionDetailsInputFrame, width=labelInputWidth, height=1, textvariable=self.releaseDateInstrText).grid(row=7, column=0)
        self.inputReleaseDate = Tkinter.StringVar() 
        self.inputReleaseDateEntry = Tkinter.Entry(self.submissionDetailsInputFrame, width=formInputWidth, textvariable=self.inputReleaseDate).grid(row=7, column=1)
        
        # Reference Details
        # Is this allele in a published paper or not?
        # 1=unpublished, 2=published
        self.publishedReferenceIntVar = IntVar()
        self.publishedReferenceIntVar.set(1)
        
        self.submissionDetailsInputFrame.pack()
 
        
        self.unpublishedReferenceFrame = Tkinter.Frame(self.interior)   
        
        self.referenceInstrText = Tkinter.StringVar()
        self.referenceInstrText.set('\nPlease provide some information about a\npublished paper relevant to this sequence.\n')
        self.referenceInstrLabel = Tkinter.Label(self.unpublishedReferenceFrame, width=70, height=4, textvariable=self.referenceInstrText).pack()#.grid(row=2, column=0)
             
        Radiobutton(self.unpublishedReferenceFrame, text="No Published Reference.", variable=self.publishedReferenceIntVar, value=1).pack()
        self.unpublishedReferenceFrame.pack()

        self.publishedReferenceFrame = Tkinter.Frame(self.interior)
        
        # Radio Button: Published
        Radiobutton(self.unpublishedReferenceFrame, text="Use This Reference:", variable=self.publishedReferenceIntVar, value=2).pack()
        
        # Reference Title
        self.referenceTitleInstrText = Tkinter.StringVar()
        self.referenceTitleInstrText.set('Reference Title:')
        self.referenceTitleInstrLabel = Tkinter.Label(self.publishedReferenceFrame, width=labelInputWidth, height=1, textvariable=self.referenceTitleInstrText).grid(row=1, column=0)
        self.inputReferenceTitle = Tkinter.StringVar() 
        self.inputReferenceTitle = Tkinter.Entry(self.publishedReferenceFrame, width=formInputWidth, textvariable=self.inputReferenceTitle).grid(row=1, column=1)
        
        # Authors
        self.referenceAuthorsInstrText = Tkinter.StringVar()
        self.referenceAuthorsInstrText.set('Reference Authors:')
        self.referenceAuthorsInstrLabel = Tkinter.Label(self.publishedReferenceFrame, width=labelInputWidth, height=1, textvariable=self.referenceAuthorsInstrText).grid(row=2, column=0)
        self.inputReferenceAuthors = Tkinter.StringVar() 
        self.inputReferenceAuthors = Tkinter.Entry(self.publishedReferenceFrame, width=formInputWidth, textvariable=self.inputReferenceAuthors).grid(row=2, column=1)
        
        # Journal
        self.referenceJournalInstrText = Tkinter.StringVar()
        self.referenceJournalInstrText.set('Reference Journal:')
        self.referenceJournalInstrLabel = Tkinter.Label(self.publishedReferenceFrame, width=labelInputWidth, height=1, textvariable=self.referenceJournalInstrText).grid(row=3, column=0)
        self.inputReferenceJournal = Tkinter.StringVar() 
        self.inputReferenceJournal = Tkinter.Entry(self.publishedReferenceFrame, width=formInputWidth, textvariable=self.inputReferenceJournal).grid(row=3, column=1)

        self.publishedReferenceFrame.pack()
               
        # Make a frame to contain the input variables.
        # I had to make 2 of them to organize my gui, maybe I can name this better.
        self.submissionDetailsInputFrame2 = Tkinter.Frame(self.interior)
            
        # /alignment -> defined by IMGT sequence alignment service        
        # In this case, it is the closest known allele.
        self.closestAlleleInstrText = Tkinter.StringVar()
        self.closestAlleleInstrText.set('Closest Known HLA Allele:')
        self.closestAlleleInstrLabel = Tkinter.Label(self.submissionDetailsInputFrame2, width=labelInputWidth, height=1, textvariable=self.closestAlleleInstrText).grid(row=1, column=0)
        self.inputClosestAllele = Tkinter.StringVar() 
        self.inputClosestAllele = Tkinter.Entry(self.submissionDetailsInputFrame2, width=formInputWidth, textvariable=self.inputClosestAllele).grid(row=1, column=1)

        
        
        # Written Description
        # Looks like this is a description of how the sequence differes from closest knnown allele
        self.closestAlleleWrittenDescriptionInstrText = Tkinter.StringVar()
        self.closestAlleleWrittenDescriptionInstrText.set('Differences from Closest Allele:')
        self.closestAlleleWrittenDescriptionInstrLabel = Tkinter.Label(self.submissionDetailsInputFrame2, width=labelInputWidth, height=1, textvariable=self.closestAlleleWrittenDescriptionInstrText).grid(row=2, column=0)
        self.inputClosestAlleleWrittenDescription = Tkinter.StringVar() 
        self.inputClosestAlleleWrittenDescription = Tkinter.Entry(self.submissionDetailsInputFrame2, width=formInputWidth, textvariable=self.inputClosestAlleleWrittenDescription).grid(row=2, column=1)

        
        # DONOR INFORMATION
        
        # Cell ID (cellnum)
        # Wait, is this the same as the sample ID? Should I move the sample ID field down here?
        
        # Ethnic Origin
        
        # Sex
        
        # Cosanguinous (T/F)
        
        # Homozygous (T/F)
        
        # Comments
        
        # Lab of Origin
        
        # Lab Contact
        
        # Cell Availability
        
            # Material Available (T/F)
            
            # Cell Bank (Text)
            
            # Cell Workshop Details
        
        # Alternative HLA DNA Typing
        # Loop? 
        # Dropdown Box with another Entry Field?
        # Yeah Start with them Blank, choose gene from box.
        # Store in globals, but don't write to config..
        
        # Source Serology Typing
        # Maybe the same as DNA typing
        
        # Sequencing Methods
            
        # Primers
        # This is probably a Dropdown with Entry field also.
        
        
        
        self.submissionDetailsInputFrame2.pack()
        
        

        

        # Make a frame for the save options button.
        self.saveOptionsFrame = Tkinter.Frame(self.interior)
        Tkinter.Button(self.saveOptionsFrame, text='Save Options', command=self.saveOptions).grid(row=0, column=0)
        self.saveOptionsFrame.pack()
        
        self.loadOptions()

    # submissionOptions is a dictionary, passed by the parent.
    def loadOptions(self):
        if getConfigurationValue('imgt_username') is not None:
            self.inputUsername.set(getConfigurationValue('imgt_username'))
            
        if getConfigurationValue('imgt_password') is not None:
            self.inputPassword.set(getConfigurationValue('imgt_password'))
            
        if getConfigurationValue('sample_id') is not None:
            self.inputSampleID.set(getConfigurationValue('sample_id'))
            
        if getConfigurationValue('gene') is not None:
            self.inputGene.set(getConfigurationValue('gene'))
            
        if getConfigurationValue('class') is not None:
            if (str(getConfigurationValue('class')) == '1'):
                self.chooseClassIntVar.set(1)
            elif (str(getConfigurationValue('class')) == '2'):
                self.chooseClassIntVar.set(2)
            else:
                raise Exception('Error loading IMGT submission options. Invalid class:' + str(getConfigurationValue('class')))
    
        if getConfigurationValue('allele_name') is not None:
            self.inputAllele.set(getConfigurationValue('allele_name'))
            
        #if getConfigurationValue('choose_project') is not None:
        #    if (str(getConfigurationValue('choose_project')) == '1'):
        #        self.chooseProjectIntVar.set(1)
        #    elif (str(getConfigurationValue('choose_project')) == '2'):
        #        self.chooseProjectIntVar.set(2)
        #    else:
        #        raise Exception('Error loading IMGT submission options. Invalid Project choice:' + str(getConfigurationValue('choose_project')))
            
        #if getConfigurationValue('study_accession') is not None:
        #    self.inputStudyAccession.set(getConfigurationValue('study_accession'))
            
        #if getConfigurationValue('study_name') is not None:
        #    self.inputStudyName.set(getConfigurationValue('study_name'))
            
        #if getConfigurationValue('study_description') is not None:
        #    self.inputStudyShortDescription.set(getConfigurationValue('study_description'))
            
        #if getConfigurationValue('study_abstract') is not None:
        #    self.inputStudyAbstract.set(getConfigurationValue('study_abstract'))
            

    def saveOptions(self):
        # TODO: Save the options to our configuration dictionary
        # Close the window
        if (self.checkOptions()):
            print ('Saving Options....')
            
            assignConfigurationValue('imgt_username', self.inputUsername.get())
            # I store this password so I can use it in the submission
            # I don't ever want to save the password. Make sure it isn't being saved in the config, in AlleleSubCommon.py
            assignConfigurationValue('imgt_password', self.inputPassword.get())
            assignConfigurationValue('sample_id', self.inputSampleID.get())
            assignConfigurationValue('gene', self.inputGene.get())
            assignConfigurationValue('class', str(self.chooseClassIntVar.get()))             
            assignConfigurationValue('allele_name', self.inputAllele.get())
            assignConfigurationValue('choose_project', str(self.chooseProjectIntVar.get()))    
            assignConfigurationValue('study_accession', self.inputStudyAccession.get())                    
            assignConfigurationValue('study_name', self.inputStudyName.get())            
            assignConfigurationValue('study_description', self.inputStudyShortDescription.get())
            assignConfigurationValue('study_abstract', self.inputStudyAbstract.get())
            
            self.parent.destroy() 
            
        else:
            #print('Not ready to save, you are missing options.')
            pass
        
    def checkOptions(self):
        # TODO this method
        print ('Checking options.')

        #chooseProjectIntVar
        
        # Don't check the IMGT Username
        # Don't check the IMGT Password
        
        if (not self.inputSampleID.get()):
            tkMessageBox.showwarning('Missing Form Value',
                'You are missing a Sample ID. Please try again.')
            return False
        
        if (not self.inputGene.get()):
            tkMessageBox.showwarning('Missing Form Value',
                'You are missing a Gene. Please try again.')
            return False
        
        # Don't check the class boolean
        
        if (not self.inputAllele.get()):
            tkMessageBox.showwarning('Missing Form Value',
                'You are missing an Allele Name. Please try again.')
            return False
        
        #if (str(self.chooseProjectIntVar.get()) == '1'):
            # Use Existing Project
        #    if (not self.inputStudyAccession.get()):
        #        tkMessageBox.showwarning('Missing Form Value',
        #            'You are missing a Study Accession number. Please try again.')
        #        return False
            
        #elif(str(self.chooseProjectIntVar.get()) == '2'):
            # Use New Project
        #    if (not self.inputStudyName.get()):
        #        tkMessageBox.showwarning('Missing Form Value',
        #            'You are missing a Study Name. Please try again.')
        #        return False
            
        #    if (not self.inputStudyShortDescription.get()):
        #        tkMessageBox.showwarning('Missing Form Value',
        #           'You are missing a Study Description. Please try again.')
        #        return False
            
            
        #    if (not self.inputStudyAbstract.get()):
        #        tkMessageBox.showwarning('Missing Form Value',
        #            'You are missing a Study Accession number. Please try again.')
        #        return False
            
        #else:
        #    raise Exception ('Unknown value of self.chooseProjectIntVar. I expect 1 or 2. Observed:' + str(self.chooseProjectIntVar)) 

        # All options look good, right?
        return True
    
    
    def closeWindow(self):
        #writeConfigurationFile()

        self.parent.destroy()        
    