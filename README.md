This projects checks to see whether a sink (represented by an uppercase letter A-Z) is connected to the source (represented by '*') through a pipe system.  Two pipes are connected if they share a common edge
(for example, '╔' and '╗' are connected through a shared edge whereas '╝' and '╚' are not connected through a shared edge).  The sinks and the source can be connected through all four of it's sides  (For
example, '╔AC' is properly connected).  This program reads from an input file the x and y coordinates of all of the pipes, sinks, and the source, and then returns in alphabetical order a string of all the
pipes that are connected properly to the source.  This program uses recursion to check to see if the sink is connected to the source.
