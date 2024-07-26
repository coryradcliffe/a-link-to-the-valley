class Animation:
    def __init__(self, frames, frame_duration):
        self.frames = frames
        self.frame_duration = frame_duration
        self.current_frame = 0
        self.current_duration = 0

    def update(self, dt):
        self.current_duration += dt
        if self.current_duration >= self.frame_duration:
            self.current_duration = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)

    def get_frame(self):
        return self.frames[self.current_frame]
