from ngspicelib import Circuit
def __main__():
    cir = Circuit('try.cir',title='This sdf')
    cir.comment('####Import models####')
    cir.include('../models/diodes.mod')
    cir.include('../models/mos.mod')
    cir.comment('####CIRCUIT####')
    cir.comment('Input voltage with intrinsic resistence')
    cir.raw_write('vin gen 0 dc 3.3v')
    cir.raw_write('c1 in 0 10u')
    cir.raw_write('l1 in drain {}'.format(str(300e-6)))
    cir.x(p=['drain', 'gate', '0', '100'],subckt='mos_model1',name='nmos')
    cir.raw_write('rgate gate switch 10')
    cir.raw_write('dsch drain out schoideal')
    cir.raw_write('c2 out 0 10n')
    cir.raw_write('rl out 0 100k')
    cir.source('switch','0','pulse (0 3.3 0 0 0 17u 20u)',name='switch')
    cir.sim_trans(0.01e-6,1e-3)

    cir.begin_control()
    cir.run_control()
    cir.save('vout.csv','in','out','switch','gate','drain','l1#branch')
    cir.end_control()

    cir.run()
if __name__=='__main__':
    __main__()
