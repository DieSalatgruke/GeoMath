# -*- coding: utf-8 -*-
import GeoMath as gema

parameter_geradenschnitt = '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Geradenschnitt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

parameter_interface = '''********************************************************************************
      Hallo, ich rechne dir den Schnittpunkte bei einem Geradenschnitt.
      Bitte gib nacheinander die Koordinaten ein.
********************************************************************************
'''


if __name__ == "__main__":
    print(parameter_interface)

    pkt1 = gema.create_koord(gema.create_east(), gema.create_north(),
                             gema.create_radius(), gema.create_richtungswinkel())
    pkt2 = gema.create_koord(gema.create_east(), gema.create_north(),
                             gema.create_radius(), gema.create_richtungswinkel())
    pkt3 = gema.create_koord(gema.create_east(), gema.create_north(),
                             gema.create_radius(), gema.create_richtungswinkel())
    pkt4 = gema.create_koord(gema.create_east(), gema.create_north(),
                             gema.create_radius(), gema.create_richtungswinkel())

    pol_one = gema.pol_function(pkt1.east, pkt1.north, pkt2.east, pkt2.north)
    pol_two = gema.pol_function(pkt3.east, pkt3.north, pkt4.east, pkt4.north)
    int_north = gema.interception_point_north(pkt1.east, pkt1.north, pkt3.east, pkt3.north, pol_one[1], pol_two[1])
    int_east = gema.interception_point_east(pkt1.east, pkt1.north, pol_one[1], int_north)

    gs1 = gema.Geradenschnitt(pol_one[0], pol_one[1], int_east, int_north)
    gs2 = gema.Geradenschnitt(pol_two[0], pol_two[1], int_east, int_north)
    gema.file_handler(parameter_geradenschnitt, pkt1.show(), pkt2.show(), pkt3.show(), pkt4.show(), gs1.show(),
                      gs2.show())
    gema.Geradenschnitt.show(pkt1)
    gema.Geradenschnitt.show(pkt3)
