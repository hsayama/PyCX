# PyCX

PyCX is a Python-based sample code repository for complex systems
research and education.

_Current version: 1.1 (June 2019)_

Sample codes are freely available from the **[Project
website](http://github.com/hsayama/PyCX/)**.

## What is PyCX?

The PyCX project aims to develop an online repository of simple,
crude, yet easy-to-understand Python sample codes for dynamic complex
systems modeling and simulation, including iterative maps, ordinary
and partial differential equations, cellular automata, network
analysis, dynamical networks, and agent-based models. You can run,
read and modify any of its codes to learn the basics of complex
systems modeling and simulation in Python.

The target audiences of PyCX are researchers and students who are
interested in developing their own software to study complex systems
using a general-purpose programming language but do not have much
experience in computer programming.

The core philosophy of PyCX is therefore placed on the simplicity,
readability, generalizability, and pedagogical values of sample
codes. This is often achieved even at the cost of computational speed,
efficiency, or maintainability. For example, PyCX does not use
object-oriented programming paradigms so much, it does not use
sophisticated but complicated algorithm or data structure, it *does*
use global variables frequently, and so on. These choices were
intentionally made based on the author's experience in teaching
complex systems modeling and simulation to non-computer scientists
coming from a wide variety of domains.

For more details of its philosophy and background, see the following
open-access article: Sayama, H. (2013) PyCX: A Python-based simulation
code repository for complex systems education. Complex Adaptive
Systems Modeling 1:2.  http://www.casmodeling.com/content/1/1/2

## How to use it?

1. Install Python 3 (or 2, if you want), numpy, scipy, matplotlib, and
NetworkX.

   Installers are available from the following websites:
   * http://python.org/
   * http://scipy.org/
   * http://matplotlib.org/
   * http://networkx.github.io/
  
   Alternatively, you can use prepackaged Python suites, such as:
   * [Anaconda Individual Edition](https://www.anaconda.com/products/individual)

   The codes were tested using Anaconda Individual Edition of Python 3.7
and 2.7 on their Spyder and Jupyter Notebook environments.

2. Choose a PyCX sample code of your interest.

3. Run it. To run a dynamic, interactive simulation, make sure you have [pycxsimulator.py](https://github.com/hsayama/PyCX/blob/master/pycxsimulator.py).

4. Read the code to learn how the model was implemented.

5. Change the code as you like.

*Note for Spyder users:* Dynamic simulations may cause a conflict with Spyder's own graphics backend. In such a case, go to "Run" -> "Configuration per file" and select "Execute in an external system terminal".

*Note for Jupyter Notebook users:* You can run PyCX codes by entering "%run sample-code-name" in your Notebook.

## Revision history

### What's new in version 1.1?

* Matplotlib's backend issue has been resolved by Steve Morgan for Mac users.

* MatplotlibDeprecationWarning has been suppressed (particularly for examples that use subplots).

* NetworkX's "node" attribute of a Graph object has been renamed as "nodes" to be compatible with NetworkX 2.

### What's new in version 1.0?

* All the codes, including pycxsimulator.py, were updated to be compatible with both Python 2.7 and Python 3.7. They can run in both languages with no modification. Special thanks to [Prof. Toshi Tanizawa](http://www.ee.kochi-ct.ac.jp/~tanizawa/) at the National Institute of Technology, Kochi College!

* Several bug fixes were applied to pycxsimulator.py's GUI so that it works more robustly within the IPython environment.

* Codes for network modeling and analysis were updated to be compatible with NetworkX 2.

* The coding style was simplified to be more readable and more consistent with the author's [OpenSUNY Textbook](http://tinyurl.com/imacsbook) style.

* The file names of sample codes were updated so that all codes start with the following prefix:
   * "ds-": for low-dimensional dynamical systems
   * "dynamic-": for demonstration of how to use pycxsimulator.py
   * "ca-": for cellular automata
   * "pde-": for partial differential equations
   * "net-": for network models
   * "abm-": for agent-based models

* Some new examples were added, including: Hopfield networks, simple swarming, network attack experiment, and population-ecomony interactions.

* Minor bug fixes were applied to examples of cascading failure, network communities, etc.

### What was in previous versions 0.3/0.31/0.32?

* Ver. 0.3:
     - Przemyslaw Szufel and Bogumil Kaminski at the Warsaw School of
       Economics made a substantial improvement to pycxsimulator.py, implementing interactive control of model and
       visualization parameters.
     - Several additional sample codes were added.

* Ver. 0.31:
     - ttk was used as a graphics backend instead of Tix, so that Mac
       users could run the sample codes without installing Tix.

* Ver. 0.32: 
    - pycxsimulator.py's GUI was updated with several bug
      fixes by Toshi Tanizawa and Alex Hill.
    - Sample codes used in the author's [OpenSUNY Textbook](http://tinyurl.com/imacsbook) were included in the
      "textbook-sample-codes" subfolder.

## Questions? Comments? Send them to sayama@binghamton.edu.

* [Old project website](http://pycx.sourceforge.net/)
