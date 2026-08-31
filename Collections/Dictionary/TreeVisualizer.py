import tkinter as tk


class TreeVisualizer:
    NODE_RADIUS = 30
    LEVEL_HEIGHT = 100

    def __init__(self, root_node):
        self.root_node = root_node

        self.window = tk.Tk()
        self.window.title("Binary Search Tree Visualizer")

        self.canvas = tk.Canvas(
            self.window,
            width=1400,
            height=800,
            bg="white"
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.draw_tree()

    def draw_tree(self):
        self.canvas.delete("all")

        if self.root_node is not None:
            width = self.canvas.winfo_reqwidth()
            self.draw_node(
                self.root_node,
                width // 2,
                80,
                width // 4
            )

    def draw_node(self, node, x, y, horizontal_spacing):
        if node is None:
            return

        # Draw node circle
        self.canvas.create_oval(
            x - self.NODE_RADIUS,
            y - self.NODE_RADIUS,
            x + self.NODE_RADIUS,
            y + self.NODE_RADIUS,
            fill="lightblue",
            outline="black",
            width=2
        )

        # Draw information inside node
        text = (
            f"{node.key}\n"
            f"{node.value}\n"
            f"cnt={node.countOfSubNodesAndSelf}"
        )

        self.canvas.create_text(
            x,
            y,
            text=text,
            font=("Arial", 9)
        )

        child_y = y + self.LEVEL_HEIGHT

        # Left child
        if node.leftSubTree is not None:
            child_x = x - horizontal_spacing

            self.canvas.create_line(
                x,
                y + self.NODE_RADIUS,
                child_x,
                child_y - self.NODE_RADIUS,
                width=2
            )

            self.draw_node(
                node.leftSubTree,
                child_x,
                child_y,
                max(horizontal_spacing // 2, 40)
            )

        # Right child
        if node.rightSubTree is not None:
            child_x = x + horizontal_spacing

            self.canvas.create_line(
                x,
                y + self.NODE_RADIUS,
                child_x,
                child_y - self.NODE_RADIUS,
                width=2
            )

            self.draw_node(
                node.rightSubTree,
                child_x,
                child_y,
                max(horizontal_spacing // 2, 40)
            )

    def run(self):
        self.window.mainloop()

