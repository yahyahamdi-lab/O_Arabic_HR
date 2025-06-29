import numpy as np
from scipy.ndimage import gaussian_filter1d

def resample_2d_points(points_segment, fixed_num_points):
    """
    Resample a 2D point sequence to a fixed number of points while preserving shape
    
    Args:
        points_segment: numpy array of shape (N, 2) containing 2D points
        fixed_num_points: desired number of points in output
        
    Returns:
        numpy array of shape (fixed_num_points, 2) with resampled points
    """
    # Initial filtering
    points_segment = smooth_points(points_segment, radius=2, sigma=0.4)
    
    # Calculate cumulative distances along the path
    distances = np.sqrt(np.sum(np.diff(points_segment, axis=0)**2, axis=1))
    cum_distances = np.insert(np.cumsum(distances), 0, 0)
    total_length = cum_distances[-1]
    
    # Create evenly spaced distances for resampling
    if fixed_num_points > 1:
        sample_distances = np.linspace(0, total_length, fixed_num_points)
    else:
        sample_distances = np.array([total_length/2])
    
    # Linearly interpolate points at these distances
    resampled_points = []
    for dist in sample_distances:
        idx = np.searchsorted(cum_distances, dist) - 1
        idx = max(0, min(idx, len(points_segment)-2))
        
        if idx < 0 or idx >= len(points_segment)-1:
            resampled_points.append(points_segment[-1])
            continue
            
        segment_start = points_segment[idx]
        segment_end = points_segment[idx+1]
        segment_length = distances[idx]
        
        if segment_length > 0:
            t = (dist - cum_distances[idx]) / segment_length
            new_point = segment_start + t * (segment_end - segment_start)
        else:
            new_point = segment_start
            
        resampled_points.append(new_point)
    
    resampled_points = np.array(resampled_points)
    
    # Final smoothing
    resampled_points = smooth_points(resampled_points, radius=2, sigma=0.4)
    
    return resampled_points

def smooth_points(points, radius=2, sigma=0.4):
    """Apply Gaussian smoothing to a sequence of points"""
    if len(points) <= 1:
        return points.copy()
    
    # Pad the array for boundary conditions
    padded = np.pad(points, ((radius, radius), (0, 0)), mode='edge')
    
    # Apply Gaussian filter to each dimension
    smoothed = np.zeros_like(points)
    for dim in range(2):
        smoothed[:, dim] = gaussian_filter1d(
            padded[:, dim], 
            sigma=sigma, 
            mode='nearest'
        )[radius:-radius]
    
    return smoothed


# Example usage
if __name__ == "__main__":
    # Create a sample curve (semi-circle)
    theta = np.linspace(0, np.pi, 50)
    x = np.cos(theta)
    y = np.sin(theta)
    original_points = np.column_stack((x, y))
    
    # Resample to 20 points
    resampled = resample_2d_points(original_points, 20)
    
    print(f"Original points shape: {original_points.shape}")
    print(f"Resampled points shape: {resampled.shape}")
    print("First 5 resampled points:")
    print(resampled[:5])