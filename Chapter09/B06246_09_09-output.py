# Getting the output file names from processing algorithms

import processing

def proc_output(algorithm):
    for output in processing.Processing.getAlgorithm(algorithm).outputs:
        return output.name

proc_output("grass7:r.aspect")
# 'aspect'

proc_output("qgis:joinattributesbylocation")
# 'OUTPUT'

