
import scipy.linalg as la
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import scipy.special as sp

"""
Creating an entire pressure field based on the locations of various sources
"""
def pressure_field(positions,frequencies,
               time = 0.0,
               areas = [0.001],
               velocities = [0.01],
               strengths = [0.01],
               phases = [0],
               x_range = [-1,1],
               y_range = [-1,1],
               z_range = [-1,1],
               point_density = 100,
               directivity_distance = 1000,
               num_directivity_points = 10000,
               method = "Monopole Addition",
               dimensions = 2,
               directivity_only = False,
               directivity_plot_alone = False,
               show_plots = False,
               color_limits = [-100,100]):
    
    # Making all arrays that describe the sources be equal lengths
    num_sources = len(positions)
    positions = np.asarray(positions)
    
    if np.size(frequencies) == 1:
        frequencies = np.ones(num_sources) * frequencies
    
    if np.size(areas) == 1:
        areas = np.ones(num_sources) * areas
        
    if np.size(strengths) == 1:
        strengths = np.ones(num_sources) * strengths
        
    if np.size(phases) == 1:
        phases = np.ones(num_sources) * phases

    if np.size(velocities) == 1:
        velocities = np.ones(num_sources) * velocities

    time = complex(time)

    if dimensions == 1:
        numPoints_x = int(np.floor((x_range[1] - x_range[0]) * point_density))
        x = np.linspace(x_range[0],x_range[1],numPoints_x)
        x = x[x != 0]
        field_points = x.reshape(-1,1)

    elif dimensions == 2:
        numPoints_x = int(np.floor((x_range[1] - x_range[0]) * point_density))
        numPoints_y = int(np.floor((y_range[1] - y_range[0]) * point_density))
        x = np.linspace(x_range[0],x_range[1],numPoints_x)
        y = np.linspace(y_range[0],y_range[1],numPoints_y)

        grid = np.meshgrid(x,y)
        field_points = np.append(grid[0].reshape(-1,1),grid[1].reshape(-1,1),axis=1)
        X = grid[0]
        Y = grid[1]

    elif dimensions == 3:
        numPoints_x = int(np.floor((x_range[1] - x_range[0]) * point_density))
        numPoints_y = int(np.floor((y_range[1] - y_range[0]) * point_density))
        numPoints_z = int(np.floor((z_range[1] - z_range[0]) * point_density))
        x = np.linspace(x_range[0],x_range[1],numPoints_x)
        y = np.linspace(y_range[0],y_range[1],numPoints_y)
        z = np.linspace(z_range[0],z_range[1],numPoints_z)

        grid = np.meshgrid(x,y,z)
        field_points = np.append(grid[0].reshape(-1,1),np.append(grid[1].reshape(-1,1),grid[2].reshape(-1,1),axis = 1),axis=1)
        X = grid[0]
        Y = grid[1]
        Z = grid[2]
    
    if method == "Rayleigh":
        
        if not directivity_only:
            pressure_field = rayleigh(positions,areas,velocities,phases,field_points,frequencies,time)
            pressure_field = pressure_field.reshape(-1,len(x)) # It's the number of points in the x-direction that you use here
        else:
            pressure_field = 0
        
        # Getting the directivity at a given distance. Default is 1000 meters away
        if not dimensions == 1:
            directivity_points, theta = define_arc(directivity_distance,num_directivity_points)
            directivity = np.abs(rayleigh(positions,areas,velocities,phases,directivity_points,frequencies,time))
            directivity = directivity / np.max(directivity)
    
    elif method == "Monopole Addition":
        
        if not directivity_only:
            pressure_field = monopole_field(positions,frequencies,strengths,phases,field_points,time)
            pressure_field = pressure_field.reshape(-1,len(x))
        else:
            pressure_field = 0
        
        # Getting the directivity at a given distance. Default is 1000 meters away
        if not dimensions == 1:
            directivity_points, theta = define_arc(directivity_distance,num_directivity_points)
            directivity = np.abs(monopole_field(positions,frequencies,strengths,phases,directivity_points,time))
            directivity = directivity / np.max(directivity)
    
    # Only show plots if you calculated the entirie pressure field
    if dimensions == 1:
        plot_1D(x,pressure_field,positions,show_plots,color_limits,directivity_only)
        theta = 0
        directivity = 0

    if dimensions == 2:
        plot_2D(X,Y,pressure_field,positions,method,theta,directivity,show_plots,directivity_only,directivity_distance,directivity_plot_alone,color_limits)

    if dimensions == 3:
        plot_3D(X,Y,Z,pressure_field,positions,method,theta,directivity,show_plots,directivity_only,directivity_distance,directivity_plot_alone,color_limits)
        
    return pressure_field, directivity, theta

