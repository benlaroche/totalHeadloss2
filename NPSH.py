from pyXSteam.XSteam import XSteam
from pipeLosses import flow_properties,sch_40_pipe_id_m

steamTable = XSteam(XSteam.UNIT_SYSTEM_BARE)
p_v = steamTable.psat_t(294.261) * 1000000
p_v1 = steamTable.psat_t(373.15) * 1000000
_g_m_s2 = 9.81

flow = flow_properties(12 * 6.309E-5, sch_40_pipe_id_m["1 1/4"])
flow1 = flow_properties(100 * 6.309E-5, sch_40_pipe_id_m["3"])


def npsha(p_i_pa, rho_kg_m3, v_i_m_s, p_v_pa):
    inlet_p = p_i_pa / (_g_m_s2 * rho_kg_m3)
    inlet_v = v_i_m_s ** 2 / (2 * _g_m_s2)
    inlet_vp = p_v_pa / (rho_kg_m3 * _g_m_s2)
    print("inlet_p: " + str(inlet_p))
    print("inlet_v: " + str(inlet_v))
    print("inlet_vp: " + str(inlet_vp))
    print("NPSHa: " + str(inlet_p + inlet_v - inlet_vp))
    print()


npsha((11.55*1 - 3.42) * 2988.98+101325, 1000, flow.u_m_s(), p_v)
npsha(5.9 * 2988.98+101325, 1000, flow1.u_m_s(), p_v1)
