def rgb_to_hue_xy(rgb_code: str):
    rgb_code = rgb_code.lstrip('#')
    
    rgb_code = rgb_code if rgb_code != '000000' else '020202'
    
    r = round(int(rgb_code[0:2],16)/255,2)
    g = round(int(rgb_code[2:4],16)/255,2)
    b = round(int(rgb_code[4:6],16)/255,2)
    
    # hacking a brightness value using this algorithm: https://www.w3.org/TR/AERT/#color-contrast
    # brightness = int((0.299*r + 0.587*g + 0.114*b)*255)
    
    # apply gamma correction to the RGB values
    r = pow((r + 0.055) / (1.0 + 0.055), 2.4) if r > 0.04045 else r / 12.92
    g = pow((g + 0.055) / (1.0 + 0.055), 2.4) if g > 0.04045 else g / 12.92
    b = pow((b + 0.055) / (1.0 + 0.055), 2.4) if b > 0.04045 else b / 12.92
    
    # Convert the RGB values to XYZ using the Wide RGB D65 conversion formula
    X = r * 0.649926 + g * 0.103455 + b * 0.197109;
    Y = r * 0.234327 + g * 0.743075 + b * 0.022598;
    Z = r * 0.0000000 + g * 0.053077 + b * 1.035763;
    
    xyz = X + Y + Z if X + Y + Z != 0 else .002
    
    # Calculate the xy values from the XYZ values
    x = X / xyz
    y = Y / xyz
    
    return {'xy': [round(x,4),round(y,4)], 'brightness': int(round(Y,2)*254)}

def hue_xy_to_rgb(x: float, y: float, bri: int):
    z = 1.0 - x - y;
    
    Y = bri/254;
    X = (Y / y) * x;
    Z = (Y / y) * z;
    
    # Convert to RGB using Wide RGB D65 conversion
    r = X * 1.4628067 - Y * 0.1840623 - Z * 0.2743606
    g = -X * 0.5217933 + Y * 1.4472381 + Z * 0.0677227
    b = X * 0.0349342 - Y * 0.0968930 + Z * 1.2884099
    
    # Apply reverse gamma correction
    r = 12.92 * r if r <= 0.0031308 else (1.0 + 0.055) * pow(r, (1.0 / 2.4)) - 0.055
    g = 12.92 * g if g <= 0.0031308 else (1.0 + 0.055) * pow(g, (1.0 / 2.4)) - 0.055
    b = 12.92 * b if b <= 0.0031308 else (1.0 + 0.055) * pow(b, (1.0 / 2.4)) - 0.055
    
    # scale 
    r =  max(0,min(int(r * 254),254))
    g =  max(0,min(int(g * 254),254))
    b =  max(0,min(int(b * 254),254))
    
    # convert to hex and return
    return "#{0:02x}{1:02x}{2:02x}".format(r, g, b)
    
    
    
    
    