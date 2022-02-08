import math
from typing import List

_g_m_s2 = 9.81

minor_loss_coefficients = {
    "Tee, Flanged, Dividing Line Flow": 0.2,
    "Tee, Threaded, Dividing Line Flow": 1.0,
    "Tee, Threaded, Dividing Branch Flow": 2.0,
    "Union, Threaded": 0.08,
    "Elbow, Flanged Regular 90o": 0.3,
    "Elbow, Threaded Regular 90o": 1.5,
    "Elbow, Threaded Regular 45o": 0.4,
    "Elbow, Flanged Long Radius 90o": 0.2,
    "Elbow, Threaded Long Radius 90o": 0.7,
    "Elbow, Flanged Long Radius 45o": 0.2,
    "Return Bend, Flanged 180o": 0.2,
    "Return Bend, Threaded 180o": 1.5,
    "Globe Valve, Fully Open": 10,
    "Angle Valve, Fully Open": 2,
    "Gate Valve, Fully Open": 0.15,
    "Gate Valve, 1 / 4 Closed": 0.26,
    "Gate Valve, 1 / 2 Closed ": 2.1,
    "Gate Valve, 3 / 4 Closed": 17,
    "Swing Check Valve, Forward Flow": 2,
    "Ball Valve, Fully Open": 0.05,
    "Ball Valve, 1 / 3 Closed ": 5.5,
    "Ball Valve, 2 / 3 Closed": 200,
    "Diaphragm Valve, Open": 2.3,
    "Diaphragm Valve, Half Open": 4.3,
    "Diaphragm Valve, 1 / 4 Open": 21,
    "Water meter": 7
}

sch_40_pipe_id_m = {
    "1/8": 0.0686,
    "1/4": 0.0914,
    "3/8": 0.0124,
    "1/2": 0.0157,
    "3/4": 0.0208,
    "1": 0.0267,
    "1 1/4": 0.0351,
    "1 1/2": 0.0409,
    "2": 0.0526,
    "2 1/2": 0.0627,
    "3": 0.0780,
    "3 1/2": 0.0902,
    "4": 0.102,
    "5": 0.128,
    "6": 0.154,
    "8": 0.203,
    "10": 0.255,
    "12": 0.303,
    "14": 0.334,
    "16": 0.381,
    "18": 0.429,
    "20": 0.478,
    "24": 0.575,
}


def minor_loss_coefficient_reducers(d1: float, d2: float):
    if d1 > d2:
        val = 0.5 * (1 - (d2 / d1) ** 2)
    else:
        val = 2.0 * (1 - (d1 / d2) ** 4)
    return val


class flow_properties:
    def __init__(self, flow_m3_s: float, d_h_m: float, k_m=4.5E-05, v_m2_s=9.757E-07, lambda_guess=0.03):
        self.k_m = k_m
        self.flow_m3_s = flow_m3_s
        self.d_h_m = d_h_m
        self.v_m2_s = v_m2_s
        self.lambda_guess = lambda_guess

    def u_m_s(self):
        if self.d_h_m != 0:
            val = self.flow_m3_s / ((self.d_h_m / 2) ** 2 * math.pi)
        else:
            val = 0
        return val

    def re(self):
        if self.v_m2_s != 0:
            val = flow_properties.u_m_s(self) * self.d_h_m / self.v_m2_s
        else:
            val = 0
        return val

    def lambda_c(self):
        try:
            lambda_c = (1.0 / (-2.0 * math.log(
                2.51 / (flow_properties.re(self) * self.lambda_guess ** 0.5) + (self.k_m / self.d_h_m) / 3.72))) ** 2.0
            for i in range(20):
                lambda_c = (1.0 / (-2.0 * math.log(
                    2.51 / (flow_properties.re(self) * lambda_c ** 0.5) + (self.k_m / self.d_h_m) / 3.72))) ** 2.0
        except ValueError:
            lambda_c = 0
        return lambda_c


class epsilon_qty:
    def __init__(self, epsilon, qty):
        self.epsilon = epsilon
        self.qty = qty


class minor_loss:
    def __init__(self, flow: flow_properties, epsilon_qty_list: List[epsilon_qty], qty=0, epsilon=0):
        self.flow = flow
        self.qty = qty
        self.epsilon = epsilon
        self.epsilon_qty_list = epsilon_qty_list

    def h_minor_loss_m(self):
        try:
            val = self.qty * self.epsilon * self.flow.u_m_s() ** 2 / (2 * _g_m_s2)
        except ValueError:
            val = 0
        return val

    def h_minor_loss_m(self):
        if self.epsilon_qty_list is not None:
            total = 0
            for obj in self.epsilon_qty_list:
                total += obj.qty * obj.epsilon * self.flow.u_m_s() ** 2 / (2 * _g_m_s2)

        else:
            total = 0
        return total


class major_loss:
    def __init__(self, flow: flow_properties, l_m):
        self.flow = flow
        self.l_m = l_m

    def h_major_loss_m(self):
        try:
            val = self.flow.lambda_c() * (self.l_m / self.flow.d_h_m) * (self.flow.u_m_s() ** 2 / (2 * _g_m_s2))
        except AttributeError:
            val = 0
        return val


class pipe_section:
    def __init__(self, flow: flow_properties = None, l_m=0.0, epsilon_qty_list: List[epsilon_qty] = None,
                 additional_loss_m={}):
        self.major_loss = major_loss(flow, l_m)
        self.minor_loss = minor_loss(flow, epsilon_qty_list)
        self.additional_loss = additional_loss_m

    def loss_m(self):
        return self.major_loss.h_major_loss_m() + self.minor_loss.h_minor_loss_m() + sum(self.additional_loss.values())
