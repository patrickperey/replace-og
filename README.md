# replace-og
Disclamier: use at your own risk and with caution, this script has been running at my plotters for a week now and no issues.
Script to replace OG plots by date, as soon as madmax start a copy to destination, it will delete 1 OG plot, thus 'replacing' old plot.
Place into directory as madmax plotter
find line in 'script'
change the find /path/to/plots -name 'plot-k32*' ! -newermt '2021-06-29 10:00:00' -delete -quit

change -newermt '2021-06-29 10:00:00' to the last creation date of OG plot.
For example if you stopped plotting OG polots at 27 june then set it to -newermt '2021-06-27 10:00:00'
syntax is before YYYY-MM-DD HH:MM:SS
