print((lambda a : '###\nPlayer X Wins!\n###' if a==['X']*9 else '###\nPlayer O Wins!\n###' if a ==['O']*9 else '###\nDraw\n###')((lambda a : a[0] if a[1] == None else [a[1]]*9)((lambda a : (lambda a: [a,'X' if ((a[6] == 'X' and a[7] == 'X' and a[8] == 'X') or (a[3] == 'X' and a[4] == 'X' and a[5] == 'X') or (a[0] == 'X' and a[1] == 'X' and a[2] == 'X') or (a[6] == 'X' and a[3] == 'X' and a[0] == 'X') or (a[7] == 'X' and a[4] == 'X' and a[1] == 'X') or (a[8] == 'X' and a[5] == 'X' and a[2] == 'X') or (a[6] == 'X' and a[4] == 'X' and a[2] == 'X') or (a[8] == 'X' and a[4] == 'X' and a[0] == 'X')) else 'O' if ((a[6] == 'O' and a[7] == 'O' and a[8] == 'O') or (a[3] == 'O' and a[4] == 'O' and a[5] == 'O') or (a[0] == 'O' and a[1] == 'O' and a[2] == 'O') or (a[6] == 'O' and a[3] == 'O' and a[0] == 'O') or (a[7] == 'O' and a[4] == 'O' and a[1] == 'O') or (a[8] == 'O' and a[5] == 'O' and a[2] == 'O') or (a[6] == 'O' and a[4] == 'O' and a[2] == 'O') or (a[8] == 'O' and a[4] == 'O' and a[0] == 'O')) else None])((lambda a:[[print((lambda a:'\x1B[4m' + a + '\x1B[24m')(' ' * 12)),[print((lambda a:'\x1B[4m' + a + '\x1B[24m')('| ' + str(a[w+(w*2)]) + ' | ' + str(a[w+1+(w*2)]) + ' | ' + str(a[w+2+(w*2)]) + ' ') + '|') for w in range(3)]],a][1])((lambda a,b,c: [a.pop(b.index(c[1])),a.insert(b.index(c[1]),'X'),a][-1])(a,['1','2','3','4','5','6','7','8','9'],[(lambda a:[print((lambda a:'\x1B[4m' + a + '\x1B[24m')(' ' * 12)),[print((lambda a:'\x1B[4m' + a + '\x1B[24m')('| ' + str(a[w+(w*2)]) + ' | ' + str(a[w+1+(w*2)]) + ' | ' + str(a[w+2+(w*2)]) + ' ') + '|') for w in range(3)]])(['1','2','3','4','5','6','7','8','9']),input('Player X Type a valid number: ')]))) if a!=['X']*9 and a!=['O']*9 else a)((lambda a : a[0] if a[1] == None else [a[1]]*9)((lambda a : (lambda a: [a,'X' if ((a[6] == 'X' and a[7] == 'X' and a[8] == 'X') or (a[3] == 'X' and a[4] == 'X' and a[5] == 'X') or (a[0] == 'X' and a[1] == 'X' and a[2] == 'X') or (a[6] == 'X' and a[3] == 'X' and a[0] == 'X') or (a[7] == 'X' and a[4] == 'X' and a[1] == 'X') or (a[8] == 'X' and a[5] == 'X' and a[2] == 'X') or (a[6] == 'X' and a[4] == 'X' and a[2] == 'X') or (a[8] == 'X' and a[4] == 'X' and a[0] == 'X')) else 'O' if ((a[6] == 'O' and a[7] == 'O' and a[8] == 'O') or (a[3] == 'O' and a[4] == 'O' and a[5] == 'O') or (a[0] == 'O' and a[1] == 'O' and a[2] == 'O') or (a[6] == 'O' and a[3] == 'O' and a[0] == 'O') or (a[7] == 'O' and a[4] == 'O' and a[1] == 'O') or (a[8] == 'O' and a[5] == 'O' and a[2] == 'O') or (a[6] == 'O' and a[4] == 'O' and a[2] == 'O') or (a[8] == 'O' and a[4] == 'O' and a[0] == 'O')) else None])((lambda a:[[print((lambda a:'\x1B[4m' + a + '\x1B[24m')(' ' * 12)),[print((lambda a:'\x1B[4m' + a + '\x1B[24m')('| ' + str(a[w+(w*2)]) + ' | ' + str(a[w+1+(w*2)]) + ' | ' + str(a[w+2+(w*2)]) + ' ') + '|') for w in range(3)]],a][1])((lambda a,b,c: [a.pop(b.index(c[1])),a.insert(b.index(c[1]),'O'),a][-1])(a,['1','2','3','4','5','6','7','8','9'],[(lambda a:[print((lambda a:'\x1B[4m' + a + '\x1B[24m')(' ' * 12)),[print((lambda a:'\x1B[4m' + a + '\x1B[24m')('| ' + str(a[w+(w*2)]) + ' | ' + str(a[w+1+(w*2)]) + ' | ' + str(a[w+2+(w*2)]) + ' ') + '|') for w in range(3)]])(['1','2','3','4','5','6','7','8','9']),input('Player O Type a valid number: ')]))) if a!=['X']*9 and a!=['O']*9 else a)((lambda a : a[0] if a[1] == None else [a[1]]*9)((lambda a : (lambda a: [a,'X' if ((a[6] == 'X' and a[7] == 'X' and a[8] == 'X') or (a[3] == 'X' and a[4] == 'X' and a[5] == 'X') or (a[0] == 'X' and a[1] == 'X' and a[2] == 'X') or (a[6] == 'X' and a[3] == 'X' and a[0] == 'X') or (a[7] == 'X' and a[4] == 'X' and a[1] == 'X') or (a[8] == 'X' and a[5] == 'X' and a[2] == 'X') or (a[6] == 'X' and a[4] == 'X' and a[2] == 'X') or (a[8] == 'X' and a[4] == 'X' and a[0] == 'X')) else 'O' if ((a[6] == 'O' and a[7] == 'O' and a[8] == 'O') or (a[3] == 'O' and a[4] == 'O' and a[5] == 'O') or (a[0] == 'O' and a[1] == 'O' and a[2] == 'O') or (a[6] == 'O' and a[3] == 'O' and a[0] == 'O') or (a[7] == 'O' and a[4] == 'O' and a[1] == 'O') or (a[8] == 'O' and a[5] == 'O' and a[2] == 'O') or (a[6] == 'O' and a[4] == 'O' and a[2] == 'O') or (a[8] == 'O' and a[4] == 'O' and a[0] == 'O')) else None])((lambda a:[[print((lambda a:'\x1B[4m' + a + '\x1B[24m')(' ' * 12)),[print((lambda a:'\x1B[4m' + a + '\x1B[24m')('| ' + str(a[w+(w*2)]) + ' | ' + str(a[w+1+(w*2)]) + ' | ' + str(a[w+2+(w*2)]) + ' ') + '|') for w in range(3)]],a][1])((lambda a,b,c: [a.pop(b.index(c[1])),a.insert(b.index(c[1]),'X'),a][-1])(a,['1','2','3','4','5','6','7','8','9'],[(lambda a:[print((lambda a:'\x1B[4m' + a + '\x1B[24m')(' ' * 12)),[print((lambda a:'\x1B[4m' + a + '\x1B[24m')('| ' + str(a[w+(w*2)]) + ' | ' + str(a[w+1+(w*2)]) + ' | ' + str(a[w+2+(w*2)]) + ' ') + '|') for w in range(3)]])(['1','2','3','4','5','6','7','8','9']),input('Player X Type a valid number: ')]))) if a!=['X']*9 and a!=['O']*9 else a)((lambda a : a[0] if a[1] == None else [a[1]]*9)((lambda a : (lambda a: [a,'X' if ((a[6] == 'X' and a[7] == 'X' and a[8] == 'X') or (a[3] == 'X' and a[4] == 'X' and a[5] == 'X') or (a[0] == 'X' and a[1] == 'X' and a[2] == 'X') or (a[6] == 'X' and a[3] == 'X' and a[0] == 'X') or (a[7] == 'X' and a[4] == 'X' and a[1] == 'X') or (a[8] == 'X' and a[5] == 'X' and a[2] == 'X') or (a[6] == 'X' and a[4] == 'X' and a[2] == 'X') or (a[8] == 'X' and a[4] == 'X' and a[0] == 'X')) else 'O' if ((a[6] == 'O' and a[7] == 'O' and a[8] == 'O') or (a[3] == 'O' and a[4] == 'O' and a[5] == 'O') or (a[0] == 'O' and a[1] == 'O' and a[2] == 'O') or (a[6] == 'O' and a[3] == 'O' and a[0] == 'O') or (a[7] == 'O' and a[4] == 'O' and a[1] == 'O') or (a[8] == 'O' and a[5] == 'O' and a[2] == 'O') or (a[6] == 'O' and a[4] == 'O' and a[2] == 'O') or (a[8] == 'O' and a[4] == 'O' and a[0] == 'O')) else None])((lambda a:[[print((lambda a:'\x1B[4m' + a + '\x1B[24m')(' ' * 12)),[print((lambda a:'\x1B[4m' + a + '\x1B[24m')('| ' + str(a[w+(w*2)]) + ' | ' + str(a[w+1+(w*2)]) + ' | ' + str(a[w+2+(w*2)]) + ' ') + '|') for w in range(3)]],a][1])((lambda a,b,c: [a.pop(b.index(c[1])),a.insert(b.index(c[1]),'O'),a][-1])(a,['1','2','3','4','5','6','7','8','9'],[(lambda a:[print((lambda a:'\x1B[4m' + a + '\x1B[24m')(' ' * 12)),[print((lambda a:'\x1B[4m' + a + '\x1B[24m')('| ' + str(a[w+(w*2)]) + ' | ' + str(a[w+1+(w*2)]) + ' | ' + str(a[w+2+(w*2)]) + ' ') + '|') for w in range(3)]])(['1','2','3','4','5','6','7','8','9']),input('Player O Type a valid number: ')]))) if a!=['X']*9 and a!=['O']*9 else a)((lambda a : a[0] if a[1] == None else [a[1]]*9)((lambda a : (lambda a: [a,'X' if ((a[6] == 'X' and a[7] == 'X' and a[8] == 'X') or (a[3] == 'X' and a[4] == 'X' and a[5] == 'X') or (a[0] == 'X' and a[1] == 'X' and a[2] == 'X') or (a[6] == 'X' and a[3] == 'X' and a[0] == 'X') or (a[7] == 'X' and a[4] == 'X' and a[1] == 'X') or (a[8] == 'X' and a[5] == 'X' and a[2] == 'X') or (a[6] == 'X' and a[4] == 'X' and a[2] == 'X') or (a[8] == 'X' and a[4] == 'X' and a[0] == 'X')) else 'O' if ((a[6] == 'O' and a[7] == 'O' and a[8] == 'O') or (a[3] == 'O' and a[4] == 'O' and a[5] == 'O') or (a[0] == 'O' and a[1] == 'O' and a[2] == 'O') or (a[6] == 'O' and a[3] == 'O' and a[0] == 'O') or (a[7] == 'O' and a[4] == 'O' and a[1] == 'O') or (a[8] == 'O' and a[5] == 'O' and a[2] == 'O') or (a[6] == 'O' and a[4] == 'O' and a[2] == 'O') or (a[8] == 'O' and a[4] == 'O' and a[0] == 'O')) else None])((lambda a:[[print((lambda a:'\x1B[4m' + a + '\x1B[24m')(' ' * 12)),[print((lambda a:'\x1B[4m' + a + '\x1B[24m')('| ' + str(a[w+(w*2)]) + ' | ' + str(a[w+1+(w*2)]) + ' | ' + str(a[w+2+(w*2)]) + ' ') + '|') for w in range(3)]],a][1])((lambda a,b,c: [a.pop(b.index(c[1])),a.insert(b.index(c[1]),'X'),a][-1])(a,['1','2','3','4','5','6','7','8','9'],[(lambda a:[print((lambda a:'\x1B[4m' + a + '\x1B[24m')(' ' * 12)),[print((lambda a:'\x1B[4m' + a + '\x1B[24m')('| ' + str(a[w+(w*2)]) + ' | ' + str(a[w+1+(w*2)]) + ' | ' + str(a[w+2+(w*2)]) + ' ') + '|') for w in range(3)]])(['1','2','3','4','5','6','7','8','9']),input('Player X Type a valid number: ')]))) if a!=['X']*9 and a!=['O']*9 else a)((lambda a:[[print((lambda a:'\x1B[4m' + a + '\x1B[24m')(' ' * 12)),[print((lambda a:'\x1B[4m' + a + '\x1B[24m')('| ' + str(a[w+(w*2)]) + ' | ' + str(a[w+1+(w*2)]) + ' | ' + str(a[w+2+(w*2)]) + ' ') + '|') for w in range(3)]],a][1])((lambda a,b,c: [a.pop(b.index(c[1])),a.insert(b.index(c[1]),'O'),a][-1])((lambda a:[[print((lambda a:'\x1B[4m' + a + '\x1B[24m')(' ' * 12)),[print((lambda a:'\x1B[4m' + a + '\x1B[24m')('| ' + str(a[w+(w*2)]) + ' | ' + str(a[w+1+(w*2)]) + ' | ' + str(a[w+2+(w*2)]) + ' ') + '|') for w in range(3)]],a][1])((lambda a,b,c: [a.pop(b.index(c[1])),a.insert(b.index(c[1]),'X'),a][-1])((lambda a:[[print((lambda a:'\x1B[4m' + a + '\x1B[24m')(' ' * 12)),[print((lambda a:'\x1B[4m' + a + '\x1B[24m')('| ' + str(a[w+(w*2)]) + ' | ' + str(a[w+1+(w*2)]) + ' | ' + str(a[w+2+(w*2)]) + ' ') + '|') for w in range(3)]],a][1])((lambda a,b,c: [a.pop(b.index(c[1])),a.insert(b.index(c[1]),'O'),a][-1])((lambda a:[[print((lambda a:'\x1B[4m' + a + '\x1B[24m')(' ' * 12)),[print((lambda a:'\x1B[4m' + a + '\x1B[24m')('| ' + str(a[w+(w*2)]) + ' | ' + str(a[w+1+(w*2)]) + ' | ' + str(a[w+2+(w*2)]) + ' ') + '|') for w in range(3)]],a][1])((lambda a,b,c: [a.pop(b.index(c[1])),a.insert(b.index(c[1]),'X'),a][-1])([' ',' ',' ',' ',' ',' ',' ',' ',' '],['1','2','3','4','5','6','7','8','9'],[(lambda a:[print((lambda a:'\x1B[4m' + a + '\x1B[24m')(' ' * 12)),[print((lambda a:'\x1B[4m' + a + '\x1B[24m')('| ' + str(a[w+(w*2)]) + ' | ' + str(a[w+1+(w*2)]) + ' | ' + str(a[w+2+(w*2)]) + ' ') + '|') for w in range(3)]])(['1','2','3','4','5','6','7','8','9']),input('Player X Type a valid number: ')])),['1','2','3','4','5','6','7','8','9'],[(lambda a:[print((lambda a:'\x1B[4m' + a + '\x1B[24m')(' ' * 12)),[print((lambda a:'\x1B[4m' + a + '\x1B[24m')('| ' + str(a[w+(w*2)]) + ' | ' + str(a[w+1+(w*2)]) + ' | ' + str(a[w+2+(w*2)]) + ' ') + '|') for w in range(3)]])(['1','2','3','4','5','6','7','8','9']),input('Player O Type a valid number: ')])),['1','2','3','4','5','6','7','8','9'],[(lambda a:[print((lambda a:'\x1B[4m' + a + '\x1B[24m')(' ' * 12)),[print((lambda a:'\x1B[4m' + a + '\x1B[24m')('| ' + str(a[w+(w*2)]) + ' | ' + str(a[w+1+(w*2)]) + ' | ' + str(a[w+2+(w*2)]) + ' ') + '|') for w in range(3)]])(['1','2','3','4','5','6','7','8','9']),input('Player X Type a valid number: ')])),['1','2','3','4','5','6','7','8','9'],[(lambda a:[print((lambda a:'\x1B[4m' + a + '\x1B[24m')(' ' * 12)),[print((lambda a:'\x1B[4m' + a + '\x1B[24m')('| ' + str(a[w+(w*2)]) + ' | ' + str(a[w+1+(w*2)]) + ' | ' + str(a[w+2+(w*2)]) + ' ') + '|') for w in range(3)]])(['1','2','3','4','5','6','7','8','9']),input('Player O Type a valid number: ')]))))))))))))))
