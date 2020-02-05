class Modifier:
    """Regroup the modifiers affecting ressource production.
    
    Attributes:
        commerce_output(float)
        commerce_modifier(float)
        manpower_output(float)
        manpower_modifier(float)
        research_output(float)
        research_modifier(float)
        tax_output(float)
        tax_modifier(float)
        The sum of the pops base output of each type (commerce, manpower,...) shall be multiplied by
        the product of sum of the _modifier by the sum of the _output.
        I.e. : (commerce_output1 + commerce_output2) * (commerce_modifier1 + commerce_modifier2) = total_commerce
    """
    
    def __init__(self):
        
        self._commerce_output = 0
        self._commerce_modifier = 0
        self._manpower_output = 0
        self._manpower_modifier = 0
        self._research_output = 0
        self._research_modifier = 0
        self._tax_output = 0
        self._tax_modifier = 0
    
    @property
    def commerce_output(self):
        return self._commerce_output
    
    @commerce_output.setter
    def commerce_output(self, n):
        self._commerce_output = n
        
    @property
    def commerce_modifier(self):
        return self._commerce_modifier
    
    @commerce_modifier.setter
    def commerce_modifier(self, n):
        self._commerce_modifier = n
        
    @property
    def manpower_output(self):
        return self._manpower_output
    
    @manpower_output.setter
    def manpower_output(self, n):
        self._manpower_output = n
        
    @property
    def manpower_modifier(self):
        return self._manpower_modifier
    
    @manpower_modifier.setter
    def manpower_modifier(self, n):
        self._manpower_modifier = n
        
    @property
    def research_output(self):
        return self._research_output
    
    @research_output.setter
    def research_output(self, n):
        self._research_output = n