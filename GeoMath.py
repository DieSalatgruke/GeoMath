import math as m

gon_faktor = float(10 / 9)
rundungs_faktor = 8


def create(koord_east_pkt1, koord_noth_pkt1, koord_east_pkt2, koord_noth_pkt2):
    return GeoFunction(koord_east_pkt1, koord_noth_pkt1, koord_east_pkt2, koord_noth_pkt2)


class GeoFunction:

    def __init__(self, koord_east_pkt1, koord_noth_pkt1, koord_east_pkt2, koord_noth_pkt2):
        self.koord_east_pkt1 = koord_east_pkt1
        self.koord_noth_pkt1 = koord_noth_pkt1
        self.koord_east_pkt2 = koord_east_pkt2
        self.koord_noth_pkt2 = koord_noth_pkt2

    def PolFunction(self, koord_east_pkt1, koord_noth_pkt1, koord_east_pkt2, koord_noth_pkt2):
        delta_east = m.pow((koord_east_pkt2 - koord_east_pkt1), 2)
        delta_north = m.pow((koord_noth_pkt2 - koord_noth_pkt1), 2)
        hypotenuse = m.sqrt(delta_east + delta_north)
        rounded_hypotenuse = round(hypotenuse, rundungs_faktor)

        riwi_rad = m.atan(delta_east / delta_north)
        riwi_gon = m.degrees(riwi_rad) * gon_faktor
        rounded_riwi_gon = round(riwi_gon, rundungs_faktor)
        if rounded_riwi_gon < 0:
            rounded_riwi_gon += 400
            richtungswinkel_gon = rounded_riwi_gon

        else:
            richtungswinkel_gon = rounded_riwi_gon

        return rounded_hypotenuse, richtungswinkel_gon
