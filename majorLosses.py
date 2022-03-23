from internalFlowProperties import internalFlowProperties

g_m_s2 = 9.81
"gravitational acceleration [m/s^2]"

class majorLosses:
    """
    Major losses are due to friction
    """
    def __init__(self, flow, l_m):
        """

        :param internalFlowProperties flow: flow properties object for this length of pipe
        :param float l_m: length of pipe [m]
        """
        self._flow = flow
        self._l_m = l_m

    @property
    def l_m(self):
        """length of pipe [m]"""
        return self._l_m

    @property
    def flow(self):
        """flow properties object for this length of pipe"""
        return self._flow

    @property
    def major_loss_m(self):
        """
         major loss due to friction [2, pp. 162]

        :return: major loss [m]
        """
        return self.flow.f * self.l_m * self.flow.u_m_s ** 2 / (self.flow.d_h_m * 2 * g_m_s2)
