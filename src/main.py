class num_colored_ridges:
    '''finde the color number of the edge of a graph
    '''
    def __init__(self,num_head,*composition_edge):
        self.num_head = num_head
        self.composition_edge = composition_edge
        return self.composition_edge
    def most_number(*List_num):
        list_num.sort()
        return list_num.pop()
#################################################
list_num = []
for (i,j) in composition_edg:
    num_i = 0
    num_j = 0
    for k in range(len(composition_edg)):
        for f in range(2):
            if i == composition_edg[k][f] :
                num_i += 1
        for f in range(2):
            if j == composition_edg[k][f] :
                num_j += 1
    list_num.append(num_i)
    list_num.append(num_j)
#################################################
