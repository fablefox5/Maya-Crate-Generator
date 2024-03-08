import maya.cmds as cs


def create_crate(x_width, z_depth, spacing, num_boards):
    yHeight = x_width / 3
    # create starting boards
    cs.polyCube(name='boardBo', width=x_width, height=yHeight, depth=z_depth + (2 * yHeight))
    cs.polyCube(name='boardL', width=x_width, height=yHeight,
                depth=(x_width * num_boards) + (spacing * (num_boards - 1)))
    cs.polyCube(name='boardR', width=x_width, height=yHeight,
                depth=(x_width * num_boards) + (spacing * (num_boards - 1)))
    cs.polyCube(name='boardF', width=x_width, height=yHeight, depth=z_depth + (2 * yHeight))
    cs.polyCube(name='boardBa', width=x_width, height=yHeight, depth=z_depth + (2 * yHeight))

    # move boards to correct positions
    cs.rotate('-90deg', 0, '-90deg', 'boardL')
    cs.move((num_boards - 1) * ((x_width + spacing) / 2), yHeight / 2 + (x_width / 2), (z_depth / 2) + (yHeight / 2),
            'boardL')
    cs.rotate('-90deg', 0, '-90deg', 'boardR')
    cs.move((num_boards - 1) * ((x_width + spacing) / 2), yHeight / 2 + (x_width / 2), -((z_depth / 2) + (yHeight / 2)),
            'boardR')
    cs.rotate(0, 0, '-90deg', 'boardF')
    cs.move((((2 * num_boards) - 1) * (x_width / 2)) + ((num_boards - 1) * spacing) + yHeight / 2, yHeight * 2, 0,
            'boardF')
    cs.rotate(0, 0, '-90deg', 'boardBa')
    cs.move(-((x_width / 2) + (yHeight / 2)), yHeight * 2, 0, 'boardBa')

    # create levels
    for i in range(1, num_boards):
        new_board = cs.duplicate('boardBo')
        cs.move((x_width + spacing) * i, 0, 0, new_board)

        new_board = cs.duplicate('boardL')
        cs.move((num_boards - 1) * ((x_width + spacing) / 2), x_width / 6 + (x_width / 2) + (x_width + spacing) * i,
                (z_depth / 2) + (yHeight / 2),
                new_board)

        new_board = cs.duplicate('boardR')
        cs.move((num_boards - 1) * ((x_width + spacing) / 2), x_width / 6 + (x_width / 2) + (x_width + spacing) * i,
                -((z_depth / 2) + (yHeight / 2)),
                new_board)

        new_board = cs.duplicate('boardF')
        cs.move((((2 * num_boards) - 1) * (x_width / 2)) + ((num_boards - 1) * spacing) + yHeight / 2,
                x_width / 6 + (x_width / 2) + (x_width + spacing) * i, 0, new_board)

        new_board = cs.duplicate('boardBa')
        cs.move(-((x_width / 2) + (yHeight / 2)), x_width / 6 + (x_width / 2) + (x_width + spacing) * i, 0, new_board)

    # create corners
    cs.polyCube(name='corner_ba_r',
                width=x_width / 2,
                height=((num_boards * x_width) + (spacing * (num_boards - 1))),
                depth=x_width / 2)
    cs.move(-(x_width / 4), (((num_boards * x_width) + (spacing * (num_boards - 1))) / 2) + (yHeight / 2),
            -((z_depth / 2) - (x_width / 4)), 'corner_ba_r')

    cs.polyCube(name='corner_fr',
                width=x_width / 2,
                height=((num_boards * x_width) + (spacing * (num_boards - 1))),
                depth=x_width / 2)
    cs.move((x_width / 4) + ((spacing + x_width) * (num_boards - 1)),
            (((num_boards * x_width) + (spacing * (num_boards - 1))) / 2) + (yHeight / 2),
            -((z_depth / 2) - (x_width / 4)),
            'corner_fr')

    cs.polyCube(name='corner_ba_l',
                width=x_width / 2,
                height=((num_boards * x_width) + (spacing * (num_boards - 1))),
                depth=x_width / 2)
    cs.move(-(x_width / 4), (((num_boards * x_width) + (spacing * (num_boards - 1))) / 2) + (yHeight / 2),
            ((z_depth / 2) - (x_width / 4)), 'corner_ba_l')

    cs.polyCube(name='corner_fl',
                width=x_width / 2,
                height=((num_boards * x_width) + (spacing * (num_boards - 1))),
                depth=x_width / 2)
    cs.move((x_width / 4) + ((spacing + x_width) * (num_boards - 1)),
            (((num_boards * x_width) + (spacing * (num_boards - 1))) / 2) + (yHeight / 2),
            ((z_depth / 2) - (x_width / 4)),
            'corner_fl')

    # convert from poles to triangle shaped
    cs.polyDelEdge('corner_ba_r.e[5]')
    cs.polyDelVertex('corner_ba_r.vtx[3]')
    cs.polyDelVertex('corner_ba_r.vtx[1]')

    cs.polyDelEdge('corner_fr.e[4]')
    cs.polyDelVertex('corner_fr.vtx[2]')
    cs.polyDelVertex('corner_fr.vtx[0]')

    cs.polyDelEdge('corner_fl.e[8]')
    cs.polyDelVertex('corner_fl.vtx[4]')
    cs.polyDelVertex('corner_fl.vtx[6]')

    cs.polyDelEdge('corner_ba_l.e[9]')
    cs.polyDelVertex('corner_ba_l.vtx[5]')
    cs.polyDelVertex('corner_ba_l.vtx[7]')
    # combine sides and delete history (cleanup)
    rSide = cs.polyUnite('boardR', 'boardR1', name='rSide', o=True)
    cs.DeleteHistory()
    lSide = cs.polyUnite('boardL', 'boardL1', name='lSide', o=True)
    cs.DeleteHistory()
    fSide = cs.polyUnite('boardF', 'boardF1', name='fSide', o=True)
    cs.DeleteHistory()
    baSide = cs.polyUnite('boardBa', 'boardBa1', name='baSide', o=True)
    cs.DeleteHistory()
    boSide = cs.polyUnite('boardBo', 'boardBo1', name='boSide', o=True)
    cs.DeleteHistory()
    
    for i in range(2, num_boards):
        cs.polyUnite('rSide', 'boardR' + str(i), name='rSide', o=True, ch=False)
        cs.DeleteHistory()
        cs.rename('rSide')
        cs.polyUnite('lSide', 'boardL' + str(i), name='lSide', o=True, ch=False)
        cs.DeleteHistory()
        cs.rename('lSide')
        cs.polyUnite('fSide', 'boardF' + str(i), name='fSide', o=True, ch=False)
        cs.DeleteHistory()
        cs.rename('fSide')
        cs.polyUnite('baSide', 'boardBa' + str(i), name='baSide', o=True, ch=False)
        cs.DeleteHistory()
        cs.rename('baSide')
        cs.polyUnite('boSide', 'boardBo' + str(i), name='boSide', o=True, ch=False)
        cs.DeleteHistory()
        cs.rename('boSide')
       
    #cs.polyUnite('boardR', 'boardR1', 'boardR2', name='rSide')
    #cs.DeleteHistory()
    #cs.polyUnite(' boardL', 'boardL1', 'boardL2', name='lSide')
    #cs.DeleteHistory()
    #cs.polyUnite('boardF', 'boardF1', 'boardF2', name='fSide')
    #cs.DeleteHistory()
    #cs.polyUnite('boardBa', 'boardBa1', 'boardBa2', name='baSide')
    #cs.DeleteHistory()
    #cs.polyUnite('boardBo', 'boardBo1', 'boardBo2', name='boSide')
   # cs.DeleteHistory()
    cs.polyUnite('corner_ba_r', 'corner_fr', 'corner_ba_l', 'corner_fl', name='corners')
    cs.DeleteHistory()
    cs.polyUnite('rSide', 'lSide', 'fSide', 'baSide', 'boSide', 'corners')
    '''
    if num_boards > 2:
        cs.polyUnite('rSide', 'lSide', 'fSide', 'baSide', 'boSide', 'corners')
        #cs.polyUnite('rSide_og', 'lSide_og', 'fSide_og', 'baSide_og', 'boSide_og', 'corners')
    else:
        #cs.polyUnite('rSide', 'lSide', 'fSide', 'baSide', 'boSide', 'corners')
        cs.polyUnite('rSide_og', 'lSide_og', 'fSide_og', 'baSide_og', 'boSide_og', 'corners')
    '''
    cs.DeleteHistory()
    