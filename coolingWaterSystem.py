from totalHeadLoss import totalHeadLoss, sch_40_pipe_id_m
from internalFlowProperties import internalFlowProperties
from minorLosses import epsilonQty, epsilons

k_m = 0.015e-3
"surface roughness for SS pipe"
mu_kg_ms = 10.0e-3
"absolute viscosity for sub-cooled water"
rho_kg_m3 = 1000.0
"density of sub-cooled water"

section_1 = totalHeadLoss(internalFlowProperties(m_dot_kg_s=0.75708,
                                                 d_h_m=sch_40_pipe_id_m['1'],
                                                 rho_kg_m3=rho_kg_m3,
                                                 mu_kg_ms=mu_kg_ms,
                                                 k_m=k_m),
                          l_m=2.779776,
                          epsilonQtyList=[epsilonQty(epsilons["Elbow, Flanged Regular 90o"], 2),
                                          epsilonQty(epsilons["Tee, Threaded, Dividing Line Flow"], 2),
                                          epsilonQty(epsilons["Tee, Threaded, Dividing Branch Flow"], 1)
                                          ])

section_2 = totalHeadLoss(internalFlowProperties(m_dot_kg_s=0.31545,
                                                 d_h_m=sch_40_pipe_id_m['1'],
                                                 rho_kg_m3=rho_kg_m3,
                                                 mu_kg_ms=mu_kg_ms,
                                                 k_m=k_m),
                          l_m=3.112008,
                          epsilonQtyList=[epsilonQty(epsilons["Elbow, Flanged Regular 90o"], 5),
                                          epsilonQty(epsilons["Tee, Threaded, Dividing Line Flow"], 2)
                                          ])

section_3 = totalHeadLoss(internalFlowProperties(m_dot_kg_s=0.31545,
                                                 d_h_m=sch_40_pipe_id_m['1'],
                                                 rho_kg_m3=rho_kg_m3,
                                                 mu_kg_ms=mu_kg_ms,
                                                 k_m=k_m),
                          l_m=3.590544,
                          epsilonQtyList=[epsilonQty(epsilons["Elbow, Flanged Regular 90o"], 5),
                                          epsilonQty(epsilons["Tee, Threaded, Dividing Line Flow"], 2)
                                          ])

print("path 1-2-7-8-9:  " + str(section_1.total_head_loss_m +
                                section_2.total_head_loss_m +
                                section_3.total_head_loss_m))

print("path 1-3-4-4.1-6-7-8-9:    " + str())

print("path 1-3-5-5.1-5.2-6-7-8-9:  " + str())
