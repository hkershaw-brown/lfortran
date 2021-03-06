results = [
    ('Num', (1, 1), '1'),
    ('BinOp', (1, 1), ('Num', (1, 1), '2'), ('Add',), ('Num', (1, 1), '3')),
    ('BinOp', (1, 1), ('BinOp', (1, 1), ('Num', (1, 1), '1'), ('Add',), ('Num', (1, 1), '3')), ('Mul',), ('Num', (1, 1), '4')),
    ('BinOp', (1, 1), ('Num', (1, 1), '1'), ('Add',), ('BinOp', (1, 1), ('Num', (1, 1), '3'), ('Mul',), ('Num', (1, 1), '4'))),
    ('Name', (1, 1), 'x'),
    ('Name', (1, 1), 'yx'),
    ('BinOp', (1, 1), ('Name', (1, 1), 'x'), ('Add',), ('Name', (1, 1), 'y')),
    ('BinOp', (1, 1), ('Num', (1, 1), '2'), ('Add',), ('Name', (1, 1), 'x')),
    ('BinOp', (1, 1), ('BinOp', (1, 1), ('Name', (1, 1), 'x'), ('Add',), ('Name', (1, 1), 'y')), ('Pow',), ('Num', (1, 1), '2')),
    ('BinOp', (1, 1), ('BinOp', (1, 1), ('Name', (1, 1), 'x'), ('Add',), ('Name', (1, 1), 'y')), ('Mul',), ('Num', (1, 1), '3')),
    ('BinOp', (1, 1), ('Name', (1, 1), 'x'), ('Add',), ('BinOp', (1, 1), ('Name', (1, 1), 'y'), ('Mul',), ('Num', (1, 1), '3'))),
    ('BinOp', (1, 1), ('BinOp', (1, 1), ('BinOp', (1, 1), ('Num', (1, 1), '1'), ('Add',), ('Num', (1, 1), '2')), ('Add',), ('Name', (1, 1), 'a')), ('Mul',), ('Num', (1, 1), '3')),
    ('BinOp', (1, 1), ('FuncCallOrArray', (1, 1), 'f', [('Num', (1, 1), '3')], []), ('Add',), ('Num', (1, 1), '6')),
    ('FuncCallOrArray', (1, 1), 'f', [('BinOp', (1, 1), ('Num', (1, 1), '3'), ('Add',), ('Num', (1, 1), '6'))], []),
    ('FuncCallOrArray', (1, 1), 'real', [('Name', (1, 1), 'b'), ('Name', (1, 1), 'dp')], []),
    ('BinOp', (1, 1), ('BinOp', (1, 1), ('Num', (1, 1), '2'), ('Mul',), ('Name', (1, 1), 'u')), ('Sub',), ('Num', (1, 1), '1')),
    ('FuncCallOrArray', (1, 1), 'sum', [('BinOp', (1, 1), ('Name', (1, 1), 'u'), ('Pow',), ('Num', (1, 1), '2'))], []),
    ('FuncCallOrArray', (1, 1), 'u', [('Num', (1, 1), '2')], []),
    ('BinOp', (1, 1), ('Name', (1, 1), 'u'), ('Mul',), ('FuncCallOrArray', (1, 1), 'sqrt', [('UnaryOp', (1, 1), ('USub',), ('BinOp', (1, 1), ('BinOp', (1, 1), ('Num', (1, 1), '2'), ('Mul',), ('FuncCallOrArray', (1, 1), 'log', [('Name', (1, 1), 'r2')], [])), ('Div',), ('Name', (1, 1), 'r2')))], [])),
    ('UnaryOp', (1, 1), ('Not',), ('Name', (1, 1), 'first')),
    ('BinOp', (1, 1), ('Name', (1, 1), 'a'), ('Sub',), ('BinOp', (1, 1), ('Num', (1, 1), '1._dp'), ('Div',), ('Num', (1, 1), '3'))),
    ('BinOp', (1, 1), ('Num', (1, 1), '1'), ('Div',), ('FuncCallOrArray', (1, 1), 'sqrt', [('BinOp', (1, 1), ('Num', (1, 1), '9'), ('Mul',), ('Name', (1, 1), 'd'))], [])),
    ('BinOp', (1, 1), ('BinOp', (1, 1), ('Num', (1, 1), '1'), ('Add',), ('BinOp', (1, 1), ('Name', (1, 1), 'c'), ('Mul',), ('Name', (1, 1), 'x'))), ('Pow',), ('Num', (1, 1), '3')),
    ('BinOp', (1, 1), ('Name', (1, 1), 'i'), ('Add',), ('Num', (1, 1), '1')),
    ('Str', (1, 1), 's'),
    ('Str', (1, 1), 'some text'),
    ('Array', (1, 1), 'a', [('ArrayIndex', None, None, None), ('ArrayIndex', None, None, None)]),
    ('Array', (1, 1), 'b', [('ArrayIndex', None, None, None)]),
    ('BinOp', (1, 1), ('Array', (1, 1), 'a', [('ArrayIndex', None, None, None), ('ArrayIndex', None, None, None)]), ('Add',), ('Array', (1, 1), 'b', [('ArrayIndex', None, None, None)])),
    ('ArrayInitializer', (1, 1), [('Num', (1, 1), '1'), ('Num', (1, 1), '2'), ('Num', (1, 1), '3'), ('Name', (1, 1), 'i')]),
    ('FuncCallOrArray', (1, 1), 'f', [], []),
    ('Name', (1, 1), 'a'),
    ('FuncCallOrArray', (1, 1), 'a', [], []),
    ('FuncCallOrArray', (1, 1), 'b', [('Name', (1, 1), 'i'), ('Name', (1, 1), 'j')], []),
    ('Array', (1, 1), 'c', [('ArrayIndex', ('Num', (1, 1), '5'), None, None), ('ArrayIndex', None, None, None)]),
    ('Name', (1, 1), 'a'),
    ('FuncCallOrArray', (1, 1), 'b', [('Name', (1, 1), 'i'), ('Name', (1, 1), 'j')], []),
    ('Array', (1, 1), 'c', [('ArrayIndex', ('Num', (1, 1), '5'), None, None), ('ArrayIndex', None, None, None)]),
    ('Str', (1, 1), "a'b'c"),
    ('Str', (1, 1), 'a"b"c'),
    ('Str', (1, 1), 'a""bc""x'),
    ('Str', (1, 1), 'a"c'),
    ('Str', (1, 1), 'a"b"c'),
    ('Str', (1, 1), '"zippo"'),
    ('Str', (1, 1), "a'c"),
    ('Str', (1, 1), "a'b'c"),
    ('Str', (1, 1), "'zippo'"),
    ('BoolOp', (1, 1), ('Num', (1, 1), '1'), ('And',), ('Num', (1, 1), '2')),
    ('BoolOp', (1, 1), ('Name', (1, 1), 'a'), ('And',), ('Name', (1, 1), 'b')),
    ('BoolOp', (1, 1), ('Compare', (1, 1), ('Name', (1, 1), 'a'), ('Eq',), ('Num', (1, 1), '1')), ('And',), ('Compare', (1, 1), ('Name', (1, 1), 'b'), ('Eq',), ('Num', (1, 1), '2'))),
    ('BoolOp', (1, 1), ('Compare', (1, 1), ('Name', (1, 1), 'a'), ('Eq',), ('Num', (1, 1), '1')), ('Or',), ('Compare', (1, 1), ('Name', (1, 1), 'b'), ('Eq',), ('Num', (1, 1), '2'))),
    ('BoolOp', (1, 1), ('BoolOp', (1, 1), ('Name', (1, 1), 'a'), ('And',), ('Name', (1, 1), 'b')), ('And',), ('Name', (1, 1), 'c')),
    ('BoolOp', (1, 1), ('BoolOp', (1, 1), ('Name', (1, 1), 'a'), ('Or',), ('Name', (1, 1), 'b')), ('Or',), ('Name', (1, 1), 'c')),
    ('UnaryOp', (1, 1), ('Not',), ('Compare', (1, 1), ('Name', (1, 1), 'a'), ('Eq',), ('Num', (1, 1), '1'))),
    ('BoolOp', (1, 1), ('Compare', (1, 1), ('Name', (1, 1), 'a'), ('Eq',), ('Num', (1, 1), '1')), ('And',), ('UnaryOp', (1, 1), ('Not',), ('Compare', (1, 1), ('Name', (1, 1), 'b'), ('Eq',), ('Num', (1, 1), '2')))),
]
