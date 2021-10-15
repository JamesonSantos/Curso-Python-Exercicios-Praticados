l = float(input('Largura da parde: '))
a = float(input('Altura da parede: '))
me = l * a
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(l, a, me))
tinta = me / 2
print('Para pintar essa parde, você precisará de {}L de tinta'.format(tinta))