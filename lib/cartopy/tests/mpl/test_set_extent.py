# (C) British Crown Copyright 2011 - 2012, Met Office
#
# This file is part of cartopy.
#
# cartopy is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# cartopy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with cartopy.  If not, see <http://www.gnu.org/licenses/>.

from matplotlib.testing.decorators import cleanup
import matplotlib.pyplot as plt
import numpy as np
from numpy.testing import assert_array_almost_equal

import cartopy.crs as ccrs

from cartopy.tests.mpl import image_comparison


@cleanup
def test_extents():
    # tests that one can set the extents of a map in a variety of coordinate systems, for a variety
    # of projection
    uk = [-12.5, 4, 49, 60]
    uk_crs = ccrs.Geodetic()
    
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_extent(uk, crs=uk_crs)
#    ax.coastlines() # <- enable to see what is going on (and to make sure it is a plot of the uk)
    assert_array_almost_equal(ax.viewLim.get_points(), np.array([[-12.5,  49. ], [  4. ,  60. ]]))
    
    ax = plt.axes(projection=ccrs.NorthPolarStereo())
    ax.set_extent(uk, crs=uk_crs)
#    ax.coastlines() # <- enable to see what is going on (and to make sure it is a plot of the uk)
    assert_array_almost_equal(ax.viewLim.get_points(), 
                              np.array([[-1034046.22566261, -4765889.76601514],
                                        [  333263.47741164, -3345219.0594531 ]])
                              )
    
    # given that we know the PolarStereo coordinates of the UK, try using those in a PlateCarree plot
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_extent([-1034046, 333263, -4765889, -3345219], crs=ccrs.NorthPolarStereo())
#    ax.coastlines() # <- enable to see what is going on (and to make sure it is a plot of the uk)
    assert_array_almost_equal(ax.viewLim.get_points(), 
                              np.array([[-17.17698577,  48.21879707],
                                        [  5.68924381, 60.54218893]])
                              )
    

if __name__=='__main__':
    import nose
    nose.runmodule(argv=['-s','--with-doctest'], exit=False)
    