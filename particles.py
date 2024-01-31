from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class ParticleVideo(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=0*DEGREES, theta=-90*DEGREES)

        num_particles = 1000

        def distribution_function(theta, phi):
            r = 1 / np.sqrt(np.sin(phi)**2 + np.cos(theta)**2 * np.cos(phi)**2)
            return r

        particles = VGroup(*[Dot(radius=0.02) for _ in range(num_particles)])
        
        for particle in particles:
            theta = np.random.uniform(0, 2 * PI)
            phi = np.arccos(np.random.uniform(-1, 1))
            r = distribution_function(theta, phi)
            particle.move_to(np.array([r * np.sin(phi) * np.cos(theta), r * np.sin(phi) * np.sin(theta), r * np.cos(phi)]))

        self.add(particles)
        self.move_camera(phi=70*DEGREES, theta=-45*DEGREES, run_time=2)

        particles_speeds = [np.random.uniform(low=-0.1, high=0.3) for _ in range(num_particles)]

        def particle_updater(mobj, dt):
            for particle, speed in zip(mobj, particles_speeds):
                particle.shift(speed * dt * DOWN + LEFT + RIGHT)
                if particle.get_center()[0] < -10:
                    particle.move_to(np.array([10, np.random.uniform(-10, 10), np.random.uniform(-10, 10)]))

        particles.add_updater(particle_updater)
        self.play(particles.animate.set_color(PURPLE), run_time=2)
        self.play(particles.animate.set_color(PINK), run_time=2)
        self.play(particles.animate.set_color(GRAY_C), run_time=2)
        self.play(particles.animate.set_color(RED), run_time=2)
        self.play(particles.animate.set_color(LIGHT_GRAY), run_time=2)
