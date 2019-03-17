
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMA IDENT IF INTEGER LABEL LBRACKET LPAREN NEWLINE RBRACKET RPARENprogram : program instruction\n                   | instructioninstruction : term argument_list\n                       | param_term argument_listinstruction : NEWLINEterm : IDENT\n                | INTEGER\n                | lookuplookup : IDENT LBRACKET INTEGER RBRACKETparam_term : IDENT LPAREN argument_list RPARENargument_list : termargument_list : term COMMA argument_list'
    
_lr_action_items = {'NEWLINE':([0,1,2,5,7,8,9,10,11,12,13,19,21,],[5,5,-2,-5,-7,-8,-1,-11,-3,-6,-4,-12,-9,]),'IDENT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,19,20,21,],[6,6,-2,12,12,-5,-6,-7,-8,-1,-11,-3,-6,-4,12,12,-12,-10,-9,]),'INTEGER':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,19,20,21,],[7,7,-2,7,7,-5,-6,-7,-8,-1,-11,-3,-6,-4,7,18,7,-12,-10,-9,]),'$end':([1,2,5,7,8,9,10,11,12,13,19,21,],[0,-2,-5,-7,-8,-1,-11,-3,-6,-4,-12,-9,]),'LPAREN':([6,],[14,]),'LBRACKET':([6,12,],[15,15,]),'COMMA':([7,8,10,12,21,],[-7,-8,16,-6,-9,]),'RPAREN':([7,8,10,12,17,19,21,],[-7,-8,-11,-6,20,-12,-9,]),'RBRACKET':([18,],[21,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'instruction':([0,1,],[2,9,]),'term':([0,1,3,4,14,16,],[3,3,10,10,10,10,]),'param_term':([0,1,],[4,4,]),'lookup':([0,1,3,4,14,16,],[8,8,8,8,8,8,]),'argument_list':([3,4,14,16,],[11,13,17,19,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program instruction','program',2,'p_program','parser.py',14),
  ('program -> instruction','program',1,'p_program','parser.py',15),
  ('instruction -> term argument_list','instruction',2,'p_instruction','parser.py',28),
  ('instruction -> param_term argument_list','instruction',2,'p_instruction','parser.py',29),
  ('instruction -> NEWLINE','instruction',1,'p_instruction_newline','parser.py',33),
  ('term -> IDENT','term',1,'p_term','parser.py',37),
  ('term -> INTEGER','term',1,'p_term','parser.py',38),
  ('term -> lookup','term',1,'p_term','parser.py',39),
  ('lookup -> IDENT LBRACKET INTEGER RBRACKET','lookup',4,'p_lookup','parser.py',43),
  ('param_term -> IDENT LPAREN argument_list RPAREN','param_term',4,'p_param_term','parser.py',47),
  ('argument_list -> term','argument_list',1,'p_argument_list','parser.py',51),
  ('argument_list -> term COMMA argument_list','argument_list',3,'p_argument_list_args','parser.py',55),
]
