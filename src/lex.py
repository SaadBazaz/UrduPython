# ------------------------------------------------------------
# ply_test.py
#
# tokenizer to test UrduPython grammer
# ------------------------------------------------------------


def run(args):

    # ------------- Debugging ---------------
    # print ("'a' in ASCII number is:", ord('a'))
    # print ("'ا' in ASCII number is:", ord('ا'))
    # print ("'۰' in ASCII number is:", ord('۰'))
    # print ("'۲' in ASCII number is:", ord('۲'))
    # print ("'۹' in ASCII number is:", ord('۹'))
    # ------------- Debugging ---------------


    from unidecode import unidecode

    # ------------- Debugging ---------------
    # print (unidecode("۰۱۲۳۴۵۶۷۸۹"))
    # print (unidecode("۰۱۲۳۴۵۶۷۸۹۔۱۲۳"))
    # print (unidecode("ابپتٹ"))
    # ------------- Debugging ---------------


    # ------------- Debugging ---------------
    # print ("'۲' converted to int is:", int('۲'))
    # print ("'۲.۰' converted to int is:", int('۲۔۰'))
    # print ("Does = = work?", "hello" == "hello")
    # ------------- Debugging ---------------

    import ply.lex as lex
    import re


    # By default, the lexer validates all rules against only
    # English characters. We can't have that, can we?
    lex._is_identifier = re.compile(r'.')

    # Regular expression rules for simple tokens
    t_PLUS          = r'\+'
    t_MINUS         = r'-'
    t_TIMES         = r'\*'
    t_DIVIDE        = r'/'
    t_LPAREN        = r'\('
    t_RPAREN        = r'\)'
    t_EQUALS        = r'=='
    t_ASSIGNMENT    = r'='


    # from cpython/Grammer/Tokens
    # t_LPAR                    = r'\('
    # t_RPAR                    = r'\)'
    # t_LSQB                    = r'['
    # t_RSQB                    = r']'
    # t_COLON                   = r':'
    # t_COMMA                   = r','
    # t_SEMI                    = r';'
    # t_PLUS                    = r'+'
    # t_MINUS                   = r'-'
    # t_STAR                    = r'*'
    # t_SLASH                   = r'/'
    # t_VBAR                    = r'|'
    # t_AMPER                   = r'&'
    # t_LESS                    = r'<'
    # t_GREATER                 = r'>'
    # t_EQUAL                   = r'='
    # t_DOT                     = r'.'
    # t_PERCENT                 = r'%'
    # t_LBRACE                  = r'{'
    # t_RBRACE                  = r'}'
    # t_EQEQUAL                 = r'=='
    # t_NOTEQUAL                = r'!='
    # t_LESSEQUAL               = r'<='
    # t_GREATEREQUAL            = r'>='
    # t_TILDE                   = r'~'
    # t_CIRCUMFLEX              = r'^'
    # t_LEFTSHIFT               = r'<<'
    # t_RIGHTSHIFT              = r'>>'
    # t_DOUBLESTAR              = r'**'
    # t_PLUSEQUAL               = r'+='
    # t_MINEQUAL                = r'-='
    # t_STAREQUAL               = r'*='
    # t_SLASHEQUAL              = r'/='
    # t_PERCENTEQUAL            = r'%='
    # t_AMPEREQUAL              = r'&='
    # t_VBAREQUAL               = r'|='
    # t_CIRCUMFLEXEQUAL         = r'^='
    # t_LEFTSHIFTEQUAL          = r'<<='
    # t_RIGHTSHIFTEQUAL         = r'>>='
    # t_DOUBLESTAREQUAL         = r'**='
    # t_DOUBLESLASH             = r'//'
    # t_DOUBLESLASHEQUAL        = r'//='
    # t_AT                      = r'@'
    # t_ATEQUAL                 = r'@='
    # t_RARROW                  = r'->'
    # t_ELLIPSIS                = r'...'
    # t_COLONEQUAL              = r':='


    # A regular expression rule with some action code
    def t_NUMBER(t):
        r'[۰-۹][۰-۹]*[۔]{0,1}[۰-۹]*'

        # ------------- Debugging ---------------
        # print ("The number was:", t.value)
        # ------------- Debugging ---------------
        
        t.value = unidecode(t.value)
        
        # ------------- Debugging ---------------
        # print ("The number is now:", t.value)
        # ------------- Debugging ---------------

        return t



    # reserved = {
    #     # "۱":          "1",
    #     # "۲":          "2",
    #     # "۳":          "3",
    #     # "۴":          "4",
    #     # "۵":          "5",
    #     # "۶":          "6",
    #     # "۷":          "7",
    #     # "۸":          "8",
    #     # "۹":          "9",
    #     # "۰":          "0",
    #     "چھاپ":       "print",
    #     "ورنہ اگر":   "elif",
    #     "اگر":        "if",
    #     "ورنہ":       "else",
    #     "جبتک":       "while",
    #     "جو":         "for",
    #     "اندر":       "in", 
    #     "داخلہ":      "input",
    #     "توڑ":        "break",
    #     "جاری":       "continue",
    #     "گزر":        "pass",
    #     "حق":         "True",
    #     "باطل":       "False",
    #     "ہے":         "is",
    #     "طبقہ":       "class",
    #     "وضح":        "def",
    #     "__ابتدا__":  "__init__",
    #     "خود":        "self",
    #     "واپس":       "return",
    #     "ستلی":       "string",
    #     "ستل":        "str",
    #     "شامل":       "append",
    #     "نکل":        "pop",
    #     "اور":        "and",
    #     "یا":         "or",    
    #     "سب":         "all",
    #     "کوئ":        "any",
    #     "ندارد":      "None",
    #     "عدد":        "int",    
    # }    

    import yaml
    language_dict = yaml.load(open("./ur_native.lang.yaml"), Loader=yaml.SafeLoader)

    reserved = language_dict.get("reserved")

    # List of token names.   This is always required
    tokens =  [
        "PLUS", 
        "MINUS",
        "TIMES",
        "DIVIDE",
        "LPAREN",
        "RPAREN",
        "EQUALS",
        "ASSIGNMENT",
        "NUMBER",
        "STRING",
        'ID',

        'newline',
        # 'tab',

    ] + list(reserved.values())

    # Define a rule so we can track line numbers
    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        return t

    # # Define a rule so we can track tabs
    # def t_tab(t):
    #     r'.+'
    #     print ("Found a tab or space!")
    #     # t.lexer.lineno += len(t.value)
    #     return t

    # # Define a rule so we can track tabs
    # def t_space(t):
    #     r' +'
    #     print ("Found a space!")
    #     # t.lexer.lineno += len(t.value)
    #     return t

    def t_ID(t):
        # r'[a-zA-Z_][a-zA-Z_0-9]*'
        # r'[ا-ی_][۰-۹_ا-ی]*'

        ## Docstring is assigned AFTER the function, because it has variables in the regex...
        ## Reference: https://stackoverflow.com/questions/12217816/regex-with-variable-data-in-it-ply-lex

        t.type = reserved.get(t.value,'ID')    # Check for reserved words    
        
        # ------------- Debugging ---------------
        # print ("Type is:", t.type)
        # ------------- Debugging ---------------


        if args['translate']:
            if t.type == 'ID':
                t.value = unidecode(t.value)

        return t

    t_ID.__doc__ = r'['+language_dict["letters"]["start"]+'-'+language_dict["letters"]["end"]+'_]['+language_dict["numbers"]["start"]+'-'+language_dict["numbers"]["end"]+'_'+language_dict["letters"]["start"]+'-'+language_dict["letters"]["end"]+']*'


    # A string containing ignored characters (spaces and tabs)
    # t_ignore  = ' \t'

    # Error handling rule
    def t_error(t):
        # ------------- Debugging ---------------
        # print("Illegal character '%s'" % t.value[0])
        # ------------- Debugging ---------------

        t.value = t.value[0]
        t.lexer.skip(1)

        # ------------- Debugging ---------------
        # print("still keeping it tho")
        # ------------- Debugging ---------------

        return t

    # Strings rule
    def t_STRING(t):
        # r'[\"][.][\"]'
        
        r'("(\\"|[^"])*")|(\'(\\\'|[^\'])*\')'

        # ------------- Debugging ---------------
        # print ("Found a string!", t.value)
        # ------------- Debugging ---------------

        return t

    # Build the lexer
    lexer = lex.lex()

    # Give the lexer some input!

    # ------------- Debugging ---------------
    # lexer.input("#print 1==2")
    # lexer.input("""

    # اگر (۱==۱):
    #     چھاپ(۲==۲)

    # """)
    # ------------- Debugging ---------------


    ur_pyfile = open(args["file"][0])
        
    code = ur_pyfile.read()

    dots_and_stuff = {
        "۔":          ".",
        "،":          ",",  
    }

    for key, value in dots_and_stuff.items():
        code = code.replace(key, value)

    lexer.input(code)

    if args["keep"] or args["keep_only"]:
        eng_pyfile = open("compiled.en.py", "wt")


    compiled_code = ""

    if args["keep_only"]:
        print ("Compiling", args["file"][0], "...")

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input

        # ------------- Debugging ---------------
        #print(tok)
        #print ("Tok's value is:", tok.value)
        #print ("Tok's type is:", tok.type)
        # ------------- Debugging ---------------

        if tok.value in reserved.keys():

            # ------------- Debugging ---------------
            # if tok.type == '۔':
            #     print ("Found an Urdu dot!")
            # ------------- Debugging ---------------

            compiled_code += tok.type
        else:
            compiled_code += tok.value

    if args["keep"] or args["keep_only"]:
        eng_pyfile.write(compiled_code)
        eng_pyfile.close()

    if args["keep_only"] is False:
        exec(compiled_code)

