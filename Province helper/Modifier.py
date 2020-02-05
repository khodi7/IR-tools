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
    
    def __init__(self, co = 0.0, cm = 0.0, mo = 0.0, mm = 0.0, ro = 0.0, rm = 0.0, to = 0.0, tm = 0.0):
        """
        Args :
            co(float) : commerce output
            cm(float) : commerce modifier
            mo(float) : manpower output
            mm(float) : manpower modifier
            ro(float) : research output
            rm(float) : research modifier
            to(float) : tax output
            tm(float) : tax modifier
        """
        
        self._commerce_output = co
        self._commerce_modifier = cm
        self._manpower_output = mo
        self._manpower_modifier = mm
        self._research_output = ro
        self._research_modifier = rm
        self._tax_output = to
        self._tax_modifier = tm
    
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
        
    @property
    def research_modifier(self):
        return self._research_modifier
    
    @research_modifier.setter
    def research_modifier(self, n):
        self._research_modifier = n
        
    @property
    def tax_output(self):
        return self._tax_output
    
    @tax_output.setter
    def tax_output(self, n):
        self._tax_output = n
        
    @property
    def tax_modifier(self):
        return self._tax_modifier
    
    @tax_modifier.setter
    def tax_modifier(self, n):
        self._tax_modifier = n