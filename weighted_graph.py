# weighted_graph.py
# Licensed under GNU Affero General Public License v3.0
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import TypeVar, Generic, List, Tuple
from graph import Graph
from weighted_edge import WeightedEdge

V = TypeVar('V')  # type of the vertices in the graph


class WeightedGraph(Generic[V], Graph[V]):
    def __init__(self, vertices: List[V] = []) -> None:
        self._vertices: List[V] = vertices
        self._edges: List[List[WeightedEdge]] = [[] for _ in vertices]

    def add_edge_by_indices(self, u: int, v: int, weight: float) -> None:
        edge: WeightedEdge = WeightedEdge(u, v, weight)
        self.add_edge(edge) # call superclass version

    def add_edge_by_vertices(self, first: V, second: V, weight: float) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v, weight)

    def neighbors_for_index_with_weights(self, index: int) -> List[Tuple[V, float]]:
        distance_tuples: List[Tuple[V, float]] = []
        for edge in self.edges_for_index(index):
            distance_tuples.append((self.vertex_at(edge.v), edge.weight))
        return distance_tuples

    def __str__(self) -> str:
        desc: str = ""
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index_with_weights(i)}\n"
        return desc


if __name__ == "__main__":
    # test basic Graph construction
    city_graph2: Graph[str] = WeightedGraph(["Bungoma","Kitale","Lodwar","Moyale","Wajir","Lamu","Malindi","Mombasa","Machakos","Nairobi","Naivasha","Nakuru","Eldoret","Kisumu","Garissa","Marsabit","Taita Taveta","Turkana"])
    city_graph2.add_edge_by_vertices("Bungoma","Kitale", 250)
    city_graph2.add_edge_by_vertices("Bungoma","Kisumu", 300)
    city_graph2.add_edge_by_vertices("Kisumu","Eldoret", 200)
    city_graph2.add_edge_by_vertices("Kisumu","Nakuru", 210)
    city_graph2.add_edge_by_vertices("Nakuru","Naivasha", 150)
    city_graph2.add_edge_by_vertices("Naivasha","Nairobi", 300)
    city_graph2.add_edge_by_vertices("Nairobi","Machakos", 85)
    city_graph2.add_edge_by_vertices("Nairobi","Garissa", 673)
    city_graph2.add_edge_by_vertices("Garissa","Marsabit", 125)
    city_graph2.add_edge_by_vertices("Garissa","Turkana", 78)
    city_graph2.add_edge_by_vertices("Turkana","Marsabit", 175)
    city_graph2.add_edge_by_vertices("Turkana","Lamu", 180)
    city_graph2.add_edge_by_vertices("Turkana","Wajir", 200)
    city_graph2.add_edge_by_vertices("Marsabit","Moyale", 75)
    city_graph2.add_edge_by_vertices("Moyale","Lodwar", 350)
    city_graph2.add_edge_by_vertices("Lodwar","Kitale", 248)
    city_graph2.add_edge_by_vertices("Lodwar","Eldoret", 473)
    city_graph2.add_edge_by_vertices("Nakuru","Eldoret", 240)
    city_graph2.add_edge_by_vertices("Eldoret","Kitale", 173)
    city_graph2.add_edge_by_vertices("Mombasa","Malindi", 863)
    city_graph2.add_edge_by_vertices("Machakos","Garissa", 776)
    city_graph2.add_edge_by_vertices("Machakos", "Mombasa", 1005)
    city_graph2.add_edge_by_vertices("Malindi","Lamu", 489)
    city_graph2.add_edge_by_vertices("Lamu","Wajir", 373)
    city_graph2.add_edge_by_vertices("Wajir","Moyale", 205)
    city_graph2.add_edge_by_vertices("Mombasa","Taita Taveta", 1000)
    city_graph2.add_edge_by_vertices("Taita Taveta","Kisumu", 500)
    city_graph2.add_edge_by_vertices("Garissa","Lodwar", 420)
    city_graph2.add_edge_by_vertices("Garissa", "Nakuru", 838)
    city_graph2.add_edge_by_vertices("Garissa", "Malindi", 998)
    city_graph2.add_edge_by_vertices("Nairobi", "Taita Taveta", 736)

    print(city_graph2)