def plot_1D(x,pressure_field,positions,show_plots,color_limits,directivity_only):

    if show_plots and not directivity_only:
        # Defining the figure
        fig = plt.figure()
        fig.set_size_inches(8,8)

        # Plotting the real part
        ax = fig.add_subplot(221)
        ax.plot(x,np.real(pressure_field)[0,:])
        ax.scatter(positions[:,0],np.zeros(len(positions[:,0])),color = "black",marker = "o",facecolors = "white",linewidth = 1.5,s = 10)
        ax.set_aspect('auto')
        ax.set_title("Real Part")
        ax.set_xlabel("X (m)")
        ax.set_ylabel("Re\{Pressure\}")
        ax.set_ylim(color_limits[0],color_limits[1])
        ax.grid("on")

        # Plotting the imaginary part
        ax = fig.add_subplot(223)
        ax.plot(x,np.imag(pressure_field)[0,:])
        ax.scatter(positions[:,0],np.zeros(len(positions[:,0])),color = "black",marker = "o",facecolors = "white",linewidth = 1.5,s = 10)
        ax.set_aspect('auto')
        ax.set_title("Imaginary Part")
        ax.set_xlabel("X (m)")
        ax.set_ylabel("Im\{Pressure\}")
        ax.set_ylim(color_limits[0],color_limits[1])
        ax.grid("on")

        # Plotting the magnitude
        ax = fig.add_subplot(222)
        ax.plot(x,np.abs(pressure_field)[0,:])
        ax.scatter(positions[:,0],np.zeros(len(positions[:,0])),color = "black",marker = "o",facecolors = "white",linewidth = 1.5,s = 10)
        ax.set_aspect('auto')
        ax.set_title("Magnitude")
        ax.set_xlabel("X (m)")
        ax.set_ylabel("|Pressure|")
        ax.set_ylim(color_limits[0]*0.05,color_limits[1])
        ax.grid("on")
        
        fig.tight_layout(pad = 0.5)
        fig.show()
        

def plot_2D(X,Y,pressure_field,positions,method,theta,directivity,show_plots,directivity_only,directivity_distance,directivity_plot_alone,color_limits):

    if show_plots and not directivity_only:
        # Defining the figure
        fig, ax = plt.subplots(2,2)
        fig.set_size_inches(8,8)

        # Plotting the real part
        c = ax[0,0].pcolormesh(X,Y,np.real(pressure_field),shading = "gouraud",cmap = "RdBu",vmin = color_limits[0],vmax = color_limits[1])
        ax[0,0].scatter(positions[:,0],positions[:,1],color = "black",marker = "o",facecolors = "white",linewidth = 1.5,s = 10)
        ax[0,0].set_aspect('equal')
        ax[0,0].set_title("Real Part")
        ax[0,0].set_xlabel("X (m)")
        ax[0,0].set_ylabel("Y (m)")
        fig.colorbar(c,ax = ax[0,0],fraction=0.046, pad=0.04)

        # Plotting the imaginary part
        c = ax[1,0].pcolormesh(X,Y,np.imag(pressure_field),shading = "gouraud",cmap = "RdBu",vmin = color_limits[0],vmax = color_limits[1])
        ax[1,0].scatter(positions[:,0],positions[:,1],color = "black",marker = "o",facecolors = "white",linewidth = 1.5,s = 10)
        ax[1,0].set_aspect('equal')
        ax[1,0].set_title("Imaginary Part")
        ax[1,0].set_xlabel("X (m)")
        ax[1,0].set_ylabel("Y (m)")
        fig.colorbar(c,ax = ax[1,0],fraction=0.046, pad=0.04)

        # Plotting the magnitude
        c = ax[0,1].pcolormesh(X,Y,np.abs(pressure_field),shading = "gouraud",cmap = "jet",vmin = 0,vmax = color_limits[1])
        ax[0,1].scatter(positions[:,0],positions[:,1],color = "black",marker = "o",facecolors = "white",linewidth = 1.5,s = 10)
        ax[0,1].set_aspect('equal')
        ax[0,1].set_title("Pressure Magnitude")
        ax[0,1].set_xlabel("X (m)")
        ax[0,1].set_ylabel("Y (m)")
        fig.colorbar(c,ax = ax[0,1],fraction=0.046, pad=0.04)

        # Plotting the directivity
        ax[1,1].axis("off")
        ax = fig.add_subplot(224,projection = 'polar')
        c = ax.plot(theta,10*np.log10(directivity))
        ax.set_rmin(-20)
        ax.set_rticks([0,-5,-10,-15,-20])
        ax.set_aspect('equal')
        ax.set_title(str("Directivity (dB) at {0} m".format(directivity_distance)))

        fig.show()

        
        if method == "Rayleigh":
            ax.set_thetamin(-90)
            ax.set_thetamax(90)
        
        fig.tight_layout(pad = 0.5)
        fig.show()
        
    if directivity_plot_alone:
        fig, ax = plt.subplots(1,2,subplot_kw={'projection': 'polar'})
        ax[0].plot(theta,directivity)
        ax[0].set_title("Normalized Directivity")
        
        ax[1].plot(theta,10*np.log10(directivity))
        ax[1].set_title("Normalized Directivity (dB)")
        ax[1].set_rmin(-20)
        ax[1].set_rticks([0,-5,-10,-15,-20])
        
        fig.tight_layout()
        fig.set_size_inches(8,8)
        fig.show()

