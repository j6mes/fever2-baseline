class ReplacementRule:

    def process_instance(self, instance):
        return self._process(instance)

    def _process(self, instance):
        raise NotImplementedError("Not implemented here")

    def name(self):
        raise NotImplementedError("NotImplemented")

