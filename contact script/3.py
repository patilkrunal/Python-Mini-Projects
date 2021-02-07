CARDMATCHER = re.compile(r"""
^                 ## Match at Start of Line (Multiline-flag)
    BEGIN:VCARD   ## Match the string "BEGIN:VCARD" exactly
$                 ## Match the End of Line (Multiline-flag)
.*?               ## Match characters (.) any number of times(*),
                  ## as few times as possible(?), including new-line(Dotall-flag)
^                 ## Match at Start of Line (Multiline-flag)
    END:VCARD     ## Match the string "END:VCARD" exactly
$                 ## Match the End of Line (Multiline-flag)
""", re.MULTILINE|re.DOTALL|re.VERBOSE)

VALUERE = re.compile("""
^(?P<type>[A-Z]+) ## Match Capital Ascii Characters at Start of Line
(?P<sep>:|;)     ## Match a colon or a semicolon
(?P<value>.*)    ## Match all other characters remaining
""", re.VERBOSE)

class MyVCard():
    def __init__(self,cardstring):
        self.info = defaultdict(list)
        ## Iterate over the card like you were doing
        for line in cardstring.split("\n"):
            ## Split Key of line
            match = VALUERE.match(line)
            if match:
                vtype = match.group("type")
                ## Line Values are separated by semicolons
                values = match.group("value").split(";")

                ## Lines with colons appear to be unique values
                if match.group("sep") == ":":
                    ## If only a single value, we don't need the list
                    if len(values) == 1:
                        self.info[vtype] = values[0]
                    else:
                        self.info[vtype] = values

                ## Otherwise (Semicolon sep), the value may not be unique
                else:
                    ## Semicolon seps also appear to have multiple keys
                    ## So we'll use a dict
                    out = {}
                    for val in values:
                        ## Get key,value for each value
                        k,v = val.split("=",maxsplit=1)
                        out[k] = v
                    ## Make sure we havea list to append to
                    self.info[vtype].append(out)
    def get_a_number(self):
        """ Naive approach to getting the number """
        if "TEL" in self.info:
            number = self.info["TEL"][0]["VALUE"]
            numbers = re.findall("tel:(.+)",number)
            if numbers:
                return numbers[0]
        return None

def get_vcards(file):
    """ Use regex to parse VCards into dicts. """
    with open(file,'r') as f:
        finput = f.read()
    cards = CARDMATCHER.findall(finput)
    return [MyVCard(card) for card in cards]

print([{"fn":card.info['FN'], "tel":card.get_a_number()} for card in get_vcards(file)])