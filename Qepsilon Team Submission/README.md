# Quantum-Natural-Language-Processing-with-lambeq---Quantinuum

## Womanium Quantum Hackathon 2022

## Team Overview -**Qepsilon**
### The team is made up by passionate computer science girls in the tech field, unfortunelty most of team members was not really able to work on the challenge because of having many occupations, but they discovered a lot in the QC world, thanks to womenium who offered us this amazing opportunity.
### Team member who worked on the project : Yousra Farhani
### Other Team members : Able Hagani, Noha Nekmiche


## Project overview

In this project, we used the quantum NLP library lambeq to transform sentences into quantum circuits and classify them by ensuring the rapidity of the process, using the DisCoCat model that helped in classifying and understanding sentences from users input


## How it works

1. By understanding the syntax and the content of words and their order in the senteces they were transformed into string diagrams
2. The string diagram is rewritten and normalized to reduce computational overhead and training time.
3. The string diagram is transformed into a quantum circuit (for QC) or tensor network (for CC), in order to visualise it.
5. Doing classification by training the model by entering different sentences from users input.


## Accuracy
the classifier has 89.34% accuracy

## Setup

1. Install python and pip. 
2. Install required libraries:

           pip install lambeq 
           pip install pytket-qiskit
           pip install ipython  # For data visualization
           pip install pylatexenc
           pip install pytest  # to run tests
   

## Limitations

- The model can have more accuracy by training it with more data, there is no enough doumentation about the lambeq, especially when it comes to the practicing part.

## Acknowledgements
- Challenge description on github
- lambeq documentation
- Some NLP challenges on Github

