from threshold_dynamics.params import *

progname = "Numerical Methods Project"
progversion = "0.1"
proginfo = """
Минков Василий Андреевич, БПС-143.
 ОС: Mac OS X El Capistan.
 Среда: PyCharm 2016.2,
 Процессор: 2,4 GHz Intel Core i7
 Оперативная память: 8 GB 1600 MHz DDR3
 Видеокарта: Intel HD Graphics 4000 1536 MB
 Разрешение экрана: 2880 x 1800
"""
figure_params = Params(xgraph1=np.arange(0.0, np.pi * 12, np.pi / 12),
                       xgraph2=np.arange(0.0, 30, 0.1),
                       xgraph3=np.arange(0.0, 30, 0.1),
                       xgraph4=np.arange(0.0, 30, 0.1),
                       xgraph5=np.arange(0.0, 30, 0.1),
                       a1=0, b1=0,
                       a2=1, b2=1,
                       a3=5, b3=1)
