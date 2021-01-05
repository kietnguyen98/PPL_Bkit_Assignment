# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u01eb\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\7\3\u009b\n\3\f\3\16\3\u009e\13\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3")
        buf.write("$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3*\3")
        buf.write("+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65")
        buf.write("\3\65\3\66\3\66\3\67\3\67\38\68\u0173\n8\r8\168\u0174")
        buf.write("\38\38\39\39\79\u017b\n9\f9\169\u017e\139\3:\3:\3:\6:")
        buf.write("\u0183\n:\r:\16:\u0184\3;\3;\3<\3<\3<\6<\u018c\n<\r<\16")
        buf.write("<\u018d\3=\3=\3=\6=\u0193\n=\r=\16=\u0194\3>\3>\3>\3>")
        buf.write("\3>\3>\3>\3>\3>\3>\5>\u01a1\n>\3?\3?\3@\6@\u01a6\n@\r")
        buf.write("@\16@\u01a7\3A\3A\7A\u01ac\nA\fA\16A\u01af\13A\3B\3B\3")
        buf.write("B\5B\u01b4\nB\3B\6B\u01b7\nB\rB\16B\u01b8\3C\3C\5C\u01bd")
        buf.write("\nC\3D\3D\3D\3E\3E\3E\3E\3E\7E\u01c7\nE\fE\16E\u01ca\13")
        buf.write("E\3E\3E\3E\3F\3F\3F\3G\3G\3G\7G\u01d5\nG\fG\16G\u01d8")
        buf.write("\13G\3G\5G\u01db\nG\3G\3G\3H\3H\3H\7H\u01e2\nH\fH\16H")
        buf.write("\u01e5\13H\3H\3H\3H\3H\3H\3\u009c\2I\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_")
        buf.write("\61a\62c\63e\64g\65i\66k\67m8o9q:s;u\2w\2y\2{<}\2\177")
        buf.write("\2\u0081\2\u0083\2\u0085=\u0087\2\u0089>\u008b?\u008d")
        buf.write("@\u008fA\3\2\22\5\2\13\f\16\17\"\"\3\2c|\6\2\62;C\\aa")
        buf.write("c|\3\2\62;\4\2ZZzz\4\2\62;CH\4\2QQqq\3\2\629\4\2GGgg\t")
        buf.write("\2))^^ddhhppttvv\6\2\f\f\17\17))^^\5\2\f\f\17\17$$\3\3")
        buf.write("\f\f\4\2$$^^\3\2^^\n\2$$))^^ddhhppttvv\2\u01f9\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2{\3\2\2\2\2\u0085\3\2\2\2\2\u0089\3\2\2\2")
        buf.write("\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\3\u0091")
        buf.write("\3\2\2\2\5\u0096\3\2\2\2\7\u00a4\3\2\2\2\t\u00a9\3\2\2")
        buf.write("\2\13\u00af\3\2\2\2\r\u00b8\3\2\2\2\17\u00bb\3\2\2\2\21")
        buf.write("\u00c0\3\2\2\2\23\u00c7\3\2\2\2\25\u00cf\3\2\2\2\27\u00d5")
        buf.write("\3\2\2\2\31\u00dc\3\2\2\2\33\u00e5\3\2\2\2\35\u00e9\3")
        buf.write("\2\2\2\37\u00f2\3\2\2\2!\u00f5\3\2\2\2#\u00ff\3\2\2\2")
        buf.write("%\u0106\3\2\2\2\'\u010b\3\2\2\2)\u010f\3\2\2\2+\u0115")
        buf.write("\3\2\2\2-\u011a\3\2\2\2/\u0120\3\2\2\2\61\u0122\3\2\2")
        buf.write("\2\63\u0125\3\2\2\2\65\u0127\3\2\2\2\67\u012a\3\2\2\2")
        buf.write("9\u012c\3\2\2\2;\u012f\3\2\2\2=\u0131\3\2\2\2?\u0133\3")
        buf.write("\2\2\2A\u0135\3\2\2\2C\u0137\3\2\2\2E\u013a\3\2\2\2G\u013d")
        buf.write("\3\2\2\2I\u013f\3\2\2\2K\u0142\3\2\2\2M\u0145\3\2\2\2")
        buf.write("O\u0147\3\2\2\2Q\u014a\3\2\2\2S\u014c\3\2\2\2U\u014f\3")
        buf.write("\2\2\2W\u0152\3\2\2\2Y\u0156\3\2\2\2[\u0159\3\2\2\2]\u015d")
        buf.write("\3\2\2\2_\u0161\3\2\2\2a\u0163\3\2\2\2c\u0165\3\2\2\2")
        buf.write("e\u0167\3\2\2\2g\u0169\3\2\2\2i\u016b\3\2\2\2k\u016d\3")
        buf.write("\2\2\2m\u016f\3\2\2\2o\u0172\3\2\2\2q\u0178\3\2\2\2s\u0182")
        buf.write("\3\2\2\2u\u0186\3\2\2\2w\u0188\3\2\2\2y\u018f\3\2\2\2")
        buf.write("{\u01a0\3\2\2\2}\u01a2\3\2\2\2\177\u01a5\3\2\2\2\u0081")
        buf.write("\u01a9\3\2\2\2\u0083\u01b0\3\2\2\2\u0085\u01bc\3\2\2\2")
        buf.write("\u0087\u01be\3\2\2\2\u0089\u01c1\3\2\2\2\u008b\u01ce\3")
        buf.write("\2\2\2\u008d\u01d1\3\2\2\2\u008f\u01de\3\2\2\2\u0091\u0092")
        buf.write("\7o\2\2\u0092\u0093\7c\2\2\u0093\u0094\7k\2\2\u0094\u0095")
        buf.write("\7p\2\2\u0095\4\3\2\2\2\u0096\u0097\7,\2\2\u0097\u0098")
        buf.write("\7,\2\2\u0098\u009c\3\2\2\2\u0099\u009b\13\2\2\2\u009a")
        buf.write("\u0099\3\2\2\2\u009b\u009e\3\2\2\2\u009c\u009d\3\2\2\2")
        buf.write("\u009c\u009a\3\2\2\2\u009d\u009f\3\2\2\2\u009e\u009c\3")
        buf.write("\2\2\2\u009f\u00a0\7,\2\2\u00a0\u00a1\7,\2\2\u00a1\u00a2")
        buf.write("\3\2\2\2\u00a2\u00a3\b\3\2\2\u00a3\6\3\2\2\2\u00a4\u00a5")
        buf.write("\7D\2\2\u00a5\u00a6\7q\2\2\u00a6\u00a7\7f\2\2\u00a7\u00a8")
        buf.write("\7{\2\2\u00a8\b\3\2\2\2\u00a9\u00aa\7D\2\2\u00aa\u00ab")
        buf.write("\7t\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad\7c\2\2\u00ad\u00ae")
        buf.write("\7m\2\2\u00ae\n\3\2\2\2\u00af\u00b0\7E\2\2\u00b0\u00b1")
        buf.write("\7q\2\2\u00b1\u00b2\7p\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4")
        buf.write("\7k\2\2\u00b4\u00b5\7p\2\2\u00b5\u00b6\7w\2\2\u00b6\u00b7")
        buf.write("\7g\2\2\u00b7\f\3\2\2\2\u00b8\u00b9\7F\2\2\u00b9\u00ba")
        buf.write("\7q\2\2\u00ba\16\3\2\2\2\u00bb\u00bc\7G\2\2\u00bc\u00bd")
        buf.write("\7n\2\2\u00bd\u00be\7u\2\2\u00be\u00bf\7g\2\2\u00bf\20")
        buf.write("\3\2\2\2\u00c0\u00c1\7G\2\2\u00c1\u00c2\7n\2\2\u00c2\u00c3")
        buf.write("\7u\2\2\u00c3\u00c4\7g\2\2\u00c4\u00c5\7K\2\2\u00c5\u00c6")
        buf.write("\7h\2\2\u00c6\22\3\2\2\2\u00c7\u00c8\7G\2\2\u00c8\u00c9")
        buf.write("\7p\2\2\u00c9\u00ca\7f\2\2\u00ca\u00cb\7D\2\2\u00cb\u00cc")
        buf.write("\7q\2\2\u00cc\u00cd\7f\2\2\u00cd\u00ce\7{\2\2\u00ce\24")
        buf.write("\3\2\2\2\u00cf\u00d0\7G\2\2\u00d0\u00d1\7p\2\2\u00d1\u00d2")
        buf.write("\7f\2\2\u00d2\u00d3\7K\2\2\u00d3\u00d4\7h\2\2\u00d4\26")
        buf.write("\3\2\2\2\u00d5\u00d6\7G\2\2\u00d6\u00d7\7p\2\2\u00d7\u00d8")
        buf.write("\7f\2\2\u00d8\u00d9\7H\2\2\u00d9\u00da\7q\2\2\u00da\u00db")
        buf.write("\7t\2\2\u00db\30\3\2\2\2\u00dc\u00dd\7G\2\2\u00dd\u00de")
        buf.write("\7p\2\2\u00de\u00df\7f\2\2\u00df\u00e0\7Y\2\2\u00e0\u00e1")
        buf.write("\7j\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3\7n\2\2\u00e3\u00e4")
        buf.write("\7g\2\2\u00e4\32\3\2\2\2\u00e5\u00e6\7H\2\2\u00e6\u00e7")
        buf.write("\7q\2\2\u00e7\u00e8\7t\2\2\u00e8\34\3\2\2\2\u00e9\u00ea")
        buf.write("\7H\2\2\u00ea\u00eb\7w\2\2\u00eb\u00ec\7p\2\2\u00ec\u00ed")
        buf.write("\7e\2\2\u00ed\u00ee\7v\2\2\u00ee\u00ef\7k\2\2\u00ef\u00f0")
        buf.write("\7q\2\2\u00f0\u00f1\7p\2\2\u00f1\36\3\2\2\2\u00f2\u00f3")
        buf.write("\7K\2\2\u00f3\u00f4\7h\2\2\u00f4 \3\2\2\2\u00f5\u00f6")
        buf.write("\7R\2\2\u00f6\u00f7\7c\2\2\u00f7\u00f8\7t\2\2\u00f8\u00f9")
        buf.write("\7c\2\2\u00f9\u00fa\7o\2\2\u00fa\u00fb\7g\2\2\u00fb\u00fc")
        buf.write("\7v\2\2\u00fc\u00fd\7g\2\2\u00fd\u00fe\7t\2\2\u00fe\"")
        buf.write("\3\2\2\2\u00ff\u0100\7T\2\2\u0100\u0101\7g\2\2\u0101\u0102")
        buf.write("\7v\2\2\u0102\u0103\7w\2\2\u0103\u0104\7t\2\2\u0104\u0105")
        buf.write("\7p\2\2\u0105$\3\2\2\2\u0106\u0107\7V\2\2\u0107\u0108")
        buf.write("\7j\2\2\u0108\u0109\7g\2\2\u0109\u010a\7p\2\2\u010a&\3")
        buf.write("\2\2\2\u010b\u010c\7X\2\2\u010c\u010d\7c\2\2\u010d\u010e")
        buf.write("\7t\2\2\u010e(\3\2\2\2\u010f\u0110\7Y\2\2\u0110\u0111")
        buf.write("\7j\2\2\u0111\u0112\7k\2\2\u0112\u0113\7n\2\2\u0113\u0114")
        buf.write("\7g\2\2\u0114*\3\2\2\2\u0115\u0116\7V\2\2\u0116\u0117")
        buf.write("\7t\2\2\u0117\u0118\7w\2\2\u0118\u0119\7g\2\2\u0119,\3")
        buf.write("\2\2\2\u011a\u011b\7H\2\2\u011b\u011c\7c\2\2\u011c\u011d")
        buf.write("\7n\2\2\u011d\u011e\7u\2\2\u011e\u011f\7g\2\2\u011f.\3")
        buf.write("\2\2\2\u0120\u0121\7-\2\2\u0121\60\3\2\2\2\u0122\u0123")
        buf.write("\7-\2\2\u0123\u0124\7\60\2\2\u0124\62\3\2\2\2\u0125\u0126")
        buf.write("\7/\2\2\u0126\64\3\2\2\2\u0127\u0128\7/\2\2\u0128\u0129")
        buf.write("\7\60\2\2\u0129\66\3\2\2\2\u012a\u012b\7,\2\2\u012b8\3")
        buf.write("\2\2\2\u012c\u012d\7,\2\2\u012d\u012e\7\60\2\2\u012e:")
        buf.write("\3\2\2\2\u012f\u0130\7^\2\2\u0130<\3\2\2\2\u0131\u0132")
        buf.write("\7\61\2\2\u0132>\3\2\2\2\u0133\u0134\7\'\2\2\u0134@\3")
        buf.write("\2\2\2\u0135\u0136\7#\2\2\u0136B\3\2\2\2\u0137\u0138\7")
        buf.write("(\2\2\u0138\u0139\7(\2\2\u0139D\3\2\2\2\u013a\u013b\7")
        buf.write("~\2\2\u013b\u013c\7~\2\2\u013cF\3\2\2\2\u013d\u013e\7")
        buf.write("?\2\2\u013eH\3\2\2\2\u013f\u0140\7?\2\2\u0140\u0141\7")
        buf.write("?\2\2\u0141J\3\2\2\2\u0142\u0143\7#\2\2\u0143\u0144\7")
        buf.write("?\2\2\u0144L\3\2\2\2\u0145\u0146\7>\2\2\u0146N\3\2\2\2")
        buf.write("\u0147\u0148\7>\2\2\u0148\u0149\7\60\2\2\u0149P\3\2\2")
        buf.write("\2\u014a\u014b\7@\2\2\u014bR\3\2\2\2\u014c\u014d\7@\2")
        buf.write("\2\u014d\u014e\7\60\2\2\u014eT\3\2\2\2\u014f\u0150\7>")
        buf.write("\2\2\u0150\u0151\7?\2\2\u0151V\3\2\2\2\u0152\u0153\7>")
        buf.write("\2\2\u0153\u0154\7?\2\2\u0154\u0155\7\60\2\2\u0155X\3")
        buf.write("\2\2\2\u0156\u0157\7@\2\2\u0157\u0158\7?\2\2\u0158Z\3")
        buf.write("\2\2\2\u0159\u015a\7@\2\2\u015a\u015b\7?\2\2\u015b\u015c")
        buf.write("\7\60\2\2\u015c\\\3\2\2\2\u015d\u015e\7?\2\2\u015e\u015f")
        buf.write("\7\61\2\2\u015f\u0160\7?\2\2\u0160^\3\2\2\2\u0161\u0162")
        buf.write("\7*\2\2\u0162`\3\2\2\2\u0163\u0164\7+\2\2\u0164b\3\2\2")
        buf.write("\2\u0165\u0166\7]\2\2\u0166d\3\2\2\2\u0167\u0168\7_\2")
        buf.write("\2\u0168f\3\2\2\2\u0169\u016a\7<\2\2\u016ah\3\2\2\2\u016b")
        buf.write("\u016c\7\60\2\2\u016cj\3\2\2\2\u016d\u016e\7.\2\2\u016e")
        buf.write("l\3\2\2\2\u016f\u0170\7=\2\2\u0170n\3\2\2\2\u0171\u0173")
        buf.write("\t\2\2\2\u0172\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174")
        buf.write("\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0176\3\2\2\2")
        buf.write("\u0176\u0177\b8\2\2\u0177p\3\2\2\2\u0178\u017c\t\3\2\2")
        buf.write("\u0179\u017b\t\4\2\2\u017a\u0179\3\2\2\2\u017b\u017e\3")
        buf.write("\2\2\2\u017c\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017dr")
        buf.write("\3\2\2\2\u017e\u017c\3\2\2\2\u017f\u0183\5u;\2\u0180\u0183")
        buf.write("\5w<\2\u0181\u0183\5y=\2\u0182\u017f\3\2\2\2\u0182\u0180")
        buf.write("\3\2\2\2\u0182\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184")
        buf.write("\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185t\3\2\2\2\u0186")
        buf.write("\u0187\t\5\2\2\u0187v\3\2\2\2\u0188\u0189\7\62\2\2\u0189")
        buf.write("\u018b\t\6\2\2\u018a\u018c\t\7\2\2\u018b\u018a\3\2\2\2")
        buf.write("\u018c\u018d\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018e\3")
        buf.write("\2\2\2\u018ex\3\2\2\2\u018f\u0190\7\62\2\2\u0190\u0192")
        buf.write("\t\b\2\2\u0191\u0193\t\t\2\2\u0192\u0191\3\2\2\2\u0193")
        buf.write("\u0194\3\2\2\2\u0194\u0192\3\2\2\2\u0194\u0195\3\2\2\2")
        buf.write("\u0195z\3\2\2\2\u0196\u0197\5\177@\2\u0197\u0198\5\u0081")
        buf.write("A\2\u0198\u0199\5\u0083B\2\u0199\u01a1\3\2\2\2\u019a\u019b")
        buf.write("\5\177@\2\u019b\u019c\5\u0081A\2\u019c\u01a1\3\2\2\2\u019d")
        buf.write("\u019e\5\177@\2\u019e\u019f\5\u0083B\2\u019f\u01a1\3\2")
        buf.write("\2\2\u01a0\u0196\3\2\2\2\u01a0\u019a\3\2\2\2\u01a0\u019d")
        buf.write("\3\2\2\2\u01a1|\3\2\2\2\u01a2\u01a3\t\5\2\2\u01a3~\3\2")
        buf.write("\2\2\u01a4\u01a6\5}?\2\u01a5\u01a4\3\2\2\2\u01a6\u01a7")
        buf.write("\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8")
        buf.write("\u0080\3\2\2\2\u01a9\u01ad\5i\65\2\u01aa\u01ac\5}?\2\u01ab")
        buf.write("\u01aa\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2")
        buf.write("\u01ad\u01ae\3\2\2\2\u01ae\u0082\3\2\2\2\u01af\u01ad\3")
        buf.write("\2\2\2\u01b0\u01b3\t\n\2\2\u01b1\u01b4\5/\30\2\u01b2\u01b4")
        buf.write("\5\63\32\2\u01b3\u01b1\3\2\2\2\u01b3\u01b2\3\2\2\2\u01b3")
        buf.write("\u01b4\3\2\2\2\u01b4\u01b6\3\2\2\2\u01b5\u01b7\5}?\2\u01b6")
        buf.write("\u01b5\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01b6\3\2\2\2")
        buf.write("\u01b8\u01b9\3\2\2\2\u01b9\u0084\3\2\2\2\u01ba\u01bd\5")
        buf.write("+\26\2\u01bb\u01bd\5-\27\2\u01bc\u01ba\3\2\2\2\u01bc\u01bb")
        buf.write("\3\2\2\2\u01bd\u0086\3\2\2\2\u01be\u01bf\7^\2\2\u01bf")
        buf.write("\u01c0\t\13\2\2\u01c0\u0088\3\2\2\2\u01c1\u01c8\7$\2\2")
        buf.write("\u01c2\u01c7\5\u0087D\2\u01c3\u01c4\7)\2\2\u01c4\u01c7")
        buf.write("\7$\2\2\u01c5\u01c7\n\f\2\2\u01c6\u01c2\3\2\2\2\u01c6")
        buf.write("\u01c3\3\2\2\2\u01c6\u01c5\3\2\2\2\u01c7\u01ca\3\2\2\2")
        buf.write("\u01c8\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01cb\3")
        buf.write("\2\2\2\u01ca\u01c8\3\2\2\2\u01cb\u01cc\7$\2\2\u01cc\u01cd")
        buf.write("\bE\3\2\u01cd\u008a\3\2\2\2\u01ce\u01cf\13\2\2\2\u01cf")
        buf.write("\u01d0\bF\4\2\u01d0\u008c\3\2\2\2\u01d1\u01d6\7$\2\2\u01d2")
        buf.write("\u01d5\5\u0087D\2\u01d3\u01d5\n\r\2\2\u01d4\u01d2\3\2")
        buf.write("\2\2\u01d4\u01d3\3\2\2\2\u01d5\u01d8\3\2\2\2\u01d6\u01d4")
        buf.write("\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01da\3\2\2\2\u01d8")
        buf.write("\u01d6\3\2\2\2\u01d9\u01db\t\16\2\2\u01da\u01d9\3\2\2")
        buf.write("\2\u01db\u01dc\3\2\2\2\u01dc\u01dd\bG\5\2\u01dd\u008e")
        buf.write("\3\2\2\2\u01de\u01e3\7$\2\2\u01df\u01e2\5\u0087D\2\u01e0")
        buf.write("\u01e2\n\17\2\2\u01e1\u01df\3\2\2\2\u01e1\u01e0\3\2\2")
        buf.write("\2\u01e2\u01e5\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e3\u01e4")
        buf.write("\3\2\2\2\u01e4\u01e6\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e6")
        buf.write("\u01e7\t\20\2\2\u01e7\u01e8\n\21\2\2\u01e8\u01e9\3\2\2")
        buf.write("\2\u01e9\u01ea\bH\6\2\u01ea\u0090\3\2\2\2\27\2\u009c\u0174")
        buf.write("\u017c\u0182\u0184\u018d\u0194\u01a0\u01a7\u01ad\u01b3")
        buf.write("\u01b8\u01bc\u01c6\u01c8\u01d4\u01d6\u01da\u01e1\u01e3")
        buf.write("\7\b\2\2\3E\2\3F\3\3G\4\3H\5")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    BLOCKCOMMENT = 2
    BODY = 3
    BREAK = 4
    CONTINUE = 5
    DO = 6
    ELSE = 7
    ELSEIF = 8
    ENDBODY = 9
    ENDIF = 10
    ENDFOR = 11
    ENDWHILE = 12
    FOR = 13
    FUNCTION = 14
    IF = 15
    PARAMETER = 16
    RETURN = 17
    THEN = 18
    VAR = 19
    WHILE = 20
    TRUE = 21
    FALSE = 22
    INT_ADD = 23
    FLOAT_ADD = 24
    INT_SUB = 25
    FLOAT_SUB = 26
    INT_MUL = 27
    FLOAT_MUL = 28
    INT_DIV = 29
    FLOAT_DIV = 30
    INT_MOD = 31
    NOT = 32
    AND = 33
    OR = 34
    EQUAL_ASSIGN = 35
    INT_EQUAL = 36
    INT_NOT_EQUAL = 37
    INT_LESS_THAN = 38
    FLOAT_LESS_THAN = 39
    INT_MORE_THAN = 40
    FLOAT_MORE_THAN = 41
    INT_LESS_OR_EQUAL = 42
    FLOAT_LESS_OR_EQUAL = 43
    INT_MORE_OR_EQUAL = 44
    FLOAT_MORE_OR_EQUAL = 45
    FLOAT_NOT_EQUAL = 46
    LB = 47
    RB = 48
    LSB = 49
    RSB = 50
    COLON = 51
    DOT = 52
    COMMA = 53
    SEMI = 54
    WS = 55
    ID = 56
    INTLIT = 57
    FLOATLIT = 58
    BOOLEANLIT = 59
    STRINGLIT = 60
    ERROR_CHAR = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", 
            "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", 
            "'For'", "'Function'", "'If'", "'Parameter'", "'Return'", "'Then'", 
            "'Var'", "'While'", "'True'", "'False'", "'+'", "'+.'", "'-'", 
            "'-.'", "'*'", "'*.'", "'\\'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'='", "'=='", "'!='", "'<'", "'<.'", "'>'", "'>.'", 
            "'<='", "'<=.'", "'>='", "'>=.'", "'=/='", "'('", "')'", "'['", 
            "']'", "':'", "'.'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "BLOCKCOMMENT", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", 
            "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
            "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", "TRUE", 
            "FALSE", "INT_ADD", "FLOAT_ADD", "INT_SUB", "FLOAT_SUB", "INT_MUL", 
            "FLOAT_MUL", "INT_DIV", "FLOAT_DIV", "INT_MOD", "NOT", "AND", 
            "OR", "EQUAL_ASSIGN", "INT_EQUAL", "INT_NOT_EQUAL", "INT_LESS_THAN", 
            "FLOAT_LESS_THAN", "INT_MORE_THAN", "FLOAT_MORE_THAN", "INT_LESS_OR_EQUAL", 
            "FLOAT_LESS_OR_EQUAL", "INT_MORE_OR_EQUAL", "FLOAT_MORE_OR_EQUAL", 
            "FLOAT_NOT_EQUAL", "LB", "RB", "LSB", "RSB", "COLON", "DOT", 
            "COMMA", "SEMI", "WS", "ID", "INTLIT", "FLOATLIT", "BOOLEANLIT", 
            "STRINGLIT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "BLOCKCOMMENT", "BODY", "BREAK", "CONTINUE", "DO", 
                  "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", 
                  "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", 
                  "VAR", "WHILE", "TRUE", "FALSE", "INT_ADD", "FLOAT_ADD", 
                  "INT_SUB", "FLOAT_SUB", "INT_MUL", "FLOAT_MUL", "INT_DIV", 
                  "FLOAT_DIV", "INT_MOD", "NOT", "AND", "OR", "EQUAL_ASSIGN", 
                  "INT_EQUAL", "INT_NOT_EQUAL", "INT_LESS_THAN", "FLOAT_LESS_THAN", 
                  "INT_MORE_THAN", "FLOAT_MORE_THAN", "INT_LESS_OR_EQUAL", 
                  "FLOAT_LESS_OR_EQUAL", "INT_MORE_OR_EQUAL", "FLOAT_MORE_OR_EQUAL", 
                  "FLOAT_NOT_EQUAL", "LB", "RB", "LSB", "RSB", "COLON", 
                  "DOT", "COMMA", "SEMI", "WS", "ID", "INTLIT", "DEC", "HEX", 
                  "OC", "FLOATLIT", "DIGITS", "INT_PART", "DEC_PART", "EXPO_PART", 
                  "BOOLEANLIT", "ESCAPE_SEQUENCES", "STRINGLIT", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[67] = self.STRINGLIT_action 
            actions[68] = self.ERROR_CHAR_action 
            actions[69] = self.UNCLOSE_STRING_action 
            actions[70] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            			self.text = self.text[1:len(self.text)-1]
            		
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             
                        raise ErrorToken(self.text[0:]) 
                    
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                        if self.text[-1]=='\n':
                             raise UncloseString(self.text[1:-1])
                        else:
                            raise UncloseString(self.text[1:])
                    
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                       raise IllegalEscape(self.text[1:])
                    
     


