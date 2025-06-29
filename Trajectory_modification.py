import numpy as np
import matplotlib.pyplot as plt

def Trajectory_modification(points_trajectoire, entrees_random_s):
    """
    Modifies a trajectory based on various parameters provided in `entrees_random_s`.

    Args:
        points_trajectoire (ndarray): Input trajectory points as a numpy array.
        entrees_random_s (list): List of random input parameters.

    Returns:
        ndarray: Modified trajectory points.
    """
    # Extract parameters from entrees_random_s
    (niveau_alpha, niveau_signe_alpha, niveau_teta_LB, niveau_signe_teta,
     niveau_rap_x_th, niveau_rap_y_th, niveau_rayon, niveau_sigma_p) = entrees_random_s

    # Define constants
    max_alpha_inclin_vertic_grapheme_p = np.pi / 10
    max_teta_LB = np.pi / 18
    max_rap_x_th, max_rap_y_th = 0.7, 0.7
    max_rayon, max_sigma_p = 2, 2

    min_alpha_inclin_vertic_grapheme_p, min_teta_LB = 0, 0
    min_rap_x_th, min_rap_y_th = 0.325, 0.325
    min_rayon, min_sigma_p = 0, 0.001

    # Calculate parameters
    signe_alpha = -1 if niveau_signe_alpha < 0.5 else 1
    alpha_inclin_vertic_grapheme_p = signe_alpha * (
        (max_alpha_inclin_vertic_grapheme_p - min_alpha_inclin_vertic_grapheme_p) * niveau_alpha + 
        min_alpha_inclin_vertic_grapheme_p
    )

    signe_teta = -1 if niveau_signe_teta < 0.5 else 1
    teta_LB = signe_teta * (
        (max_teta_LB - min_teta_LB) * niveau_teta_LB + min_teta_LB
    )

    rap_x_th = (max_rap_x_th - min_rap_x_th) * niveau_rap_x_th + min_rap_x_th
    rap_y_th = (max_rap_y_th - min_rap_y_th) * niveau_rap_y_th + min_rap_y_th
    rayon = (max_rayon - min_rayon) * niveau_rayon + min_rayon
    sigma_p = (max_sigma_p - min_sigma_p) * niveau_sigma_p + min_sigma_p

    # Filter valid points
    pure_points_trajectoire = points_trajectoire[(points_trajectoire[:, 0] != 0) | (points_trajectoire[:, 1] != 0)]

    # Determine min and max values of points
    if pure_points_trajectoire.size > 0:
        max_x_points = pure_points_trajectoire[:, 0].max()
        min_x_points = pure_points_trajectoire[:, 0].min()
        max_y_points = pure_points_trajectoire[:, 1].max()
        min_y_points = pure_points_trajectoire[:, 1].min()
    else:
        max_x_points = min_x_points = max_y_points = min_y_points = 0

    # Modify points
    for i in range(points_trajectoire.shape[0]):
        x, y = points_trajectoire[i]
        if x != 0 or y != 0:
            points_trajectoire[i] = [x, y]

    # Prepare for visualization
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.axis('equal')
    plt.title('Original Trajectory')
    plt.plot(points_trajectoire[:, 0], points_trajectoire[:, 1], 'k.')

    # Further modifications (placeholder for now, add as needed)

    # Show results
    plt.subplot(2, 1, 2)
    plt.axis('equal')
    plt.title('Modified Trajectory')
    plt.plot(points_trajectoire[:, 0], points_trajectoire[:, 1], 'b.')
    plt.show()

    return points_trajectoire

# Example usage
# Sample trajectory points
points = np.array([
    [1, 2], [2, 3], [3, 5], [0, 0], [4, 5], [5, 6], [0, 0]
])

# Random input parameters
random_inputs = [0.5, 1, 0.4, 1, 0.6, 0.7, 0.3, 0.2]

# Call the function
modified_points = Trajectory_modification(points, random_inputs)