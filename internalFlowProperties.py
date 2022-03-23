import math


class internalFlowProperties:
    """
    This class defines properties for fully developed internal flow in pipes
    """

    def __init__(self, m_dot_kg_s, d_h_m, rho_kg_m3, mu_kg_ms, k_m):
        """
        initialize the flow properties based on the following parameters

        :param float m_dot_kg_s: mass flow rate [kg/s]
        :param float mu_kg_ms: dynamic (absolute) viscosity [kg/m*s]
        :param float rho_kg_m3: density [kg/m^3]
        :param float d_h_m: hydraulic diameter [m]
        :param float k_m: surface roughness [m]
        """
        self._m_dot_kg_s = m_dot_kg_s
        self._mu_kg_ms = mu_kg_ms
        self._rho_kg_m3 = rho_kg_m3
        self._d_h_m = d_h_m
        self._k_m = k_m

    @property
    def m_dot_kg_s(self):
        """mass flow rate [kg/s]"""
        return self._m_dot_kg_s

    @property
    def mu_kg_ms(self):
        """dynamic (absolute) viscosity [kg/m*s]"""
        return self._mu_kg_ms

    @property
    def rho_kg_m3(self):
        """density [kg/m^3]"""
        return self._rho_kg_m3

    @property
    def d_h_m(self):
        """hydraulic diameter [m]"""
        return self._d_h_m

    @property
    def r_h_m(self):
        """hydraulic radius [m]"""
        return self.d_h_m / 2

    @property
    def a_h_m(self):
        """hydraulic cross section [m^2]"""
        return self.r_h_m ** 2 * math.pi

    @property
    def k_m(self):
        """surface roughness [m]"""
        return self._k_m

    @property
    def v_dot_m3_s(self):
        """volumetric flow rate [m^3/s]"""
        return self.m_dot_kg_s / self.rho_kg_m3

    @property
    def u_m_s(self):
        """average velocity over the hydraulic cross section [m/s]"""
        return self.v_dot_m3_s / self.a_h_m

    @property
    def re_d(self):
        """The Reynolds number for flow in a circular tube [2, pp.491]"""
        return self.rho_kg_m3 * self.u_m_s * self.d_h_m / self.mu_kg_ms

    @property
    def nu_m_s(self):
        """kinematic viscosity [m^2/s]"""
        return self.mu_kg_ms / self.rho_kg_m3

    def _f_laminar(self):
        """
        :return: friction factor for fully developed laminar flow [2, pp. 495]
        """
        return 64 / self.re_d

    def _f_colebrook(self, f):
        """
        Colebrook equation for fully developed flow [2, pp. 494]

        :param float f: friction factor guess
        :return: friction factor
        """
        try:
            f = (1.0 / (-2.0 * math.log((self.k_m / self.d_h_m) / 3.72) + 2.51 / (self.re_d * f ** 0.5))) ** 2.0
            for i in range(20):
                f = (1.0 / (-2.0 * math.log((self.k_m / self.d_h_m) / 3.72) + 2.51 / (self.re_d * f ** 0.5))) ** 2.0
        except ValueError:
            f = 0
        return f

    def _f_turbulent(self, f):
        """
        :return: friction factor for turbulent fully developed flow
        """
        return self._f_colebrook(f)

    @property
    def f(self, f=0.03):
        """
        friction factor for laminar and turbulent fully developed flow

        :param float f: friction factor guess to use in Colebrook equation
        :return float: friction factor
        """
        re_d_c = 2300
        "critical reynolds number [2, pp. 491]"

        if self.re_d <= re_d_c:
            return self._f_laminar()
        if self.re_d > re_d_c:
            return self._f_turbulent(f)
        else:
            return 0.0
