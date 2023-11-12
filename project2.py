from math import inf
import pygame
import time

MAX = +1
MIN = -1


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


class Play:
    @staticmethod
    def minimax(node, depth, player=MAX):
        if depth == 0:
            return node.value

        if player == MAX:
            node.value = -inf
            node.path = None
            left_child = node.leftChild
            Play.minimax(left_child, depth=depth - 1, player=MIN)
            if left_child.value > node.value:
                node.value = left_child.value
                node.path = left_child
            right_child = node.rightChild
            Play.minimax(right_child, depth=depth - 1, player=MIN)
            if right_child.value > node.value:
                node.value = right_child.value
                node.path = right_child
        else:
            node.value = +inf
            node.path = None
            left_child = node.leftChild
            Play.minimax(left_child, depth=depth - 1, player=MAX)
            if left_child.value < node.value:
                node.value = left_child.value
                node.path = left_child
            right_child = node.rightChild
            Play.minimax(right_child, depth=depth - 1, player=MAX)
            if right_child.value < node.value:
                node.value = right_child.value
                node.path = right_child
        print(node.path.value)

    @staticmethod
    def minimaxAlphaBetaPruning(screen, node, depth, alpha=-inf, beta=+inf, player=MAX):
        if depth == 0:
            return node.value

        if player == MAX:
            node.value = -inf
            node.path = None
            left_child = node.leftChild
            Play.minimax(left_child, depth=depth - 1, player=MIN)
            if left_child.value > node.value:
                node.value = left_child.value
                node.path = left_child
            alpha = max(alpha, node.value)
            if beta <= alpha:
                print(f"depth {depth} alpha {alpha} beta {beta}")
                return
            right_child = node.rightChild
            Play.minimax(right_child, depth=depth - 1, player=MIN)
            if right_child.value > node.value:
                node.value = right_child.value
                node.path = right_child
            alpha = max(alpha, node.value)
            if beta <= alpha:
                print(f"depth {depth} alpha {alpha} beta {beta}")
                return
        else:
            node.value = +inf
            node.path = None
            left_child = node.leftChild
            Play.minimax(left_child, depth=depth - 1, player=MAX)
            if left_child.value < node.value:
                node.value = left_child.value
                node.path = left_child
            beta = min(beta, node.value)
            if beta <= alpha:
                print(f"depth {depth} alpha {alpha} beta {beta}")
                return
            right_child = node.rightChild
            Play.minimax(right_child, depth=depth - 1, player=MAX)
            if right_child.value < node.value:
                node.value = right_child.value
                node.path = right_child
            beta = min(beta, node.value)
            if beta <= alpha:
                print(f"depth {depth} alpha {alpha} beta {beta}")
                return


