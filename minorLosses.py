from typing import List
from internalFlowProperties import internalFlowProperties

g_m_s2 = 9.81
"gravitational acceleration [m/s^2]"

epsilons = {
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
"minor loss coefficients"


def epsilon_reducers(d1, d2):
    """
    reference: https://neutrium.net/fluid-flow/pressure-loss-from-fittings-expansion-and-reduction-in-pipe-size/

    :param float d1: upstream diameter
    :param float d2: downstream diameter
    :return float: minor loss coefficient
    """
    if d1 > d2:
        val = 0.5 * (1 - (d2 / d1) ** 2)
    else:
        val = 2.0 * (1 - (d1 / d2) ** 4)
    return val


class epsilonQty:
    """
    a class to create a list of minor loss coefficients from
    """

    def __init__(self, qty, epsilon):
        """

        :param qty: number elements which have the corresponding loss coefficient
        :param epsilon: loss coefficient
        """
        self.epsilon = epsilon
        self.qty = qty


class minorLosses:
    """
    minor losses are due to entrances, fittings, area changes, and so forth
    """

    def __init__(self, flow, epsilon_qty_list):
        """

        :param internalFlowProperties flow: flow properties object for this length of pipe
        :param List[epsilonQty] epsilon_qty_list: list of loss coefficients and corresponding quantity
        """
        self._flow = flow
        self._epsilon_qty_list = epsilon_qty_list

    @staticmethod
    def minor_loss_m(qty, epsilon, u_m_s):
        """

        :param float qty: number elements which have the corresponding loss coefficient
        :param float epsilon: loss coefficient
        :param float u_m_s: average velocity over the cross section [m/s]
        :return float : minor loss [m]
        """
        try:
            val = qty * epsilon * u_m_s ** 2 / (2 * g_m_s2)
        except ValueError:
            val = 0.0
        return val

    @property
    def flow(self):
        """flow properties object for this length of pipe"""
        return self._flow

    @property
    def epsilon_qty_list(self):
        """list of loss coefficients and corresponding quantity"""
        return self._epsilon_qty_list

    @property
    def minor_losses_m(self):
        """

        :return: total minor losses for the list of minor loss coefficients
        """
        if self.epsilon_qty_list is not None:
            total = 0
            for obj in self.epsilon_qty_list:
                total += self.minor_loss_m(obj.qty, obj.epsilon, self.flow.u_m_s)

        else:
            total = 0
        return total
