# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u0207\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\7\6\u00b7\n\6\f\6\16\6\u00ba\13\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&")
        buf.write("\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3+\3+\3+\3,\3,\3-\3-")
        buf.write("\3-\3.\3.\3.\3/\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\61\3\62\3\62\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\6;\u018f\n;")
        buf.write("\r;\16;\u0190\3;\3;\3<\3<\7<\u0197\n<\f<\16<\u019a\13")
        buf.write("<\3=\3=\3=\6=\u019f\n=\r=\16=\u01a0\3>\3>\3?\3?\3?\6?")
        buf.write("\u01a8\n?\r?\16?\u01a9\3@\3@\3@\6@\u01af\n@\r@\16@\u01b0")
        buf.write("\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\5A\u01bd\nA\3B\3B\3C\6")
        buf.write("C\u01c2\nC\rC\16C\u01c3\3D\3D\7D\u01c8\nD\fD\16D\u01cb")
        buf.write("\13D\3E\3E\3E\5E\u01d0\nE\3E\6E\u01d3\nE\rE\16E\u01d4")
        buf.write("\3F\3F\5F\u01d9\nF\3G\3G\3G\3H\3H\3H\3H\3H\7H\u01e3\n")
        buf.write("H\fH\16H\u01e6\13H\3H\3H\3H\3I\3I\3I\3J\3J\3J\7J\u01f1")
        buf.write("\nJ\fJ\16J\u01f4\13J\3J\5J\u01f7\nJ\3J\3J\3K\3K\3K\7K")
        buf.write("\u01fe\nK\fK\16K\u0201\13K\3K\3K\3K\3K\3K\3\u00b8\2L\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w")
        buf.write("=y>{\2}\2\177\2\u0081?\u0083\2\u0085\2\u0087\2\u0089\2")
        buf.write("\u008b@\u008d\2\u008fA\u0091B\u0093C\u0095D\3\2\22\5\2")
        buf.write("\13\f\16\17\"\"\3\2c|\6\2\62;C\\aac|\3\2\62;\4\2ZZzz\4")
        buf.write("\2\62;CH\4\2QQqq\3\2\629\4\2GGgg\t\2))^^ddhhppttvv\6\2")
        buf.write("\f\f\17\17))^^\5\2\f\f\17\17$$\3\3\f\f\4\2$$^^\3\2^^\n")
        buf.write("\2$$))^^ddhhppttvv\2\u0215\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2w\3\2\2\2\2y\3\2\2\2\2\u0081\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\3\u0097\3\2\2\2\5\u009c\3\2\2\2\7\u00a4\3\2\2")
        buf.write("\2\t\u00ac\3\2\2\2\13\u00b2\3\2\2\2\r\u00c0\3\2\2\2\17")
        buf.write("\u00c5\3\2\2\2\21\u00cb\3\2\2\2\23\u00d4\3\2\2\2\25\u00d7")
        buf.write("\3\2\2\2\27\u00dc\3\2\2\2\31\u00e3\3\2\2\2\33\u00eb\3")
        buf.write("\2\2\2\35\u00f1\3\2\2\2\37\u00f8\3\2\2\2!\u0101\3\2\2")
        buf.write("\2#\u0105\3\2\2\2%\u010e\3\2\2\2\'\u0111\3\2\2\2)\u011b")
        buf.write("\3\2\2\2+\u0122\3\2\2\2-\u0127\3\2\2\2/\u012b\3\2\2\2")
        buf.write("\61\u0131\3\2\2\2\63\u0136\3\2\2\2\65\u013c\3\2\2\2\67")
        buf.write("\u013e\3\2\2\29\u0141\3\2\2\2;\u0143\3\2\2\2=\u0146\3")
        buf.write("\2\2\2?\u0148\3\2\2\2A\u014b\3\2\2\2C\u014d\3\2\2\2E\u014f")
        buf.write("\3\2\2\2G\u0151\3\2\2\2I\u0153\3\2\2\2K\u0156\3\2\2\2")
        buf.write("M\u0159\3\2\2\2O\u015b\3\2\2\2Q\u015e\3\2\2\2S\u0161\3")
        buf.write("\2\2\2U\u0163\3\2\2\2W\u0166\3\2\2\2Y\u0168\3\2\2\2[\u016b")
        buf.write("\3\2\2\2]\u016e\3\2\2\2_\u0172\3\2\2\2a\u0175\3\2\2\2")
        buf.write("c\u0179\3\2\2\2e\u017d\3\2\2\2g\u017f\3\2\2\2i\u0181\3")
        buf.write("\2\2\2k\u0183\3\2\2\2m\u0185\3\2\2\2o\u0187\3\2\2\2q\u0189")
        buf.write("\3\2\2\2s\u018b\3\2\2\2u\u018e\3\2\2\2w\u0194\3\2\2\2")
        buf.write("y\u019e\3\2\2\2{\u01a2\3\2\2\2}\u01a4\3\2\2\2\177\u01ab")
        buf.write("\3\2\2\2\u0081\u01bc\3\2\2\2\u0083\u01be\3\2\2\2\u0085")
        buf.write("\u01c1\3\2\2\2\u0087\u01c5\3\2\2\2\u0089\u01cc\3\2\2\2")
        buf.write("\u008b\u01d8\3\2\2\2\u008d\u01da\3\2\2\2\u008f\u01dd\3")
        buf.write("\2\2\2\u0091\u01ea\3\2\2\2\u0093\u01ed\3\2\2\2\u0095\u01fa")
        buf.write("\3\2\2\2\u0097\u0098\7o\2\2\u0098\u0099\7c\2\2\u0099\u009a")
        buf.write("\7k\2\2\u009a\u009b\7p\2\2\u009b\4\3\2\2\2\u009c\u009d")
        buf.write("\7k\2\2\u009d\u009e\7p\2\2\u009e\u009f\7v\2\2\u009f\u00a0")
        buf.write("\7g\2\2\u00a0\u00a1\7i\2\2\u00a1\u00a2\7g\2\2\u00a2\u00a3")
        buf.write("\7t\2\2\u00a3\6\3\2\2\2\u00a4\u00a5\7d\2\2\u00a5\u00a6")
        buf.write("\7q\2\2\u00a6\u00a7\7q\2\2\u00a7\u00a8\7n\2\2\u00a8\u00a9")
        buf.write("\7g\2\2\u00a9\u00aa\7c\2\2\u00aa\u00ab\7p\2\2\u00ab\b")
        buf.write("\3\2\2\2\u00ac\u00ad\7h\2\2\u00ad\u00ae\7n\2\2\u00ae\u00af")
        buf.write("\7q\2\2\u00af\u00b0\7c\2\2\u00b0\u00b1\7v\2\2\u00b1\n")
        buf.write("\3\2\2\2\u00b2\u00b3\7,\2\2\u00b3\u00b4\7,\2\2\u00b4\u00b8")
        buf.write("\3\2\2\2\u00b5\u00b7\13\2\2\2\u00b6\u00b5\3\2\2\2\u00b7")
        buf.write("\u00ba\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b8\u00b6\3\2\2\2")
        buf.write("\u00b9\u00bb\3\2\2\2\u00ba\u00b8\3\2\2\2\u00bb\u00bc\7")
        buf.write(",\2\2\u00bc\u00bd\7,\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf")
        buf.write("\b\6\2\2\u00bf\f\3\2\2\2\u00c0\u00c1\7D\2\2\u00c1\u00c2")
        buf.write("\7q\2\2\u00c2\u00c3\7f\2\2\u00c3\u00c4\7{\2\2\u00c4\16")
        buf.write("\3\2\2\2\u00c5\u00c6\7D\2\2\u00c6\u00c7\7t\2\2\u00c7\u00c8")
        buf.write("\7g\2\2\u00c8\u00c9\7c\2\2\u00c9\u00ca\7m\2\2\u00ca\20")
        buf.write("\3\2\2\2\u00cb\u00cc\7E\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce")
        buf.write("\7p\2\2\u00ce\u00cf\7v\2\2\u00cf\u00d0\7k\2\2\u00d0\u00d1")
        buf.write("\7p\2\2\u00d1\u00d2\7w\2\2\u00d2\u00d3\7g\2\2\u00d3\22")
        buf.write("\3\2\2\2\u00d4\u00d5\7F\2\2\u00d5\u00d6\7q\2\2\u00d6\24")
        buf.write("\3\2\2\2\u00d7\u00d8\7G\2\2\u00d8\u00d9\7n\2\2\u00d9\u00da")
        buf.write("\7u\2\2\u00da\u00db\7g\2\2\u00db\26\3\2\2\2\u00dc\u00dd")
        buf.write("\7G\2\2\u00dd\u00de\7n\2\2\u00de\u00df\7u\2\2\u00df\u00e0")
        buf.write("\7g\2\2\u00e0\u00e1\7K\2\2\u00e1\u00e2\7h\2\2\u00e2\30")
        buf.write("\3\2\2\2\u00e3\u00e4\7G\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6")
        buf.write("\7f\2\2\u00e6\u00e7\7D\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9")
        buf.write("\7f\2\2\u00e9\u00ea\7{\2\2\u00ea\32\3\2\2\2\u00eb\u00ec")
        buf.write("\7G\2\2\u00ec\u00ed\7p\2\2\u00ed\u00ee\7f\2\2\u00ee\u00ef")
        buf.write("\7K\2\2\u00ef\u00f0\7h\2\2\u00f0\34\3\2\2\2\u00f1\u00f2")
        buf.write("\7G\2\2\u00f2\u00f3\7p\2\2\u00f3\u00f4\7f\2\2\u00f4\u00f5")
        buf.write("\7H\2\2\u00f5\u00f6\7q\2\2\u00f6\u00f7\7t\2\2\u00f7\36")
        buf.write("\3\2\2\2\u00f8\u00f9\7G\2\2\u00f9\u00fa\7p\2\2\u00fa\u00fb")
        buf.write("\7f\2\2\u00fb\u00fc\7Y\2\2\u00fc\u00fd\7j\2\2\u00fd\u00fe")
        buf.write("\7k\2\2\u00fe\u00ff\7n\2\2\u00ff\u0100\7g\2\2\u0100 \3")
        buf.write("\2\2\2\u0101\u0102\7H\2\2\u0102\u0103\7q\2\2\u0103\u0104")
        buf.write("\7t\2\2\u0104\"\3\2\2\2\u0105\u0106\7H\2\2\u0106\u0107")
        buf.write("\7w\2\2\u0107\u0108\7p\2\2\u0108\u0109\7e\2\2\u0109\u010a")
        buf.write("\7v\2\2\u010a\u010b\7k\2\2\u010b\u010c\7q\2\2\u010c\u010d")
        buf.write("\7p\2\2\u010d$\3\2\2\2\u010e\u010f\7K\2\2\u010f\u0110")
        buf.write("\7h\2\2\u0110&\3\2\2\2\u0111\u0112\7R\2\2\u0112\u0113")
        buf.write("\7c\2\2\u0113\u0114\7t\2\2\u0114\u0115\7c\2\2\u0115\u0116")
        buf.write("\7o\2\2\u0116\u0117\7g\2\2\u0117\u0118\7v\2\2\u0118\u0119")
        buf.write("\7g\2\2\u0119\u011a\7t\2\2\u011a(\3\2\2\2\u011b\u011c")
        buf.write("\7T\2\2\u011c\u011d\7g\2\2\u011d\u011e\7v\2\2\u011e\u011f")
        buf.write("\7w\2\2\u011f\u0120\7t\2\2\u0120\u0121\7p\2\2\u0121*\3")
        buf.write("\2\2\2\u0122\u0123\7V\2\2\u0123\u0124\7j\2\2\u0124\u0125")
        buf.write("\7g\2\2\u0125\u0126\7p\2\2\u0126,\3\2\2\2\u0127\u0128")
        buf.write("\7X\2\2\u0128\u0129\7c\2\2\u0129\u012a\7t\2\2\u012a.\3")
        buf.write("\2\2\2\u012b\u012c\7Y\2\2\u012c\u012d\7j\2\2\u012d\u012e")
        buf.write("\7k\2\2\u012e\u012f\7n\2\2\u012f\u0130\7g\2\2\u0130\60")
        buf.write("\3\2\2\2\u0131\u0132\7V\2\2\u0132\u0133\7t\2\2\u0133\u0134")
        buf.write("\7w\2\2\u0134\u0135\7g\2\2\u0135\62\3\2\2\2\u0136\u0137")
        buf.write("\7H\2\2\u0137\u0138\7c\2\2\u0138\u0139\7n\2\2\u0139\u013a")
        buf.write("\7u\2\2\u013a\u013b\7g\2\2\u013b\64\3\2\2\2\u013c\u013d")
        buf.write("\7-\2\2\u013d\66\3\2\2\2\u013e\u013f\7-\2\2\u013f\u0140")
        buf.write("\7\60\2\2\u01408\3\2\2\2\u0141\u0142\7/\2\2\u0142:\3\2")
        buf.write("\2\2\u0143\u0144\7/\2\2\u0144\u0145\7\60\2\2\u0145<\3")
        buf.write("\2\2\2\u0146\u0147\7,\2\2\u0147>\3\2\2\2\u0148\u0149\7")
        buf.write(",\2\2\u0149\u014a\7\60\2\2\u014a@\3\2\2\2\u014b\u014c")
        buf.write("\7^\2\2\u014cB\3\2\2\2\u014d\u014e\7\61\2\2\u014eD\3\2")
        buf.write("\2\2\u014f\u0150\7\'\2\2\u0150F\3\2\2\2\u0151\u0152\7")
        buf.write("#\2\2\u0152H\3\2\2\2\u0153\u0154\7(\2\2\u0154\u0155\7")
        buf.write("(\2\2\u0155J\3\2\2\2\u0156\u0157\7~\2\2\u0157\u0158\7")
        buf.write("~\2\2\u0158L\3\2\2\2\u0159\u015a\7?\2\2\u015aN\3\2\2\2")
        buf.write("\u015b\u015c\7?\2\2\u015c\u015d\7?\2\2\u015dP\3\2\2\2")
        buf.write("\u015e\u015f\7#\2\2\u015f\u0160\7?\2\2\u0160R\3\2\2\2")
        buf.write("\u0161\u0162\7>\2\2\u0162T\3\2\2\2\u0163\u0164\7>\2\2")
        buf.write("\u0164\u0165\7\60\2\2\u0165V\3\2\2\2\u0166\u0167\7@\2")
        buf.write("\2\u0167X\3\2\2\2\u0168\u0169\7@\2\2\u0169\u016a\7\60")
        buf.write("\2\2\u016aZ\3\2\2\2\u016b\u016c\7>\2\2\u016c\u016d\7?")
        buf.write("\2\2\u016d\\\3\2\2\2\u016e\u016f\7>\2\2\u016f\u0170\7")
        buf.write("?\2\2\u0170\u0171\7\60\2\2\u0171^\3\2\2\2\u0172\u0173")
        buf.write("\7@\2\2\u0173\u0174\7?\2\2\u0174`\3\2\2\2\u0175\u0176")
        buf.write("\7@\2\2\u0176\u0177\7?\2\2\u0177\u0178\7\60\2\2\u0178")
        buf.write("b\3\2\2\2\u0179\u017a\7?\2\2\u017a\u017b\7\61\2\2\u017b")
        buf.write("\u017c\7?\2\2\u017cd\3\2\2\2\u017d\u017e\7*\2\2\u017e")
        buf.write("f\3\2\2\2\u017f\u0180\7+\2\2\u0180h\3\2\2\2\u0181\u0182")
        buf.write("\7]\2\2\u0182j\3\2\2\2\u0183\u0184\7_\2\2\u0184l\3\2\2")
        buf.write("\2\u0185\u0186\7<\2\2\u0186n\3\2\2\2\u0187\u0188\7\60")
        buf.write("\2\2\u0188p\3\2\2\2\u0189\u018a\7.\2\2\u018ar\3\2\2\2")
        buf.write("\u018b\u018c\7=\2\2\u018ct\3\2\2\2\u018d\u018f\t\2\2\2")
        buf.write("\u018e\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u018e\3")
        buf.write("\2\2\2\u0190\u0191\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0193")
        buf.write("\b;\2\2\u0193v\3\2\2\2\u0194\u0198\t\3\2\2\u0195\u0197")
        buf.write("\t\4\2\2\u0196\u0195\3\2\2\2\u0197\u019a\3\2\2\2\u0198")
        buf.write("\u0196\3\2\2\2\u0198\u0199\3\2\2\2\u0199x\3\2\2\2\u019a")
        buf.write("\u0198\3\2\2\2\u019b\u019f\5{>\2\u019c\u019f\5}?\2\u019d")
        buf.write("\u019f\5\177@\2\u019e\u019b\3\2\2\2\u019e\u019c\3\2\2")
        buf.write("\2\u019e\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u019e")
        buf.write("\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1z\3\2\2\2\u01a2\u01a3")
        buf.write("\t\5\2\2\u01a3|\3\2\2\2\u01a4\u01a5\7\62\2\2\u01a5\u01a7")
        buf.write("\t\6\2\2\u01a6\u01a8\t\7\2\2\u01a7\u01a6\3\2\2\2\u01a8")
        buf.write("\u01a9\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2")
        buf.write("\u01aa~\3\2\2\2\u01ab\u01ac\7\62\2\2\u01ac\u01ae\t\b\2")
        buf.write("\2\u01ad\u01af\t\t\2\2\u01ae\u01ad\3\2\2\2\u01af\u01b0")
        buf.write("\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1")
        buf.write("\u0080\3\2\2\2\u01b2\u01b3\5\u0085C\2\u01b3\u01b4\5\u0087")
        buf.write("D\2\u01b4\u01b5\5\u0089E\2\u01b5\u01bd\3\2\2\2\u01b6\u01b7")
        buf.write("\5\u0085C\2\u01b7\u01b8\5\u0087D\2\u01b8\u01bd\3\2\2\2")
        buf.write("\u01b9\u01ba\5\u0085C\2\u01ba\u01bb\5\u0089E\2\u01bb\u01bd")
        buf.write("\3\2\2\2\u01bc\u01b2\3\2\2\2\u01bc\u01b6\3\2\2\2\u01bc")
        buf.write("\u01b9\3\2\2\2\u01bd\u0082\3\2\2\2\u01be\u01bf\t\5\2\2")
        buf.write("\u01bf\u0084\3\2\2\2\u01c0\u01c2\5\u0083B\2\u01c1\u01c0")
        buf.write("\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c3")
        buf.write("\u01c4\3\2\2\2\u01c4\u0086\3\2\2\2\u01c5\u01c9\5o8\2\u01c6")
        buf.write("\u01c8\5\u0083B\2\u01c7\u01c6\3\2\2\2\u01c8\u01cb\3\2")
        buf.write("\2\2\u01c9\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u0088")
        buf.write("\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cc\u01cf\t\n\2\2\u01cd")
        buf.write("\u01d0\5\65\33\2\u01ce\u01d0\59\35\2\u01cf\u01cd\3\2\2")
        buf.write("\2\u01cf\u01ce\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d2")
        buf.write("\3\2\2\2\u01d1\u01d3\5\u0083B\2\u01d2\u01d1\3\2\2\2\u01d3")
        buf.write("\u01d4\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2")
        buf.write("\u01d5\u008a\3\2\2\2\u01d6\u01d9\5\61\31\2\u01d7\u01d9")
        buf.write("\5\63\32\2\u01d8\u01d6\3\2\2\2\u01d8\u01d7\3\2\2\2\u01d9")
        buf.write("\u008c\3\2\2\2\u01da\u01db\7^\2\2\u01db\u01dc\t\13\2\2")
        buf.write("\u01dc\u008e\3\2\2\2\u01dd\u01e4\7$\2\2\u01de\u01e3\5")
        buf.write("\u008dG\2\u01df\u01e0\7)\2\2\u01e0\u01e3\7$\2\2\u01e1")
        buf.write("\u01e3\n\f\2\2\u01e2\u01de\3\2\2\2\u01e2\u01df\3\2\2\2")
        buf.write("\u01e2\u01e1\3\2\2\2\u01e3\u01e6\3\2\2\2\u01e4\u01e2\3")
        buf.write("\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e7\3\2\2\2\u01e6\u01e4")
        buf.write("\3\2\2\2\u01e7\u01e8\7$\2\2\u01e8\u01e9\bH\3\2\u01e9\u0090")
        buf.write("\3\2\2\2\u01ea\u01eb\13\2\2\2\u01eb\u01ec\bI\4\2\u01ec")
        buf.write("\u0092\3\2\2\2\u01ed\u01f2\7$\2\2\u01ee\u01f1\5\u008d")
        buf.write("G\2\u01ef\u01f1\n\r\2\2\u01f0\u01ee\3\2\2\2\u01f0\u01ef")
        buf.write("\3\2\2\2\u01f1\u01f4\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f2")
        buf.write("\u01f3\3\2\2\2\u01f3\u01f6\3\2\2\2\u01f4\u01f2\3\2\2\2")
        buf.write("\u01f5\u01f7\t\16\2\2\u01f6\u01f5\3\2\2\2\u01f7\u01f8")
        buf.write("\3\2\2\2\u01f8\u01f9\bJ\5\2\u01f9\u0094\3\2\2\2\u01fa")
        buf.write("\u01ff\7$\2\2\u01fb\u01fe\5\u008dG\2\u01fc\u01fe\n\17")
        buf.write("\2\2\u01fd\u01fb\3\2\2\2\u01fd\u01fc\3\2\2\2\u01fe\u0201")
        buf.write("\3\2\2\2\u01ff\u01fd\3\2\2\2\u01ff\u0200\3\2\2\2\u0200")
        buf.write("\u0202\3\2\2\2\u0201\u01ff\3\2\2\2\u0202\u0203\t\20\2")
        buf.write("\2\u0203\u0204\n\21\2\2\u0204\u0205\3\2\2\2\u0205\u0206")
        buf.write("\bK\6\2\u0206\u0096\3\2\2\2\27\2\u00b8\u0190\u0198\u019e")
        buf.write("\u01a0\u01a9\u01b0\u01bc\u01c3\u01c9\u01cf\u01d4\u01d8")
        buf.write("\u01e2\u01e4\u01f0\u01f2\u01f6\u01fd\u01ff\7\b\2\2\3H")
        buf.write("\2\3I\3\3J\4\3K\5")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INTTYPE = 2
    BOOLEANTYPE = 3
    FLOATTYPE = 4
    BLOCKCOMMENT = 5
    BODY = 6
    BREAK = 7
    CONTINUE = 8
    DO = 9
    ELSE = 10
    ELSEIF = 11
    ENDBODY = 12
    ENDIF = 13
    ENDFOR = 14
    ENDWHILE = 15
    FOR = 16
    FUNCTION = 17
    IF = 18
    PARAMETER = 19
    RETURN = 20
    THEN = 21
    VAR = 22
    WHILE = 23
    TRUE = 24
    FALSE = 25
    INT_ADD = 26
    FLOAT_ADD = 27
    INT_SUB = 28
    FLOAT_SUB = 29
    INT_MUL = 30
    FLOAT_MUL = 31
    INT_DIV = 32
    FLOAT_DIV = 33
    INT_MOD = 34
    NOT = 35
    AND = 36
    OR = 37
    EQUAL_ASSIGN = 38
    INT_EQUAL = 39
    INT_NOT_EQUAL = 40
    INT_LESS_THAN = 41
    FLOAT_LESS_THAN = 42
    INT_MORE_THAN = 43
    FLOAT_MORE_THAN = 44
    INT_LESS_OR_EQUAL = 45
    FLOAT_LESS_OR_EQUAL = 46
    INT_MORE_OR_EQUAL = 47
    FLOAT_MORE_OR_EQUAL = 48
    FLOAT_NOT_EQUAL = 49
    LB = 50
    RB = 51
    LSB = 52
    RSB = 53
    COLON = 54
    DOT = 55
    COMMA = 56
    SEMI = 57
    WS = 58
    ID = 59
    INTLIT = 60
    FLOATLIT = 61
    BOOLEANLIT = 62
    STRINGLIT = 63
    ERROR_CHAR = 64
    UNCLOSE_STRING = 65
    ILLEGAL_ESCAPE = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'integer'", "'boolean'", "'float'", "'Body'", "'Break'", 
            "'Continue'", "'Do'", "'Else'", "'ElseIf'", "'EndBody'", "'EndIf'", 
            "'EndFor'", "'EndWhile'", "'For'", "'Function'", "'If'", "'Parameter'", 
            "'Return'", "'Then'", "'Var'", "'While'", "'True'", "'False'", 
            "'+'", "'+.'", "'-'", "'-.'", "'*'", "'*.'", "'\\'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'='", "'=='", "'!='", "'<'", 
            "'<.'", "'>'", "'>.'", "'<='", "'<=.'", "'>='", "'>=.'", "'=/='", 
            "'('", "')'", "'['", "']'", "':'", "'.'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "BOOLEANTYPE", "FLOATTYPE", "BLOCKCOMMENT", "BODY", 
            "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", 
            "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
            "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", "INT_ADD", 
            "FLOAT_ADD", "INT_SUB", "FLOAT_SUB", "INT_MUL", "FLOAT_MUL", 
            "INT_DIV", "FLOAT_DIV", "INT_MOD", "NOT", "AND", "OR", "EQUAL_ASSIGN", 
            "INT_EQUAL", "INT_NOT_EQUAL", "INT_LESS_THAN", "FLOAT_LESS_THAN", 
            "INT_MORE_THAN", "FLOAT_MORE_THAN", "INT_LESS_OR_EQUAL", "FLOAT_LESS_OR_EQUAL", 
            "INT_MORE_OR_EQUAL", "FLOAT_MORE_OR_EQUAL", "FLOAT_NOT_EQUAL", 
            "LB", "RB", "LSB", "RSB", "COLON", "DOT", "COMMA", "SEMI", "WS", 
            "ID", "INTLIT", "FLOATLIT", "BOOLEANLIT", "STRINGLIT", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "INTTYPE", "BOOLEANTYPE", "FLOATTYPE", "BLOCKCOMMENT", 
                  "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", 
                  "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", 
                  "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", "TRUE", 
                  "FALSE", "INT_ADD", "FLOAT_ADD", "INT_SUB", "FLOAT_SUB", 
                  "INT_MUL", "FLOAT_MUL", "INT_DIV", "FLOAT_DIV", "INT_MOD", 
                  "NOT", "AND", "OR", "EQUAL_ASSIGN", "INT_EQUAL", "INT_NOT_EQUAL", 
                  "INT_LESS_THAN", "FLOAT_LESS_THAN", "INT_MORE_THAN", "FLOAT_MORE_THAN", 
                  "INT_LESS_OR_EQUAL", "FLOAT_LESS_OR_EQUAL", "INT_MORE_OR_EQUAL", 
                  "FLOAT_MORE_OR_EQUAL", "FLOAT_NOT_EQUAL", "LB", "RB", 
                  "LSB", "RSB", "COLON", "DOT", "COMMA", "SEMI", "WS", "ID", 
                  "INTLIT", "DEC", "HEX", "OC", "FLOATLIT", "DIGITS", "INT_PART", 
                  "DEC_PART", "EXPO_PART", "BOOLEANLIT", "ESCAPE_SEQUENCES", 
                  "STRINGLIT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[70] = self.STRINGLIT_action 
            actions[71] = self.ERROR_CHAR_action 
            actions[72] = self.UNCLOSE_STRING_action 
            actions[73] = self.ILLEGAL_ESCAPE_action 
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
                    
     