class Node:
    def __init__(self, parent=None, side=None, depth=4, value=None):
        self.parent = parent
        self.value = value
        self.path = None
        self.leftChild = None
        self.rightChild = None
        self.position = [(0, 0), (0, 0), (0, 0)]
        self.lines_position = []

        if self.parent is None:
            # Root node
            self.position = [
                (w // 2, 30),
                (w // 2 - 30, 90),
                (w // 2 + 30, 90),
            ]
            print(f"Root node position: {self.position}")
            print()

            self.lines_position = [
                [],
                [
                    (
                        self.position[0][0]
                        + 0.5 * (self.position[1][0] - self.position[0][0]),
                        self.position[0][1]
                        + 0.5 * (self.position[1][1] - self.position[0][1]),
                    ),
                    (
                        self.position[0][0]
                        + 0.5 * (self.position[2][0] - self.position[0][0]),
                        self.position[0][1]
                        + 0.5 * (self.position[2][1] - self.position[0][1]),
                    ),
                ],
            ]

            print(self.lines_position)

        else:
            print(depth)
            offset = 85 * 2 ** (depth - 1)
            print(offset)
            if side == "L":
                if depth % 2 == 0:
                    self.position = [
                        (
                            self.parent.position[0][0] - offset,
                            self.parent.position[0][1] + 60,
                        ),
                        (
                            self.parent.position[0][0] - offset - 30,
                            self.parent.position[0][1] + 120,
                        ),
                        (
                            self.parent.position[0][0] - offset + 30,
                            self.parent.position[0][1] + 120,
                        ),
                    ]
                    self.lines_position = [
                        [
                            (
                                self.position[0][0]
                                + 0.4 * (self.position[2][0] - self.position[0][0]),
                                self.position[0][1]
                                + 0.4 * (self.position[2][1] - self.position[0][1]),
                            )
                        ],
                        [
                            (
                                self.position[0][0]
                                + 1 * (self.position[1][0] - self.position[0][0]),
                                self.position[0][1]
                                + 1 * (self.position[1][1] - self.position[0][1]),
                            ),
                            (
                                self.position[0][0]
                                + 1 * (self.position[2][0] - self.position[0][0]),
                                self.position[0][1]
                                + 1 * (self.position[2][1] - self.position[0][1]),
                            ),
                        ],
                    ]
                else:
                    self.position = [
                        (
                            self.parent.position[0][0] - offset,
                            self.parent.position[0][1] + 150,
                        ),
                        (
                            self.parent.position[0][0] - offset - 30,
                            self.parent.position[0][1] + 90,
                        ),
                        (
                            self.parent.position[0][0] - offset + 30,
                            self.parent.position[0][1] + 90,
                        ),
                    ]
                    self.lines_position = [
                        [
                            (
                                self.position[0][0]
                                + 0.7 * (self.position[2][0] - self.position[0][0]),
                                self.position[0][1]
                                + 0.7 * (self.position[2][1] - self.position[0][1]),
                            )
                        ],
                        [
                            (
                                self.position[0][0]
                                + 0.4 * (self.position[1][0] - self.position[0][0]),
                                self.position[0][1]
                                + 0.4 * (self.position[1][1] - self.position[0][1]),
                            ),
                            (
                                self.position[0][0]
                                + 0.4 * (self.position[2][0] - self.position[0][0]),
                                self.position[0][1]
                                + 0.4 * (self.position[2][1] - self.position[0][1]),
                            ),
                        ],
                    ]
                print(f"Left child node position: {self.position}")
                print()
                print(f"depth {depth}")
            elif side == "R":
                if depth % 2 == 0:
                    self.position = [
                        (
                            self.parent.position[0][0] + offset,
                            self.parent.position[0][1] + 60,
                        ),
                        (
                            self.parent.position[0][0] + offset - 30,
                            self.parent.position[0][1] + 120,
                        ),
                        (
                            self.parent.position[0][0] + offset + 30,
                            self.parent.position[0][1] + 120,
                        ),
                    ]
                    self.lines_position = [
                        [
                            (
                                self.position[0][0]
                                + 0.4 * (self.position[1][0] - self.position[0][0]),
                                self.position[0][1]
                                + 0.4 * (self.position[1][1] - self.position[0][1]),
                            )
                        ],
                        [
                            (
                                self.position[0][0]
                                + 1 * (self.position[1][0] - self.position[0][0]),
                                self.position[0][1]
                                + 1 * (self.position[1][1] - self.position[0][1]),
                            ),
                            (
                                self.position[0][0]
                                + 1 * (self.position[2][0] - self.position[0][0]),
                                self.position[0][1]
                                + 1 * (self.position[2][1] - self.position[0][1]),
                            ),
                        ],
                    ]
                else:
                    self.position = [
                        (
                            self.parent.position[0][0] + offset,
                            self.parent.position[0][1] + 150,
                        ),
                        (
                            self.parent.position[0][0] + offset - 30,
                            self.parent.position[0][1] + 90,
                        ),
                        (
                            self.parent.position[0][0] + offset + 30,
                            self.parent.position[0][1] + 90,
                        ),
                    ]
                    self.lines_position = [
                        [
                            (
                                self.position[0][0]
                                + 0.7 * (self.position[1][0] - self.position[0][0]),
                                self.position[0][1]
                                + 0.7 * (self.position[1][1] - self.position[0][1]),
                            )
                        ],
                        [
                            (
                                self.position[0][0]
                                + 0.4 * (self.position[1][0] - self.position[0][0]),
                                self.position[0][1]
                                + 0.4 * (self.position[1][1] - self.position[0][1]),
                            ),
                            (
                                self.position[0][0]
                                + 0.4 * (self.position[2][0] - self.position[0][0]),
                                self.position[0][1]
                                + 0.4 * (self.position[2][1] - self.position[0][1]),
                            ),
                        ],
                    ]
                print(f"Right child node position: {self.position}")
                print()
                print(f"depth {depth}")

    def display(self, color, player):
        font = pygame.font.Font(None, 17)
        pygame.draw.polygon(screen, color, self.position)
        triangle_rect = pygame.draw.polygon(screen, color, self.position)

        text_x = triangle_rect.centerx - font.size(str(self.value))[0] // 2
        text_y = (
            triangle_rect.centery
            - font.size(str(self.value))[1] // 2
            + (5 if player == MAX else -5)
        )

        text_surf = font.render(str(self.value), True, (255, 255, 255))
        screen.blit(text_surf, (text_x, text_y))

    def display_lines(self, color):
        if self.parent is None:
            return
        else:
            if self == self.parent.leftChild:
                pygame.draw.line(
                    screen,
                    color,
                    self.parent.lines_position[1][0],
                    self.lines_position[0][0],
                    2,
                )
            elif self == self.parent.rightChild:
                pygame.draw.line(
                    screen,
                    color,
                    self.parent.lines_position[1][1],
                    self.lines_position[0][0],
                    2,
                )


class Tree:
    def __init__(self):
        self.root_node = Node(parent=None)

    def createEmptyTree(self, node, depth, values):
        if depth == 0:
            node.value = values.pop(0)
            return
        else:
            node.leftChild = Node(node, "L", depth - 1, None)
            node.rightChild = Node(node, "R", depth - 1, None)
            self.createEmptyTree(node.leftChild, depth - 1, values)
            self.createEmptyTree(node.rightChild, depth - 1, values)

    def drawTree(self, node, depth, player):
        if depth == 0:
            node.display((82, 82, 82), player)
            node.display_lines((82, 82, 82))
            return
        else:
            node.display((82, 82, 82), player)
            node.display_lines((82, 82, 82))
            self.drawTree(node.leftChild, depth - 1, player * -1)
            self.drawTree(node.rightChild, depth - 1, player * -1)

    def printTree(self, node, depth):
        if depth == 0:
            print(node.value)
            return
        else:
            print(node.value)
            self.printTree(node.leftChild, depth - 1)
            self.printTree(node.rightChild, depth - 1)


def main():
    # Initialize pygame
    pygame.init()

    # Create the screen
    global screen
    global w
    w = 1400  # The width of the window
    global h
    h = 700  # The height of the window
    screen = pygame.display.set_mode(((w, h)))

    # Title
    pygame.display.set_caption("MINIMAX")

    tree = Tree()
    values = [10, 5, 7, 11, 12, 8, 9, 8, 5, 12, 11, 12, 9, 8, 7, 10]
    depth = 4

    # Game loop
    running = True
    draw = True

    while running:
        # RGB coloring of the screen
        screen.fill((192, 192, 192))

        # Add the quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if draw is True:
            tree.createEmptyTree(tree.root_node, depth, values)
            # tree.drawTree(tree.root_node, depth, player=MAX)

            game = Play()
            game.minimaxAlphaBetaPruning(
                screen, tree.root_node, depth, alpha=-inf, beta=+inf, player=MAX
            )

            tree.drawTree(tree.root_node, depth, player=MAX)

            pygame.display.update()
            time.sleep(1.5)
            draw = False


if __name__ == "__main__":
    main()
