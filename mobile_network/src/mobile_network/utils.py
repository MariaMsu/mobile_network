from collections import defaultdict
from typing import List, Tuple, Union, Dict, Set


class Graph:
    """
    build and handel graph of mobile towers
    """
    def __init__(self):
        self.adjacency_list = defaultdict(list)
        self.vertex_set = set()

    def add_edges(self, vertex_list: List[Tuple[str, str]]):
        """
        add edges and vertexes to the graph
        :param vertex_list: [["V_i", "V_j"], ..., ["V_k", "V_l"]]
        """
        for v1, v2 in vertex_list:
            self.adjacency_list[v1].append(v2)
            self.adjacency_list[v2].append(v1)
            self.vertex_set.update(v1, v2)

    def get_unreachable(self, start: str,
                        broken: Union[None, List[str]] = None) -> Set[str]:
        """
        search in depth for unreachable vertexes
        :param start: name of a vertex
            from which the emergency message is distributed
        :param broken: list of name broken towers
        :return: set of names unreachable towers
        """

        def depth_search(vertex):
            if vertex in broken:
                return
            visited.add(vertex)
            for v in self.adjacency_list[vertex]:
                if v not in visited:
                    depth_search(v)

        visited = set()
        depth_search(start)
        return self.vertex_set ^ visited


class Utilization:
    """
    save utilization of every tower
    and count utilization of towers subset
    """
    def __init__(self):
        self.utilization = {}

    def add_utilization(self, utilization_list: Dict[str, int]):
        """
        save utilization info into inner structure
        :param utilization_list: {"V_i": util_i, ..., "V_j": util_j}
        """
        for vertex, utilization in utilization_list.items():
            if utilization < 0:
                raise ValueError("the number of users served cannot be negative")
            self.utilization[vertex] = utilization

    def get_utilization(self, vertex_set: Set[str]) -> int:
        """
        get utilization of towers subst
        :param vertex_set: set of broken towers
        :return: sum of subset utilization
        """
        return sum(v for k, v in self.utilization.items() if k in vertex_set)