def plot_3D(X,Y,Z,pressure_field,positions,method,theta,directivity,show_plots,directivity_only,directivity_distance,directivity_plot_alone,color_limits):

    if show_plots and not directivity_only:
        # Defining the figure
        fig = plt.figure()
        fig.set_size_inches(8,8)

        # Adding opacity to the colormap
        cmap = plt.cm.RdBu_r
        my_RdBu = cmap(np.arange(cmap.N))
        my_RdBu[:,-1] = np.linspace(-1,1,cmap.N)
        my_RdBu[:,-1] = np.abs(my_RdBu[:,-1])
        my_RdBu = colors.ListedColormap(my_RdBu)

        cmap = plt.cm.jet
        my_jet = cmap(np.arange(cmap.N))
        my_jet[:,-1] = np.linspace(0,1,cmap.N)
        my_jet = colors.ListedColormap(my_jet)

        # Plotting the real part
        ax = fig.add_subplot(221,projection = '3d')
        c = ax.scatter(X,Y,Z,np.real(pressure_field), c = np.real(pressure_field),cmap = my_RdBu,vmin = color_limits[0],vmax = color_limits[1],edgecolors = None)
        ax.scatter(positions[:,0],positions[:,1],positions[:,2],color = "black",marker = "o",facecolors = "white",linewidth = 1.5,s = 10)
        ax.set_aspect('auto')
        ax.set_title("Real Part")
        ax.set_xlabel("X (m)")
        ax.set_ylabel("Y (m)")
        fig.colorbar(c,ax = ax,fraction=0.046, pad=0.04)

        # Plotting the imaginary part
        ax = fig.add_subplot(223,projection = '3d')
        c = ax.scatter(X,Y,Z,np.imag(pressure_field), c = np.imag(pressure_field),cmap = my_RdBu,vmin = color_limits[0],vmax = color_limits[1],edgecolors = None)
        ax.scatter(positions[:,0],positions[:,1],positions[:,2],color = "black",marker = "o",facecolors = "white",linewidth = 1.5,s = 10)
        ax.set_aspect('auto')
        ax.set_title("Imaginary Part")
        ax.set_xlabel("X (m)")
        ax.set_ylabel("Y (m)")
        fig.colorbar(c,ax = ax,fraction=0.046, pad=0.04)

        # Plotting the magnitude
        ax = fig.add_subplot(222,projection = '3d')
        c = ax.scatter(X,Y,Z,np.abs(pressure_field), c = np.abs(pressure_field),cmap = my_jet,vmin = 0,vmax = color_limits[1],edgecolors = None)
        ax.scatter(positions[:,0],positions[:,1],positions[:,2],color = "black",marker = "o",facecolors = "white",linewidth = 1.5,s = 10)
        ax.set_aspect('auto')
        ax.set_title("Magnitude")
        ax.set_xlabel("X (m)")
        ax.set_ylabel("Y (m)")
        fig.colorbar(c,ax = ax,fraction=0.046, pad=0.04)

        # Plotting the directivity
        ax = fig.add_subplot(224,projection = 'polar')
        c = ax.plot(theta,10*np.log10(directivity))
        ax.set_rmin(-20)
        ax.set_rticks([0,-5,-10,-15,-20])
        ax.set_aspect('equal')
        ax.set_title(str("Directivity (dB) at {0} m".format(directivity_distance)))

        fig.show()

        
        if method == "Rayleigh":
            ax.set_thetamin(-90)
            ax.set_thetamax(90)
        
        fig.tight_layout(pad = 0.5)
        fig.show()
        
    if directivity_plot_alone:
        fig, ax = plt.subplots(1,2,subplot_kw={'projection': 'polar'})
        ax[0].plot(theta,directivity)
        ax[0].set_title("Normalized Directivity")
        
        ax[1].plot(theta,10*np.log10(directivity))
        ax[1].set_title("Normalized Directivity (dB)")
        ax[1].set_rmin(-20)
        ax[1].set_rticks([0,-5,-10,-15,-20])
        
        fig.tight_layout()
        fig.set_size_inches(8,8)
        fig.show()

