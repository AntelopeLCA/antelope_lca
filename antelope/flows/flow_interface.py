class BaseEntity(object):
    """
    The very most basic characteristics of entities and entity refs
    """
    @property
    def entity_type(self):
        return NotImplemented

    @property
    def reference_entity(self):
        """
        Must have a .unit property that returns a string,
        should have .entity_type property that returns 'quantity'
        :return:
        """
        return NotImplemented

    @property
    def origin(self):
        """
        Must return a resolvable unique ID, nominally 'origin/external_ref'
        :return:
        """
        return NotImplemented

    @property
    def external_ref(self):
        """
        Must return a resolvable unique ID, nominally 'origin/external_ref'
        :return:
        """
        return NotImplemented

    @property
    def link(self):
        return '%s/%s' % (self.origin, self.external_ref)

    def properties(self):
        raise NotImplementedError

    def get(self, item):
        return NotImplemented

    @property
    def is_entity(self):
        """
        Used to distinguish between entities and catalog refs (which answer False)
        :return: True for LcEntity subclasses
        """
        return False

    def make_ref(self, query):
        """
        if is_entity is true, entity must return a ref made from the provided query
        :param query:
        :return:
        """
        return NotImplemented


class FlowInterface(BaseEntity):
    """
    An abstract class that establishes common functionality for OBSERVATIONS OF FLOWS.  A Flow consists of:
     - a reference quantity with a fixed unit
     - a flowable (a list of synonyms for the flowable substnce being described)
     - a context (a hierarchical list of strings designating the flows 'compartment' or category)

    Must be implemented (properties):
     - name - string
     - link - string
     - synonyms - iterable
    """
    @property
    def unit(self):
        return self.reference_entity.unit

    @property
    def name(self):
        return NotImplemented

    @property
    def synonyms(self):
        return NotImplemented

    def _add_synonym(self, synonym):
        raise NotImplementedError

    @property
    def context(self):
        """
        A flow's context is any hierarchical tuple of strings (generic, intermediate, ..., specific)
        0-length default for flows with no specific context
        :return:
        """
        return NotImplemented

    def get_context(self):
        raise NotImplementedError

    def match(self, other):
        """
        match if any synonyms match
        :param other:
        :return:
        """
        raise NotImplementedError
