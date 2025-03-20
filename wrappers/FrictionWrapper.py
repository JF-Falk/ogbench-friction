import gymnasium

class FrictionWrapper(gymnasium.Wrapper):
    """Wrapper to modify friction in locomotion tasks."""

    def __init__(self, env, friction_mult=1):
        """Initialize the wrapper.
        Args:
            env: Environment.
            friction_mult: Scale to apply to friction of each geom in the model. 1 leaves friction unchanged.
        """
        super().__init__(env)

        # scale friction of every geom tag in the model
        self.unwrapped.model.geom_friction *= friction_mult