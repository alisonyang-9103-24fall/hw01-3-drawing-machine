"""
9103 hw1-3
alison yang
original link: https://editor.p5js.org/thiagohersan/sketches/mJdFIgeNo
"""

import random

class Agent:
    def __init__(self):
        self.x = random.randrange(17, width, -17)
        self.y = random.randrange(17, height, -17)
        self.vx = random.randrange(-2, 2)
        self.vy = random.randrange(-2, 2)
        self.radius = random.randrange(8.16)
        self.diam = 2 * self.radius
        
    def bounceBoundary():
        if self.x + self.radius >= width or self.x - self.radius <= 0:
            self.vx *= -1
        if self.y + self.radius >= height or self.y - self.radius <= 0:
            self.vy *= -1
        
    def updateByVelocity():
        self.x += self.vx
        self.y += self.vy
        
    def update():
        self.updateByVelocity
        self.bounceBoundary()
        
    def drawAgent():
        ellipse(self.x, self.y, self.diam)
            
    def drawPoint():
        point(self.x, self.y)
        
    def drawOverlap():
        for i in range(0, len(agents)):
            otherAgent = agents[i]
            if self != otherAgent:
                tDist = dist(self.x, self.y, otherAgent.x, otherAgent.y)
                if tDist < self.radius + otherAgent.radius:
                    cx = (self.x + otherAgent.x) / 2
                    cy = (self.y + otherAgent.y) / 2
                    ellipse(cx, cy, tDist)
                    
    def draw():
        if currentMode == POINT_MODE:
            stroke(0)
            self.drawPoint()
        elif currentMode == OVERLAP_MODE:
            stroke(0, 16)
            noFill()
            self.drawOverlap()
            
maxAgents = 32
agents = []
AGENT_MODE = 0
POINT_MODE = 1
OVERLAP_MODE = 2

currentMode = AGENT_MODE

def setup():
    canvas(800, 800)
    for i in range(0, maxAgents):
        newAgent = Agent()
        agents.append(newAgent)
        
def draw():
    for i in range(0, len(agents)):
        agents[i].update()
        
    if currentMode == AGENT_MODE:
        background(220, 20, 120)
        noStroke()
        fill(255)
        for i in range(0, len(agents)):
            agents[i].drawAgent()
    else:
        for i in range(0, len(agents)):
            agents[i].draw()
            
def mouseClicked():
    currentMode = (currentMode + 1) % 3
    if currentMode != AGENT_MODE:
        background(255)
