# Flame StripAvidCrap
by Bob Maple (bobm-matchbox [at] idolum.com)

This script is licensed under the Creative Commons Attribution-ShareAlike [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/)

![Flame version](https://img.shields.io/badge/Flame-2023.1+-green)

## What

StripAvidCrap is a Python script for Autodesk Flame 2023.1 and above that
renames sequences removing "Exported.01" (etc) off sequences names
coming from Avid Media Composer AAFs.


## How

Copy into `/opt/Autodesk/shared/python` - if Flame was already running,
use **Rescan Python Hooks** from the **Flame** > **Python** menu.

Select one or more libraries, folders or reels containing sequences,
or select individual sequences, and right-click. There should now be
a new new entry on the context menu called **Project Tools**, and
inside it you will find **Strip Avid Crap**. Run it, and it will walk
through your selected items and rename any sequences it finds, removing
the Avid `.Exported.01` garbage off the ends of the names.

**NOTE** that Strip Avid Crap only looks for sequences at the root level of
the container(s) you select in the case of libraries, folders or reels.
For instance, if you have 3 different folders full of sequences inside a
library, you need to select the 3 folders as opposed to the library.
Similarly, nested folders aren't automatically traversed. This is to
prevent accidentally selecting a large library and and having the system
halt while it's looking through untold numbers of items.
