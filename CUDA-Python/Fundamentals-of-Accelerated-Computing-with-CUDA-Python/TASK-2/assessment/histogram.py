# Add your solution here
@cuda.jit
def cuda_histogram(x, xmin, xmax, hout):
    '''Increment bin counts in histogram_out, given histogram range [xmin, xmax).'''
    
    nbins = hout.shape[0]
    bin_width = (xmax - xmin) / nbins
    
    start = cuda.grid(1)
    stride = cuda.gridsize(1)
    
    for i in range(start,x.shape[0],stride):
        bin_number = np.int32((x[i] - xmin)/bin_width)
        if bin_number >= 0 and bin_number < hout.shape[0]:
            # only increment if in range
            cuda.atomic.add(hout,bin_number, 1)