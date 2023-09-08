#!/bin/env python

# StripAvidCrap.py by Bob Maple (bobm at idolum dot com)
#
# Takes a selection of libraries, folders, reels or sequences and renames
# all sequences found, removing 'Exported.01' crap from the end.
# Only looks for sequences at the root level of any selected libraries, folders.
#
# Note that if you run this on a reel on the Desktop, the names won't visually update
# until you do something else in the UI (click something, etc)

def get_media_panel_custom_ui_actions():

  def StripAvidCrap_go(sel):
    import flame
    work_count = 0

    # print( "dump of selection:" )
    # print( sel )

    for curThing in sel:
      if( isinstance( curThing, flame.PyFolder ) or isinstance( curThing, flame.PyLibrary ) or isinstance( curThing, flame.PyReel ) ):
        for curSeq in curThing.sequences:
          new_name = StripAvidStr( curSeq.name.get_value() )
          if new_name:
            curSeq.name.set_value( new_name )
            work_count += 1

      elif( isinstance( curThing, flame.PySequence ) ):
        new_name = StripAvidStr( curThing.name.get_value() )
        if new_name:
          curThing.name.set_value( new_name )
          work_count += 1

      else:
        flame.messages.show_in_dialog( title="Strip Avid Crap", message="Please select libraries, folders, reels, or sequences to process and try again.", type="error", buttons=["Ok"] )


    if( work_count > 0 ):
      flame.messages.show_in_console( "Strip Avid Crap: renamed " + str(work_count) + " items", "info", 4 )
    else:
      flame.messages.show_in_console( "Strip Avid Crap: nothing to do", "info", 4 )


  def StripAvidStr(avid_name):
    import re

    regex = re.search( '(.*)\.Exported\.[0-9]+', avid_name )
    if regex:
      return( regex.group(1) )
    else:
      return( None )


  # Adds the Project Tools menu on Flame with
  # Strip Avid Crap inside

  return [
    {
      "name": "Project Tools",
      "actions": [
        {
          "name": "Strip Avid Crap",
          "execute": StripAvidCrap_go,
          "minimumVersion": "2023.1.0.0",
        }
      ]
    }
  ]
