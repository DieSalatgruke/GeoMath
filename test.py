import GeoMath as gm

pkt1 = gm.create_koord(1, 1)
pkt2 = gm.create_koord(6, 6)
pkt3 = gm.create_koord(1, 6)
pkt4 = gm.create_koord(6, 1)


#print(pkt1.show())
#print(pkt2.show())
#print(pkt3.show())
#print(pkt4.show())

pol_one = gm.pol_function(pkt1.east, pkt1.north, pkt2.east, pkt2.north)
pol_two = gm.pol_function(pkt3.east, pkt3.north, pkt4.east, pkt4.north)
int_north = gm.interception_point_north(pkt1.east, pkt1.north, pkt3.east, pkt3.north, pol_one[1], pol_two[1])
int_east = gm.interception_point_east(pkt1.east, pkt1.north, pol_one[1], int_north)

gs1 = gm.Geradenschnitt(pol_one[0], pol_one[1], int_east, int_north)
gs2 = gm.Geradenschnitt(pol_two[0], pol_two[1], int_east, int_north)
gm.file_handler(pkt1.show(), pkt2.show(), pkt3.show(), pkt4.show(), gs1.show(), gs2.show())
