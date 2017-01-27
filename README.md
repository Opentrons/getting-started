# Getting Started with Opentrons API

The following are some Jupyter Notebooks that aim to explain the API through interactive examples. You can start using Jupyter notebooks by:

1. [Installing the Anaconda-Navigator](https://www.continuum.io/downloads) **Python 3.5 version** (not 2.7)
2. Running the application Anaconda-Navigator once installed
3. Select the `Launch` button under "Jupyter Notebook"

> Please note that if you are viewing these on GitHub, the pages render differently than when running in Jupyter so some things look a little weird.

# Tutorials

### Setup
1. [Jupyter and API](Setup/Jupyter and API.ipynb)
2. [Setup Containers](Setup/Setup Containers.ipynb)
3. [Setup Instruments](Setup/Setup Instruments.ipynb)
4. [Setup Robot](Setup/Setup Robot.ipynb)

### Commands
1. [Tips](Commands/Tips.ipynb)
2. [Tips Iterating](Commands/Tips Iterating.ipynb)
3. [Liquid Control](Commands/Liquid Control.ipynb)
4. [Moving](Commands/Moving.ipynb)

### Hello Opentrons

```python

from opentrons import containers, instruments

tiprack = containers.load('tiprack-200ul', 'A1')
plate = containers.load('96-flat', 'B1')

pipette = instruments.Pipette(axis='b', max_volume=200)

pipette.pick_up_tip(tiprack['A1'])
pipette.aspirate(100, plate['A1'])
pipette.dispense(100, plate['A2'])
pipette.drop_tip(tiprack['A1'])
```

### Human Readable

The design goal of the Opentrons API is to make code readable and easy to understand. If we were to read the above code example as if it were in plain English, it would look like the following:

```
Import the Opentrons API's containers and instruments.

Load a 200uL tip rack, placing it in slot `A1`, and name it "tiprack".
Load in a 96 well plate, placing it in slot `B1`, and name it "plate".

Create a 200uL pipette, attach it to axis `b` on the robot, and name it "pipette".

Pick up a tip from the tiprack's `A1` position.
Aspirate 100uL from the plate's `A1` well.
Dispense 100uL to the plate's `A2` well.
Drop the tip back to the tiprack's `A1` position.
```
