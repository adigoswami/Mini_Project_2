import math

def distance(x1 , y1 , x2 , y2): 
    # Calculating distance 
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) * 1.0)

def T_F_F(vertex_ai, vertex_aj, vertex_bi, ki, kj):

    dist1= distance(vertex_ai[0],vertex_ai[1],vertex_bi[0],vertex_bi[1])
    dist2= distance(vertex_bi[0],vertex_bi[1],vertex_aj[0],vertex_aj[1])

    cost = dist1 + dist2

    if (cost > (kj - ki)*10):
        return 999999
    else:
        return cost

def T_F_FDU(vertex_ai, vertex_aj, vertex_bi, ki, kj):

    t_L = 50
    t_TO = 50
    r = 2

    dist1= distance(vertex_ai[0],vertex_ai[1],vertex_bi[0],vertex_bi[1])
    dist2= distance(vertex_bi[0],vertex_bi[1],vertex_aj[0],vertex_aj[1])

    e = max(0,kj - (ki - (dist1 + dist2)))

    cost = dist1 + dist2 + t_L + r*e + t_TO

    if (cost > (kj - ki)*10):
        return 999999
    else:
        return cost

def T_F_DUFDU(vertex_ai, vertex_aj, vertex_bi, ki, ki_dash, kj):

    t_L = 50
    t_TO = 50
    r = 2

    dist1= distance(vertex_ai[0],vertex_ai[1],vertex_bi[0],vertex_bi[1])
    dist2= distance(vertex_bi[0],vertex_bi[1],vertex_aj[0],vertex_aj[1])

    e_1 = max(0,ki_dash - (ki - dist1))
    e_2 = max(0,kj - (ki_dash - dist2))

    cost = dist1 + t_L + r*e_1 + t_TO + dist2 + t_L + r*e_2 + t_TO

    if ((dist1 > (ki_dash - ki)*10) and (dist2 > (kj - ki_dash)*10)):
        return 999999
    else:
        return cost

def T_F_DUF(vertex_ai, vertex_aj, vertex_bi, ki, ki_dash, kj):

    t_L = 50
    t_TO = 50
    r = 2

    dist1= distance(vertex_ai[0],vertex_ai[1],vertex_bi[0],vertex_bi[1])
    dist2= distance(vertex_bi[0],vertex_bi[1],vertex_aj[0],vertex_aj[1])

    e = max(0,ki_dash - (ki - dist1))

    cost = dist1 + t_L + r*e + t_TO + dist2

    if ((dist1 > (ki_dash - ki)*10) and (dist2 > (kj - ki_dash)*10)):
        return 999999
    else:
        return cost

def T_F_DTU(vertex_ai, vertex_aj, vertex_bi, ki, ki_dash, kj):

    t_L = 50
    t_TO = 50
    r = 2

    dist1= distance(vertex_ai[0],vertex_ai[1],vertex_bi[0],vertex_bi[1])
    dist2= distance(vertex_bi[0],vertex_bi[1],vertex_aj[0],vertex_aj[1])

    e = max(0,kj - (ki_dash - dist2))

    cost = dist1 + t_L + max(5*dist2,r*e) + t_TO

    if (dist1 > (ki_dash - ki)*10):
        return 999999
    else:
        return cost

def main():
    coord = [[195,340], [236,373], [299,314],[267,351],[248,298],[296,333],[274,276],[317,313],[299,252],[354,292],[330,229],[378,268],[427,409],[415,635],[457,436],[453,622],[495,459],[497,601],[538,485],[540,579],[579,516],[581,563],[530,434],[1035,140],[575,463],[1072,176]]
    #print(coord)
    vertices = []
    edge_costs = {}

    b_cells = [[195,340,236,373], [299,314,267,351],[248,298,296,333],[274,276,317,313],[299,252,354,292],[330,229,378,268],[427,409,415,635],[457,436,453,622],[495,459,497,601],[538,485,540,579],[579,516,581,563],[530,434,1035,140],[575,463,1072,176] ]

    for cell in b_cells:
        temp1 = [cell[0],cell[1]]
        temp2 = [cell[2],cell[3]]
        for point in coord:
            if point == temp1 or point == temp2:
                continue
            
            for i in range(10,101,10):
                for j in range(10,101,10):
                    for k in range(10,101,10):

                        cost1 = T_F_F(temp1, point, temp2, i, k)
                        cost2 = T_F_FDU(temp1, point, temp2, i, k)
                        cost3 = T_F_DUFDU(temp1, point, temp2, i, j, k)
                        cost4 = T_F_DUF(temp1, point, temp2, i, j, k)
                        cost5 = T_F_DTU(temp1, point, temp2, i, j, k)

                        costs = [cost1, cost2, cost3, cost4, cost5]
                        names = ['T_F_F', 'T_F_FDU', 'T_F_DUFDU', 'T_F_DUF', 'T_F_DTU']
                        cost = min(costs)
                        flag = names[costs.index(cost)]
                        
                        # if cost != 999999:
                        start = temp1 + [i]
                        #middle = temp2 + [j]
                        end = point + [k]
                        #print(start,end, temp2+[j])
                        if start not in vertices:
                            vertices.append(start)
                        #if middle not in vertices:
                        #    vertices.append(middle)
                        if end not in vertices:
                            vertices.append(end)
                        index1 = vertices.index(start)
                        #index2 = vertices.index(middle)
                        index3 = vertices.index(end)
                        #print(cost, index1,index2,index3)
                        #print((index1,index3))
                        #print(list(edge_costs.keys()))
                        if (index1,index3) not in edge_costs:
                            edge_costs[(index1,index3)] = [cost, flag]
                        else:
                            previous = edge_costs[(index1,index3)]
                            if cost < previous[0]:
                                edge_costs[(index1,index3)] = [cost, flag]
                            
            
            for i in range(10,101,10):
                for j in range(10,101,10):
                    for k in range(10,101,10):

                        cost1 = T_F_F(temp2, point, temp1, i, k)
                        cost2 = T_F_FDU(temp2, point, temp1, i, k)
                        cost3 = T_F_DUFDU(temp2, point, temp1, i, j, k)
                        cost4 = T_F_DUF(temp2, point, temp1, i, j, k)
                        cost5 = T_F_DTU(temp2, point, temp1, i, j, k)

                        costs = [cost1, cost2, cost3, cost4, cost5]
                        names = ['T_F_F', 'T_F_FDU', 'T_F_DUFDU', 'T_F_DUF', 'T_F_DTU']
                        cost = min(costs)
                        flag = names[costs.index(cost)]

                        #print(cost)
                        # if cost != 999999:
                        start = temp2 + [i]
                        #middle = temp1 + [j]
                        end = point + [k]
                        if start not in vertices:
                            vertices.append(start)
                        # if middle not in vertices:
                        #     vertices.append(middle)
                        if end not in vertices:
                            vertices.append(end)
                        index1 = vertices.index(start)
                        #index2 = vertices.index(middle)
                        index3 = vertices.index(end)
                        if (index1,index3) not in edge_costs:
                            edge_costs[(index1,index3)] = [cost, flag]
                        else:
                            previous = edge_costs[(index1,index3)]
                            if cost < previous[0]:
                                edge_costs[(index1,index3)] = [cost, flag]

    # print(len(vertices))
    print(len(list(edge_costs.keys())))
    # print(vertices)
    #print(edge_costs)


if __name__ == '__main__':
    main()