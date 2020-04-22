import json
from typing import List, Tuple, Union, Dict

from mobile_network.utils import Graph, Utilization


def count_unreachable(graph_data: List[Tuple[str, str]],
                      utilization_data: Dict[str, int],
                      enter_point: str,
                      broken_points: Union[None, List[str]]):
    """
    count unreachable users for specified configuration
    :param graph_data: info about graph structure
    :param utilization_data: info about towers utilization
    :param enter_point: mane of tower from which
        the emergency message is distributed
    :param broken_points: list of names broken towers
    :return: number of users, which will not get a message
    """
    graph = Graph()
    graph.add_edges(graph_data)

    utilization = Utilization()
    utilization.add_utilization(utilization_data)

    if graph.vertex_set ^ utilization.utilization.keys() != set():
        raise ValueError(f"graph_data and utilization_data "
                         f"contain information about different vertexes")

    unreachable = graph.get_unreachable(start=enter_point, broken=broken_points)
    return utilization.get_utilization(unreachable)


def call_counter():
    """
    wrapper of count_unreachable()
    for call from terminal
    """
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True, type=str,
                        help="path to the file with input data")
    args = parser.parse_args()
    with open(args.input) as f:
        input_data = json.load(f)
    output = count_unreachable(*input_data)
    print(output)


if __name__ == "__main__":
    call_counter()
