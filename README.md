# Coordinate_wRandomSafeguard
  Python-based maze solving algorithm for a mouse-robot, created for my introductory course in Python.

  I was asked to create a random-guessing algorithm that would allow a mouse-robot (Raspbian, 3D print chassis) to traverse a given maze. I completed the algorithm before the allotted due date and decided to attempt a more efficient path algorithm. I created an abitrary set of units based on wheel rotations/time to turn the maze into a coordinate plane. This code attempts to solve by using a coordinate system to navigate to maze center.

## Primary Existing Issues
  Due to time I was unable to finish the algorithm, so it generally works in the starting quadrant (Q2) but falters in other quadrants. There is some way that my program falls out of all "if" branches and it would randomly stop. To make it usable for demonstration during the contest, I had the code resort to random guessing if the coordinate system failed.

## Project Result
  Despite my difficulties I am happy to say that my robot completed the maze in the fastest time out of both my class section, and the other class section for the year I took this course. It took a route directly to the center of the maze, and you can view my LinkedIn post about it [here](https://www.linkedin.com/posts/alexabaldon_win-python-robot-activity-6478368903033606144-O-9c).

  After this contest I was invited by my school's IEEE chapter to participate in the IEEE Student Activity Conference for 2019 where I, in a team of first-year women, competed in the SumoBot kit competition.

  I also was approached by the executives of Nexus Valley Solutions LLC, including my professor for the course, to help them with some intern work. NVS provides a curriculum to teach kids Python using the same mouse-robots (Mazey, provided by NVS) we used.

  I created technical tutorials through Python applications. These programs walked through the process of how to start from absolute basic movement to a working random guesser algorithm with a function library. Each application iterated the previous, trying to emulate how the student may build their program. It also contained comments explaining pros and cons of each iteration, possible improvements to each iteration, etc.

## Next Steps..?
Being that the course/project is over, updating this is not a priorty but should I return to it I'd like to
* Give the random algorithm "safeguard" it's own file and refer to it using a function
* Repair the coordinate pathing algorithm
    * Modularize the code using functions to increase readability and ease of modification (There is a lot of redundant code)