"""
Creating a field from a monopole
"""

def monopole_field(positions,frequencies,strengths,phases,field_points,time):
    
    # Convert everything to a numpy array
    positions = np.asarray(positions)
    strengths = np.asarray(strengths)
    phases = np.asarray(phases)
    field_points = np.asarray(field_points)
    
    # Initialize the responses
    responses = np.zeros([len(field_points),1], dtype = complex)
    
    # Define constants
    c = 343 # Phase speed in air
    rho_0 = 1.2 # Density of air
    
    for i in range(len(field_points)):
        
        # Define the current field point
        current_field_point = field_points[i,:]
        
        # Loop over all sources for a particular theta
        for j in range(len(strengths)):
            
            # Define the current source
            current_source_location = positions[j,:]
            current_source_strength = strengths[j]
            current_source_phase = phases[j]
            current_source_frequency = frequencies[j]
            #print(current_source_phase)
            
            # Define frequency-dependent quantities
            omega = 2 * np.pi * current_source_frequency # angular frequency
            k = omega / c # wavenumber
            
            # Get the distance between the field point and the source
            distance = get_distance(current_source_location,current_field_point)
            
            # get contribution to a theta location from an individual source
            A = 1j*rho_0*c*k/(4*np.pi) * current_source_strength
            current_source_impact = A * np.exp(-1j*k*distance)/distance * np.exp(1j * current_source_phase) * np.exp(1j*omega*time)
            
            responses[i] = responses[i] + current_source_impact
            
    return responses

"""
Perform Rayleigh Integration
"""

def rayleigh(positions,areas,velocities,phases,field_points,frequencies,time):
    
    # Convert everything to a numpy array
    positions = np.asarray(positions)
    areas = np.asarray(areas)
    velocities = np.asarray(velocities)
    phases = np.asarray(phases)
    field_points = np.asarray(field_points)
    
    # Initialize the responses
    responses = np.zeros([len(field_points),1], dtype = complex)
    
    # Define constants
    c = 343 # Phase speed in air
    rho_0 = 1.2 # Density of air
    
    for i in range(len(field_points)):
        
        # Define the current field point
        current_field_point = field_points[i,:]
        
        # Loop over all sources for a particular theta
        for j in range(len(velocities)):
            
            # Define the current source
            current_source_location = positions[j,:]
            current_source_velocity = velocities[j]
            current_source_phase = phases[j]
            current_source_area = areas[j]
            current_source_frequency = frequencies[j]
            
            # Define frequency-dependent quantities
            omega = 2 * np.pi * current_source_frequency # angular frequency
            k = omega / c # wavenumber
            
            # Get the distance between the field point and the source
            distance = get_distance(current_source_location,current_field_point)
            
            # get contribution to a theta location from an individual source
            current_source_impact = (1j * omega * rho_0 / (2 * np.pi) * 
                                    current_source_velocity * 
                                    np.exp(-1j * k * distance)/distance * 
                                    np.exp(1j*current_source_phase) * np.exp(1j*omega*time) * 
                                    current_source_area)
            
            responses[i] = responses[i] + current_source_impact
            
    return responses

"""
Get the distance between two 2D points
"""
def get_distance(source_point,field_point):

    if len(source_point) == 3 and len(field_point) == 1:
        field_point = np.array([field_point[0],0.0,0.0])

    if len(source_point) == 3 and len(field_point) == 2:
        field_point = np.array([field_point[0],field_point[1],0.0])

    return la.norm(field_point - source_point)

"""
Define an arc for whatever reasons you may want to do so
"""
def define_arc(radius,numPoints,theta_lims = (0,360)):
    theta_min = theta_lims[0] * np.pi/180
    theta_max = theta_lims[1] * np.pi/180
    theta = np.linspace(theta_min,theta_max,numPoints)
    
    points = np.empty([0,2])
    
    for i in range(0,numPoints):
        points = np.append(points,radius * np.array([[np.cos(theta[i]), np.sin(theta[i])]]),axis = 0)
        
    return points, theta