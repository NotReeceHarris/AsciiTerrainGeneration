import time

def skeletonChunk(size):
    """
    // This generates the structure of the chunk 
    Args:
        size (array): size of the chunk
    Returns:
        array: This is the skeleton structure of the chunk
    """
    return [[0] * size[1] for i in range(size[0])]

if __name__ == "__main__":
    # Initialize the parameters
    seed = 26207806070
    coords = [42, 12]
    size = [46, 19]

    ts = time.time() # Start the timer

    # Initialize the skeleton chunk
    chunk = skeletonChunk(size)

    ts = time.time() - ts # Stop the timer

    """ for i in range(len(chunk)):
        print(chunk[i]) """