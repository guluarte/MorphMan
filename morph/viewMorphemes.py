#-*- coding: utf-8 -*-
from morphemes import getMorphemes, ms2str
from morphemizer import getMorphemizerForNote
from util import addBrowserSelectionCmd, cfg, cfg1, infoMsg

def pre( b ): return { 'txt':'', 'morphemizer': None }

def per( st, n ):
    st['morphemizer'] = getMorphemizerForNote(n)
    for f in cfg( n.mid, None, 'morph_fields' ):
        st['txt'] += n[ f ] + '  '
    return st

def post( st ):
    ms = getMorphemes(st['morphemizer'], st['txt'])
    s = ms2str( ms )
    infoMsg( '----- All -----\n' + s )

addBrowserSelectionCmd( 'MorphMan: View Morphemes', pre, per, post, tooltip='View Morphemes for selected note', shortcut=('Ctrl+Shift+V',) )
