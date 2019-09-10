# Coordinate_wRandomSafeguard
Python-based maze solving algorithm for a mouse-robot, created for my introductory course in Python.

I was asked to create a random-guessing algorithm that would allow a mouse-robot (Raspbian, 3D print chassis) to traverse a given maze. I completed the algorithm before the allotted due date and decided to attempt a more efficient algorithm. I created an abitrary set of units based on wheel rotations/time to turn the maze into a coordinate plane. This code attempts to solve by using a coordinate system to navigate to maze center.

Due to time I was unable to finish the algorithm, so it generally works in the starting quadrant (Q2) but falters in other quadrants. To make it usable for demonstration, I had the code resort to random guessing if the coordinate system fails.
