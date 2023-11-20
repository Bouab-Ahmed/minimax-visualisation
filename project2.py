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
        if depth == 0:  # terminal node
            return node.value

        # if node.parent is None:
        #     node.display((82, 82, 82), player, True)
        #     node.display_lines((82, 82, 82))
        #     pygame.display.update()
        #     time.sleep(1)

        if player == MAX:
            max_value = -inf
            node.value = max_value
            node.path = None
            node.display((49, 66, 78), player, True)
            node.display_lines((49, 66, 78))
            pygame.display.update()
            left_child = node.leftChild
            right_child = node.rightChild
            for child in [left_child, right_child]:
                # Marking current node as visited (in blue)
                child_value = Play.minimax(child, depth=depth - 1, player=MIN)
                time.sleep(1)
                child.display((190, 51, 26), player, True)
                child.display_lines((190, 51, 26))
                pygame.display.update()

                if child_value > max_value:
                    child.display((190, 51, 26), player, True)
                    child.display_lines((190, 51, 26))
                    pygame.display.update()
                    max_value = child_value
                    node.path = child
            print(f"node {node.value} childred {left_child.value} {right_child.value}")
            node.value = max_value
            if node.parent is None:
                node.display((49, 66, 78), player, True)
                node.display_lines((82, 82, 82))
                pygame.display.update()
            if max_value == left_child.value:
                right_child.display((49, 66, 78), player, True)
                right_child.display_lines((49, 66, 78))
                pygame.display.update()
                left_child.display((190, 51, 26), player, True)
                left_child.display_lines((190, 51, 26))
                pygame.display.update()
            else:
                left_child.display((49, 66, 78), player, True)
                left_child.display_lines((49, 66, 78))
                pygame.display.update()
                right_child.display((190, 51, 26), player, True)
                right_child.display_lines((190, 51, 26))
                pygame.display.update()
            return node.value

        else:
            min_value = +inf
            node.value = min_value
            node.path = None
            node.display((49, 66, 78), player, True)
            node.display_lines((82, 82, 82))
            pygame.display.update()
            left_child = node.leftChild
            right_child = node.rightChild
            for child in [left_child, right_child]:
                child_value = Play.minimax(child, depth=depth - 1, player=MAX)
                time.sleep(1)
                child.display((49, 66, 78), player, True)
                child.display_lines((49, 66, 78))
                pygame.display.update()

                if child_value < min_value:
                    child.display((190, 51, 26), player, True)
                    child.display_lines((190, 51, 26))
                    pygame.display.update()
                    min_value = child_value
                    node.path = child
            print(f"node {node.value} childred {left_child.value} {right_child.value}")
            node.value = min_value
            if min_value == left_child.value:
                right_child.display((49, 66, 78), player, True)
                right_child.display_lines((49, 66, 78))
                pygame.display.update()
                left_child.display((190, 51, 26), player, True)
                left_child.display_lines((190, 51, 26))
                pygame.display.update()
            else:
                left_child.display((49, 66, 78), player, True)
                left_child.display_lines((49, 66, 78))
                pygame.display.update()
                right_child.display((190, 51, 26), player, True)
                right_child.display_lines((190, 51, 26))
                pygame.display.update()
            return node.value

    @staticmethod
    def minimaxAlphaBetaPruning(node, depth, alpha=-inf, beta=+inf, player=MAX):
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
    def __init__(self, parent=None, side=None, depth=4, value=None, id=0):
        self.parent = parent
        self.value = value
        self.path = None
        self.leftChild = None
        self.rightChild = None
        self.position = [(0, 0), (0, 0), (0, 0)]
        self.lines_position = []
        self.id = id

        if self.parent is None:
            # Root node
            self.position = [
                (w // 2, 30),
                (w // 2 - 30, 90),
                (w // 2 + 30, 90),
            ]

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

        else:
            offset = 85 * 2 ** (depth - 1)
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

    def display(self, color, player, print_values):
        pygame.draw.polygon(screen, color, self.position)
        triangle_rect = pygame.draw.polygon(screen, color, self.position)

        if print_values:
            font = pygame.font.Font(None, 17)
            text_x = triangle_rect.centerx - font.size(str(self.value))[0] // 2
            text_y = triangle_rect.centery - font.size(str(self.value))[1] // 2 + 5

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
                    3,
                )
            elif self == self.parent.rightChild:
                pygame.draw.line(
                    screen,
                    color,
                    self.parent.lines_position[1][1],
                    self.lines_position[0][0],
                    3,
                )


class Tree:
    def __init__(self):
        self.root_node = Node(parent=None)

    def createEmptyTree(self, node, depth, values):
        if depth == 0:
            node.value = values.pop(0)
            return
        else:
            id = node.id
            node.leftChild = Node(node, "L", depth - 1, None, id + 1)
            node.rightChild = Node(node, "R", depth - 1, None, id + 2)
            self.createEmptyTree(node.leftChild, depth - 1, values)
            self.createEmptyTree(node.rightChild, depth - 1, values)

    def drawTree(self, node, depth, player):
        if depth == 0:
            node.display((82, 82, 82), player, print_values=True)
            node.display_lines((82, 82, 82))
            return
        else:
            node.display((82, 82, 82), player, print_values=False)
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
            # draw ruler
            for i in range(0, w, 50):
                font = pygame.font.Font(None, 17)
                text_surf = font.render(str(i), True, (0, 0, 0))
                screen.blit(text_surf, (i, 5))

            for i in range(0, h, 50):
                font = pygame.font.Font(None, 17)
                text_surf = font.render(str(i), True, (0, 0, 0))
                screen.blit(text_surf, (5, i))

            tree.createEmptyTree(tree.root_node, depth, values)
            # tree.drawTree(tree.root_node, depth, player=MAX)

            tree.drawTree(tree.root_node, depth, player=MAX)
            time.sleep(1.5)
            game = Play()
            game.minimax(tree.root_node, depth, player=MAX)

            pygame.display.update()
            time.sleep(1.5)
            draw = False


if __name__ == "__main__":
    main()
