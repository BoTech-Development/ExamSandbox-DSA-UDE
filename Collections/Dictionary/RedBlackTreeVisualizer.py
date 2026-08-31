from __future__ import annotations

from graphviz import Digraph
from typing import Any

import os

os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"


class RedBlackTreeVisualizer:
    def __init__(self, black_value: bool) -> None:
        self.black_value = black_value
        self._nil_counter = 0

    def visualize(self, root: Any, filename: str = "tree") -> None:
        graph = Digraph()
        graph.attr("node", shape="circle")

        self._add_node(graph, root)

        graph.render(filename, format="png", cleanup=True)

    def _add_node(self, graph: Digraph, node: Any) -> None:
        if node is None:
            return

        node_id = str(id(node))

        graph.node(node_id, str(node.key))

        #
        # LEFT CHILD
        #
        if node.leftSubTree is not None:
            left_id = str(id(node.leftSubTree))

            graph.edge(
                node_id,
                left_id,
                color=self._edge_color(node.leftSubTree),
                penwidth="2",
            )

            self._add_node(graph, node.leftSubTree)

        else:
            nil_id = self._create_nil_node(graph)

            graph.edge(
                node_id,
                nil_id,
                color="black",
                style="dashed",
            )

        #
        # RIGHT CHILD
        #
        if node.rightSubTree is not None:
            right_id = str(id(node.rightSubTree))

            graph.edge(
                node_id,
                right_id,
                color=self._edge_color(node.rightSubTree),
                penwidth="2",
            )

            self._add_node(graph, node.rightSubTree)

        else:
            nil_id = self._create_nil_node(graph)

            graph.edge(
                node_id,
                nil_id,
                color="black",
                style="dashed",
            )

    def _create_nil_node(self, graph: Digraph) -> str:
        nil_id = f"nil_{self._nil_counter}"
        self._nil_counter += 1

        graph.node(
            nil_id,
            label="NIL",
            shape="circle",
            width="0.3",
            height="0.3",
            style="filled",
            fillcolor="lightgray",
        )

        return nil_id

    def _edge_color(self, node: Any) -> str:
        return (
            "black"
            if node.parentEdgeColor == self.black_value
            else "red"
        )
'''

from __future__ import annotations

from graphviz import Digraph
from typing import Any

import os



class RedBlackTreeVisualizer:
    def __init__(self, black_value: bool) -> None:
        """
        black_value is the value of your BLACK constant.
        Example:
            visualizer = RedBlackTreeVisualizer(BLACK)
        """
        self.black_value = black_value

    def visualize(self, root: Any, filename: str = "tree") -> None:
        graph = Digraph()
        graph.attr("node", shape="circle")

        self._add_node(graph, root)

        graph.render(filename, format="png", cleanup=True)

    def _add_node(self, graph: Digraph, node: Any) -> None:
        if node is None:
            return

        node_id = str(id(node))

        graph.node(node_id, str(node.key))

        if node.leftSubTree is not None:
            left_id = str(id(node.leftSubTree))

            graph.edge(
                node_id,
                left_id,
                color=self._edge_color(node.leftSubTree),
                penwidth="2",
            )

            self._add_node(graph, node.leftSubTree)

        if node.rightSubTree is not None:
            right_id = str(id(node.rightSubTree))

            graph.edge(
                node_id,
                right_id,
                color=self._edge_color(node.rightSubTree),
                penwidth="2",
            )

            self._add_node(graph, node.rightSubTree)

    def _edge_color(self, node: Any) -> str:
        return (
            "black"
            if node.parentEdgeColor == self.black_value
            else "red"
        )
'''