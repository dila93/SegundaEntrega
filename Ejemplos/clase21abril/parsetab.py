
# parsetab.py
# This file is automatically generated. Do not edit.

_lr_method = 'SLR'

_lr_signature = '\xc3\x8a\xef\xd3\x90\xf6\x18bY\xfb3D\x8a\xf0\xc5\xb7'

_lr_action_items = {'PARENDER':([2,4,5,],[-1,5,-2,]),'ID':([0,3,],[2,2,]),'PARENIZQ':([0,3,],[3,3,]),'$end':([1,2,5,],[0,-1,-2,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _lr_action.has_key(_x):  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'A':([0,3,],[1,4,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _lr_goto.has_key(_x): _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S'",1,None,None,None),
  ('A',1,'p_A','anidados.py',39),
  ('A',3,'p_AA','anidados.py',43),
]
