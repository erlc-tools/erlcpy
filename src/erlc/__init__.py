from erlc.classes.client import ( Client )
from erlc.logging import debug


debug("Enabling debug is dangerous!!!", "It may reveal keys, ratelimit authorization keys, etc.",
      "Make sure you aren't ssh'ing or screen sharing!")

exports = [Client] # change this instead of __all__!
__all__ = exports