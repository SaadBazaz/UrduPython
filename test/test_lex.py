# ------------------------------------------------------------
# ply_test.py
#
# tokenizer to test UrduPython grammer
# ------------------------------------------------------------

import yaml
from unidecode import unidecode
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


default_tokens =  [
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
    'COMMENT',
    # 'tab',

]



# Strings rule
def t_STRING(t):
    # r'[\"][.][\"]'
    
    r'("(\\"|[^"])*")|(\'(\\\'|[^\'])*\')'

    # ------------- Debugging ---------------
    # print ("Found a string!", t.value)
    # ------------- Debugging ---------------

    return t

# Comments rule
def t_COMMENT(t):
    r'\#.*\n'

    # ------------- Debugging ---------------
    # print ("Found a comment!", t.value)
    # ------------- Debugging ---------------

    return t







def run(args, code):

    language_dict = yaml.load(open(args["dictionary"]), Loader=yaml.SafeLoader)

    if args["reverse"]:
        reserved = {value:key for key, value in language_dict.get("reserved").items()}
        # ------------- Debugging ---------------
        # print ("Reversed:", reserved)
        # ------------- Debugging ---------------

    else:
        reserved = language_dict.get("reserved")
        # ------------- Debugging ---------------
        # print ("normal:", reserved)
        # ------------- Debugging ---------------

        

    # ------------- Debugging ---------------
    # print ("'a' in ASCII number is:", ord('a'))
    # print ("'ا' in ASCII number is:", ord('ا'))
    # print ("'۰' in ASCII number is:", ord('۰'))
    # print ("'۲' in ASCII number is:", ord('۲'))
    # print ("'۹' in ASCII number is:", ord('۹'))
    # ------------- Debugging ---------------



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

    # List of token names.   This is always required
    tokens =  default_tokens + list(reserved.values())

    # A regular expression rule with some action code
    def t_NUMBER(t):
        # ------------- Debugging ---------------
        # print ("The number was:", t.value)
        # ------------- Debugging ---------------
        

        if args["reverse"]:
            value_str = list(t.value)
            for i in range(0, len(value_str)):
                value_str[i] = reserved.get(value_str[i], value_str[i])
            t.value = ''.join(value_str)
        else:
            import urdupython.filters.unidecoder as num_filter
            t.value = num_filter.filter(t.value)
        
        # ------------- Debugging ---------------
        # print ("The number is now:", t.value)
        # ------------- Debugging ---------------

        return t


    # Define a rule so we can track line numbers
    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        return t

    def t_ID(t):
        # r'[a-zA-Z_][a-zA-Z_0-9]*'
        # r'[ا-ی_][۰-۹_ا-ی]*'

        ## Docstring is assigned AFTER the function, because it has variables in the regex...
        ## Reference: https://stackoverflow.com/questions/12217816/regex-with-variable-data-in-it-ply-lex

        t.type = reserved.get(t.value,'ID')    # Check for reserved words    
        
        # if ttt

        # ------------- Debugging ---------------
        # print ("looking for error:", t.type, ", ", t.value)
        # ------------- Debugging ---------------

        # ------------- Debugging ---------------
        # print ("Type is:", t.type)
        # ------------- Debugging ---------------

        # ------------- Debugging ---------------
        # print ("Value is:", t.value)
        # ------------- Debugging ---------------


        if args['translate']:
            if t.type == 'ID':
                t.value = unidecode(t.value)




        return t


    # Error handling rule
    def t_error(t):
        # ------------- Debugging ---------------
        # print("Illegal character '%s'" % t.value[0])
        # ------------- Debugging ---------------

        if args["reverse"] is False:
            t.value = unidecode(t.value[0])
        else:
            t.value = t.value[0]

        t.lexer.skip(1)


        # ------------- Debugging ---------------
        # print("Now becomes '%s'" % t.value[0])
        # print("still keeping it tho")
        # ------------- Debugging ---------------

        return t

        # r'[۰-۹][۰-۹]*[۔]{0,1}[۰-۹]*'
    if args["reverse"]:
        t_NUMBER.__doc__ = r'[0-9][0-9]*[۔]{0,1}[0-9]*'
    else:    
        t_NUMBER.__doc__ = r'['+language_dict["numbers"]["start"]+'-'+language_dict["numbers"]["end"]+']['+language_dict["numbers"]["start"]+'-'+language_dict["numbers"]["end"]+']*[۔]{0,1}['+language_dict["numbers"]["start"]+'-'+language_dict["numbers"]["end"]+']*'


    if args["reverse"]:
        t_ID.__doc__ = r'[a-zA-Z_][a-zA-Z_0-9]*'
    else:    
        t_ID.__doc__ = r'['+language_dict["letters"]["start"]+'-'+language_dict["letters"]["end"]+'_]['+language_dict["numbers"]["start"]+'-'+language_dict["numbers"]["end"]+'_'+language_dict["letters"]["start"]+'-'+language_dict["letters"]["end"]+']*'


    # A string containing ignored characters (spaces and tabs)
    # t_ignore  = ' \t'

    # Build the lexer
    lexer = lex.lex()

    # Give the lexer some input!

    # ------------- Debugging ---------------
    # lexer.input("#print 1==2")
    # lexer.input("""

    # اگر (۱==۱):
    #     لکھو(۲==۲)

    # """)
    # ------------- Debugging ---------------


    # ur_pyfile = open(args["file"][0])
        
    # code = ur_pyfile.read()

    dots_and_stuff = {
        "۔":          ".",
        "،":          ",",  
    }

    # ------------- Debugging ---------------
    # print ("normal:", dots_and_stuff)
    # ------------- Debugging ---------------

    if args["reverse"]:
        dots_and_stuff = {value:key for key, value in dots_and_stuff.items()}
        # ------------- Debugging ---------------
        # print ("Reversed:", dots_and_stuff)
        # ------------- Debugging ---------------

    for key, value in dots_and_stuff.items():
        code = code.replace(key, value)

    # ------------- Debugging ---------------
    # print ("Code is,\n", code)
    # ------------- Debugging ---------------

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
        print(tok)
        print ("Tok's value is:", tok.value)
        print ("Tok's type is:", tok.type)
        # ------------- Debugging ---------------



        if tok.value in reserved.keys():

            # ------------- Debugging ---------------
            # if tok.type == '۔':
            #     print ("Found an Urdu dot!")
            # ------------- Debugging ---------------
    
            # if args["reverse"] and tok.type == 'NUMBER':
            #     compiled_code += tok.value
            # else:
            compiled_code += tok.type
        else:
            compiled_code += tok.value


    if args["keep"] or args["keep_only"]:
        eng_pyfile.write(compiled_code)
        eng_pyfile.close()


    if args["return"] is True:
        return compiled_code

    elif args["keep_only"] is False:
        exec(compiled_code)