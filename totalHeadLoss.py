from typing import List
from internalFlowProperties import internalFlowProperties
from minorLosses import minorLosses
from majorLosses import majorLosses

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
"nominal SCH 40 pipe inner diameter in meters. Dictionary as a function of Nominal size in inches"


class totalHeadLoss:
    """
    The total head loss in a piping network may be calculated as the sum of the major and minor losses. Its dimension
    is length and it represents the irreversible conversion of mechanical energy to heat [1, pp. 161]
    """
    def __init__(self, flow, l_m, epsilonQtyList, additional_loss_m = 0.0):
        """

        :param internalFlowProperties flow: flow properties object for this length of pipe
        :param float l_m: length of pipe [m]
        :param [epsilonQty] epsilonQtyList: list of minor loss coefficients and their quantity
        :param float additional_loss_m: any additional losses to be added such as flow balancing valves or known losses
        """
        self._majorLoss = majorLosses(flow, l_m)
        self._minor_loss = minorLosses(flow, epsilonQtyList)
        self._additional_loss = additional_loss_m

    @property
    def major_loss_m(self):
        return self._majorLoss.major_loss_m

    @property
    def minor_losses_m(self):
        return self._minor_loss.minor_losses_m

    @property
    def additional_loss_m(self):
        return self._additional_loss

    @property
    def total_head_loss_m(self):
        return self.minor_losses_m + self.major_loss_m + self.additional_loss_m
