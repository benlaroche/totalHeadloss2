from pipeLosses import flow_properties, epsilon_qty, pipe_section, minor_loss_coefficients, sch_40_pipe_id_m, \
    minor_loss_coefficient_reducers

sections = {
    "section 1": pipe_section(
        flow=flow_properties(
            flow_m3_s=0.0007571,
            d_h_m=sch_40_pipe_id_m["1"]),
        l_m=2.779776,
        epsilon_qty_list=[epsilon_qty(minor_loss_coefficients["Elbow, Flanged Regular 90o"], 2),
                          epsilon_qty(minor_loss_coefficients["Tee, Threaded, Dividing Line Flow"], 2),
                          epsilon_qty(minor_loss_coefficients["Tee, Threaded, Dividing Branch Flow"], 1)
                          ]
    ),
    "section 2": pipe_section(
        flow=flow_properties(
            flow_m3_s=0.0003155,
            d_h_m=sch_40_pipe_id_m["1"]),
        l_m=3.112008,
        epsilon_qty_list=[epsilon_qty(minor_loss_coefficients["Elbow, Flanged Regular 90o"], 5),
                          epsilon_qty(minor_loss_coefficients["Tee, Threaded, Dividing Line Flow"], 2)
                          ],
        additional_loss_m={
            "Condensate Cooler": 0.073152,
            "balancing valve": 4.673489734248714 - 0.5052507698115278
        }
    ),
    "section 3": pipe_section(
        flow=flow_properties(
            flow_m3_s=0.0004416,
            d_h_m=sch_40_pipe_id_m["1"]),
        l_m=3.590544,
        epsilon_qty_list=[epsilon_qty(minor_loss_coefficients["Tee, Threaded, Dividing Branch Flow"], 1),
                          epsilon_qty(minor_loss_coefficients["Tee, Threaded, Dividing Line Flow"], 1)
                          ]
    ),
    "section 4": pipe_section(
        flow=flow_properties(
            flow_m3_s=0.0001262,
            d_h_m=sch_40_pipe_id_m["1"]),
        l_m=0.71628,
        epsilon_qty_list=[epsilon_qty(minor_loss_coefficients["Elbow, Threaded Long Radius 90o"], 5),
                          epsilon_qty(minor_loss_coefficients["Tee, Threaded, Dividing Line Flow"], 2),
                          epsilon_qty(minor_loss_coefficients["Tee, Threaded, Dividing Branch Flow"], 1),
                          epsilon_qty(minor_loss_coefficient_reducers(sch_40_pipe_id_m["1"], sch_40_pipe_id_m["3/8"]),
                                      1)],
        additional_loss_m={
            "DA pump seal": 3.52044,
            "balancing valve": 0.3048
        }
    ),
    "section 4.1": pipe_section(
        flow=flow_properties(
            flow_m3_s=0.0001262,
            d_h_m=sch_40_pipe_id_m["3/8"]),
        l_m=0.219456,
        epsilon_qty_list=[epsilon_qty(minor_loss_coefficients["Elbow, Threaded Regular 90o"], 2),
                          epsilon_qty(minor_loss_coefficient_reducers(sch_40_pipe_id_m["3/8"], sch_40_pipe_id_m["1"]),
                                      1)
                          ]
    ),
    "section 5": pipe_section(
        flow=flow_properties(
            flow_m3_s=0.0003155,
            d_h_m=sch_40_pipe_id_m["1"]),
        l_m=4.696968,
        epsilon_qty_list=[epsilon_qty(minor_loss_coefficients["Elbow, Threaded Regular 90o"], 2),
                          epsilon_qty(minor_loss_coefficients["Tee, Threaded, Dividing Line Flow"], 1),
                          epsilon_qty(minor_loss_coefficient_reducers(sch_40_pipe_id_m["1"], sch_40_pipe_id_m["1/2"]),
                                      1)
                          ]
    ),
    "section 5.1": pipe_section(
        flow=flow_properties(
            flow_m3_s=0.0003155,
            d_h_m=sch_40_pipe_id_m["1/2"]),
        l_m=5.047488,
        epsilon_qty_list=[epsilon_qty(minor_loss_coefficients["Elbow, Threaded Regular 90o"], 2),
                          epsilon_qty(minor_loss_coefficient_reducers(sch_40_pipe_id_m["1/2"], sch_40_pipe_id_m["3/8"]),
                                      1),
                          epsilon_qty(minor_loss_coefficient_reducers(sch_40_pipe_id_m["1/2"], sch_40_pipe_id_m["1"]),
                                      1)
                          ],
        additional_loss_m={
            "balancing valve": 4.673489734248714 - 2.062616851042489
        }
    ),
    "section 5.2": pipe_section(
        flow=flow_properties(
            flow_m3_s=0.0003155,
            d_h_m=sch_40_pipe_id_m["3/8"]),
        l_m=0.201168,
        epsilon_qty_list=[epsilon_qty(minor_loss_coefficient_reducers(sch_40_pipe_id_m["3/8"], sch_40_pipe_id_m["1/2"]),
                                      1)
                          ],
        additional_loss_m={
            "distillate cooler": 0.01524
        }
    ),
    "section 6": pipe_section(
        flow=flow_properties(
            flow_m3_s=0.0004416,
            d_h_m=sch_40_pipe_id_m["1"]),
        l_m=3.983736,
        epsilon_qty_list=[epsilon_qty(minor_loss_coefficients["Tee, Threaded, Dividing Line Flow"], 1)
                          ]
    ),
    "section 7": pipe_section(
        flow=flow_properties(
            flow_m3_s=0.0007571,
            d_h_m=sch_40_pipe_id_m["1"]),
        l_m=3.45948,
        epsilon_qty_list=[epsilon_qty(minor_loss_coefficients["Elbow, Threaded Regular 90o"], 4),
                          epsilon_qty(minor_loss_coefficients["Tee, Threaded, Dividing Line Flow"], 1),
                          epsilon_qty(minor_loss_coefficient_reducers(sch_40_pipe_id_m["1"], sch_40_pipe_id_m["1 1/4"]),
                                      1)
                          ],
        additional_loss_m={
            "cooling heat sink": 1.258824,
            "balancing valve": 0.3048,  # 21.336 - 4.9782897342487145 + 0.3048,
        }
    ),
    "section 8": pipe_section(
        additional_loss_m={
            "pressure regulator outlet": -3,
        }
    ),
    "section 9": pipe_section(
        flow=flow_properties(
            flow_m3_s=0.0007571,
            d_h_m=sch_40_pipe_id_m["1"]),
        l_m=2.770632,
        epsilon_qty_list=[epsilon_qty(minor_loss_coefficients["Elbow, Threaded Regular 90o"], 3),
                          epsilon_qty(minor_loss_coefficients["Tee, Threaded, Dividing Line Flow"], 3),
                          epsilon_qty(minor_loss_coefficient_reducers(sch_40_pipe_id_m["1 1/4"], sch_40_pipe_id_m["1"]),
                                      1)
                          ]
    )
}

print("path 1-2-7-8-9:  " + str(
    + sections["section 1"].loss_m()
    + sections["section 2"].loss_m()
    + sections["section 7"].loss_m()
    + sections["section 8"].loss_m()
    + sections["section 9"].loss_m()
))

print("path 1-3-4-4.1-6-7-8-9:    " + str(
    + sections["section 1"].loss_m()
    + sections["section 3"].loss_m()
    + sections["section 4"].loss_m()
    + sections["section 4.1"].loss_m()
    + sections["section 6"].loss_m()
    + sections["section 7"].loss_m()
    + sections["section 8"].loss_m()
    + sections["section 9"].loss_m()
))

print("path 1-3-5-5.1-5.2-6-7-8-9:  " + str(
    + sections["section 1"].loss_m()
    + sections["section 3"].loss_m()
    + sections["section 5"].loss_m()
    + sections["section 5.1"].loss_m()
    + sections["section 5.2"].loss_m()
    + sections["section 6"].loss_m()
    + sections["section 7"].loss_m()
    + sections["section 8"].loss_m()
    + sections["section 9"].loss_m()
))
