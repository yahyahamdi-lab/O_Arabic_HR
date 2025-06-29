import numpy as np

def linear_filter(points, radius=2, sigma_p=0.4):
    """
    Apply linear filtering using a Gaussian sliding window
    
    Args:
        points: Input array (1D or 2D) to be filtered
        radius: Radius of the Gaussian window
        sigma_p: Standard deviation of the Gaussian
        
    Returns:
        Filtered array of same shape as input
    """
    points = np.asarray(points)
    is_1d = points.ndim == 1
    
    if is_1d:
        points = points.reshape(-1, 1)
    
    # Create Gaussian weights
    x = np.arange(1, radius+1)
    weights = np.exp(-((x-1)/sigma_p)**2 / 2) / (sigma_p * 2.5066)
    weights = np.concatenate([weights[::-1], [1/(sigma_p*2.5066)], weights])
    weights /= weights.sum()  # Normalize
    
    # Pad the array for boundary conditions
    padded = np.pad(points, ((radius, radius), (0, 0)), mode='edge')
    
    # Apply filtering
    filtered = np.zeros_like(points)
    for i in range(points.shape[0]):
        window = padded[i:i+2*radius+1]
        filtered[i] = np.sum(weights.reshape(-1, 1) * window, axis=0)
    
    return filtered.flatten() if is_1d else filtered


# Example usage
if __name__ == "__main__":
    # Create sample data (sine wave with noise)
    x = np.linspace(0, 2*np.pi, 100)
    noisy_signal = np.sin(x) + np.random.normal(0, 0.2, size=100)
    
    # Apply filter
    filtered_signal = linear_filter(noisy_signal, radius=3, sigma_p=0.5)
    
    print("Original signal (first 5 points):", noisy_signal[:5])
    print("Filtered signal (first 5 points):", filtered_signal[:5])
    
    # 2D example (x,y coordinates)
    points_2d = np.column_stack([x, noisy_signal])
    filtered_2d = linear_filter(points_2d, radius=2, sigma_p=0.4)
    
    print("\nOriginal 2D points (first 5):")
    print(points_2d[:5])
    print("\nFiltered 2D points (first 5):")
    print(filtered_2d[:5])