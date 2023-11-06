#!/bin/env python

# StripAvidCrap.py by Bob Maple
# VER: 2023-11-05
#
# Takes a selection of libraries, folders, reels or sequences and renames
# all sequences found, removing 'Exported.01' crap from the end.
# Only looks for sequences at the root level of any selected libraries, folders.
# For every sequence found, it also renames all clips on the sequence stripping
# off 'sync.01' and 'new.01' from the clip names (only works on video segments)
#
# Note that if you run this on a reel on the Desktop, the names won't visually update
# until you do something else in the UI (click something, etc)

def get_media_panel_custom_ui_actions():

  def StripAvidCrap_go(sel):
    import flame
    seq_count = 0
    seg_count = 0

    # print( "dump of selection:" )
    # print( sel )

    for curThing in sel:

      if( isinstance( curThing, flame.PyFolder ) or isinstance( curThing, flame.PyLibrary ) or isinstance( curThing, flame.PyReel ) ):
        doSequences = curThing.sequences
      elif( isinstance( curThing, flame.PySequence ) ):
        doSequences = [curThing]
      else:
        flame.messages.show_in_dialog( title="Strip Avid Crap", message="Please select only libraries, folders, reels, or sequences to process.", type="error", buttons=["Ok"] )
        doSequences = false

      if( doSequences ):
        for curSeq in doSequences:

          # Rename the sequence its self
          new_name = StripAvidStr( curSeq.name.get_value() )
          if new_name:
            curSeq.name.set_value( new_name )
            seq_count += 1

          # Walk through the sequence and rename segments - video
          for curTrack in curSeq.versions[0].tracks:
            for curSeg in curTrack.segments:
              new_segname = StripAvidStr( curSeg.name.get_value() )
              if new_segname:
                curSeg.name.set_value( new_segname )
                seg_count += 1

    if( seq_count + seg_count > 0 ):
      flame.messages.show_in_console( "Strip Avid Crap: renamed " + str(seq_count) + " sequences and " + str(seg_count) + " segments", "info", 4 )
    else:
      flame.messages.show_in_console( "Strip Avid Crap: nothing to do", "info", 4 )


  def StripAvidStr(avid_name):
    import re

    regex = re.search( '(.*)\.(Exported|sync|new)\.[0-9]+', avid_name )
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
