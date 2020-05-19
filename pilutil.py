# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# ========================================================================
def converta(pymagens):
    ''' (list) -> list
    recebe uma lista de pymagens e retorna uma lista de imagens
    (arrays de Numpy) prontas para serem animadas.
    A função pega a matriz da pymagem usando o método .get_mat()
    '''
    npimgs = []
    for pym in pymagens:
        npimgs.append( [plt.imshow( np.array( pym.get_mat() ), cmap='gray', vmin=0, vmax=255, animated=True)] )
    return npimgs

# ========================================================================
def mostre_animacao( pymagens = [], interval=50, blit=True, repeat_delay=1000 ):
    ''' (list) -> None
    Recebe uma lista de Pymagens em pymagens
    e cria e mostra uma animação dessas Pymagens.
    '''
    fig = plt.figure()
    npimgs = converta( pymagens )
    ani = animation.ArtistAnimation(fig, npimgs, interval, blit, repeat_delay)
    plt.show()

# ========================================================================

def salve_animacao( pymagens = [], interval=50, blit=True, repeat_delay=1000 ):
    ''' (list) -> None
    Recebe uma lista de Pymagens em pymagens
    e cria e mostra uma animação dessas Pymagens.
    '''
    fig = plt.figure()
    npimgs = converta( pymagens )
    ani = animation.ArtistAnimation(fig, npimgs, interval, blit, repeat_delay)
    
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps = 15, metadata=dict(artist='mac0122-EP04'), bitrate=1800)
    ani.save('ep04-saida.mp4', writer=writer)

# ========================================================================