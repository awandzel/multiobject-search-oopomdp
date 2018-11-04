'''
    Created by awandzel on 10/30/18.
'''

class PomcpParmeters:
    def __init__(self, maxSamples, maxActions, pomcpHeight, pomcpReinvigorate, pomcpReinvigorateSamples, pomcpExploration, pomcpDiscount):
        self.maxSamples = maxSamples
        self.maxActions = maxActions
        self.pomcpHeight = pomcpHeight
        self.pomcpReinvigorate = pomcpReinvigorate
        self.pomcpReinvigorateSamples = pomcpReinvigorateSamples
        self.pomcpExploration = pomcpExploration
        self.pomcpDiscount = pomcpDiscount

class PompdParameters:
    def __init__(self, objectReward, actionCost):
        self.objectReward = objectReward
        self.actionCost = actionCost

class ObservationModelParameters:
    def __init__(self, observationAccuracy, sdvForEventA, visionDepth, betaV, gammaV, alphaV, betaNV, gammaNV, alphaNV):
        self.observationAccuracy = observationAccuracy
        self.sdvForEventA = sdvForEventA
        self.visionDepth = visionDepth
        self.betaV = betaV
        self.gammaV = gammaV
        self.alphaV = alphaV
        self.betaNV = betaNV
        self.gammaNV = gammaNV
        self.alphaNV = alphaNV

class LanguageParameters:
    def __init__(self, adversarial, psi):
        self.adversarial = adversarial
        self.psi = psi


# helper data structure
class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return 37 * (self.x + self.y)

    def __eq__(self, other):
        if other == None or self.__class__ != other.__class__: return False
        if not isinstance(other, Location): return False

        return other.x == self.x and other.y == self.y

    def __str__(self):
        return "x=" + str(self.x) + ", " + "y=" + str(self.y)











