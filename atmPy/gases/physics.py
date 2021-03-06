from scipy import constants as _const
import numpy as _np

class Ideal_Gas_Classic(object):
    """units:
        pressure:           Pa
        temp:               K
        density_mass:       g/m^3
        density_molar:      mol/m^3
        density_molecule:   number/m^3
    """

    def __init__(self):
        self.updated()
        self.R = _const.physical_constants['molar gas constant']
        self.N_a = _const.physical_constants['Avogadro constant']
        self.molecular_mass_air = 28.966
 #g/mol

    def updated(self):
        self.__pressure = None
        self.__volume = None
        self.__temp = None
        self.__n_mole = None

        self.__density_molar = None
        self.__density_mass = None
        self.__density_number = None

    @property
    def density_mass(self):
        if not _np.any(self.__density_mass):
            self.__density_mass = self.density_molar * self.molecular_mass_air
        return self.__density_mass

    @property
    def density_molar(self):
        if not _np.any(self.__density_molar):
            self.__density_molar = self.__pressure / (self.R[0] * self.__temp)
        return self.__density_molar

    @density_molar.setter
    def density_molar(self,value):
        self.__density_molar = value

    @property
    def density_number(self):
        if not _np.any(self.__density_number):
            self.__density_number = self.density_molar * self.N_a[0]
        return self.__density_number

    @density_number.setter
    def density_number(self, value):
        self.__density_number = value

    @property
    def pressure(self):
        if not _np.any(self.__pressure):
            self.__pressure = self.__n_mole * self.R[0] * self.__temp / self.__volume
        return self.__pressure
    @pressure.setter
    def pressure(self,value):
        self.__pressure = value

    @property
    def n_mole(self):
        if not _np.any(self.__n_mole):
            self.__n_mole = self.__pressure / (self.R[0] * self.__temp / self.__volume)
        return self.__n_mole

    @n_mole.setter
    def n_mole(self, value):
        self.__n_mole = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    @property
    def temp(self):
        return self.__temp

    @temp.setter
    def temp(self, value):
        self.__temp = value
