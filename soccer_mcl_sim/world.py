# world.py
import pygame
import math


class Field:
    def __init__(self):
        self.width = 600
        self.length = 900

        self.landmarks_L = [
            (0.0, 0.0), # kiri atas
            (0.0, 600.0), # kiri bawah
            # (100.0, 50.0), # area goal kiri atas
            # (100.0, 550.0), # area goal kiri bawah
            (900.0, 0.0), # kanan atas
            (900.0, 600.0), # kanan bawah
            # (800.0, 50.0), # area goal kanan atas
            # (800.0, 550.0), # area goal kanan bawah
            (200.0, 100.0), # penalty area kiri atas
            (200.0, 500.0), # penalty area kiri bawah
            (700.0, 100.0), # penalty area kanan atas
            (700.0, 500.0), # penalty area kanan bawah
            (100.0, 150.0), # goal area kiri atas
            (100.0, 450.0), # goal area kiri bawah
            (800.0, 150.0), # goal area kanan atas
            (800.0, 450.0), # goal area kanan bawah
        ]

        self.landmarks_T = [
            # (0.0, 50.0), # kiri atas
            # (0.0, 550.0), # kiri bawah
            (450.0, 0.0), # tengah atas
            (450.0, 600.0), # tengah bawah
            # (900.0, 50.0), # kanan atas
            # (900.0, 550.0), # kanan bawah
            (0.0, 100.0), # penalty area kiri atas
            (0.0, 500.0), # penalty area kiri bawah
            (900.0, 100.0), # penalty area kanan atas
            (900.0, 500.0), # penalty area kanan bawah
            (0.0, 150.0), # goal area kiri atas
            (0.0, 450.0), # goal area kiri bawah
            (900.0, 150.0), # goal area kanan atas
            (900.0, 450.0), # goal area kanan bawah
        ]

        self.landmarks_X = [
            # (210, 300), # titik penalti kiri
            # (690, 300), # titik penalti kanan
            (450, 300), # tengah lapangan
            (450, 375), # tengah lapangan bawah
            (450, 225), # tengah lapangan atas
            (150, 300), # titik penalti kiri
            (750, 300), # titik penalti kanan
        ]

        self.landmarks_goalpost = [
            (0.0, 210.0),
            (0.0, 390.0),
            (900.0, 210.0),
            (900.0, 390.0),
        ]

    def draw(self, screen, scale=1.0, offset_x=0, offset_y=0):
        # Colors
        GREEN = (40, 150, 40)
        WHITE = (245, 245, 245)
        RED = (220, 50, 50)
        BLUE = (50, 100, 220)
        YELLOW = (240, 200, 40)
        BLACK = (20, 20, 20)

        FIELD_W = int(self.width * scale)
        FIELD_L = int(self.length * scale)

        LINE_W = 4
        MARK_SIZE = 6

        # Background grass (full screen not overwritten)
        pygame.draw.rect(
            screen,
            GREEN,
            pygame.Rect(offset_x, offset_y, FIELD_L, FIELD_W),
        )

        # =============================
        # Field lines
        # =============================

        # Outer boundary
        pygame.draw.rect(
            screen,
            WHITE,
            pygame.Rect(offset_x, offset_y, FIELD_L, FIELD_W),
            LINE_W,
        )

        # Center line
        pygame.draw.line(
            screen,
            WHITE,
            (offset_x + FIELD_L // 2, offset_y),
            (offset_x + FIELD_L // 2, offset_y + FIELD_W),
            LINE_W,
        )

        # Center circle
        pygame.draw.circle(
            screen,
            WHITE,
            (offset_x + FIELD_L // 2, offset_y + FIELD_W // 2),
            int(75 * scale),
            LINE_W,
        )

        # =============================
        # Penalty Area (Kotak Besar)
        # =============================

        penalty_w = int(200 * scale)
        penalty_h = int(400 * scale)

        # Left penalty
        pygame.draw.rect(
            screen,
            WHITE,
            pygame.Rect(
                offset_x,
                offset_y + int(100 * scale),
                penalty_w,
                penalty_h,
            ),
            LINE_W,
        )

        # Right penalty
        pygame.draw.rect(
            screen,
            WHITE,
            pygame.Rect(
                offset_x + FIELD_L - penalty_w,
                offset_y + int(100 * scale),
                penalty_w,
                penalty_h,
            ),
            LINE_W,
        )


        # =============================
        # Goal Area (Kotak Kecil)
        # =============================

        goal_w = int(100 * scale)
        goal_h = int(300 * scale)

        # Left goal
        pygame.draw.rect(
            screen,
            WHITE,
            pygame.Rect(
                offset_x,
                offset_y + int(150 * scale),
                goal_w,
                goal_h,
            ),
            LINE_W,
        )

        # Right goal
        pygame.draw.rect(
            screen,
            WHITE,
            pygame.Rect(
                offset_x + FIELD_L - goal_w,
                offset_y + int(150 * scale),
                goal_w,
                goal_h,
            ),
            LINE_W,
        )

        # Penalty points
        pygame.draw.circle(
            screen,
            WHITE,
            (offset_x + int(150 * scale), offset_y + FIELD_W // 2),
            8,
        )

        pygame.draw.circle(
            screen,
            WHITE,
            (offset_x + int(750 * scale), offset_y + FIELD_W // 2),
            8,
        )

        # =============================
        # Landmarks
        # =============================

        # L landmarks
        for x, y in self.landmarks_L:
            px = offset_x + int(x * scale)
            py = offset_y + int(y * scale)
            pygame.draw.circle(screen, RED, (px, py), MARK_SIZE)
            pygame.draw.circle(screen, BLACK, (px, py), MARK_SIZE, 2)

        # T landmarks
        for x, y in self.landmarks_T:
            px = offset_x + int(x * scale)
            py = offset_y + int(y * scale)
            pygame.draw.rect(
                screen,
                BLUE,
                pygame.Rect(px - 5, py - 5, 10, 10),
            )
            pygame.draw.rect(
                screen,
                BLACK,
                pygame.Rect(px - 5, py - 5, 10, 10),
                2,
            )

        # X landmarks
        for x, y in self.landmarks_X:
            px = offset_x + int(x * scale)
            py = offset_y + int(y * scale)
            pygame.draw.line(
                screen, YELLOW, (px - 6, py - 6), (px + 6, py + 6), 5
            )
            pygame.draw.line(
                screen, YELLOW, (px - 6, py + 6), (px + 6, py - 6), 5
            )

        # Goalposts
        for x, y in self.landmarks_goalpost:
            px = offset_x + int(x * scale)
            py = offset_y + int(y * scale)
            pygame.draw.circle(screen, WHITE, (px, py), 10)
            pygame.draw.circle(screen, BLACK, (px, py), 10, 3)
