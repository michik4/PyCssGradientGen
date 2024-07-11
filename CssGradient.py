class CssGradient:
    def Gen(color_left,
            color_right,
            angle : int
        ) -> str:
        background : str = 'background: '
        gradient : str = 'background: '
        if type(color_left) == str:
            color_left = CssGradient.ColorEncrypt(color_left)
        if type(color_right) == str:
            color_right = CssGradient.ColorEncrypt(color_right)            
        background += CssGradient.FuncFill('rgb', color_left)
        background += ';'
        
        gradient += CssGradient.FuncFill('linear-gradient',
                                        CssGradient.AtrFill(
                                                [f'{angle}deg',
                                                CssGradient.FuncFill('rgb', color_left),
                                                CssGradient.FuncFill('rgb', color_right)]
                                             )
                                         )
        gradient += ';'        
        return background + '\n' + gradient
    
    def ColorEncrypt(color) -> list:
         сolor_16 : str = color.replace("#","")
         red : int = int(сolor_16[0:2], 16)
         green : int = int(сolor_16[2:4], 16)
         blue : int = int(сolor_16[4:6], 16)
         color = [red, green, blue]
         return color
        
    def AtrFill(attributes : list) -> str:
        atr : str = ''
        for i in attributes:
            atr += str(i) + ', '
        atr = atr[:-2]
        return atr
    
    def FuncFill(func : str, atr) -> str:
        function : str = ''
        if type(atr) == list:
            function += f'{func}({CssGradient.AtrFill(atr)})'
        elif type(atr) == str:
            function += f'{func}({atr})'
        else:
            assert type(atr) != str or list 
        return function         
        
if __name__ == '__main__':
    print(CssGradient.Gen('#0ef0ff', '#ff0000', 120))
