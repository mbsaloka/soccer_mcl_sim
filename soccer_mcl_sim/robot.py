# robot.py
import math
import pygame

class Robot:
    def __init__(self):
        self.x = 450.0
        self.y = 300.0
        self.theta = 0.0  # rad
        self.head_pan = 0.0  # rad

        self.belief_x = self.x
        self.belief_y = self.y
        self.belief_theta = self.theta

        self.vx = 0.0
        self.vy = 0.0
        self.omega = 0.0

    def update(self, dt):
        dx = self.vx * math.cos(self.theta) - self.vy * math.sin(self.theta)
        dy = self.vx * math.sin(self.theta) + self.vy * math.cos(self.theta)

        self.x += dx * dt
        self.y += dy * dt
        self.theta += self.omega * dt

    def draw(self, screen, scale=1.0):
        px = int(self.x * scale)
        py = int(self.y * scale)

        R = 14

        pygame.draw.circle(screen, (0, 0, 0), (px, py), R, 2)

        # arah body
        hx = px + R * math.cos(self.theta)
        hy = py + R * math.sin(self.theta)
        pygame.draw.line(screen, (0, 0, 0), (px, py), (hx, hy), 2)

        # arah head
        hx2 = px + (R + 10) * math.cos(self.theta - self.head_pan)
        hy2 = py + (R + 10) * math.sin(self.theta - self.head_pan)
        pygame.draw.line(screen, (255, 0, 0), (px, py), (hx2, hy2), 2)


    def draw_belief(self, screen, scale=1.0):
        px = int(self.belief_x * scale)
        py = int(self.belief_y * scale)

        R = 14

        pygame.draw.circle(screen, (255, 200, 0), (px, py), R, 2)

        hx = px + R * math.cos(self.belief_theta)
        hy = py + R * math.sin(self.belief_theta)
        pygame.draw.line(screen, (255, 200, 0), (px, py), (hx, hy), 2)

    def kidnap(self, x, y, theta=None):
        self.x = x
        self.y = y
        if theta is not None:
            self.theta = theta
