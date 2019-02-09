



def req_imports(cur_version):
    version = (3, 0)
    if cur_version >= version:

        print("Imported ! 3.0")
    else:

        print("Imported ! 2.7")


def return_htmlparser_class(cur_version):
    version = (3, 0)
    if cur_version >= version:
        from html.parser import HTMLParser
        from html.entities import name2codepoint
        class MyHTMLParser(HTMLParser):
            def handle_starttag(self, tag, attrs):
                print("Start tag:", tag)
                for attr in attrs:
                    print("     attr:", attr)

            def handle_endtag(self, tag):
                print("End tag  :", tag)

            def handle_data(self, data):
                print("Data     :", data)

            def handle_comment(self, data):
                print("Comment  :", data)

            def handle_entityref(self, name):
                c = chr(name2codepoint[name])
                print("Named ent:", c)

            def handle_charref(self, name):
                if name.startswith('x'):
                    c = chr(int(name[1:], 16))
                else:
                    c = chr(int(name))
                print("Num ent  :", c)

            def handle_decl(self, data):
                print("Decl     :", data)
        return MyHTMLParser()
    else:
        from HTMLParser import HTMLParser
        from htmlentitydefs import name2codepoint
        class MyHTMLParser(HTMLParser):
            def handle_starttag(self, tag, attrs):
                print "Start tag:", tag
                for attr in attrs:
                    print "     attr:", attr

            def handle_endtag(self, tag):
                print "End tag  :", tag

            def handle_data(self, data):
                print "Data     :", data

            def handle_comment(self, data):
                print "Comment  :", data

            def handle_entityref(self, name):
                c = unichr(name2codepoint[name])
                print "Named ent:", c

            def handle_charref(self, name):
                if name.startswith('x'):
                    c = unichr(int(name[1:], 16))
                else:
                    c = unichr(int(name))
                print "Num ent  :", c

            def handle_decl(self, data):
                print "Decl     :", data

        return MyHTMLParser()
