# COP4533-PA1



Student(s):



Leo Graham, UFID: 7279-6525

N/A, UFID: N/A



Run Instructions:



* Matcher:

&nbsp;    - In the command line, navigate to the /src/ directory from the repository. Once in the /src/ directory, run:

&nbsp;    -- python matchingengine.py



* Verifier:

&nbsp;    - In the command line, navigate to the /src/ directory from the repository. Once in the /src/ directory, run:

&nbsp;    -- python verifier.py

* Example Generator:

&nbsp;    The purpose of this program, examplegenerator.py, was to assist in Task C, but can also be a general solution for creating example files. 
&nbsp;    Upon execution, it will create several example files, following the naming convention example_n.in, with n = 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048.
&nbsp;    If you wish to use any of these files as the input for either the generator or verifier, you will need to drag the file into /data/ and manually name it to example.in



&nbsp;    - In the command line, navigate to the /src/ directory from the repository. Once in the /src/ directory, run:

&nbsp;    -- python examplegenerator.py




Assumptions:



* The input file must be located in the /data/ directory, and must be named example.in
* The output file, used for verification in verifier.py, must be located in /data/, and must be named example.out

&nbsp;    - It will automatically populate in /data/ upon running matchingengine.py



Task C:

Matching Generator Graph:
<img width="1496" height="719" alt="image" src="https://github.com/user-attachments/assets/7d009ac6-36f0-4a8a-a853-74bda63f56b8" />
This graph is consistent with the Big-Oh time complexity of the gale-shapley algorithm, O(n^2).

Verifier Graph:
<img width="1399" height="736" alt="image" src="https://github.com/user-attachments/assets/8b200689-eece-4225-af82-ee55fe2d892e" />
This graph is consistent with the Big-Oh time complexity derived from the verification program, O(n^3).

