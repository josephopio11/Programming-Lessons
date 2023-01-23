version = 100000
from requests import get as webget
from sys import exit as close

x = webget('https://pastebin.com/raw/HKdz8B1x')
# int(x.text[8:14])
if int(x.text[8:14]) > version:
    print("updating...")
    open("maina.py", "w").write(x.text)
    print("runing")
    exec(x.text)
    close(0)
if True:  # import guizero things
    print("IMPORT GUIZERO")
    from guizero import Text
    from guizero import TextBox
    from guizero import App
    from guizero import Window
    from guizero import MenuBar
    from guizero import ListBox
    from guizero import Box
    from guizero import PushButton
    from guizero import Slider
    from guizero import Combo
    from guizero import CheckBox
    from guizero import Picture
    from guizero import Drawing
    from guizero import RadioButton
    from guizero import ButtonGroup
    from guizero import dialog
    from guizero import event
    from guizero import base
    from guizero import Waffle
    from guizero import utilities
    from guizero import tkmixins

    # import specific functions
    print("IMPORT FUNCTIONS")
    from json import dump
    from json import dumps
    from json import load
    from json import loads
    from os import remove
    from os import mkdir
    from os import walk
    from os.path import exists
    from os.path import getsize
    from zipfile import ZipFile
    from configparser import ConfigParser
    from threading import Thread

    # sets globals
    print("SET GLOBALS")
    global now
    global path
    global ison
    global templist
    global dat
    global neww
    global now
    global basel
    global addk
    global dlobalind
    global b1
    global b2
    # vars set
    print("SET VARABLES")
    now = False
    path = ""
    dat = {}
    templist = []
    basel = "en"
    globalind = []
    # init Gui
    print("INT GUI")
    # wset = Configparser()#config thing
    app = App(title="pewmine-moding")  # window setup

    # start up loads
    print("FIRST START PAYLOADS")
    for a in ['resorces', 'cache', 'build']:
        try:
            mkdir(a)
        except:
            pass
    if not exists("cache/cache"):
        b = {
            "opens": []
        }
        # open("cache/cache","w").write(dumps(b))
        del b
    del a


def mforge(dat: dict,
           key: list,
           rule: str,
           pre: str):
    fin = pre
    for i in dat.keys():
        ke = dat[i]
        kp = [i]
        for c in key:
            kp.append(ke[c])
        fin += rule.format(*kp).replace("\\(", "{").replace("\\)", "}")
    return fin


"""Highly optimised for ini and json conversion"""


def Sjsontoini(inn, name="foob"):
    if exists("cache/cv_{}.ini".format(name)):
        return open("cache/cv_{}.ini".format(name), "r").read()
    level = []
    dn = 0
    out = ConfigParser()

    def layer(level, area, dn):
        out.add_section(''.join(level))
        print('layer:' + ''.join(level))
        for b in area:
            dn += 1
            if type(area[b]) == dict:
                level.append('/' + str(b))
                dn = layer(level, area[b], dn)
            else:
                out.set(str(''.join(level)), b, str(area[b]))
        level.pop(-1)
        return dn

    print('CONV-{}:DEFAULT'.format(name))
    for b in inn:
        dn += 1
        if type(inn[b]) == dict:
            level.append(str(b))
            dn = layer(level, inn[b], dn)
        else:
            out.set('DEFAULT', str(b), str(inn[b]))
    with open("cache/cv_{}.ini".format(name), "w") as fp:
        out.write(fp)
    return open("cache/cv_{}.ini".format(name), "r").read()  # .dump()


def jsontoini(fn, out):
    level = []
    out = ConfigParser()
    inp = loads(open(fn, "r"))
    dn = 0

    def layer(level, area, dn):
        out.add_section(''.join(level))
        print('layer:' + ''.join(level))
        for b in area:
            dn += 1
            if type(area[b]) == dict:
                level.append('/' + str(b))
                dn = layer(level, area[b], dn)
            else:
                out.set(str(''.join(level)), b, str(area[b]))
        level.pop(-1)
        return dn

    print('layer:DEFAULT')
    for b in inp:
        dn += 1
        if type(inp[b]) == dict:
            level.append(str(b))
            dn = layer(level, inp[b], dn)
        else:
            out.set('DEFAULT', str(b), str(inp[b]))
    print(f'''{dn} stuff did
writeing...''')
    out.write(open(out, 'w'))


def Sinitojson(inip):
    global out
    out = {};
    md = ''

    def addto(md, val, run="out"):
        for i in md.split('/'): run += f"['{i}']"
        if type(val) == str:
            run += f" = '{val}'"
        elif type(val) == dict:
            run += " = {}"
        else:
            run += f" = {val}"
        exec(run, globals(), locals())

    for i in inip.split('\n'):
        if i == '' or i.startswith("#"):
            continue
        elif i.startswith('[') and i.endswith(']'):
            md = i[1:-1]
            if md == 'DEFAULT':
                pass
            else:
                addto(md, {})
            print(f'key switch:{md}')
            continue
        else:
            c = i.split('=', 1)
            c[0] = c[0].strip()
            c[1] = c[1].strip()
            try:
                c[1] = int(c[1])
            except:
                pass
            print(md + '/' + c[0], c[1])
            if md == 'DEFAULT':
                addto(c[0], c[1])
            else:
                addto(md + '/' + c[0], c[1])
            continue
    print('done')
    return out


def initojson(fn):
    inp = ConfigParser()
    inp.read(open(fn, "r"))
    inip = open(fn, "r").read()
    out = {};
    md = ''

    def addto(md, val, run="out"):
        for i in md.split('/'): run += f"['{i}']"
        if type(val) == str:
            run += f" = '{val}'"
        elif type(val) == dict:
            run += " = {}"
        else:
            run += f" = {val}"
        exec(run, globals(), locals())

    def rsl(text):  # remove space left
        while True:
            if text[0] == " ":
                text = text[1:]
            else:
                return text

    def rsr(text):  # remove space right
        while True:
            if text[-1] == " ":
                text = text[:-1]
            else:
                return text

    for i in inip.split('\n'):
        if i == '' or i.startswith("#"):
            continue
        elif i.startswith('[') and i.endswith(']'):
            md = i[1:-1]
            if md == 'DEFAULT':
                pass
            else:
                addto(md, {})
            print(f'key switch:{md}')
            continue
        else:
            c = i.split('=', 1)
            c[0] = c[0].strip()
            c[1] = c[1].strip()
            try:
                c[1] = int(c[1])
            except:
                pass
            addto(md + '/' + c[0], c[1])
            continue
    print('writeing...')
    dump(out, open(fn[:-3] + 'json', 'w'), indent=2)


print("FUNCTIONS")


def newmake():  # make a project
    name = templist[0].value
    prefix = templist[2].value
    if True:  # try:
        mkdir("workspace/{}".format(name))
        dat = {
            "meta": {
                "name": name,
                "prefix": prefix,
                "disc": templist[2].value,
                "showname": templist[1].value,
                "ver": 0.1,
                "severpow": False,  # uses sever powers
            },
            "metav": {},
            "items": {},
            "objects": {},
            "pews": {},
            "lang": {
                "menu": {},
                "dyns": {}
            },
            "foop": {}
        }
        dump(dat, open("{0}.prjmap".format(name), "w"))
        app.info("info", "new project made")
    # except:
    #  app.error("error", "unable to make new project")
    neww.hide()


def new():  # ui for new
    global neww
    neww = Window(app, title="new")
    Text(neww, text="project name")
    templist.append(TextBox(neww, width="fill"))
    Text(neww, text="display name")
    templist.append(TextBox(neww, width="fill"))
    Text(neww, text="prefix (can not change later)")
    templist.append(TextBox(neww, width="fill"))
    Text(neww, text="discription")
    templist.append(TextBox(neww, width="fill", height=3, multiline=True, scrollbar=True))
    PushButton(neww, command=newmake, text="make")
    neww.show()


def null():  # pass
    print("not imp")
    update_index()


def linkr_start():
    link = Window(app, title="link")


def build():
    # try:DEL("{}.zip".format(dat["meta"]["name"]))
    # except:print("no prebuild found")
    def writefile(archive, fn, dat):
        with archive.open(fn, mode="w") as file:
            file.write(bytes(dat, 'utf-8'))
            print(f"BWRITE:{fn}")

    def writefileB(archive, fn, dat):
        with archive.open(fn, mode="w") as file:
            file.write(dat)
            print(f"BWRITE:{fn}")

    name = dat["meta"]["name"]
    fn = f"{name}.zip"
    if exists(fn):
        num = 1
        while exists(fn) == True:
            fn = f"{name} ({num}).zip"
        del num
    with ZipFile(fn, mode="w") as archive:
        for f in dat["foop"].keys():  # foop
            writefile(archive, f"foop/{f}.foop", dat['foop'][f])
        for f in dat["files"].keys():  # foop
            writefile(archive, f, dat['files'][f])
        writefile(archive, "META.ini", Sjsontoini(dat['meta'], name="metaBUILD"))
        writefile(archive, "LANG.ini", Sjsontoini(dat['lang'], name="langBUILD"))
        writefile(archive, "ITEM.json", dumps(dat['items']))
        writefile(archive, "OBJECT.json", dumps(dat['objects']))
        writefile(archive, "PEW.json", dumps(dat['pews']))

    app.info("Build", "build done")
    # DEL("cache/cv-buld_lang")


def raw_build():
    open("build/get_item.gml", "w").write(mforge(
        dat=dat['items'],
        key=["sprite", "value"],
        rule="""//{0}.item
if argument0=="{0}"\\(
ds_map_add(item, "sprite", {1});
ds_map_add(item, "value", {2});
return item
\\)""",
        pre="""//setup vars
item=ds_map_create();
"""))
    open("build/get_object.gml", "w").write(mforge(
        dat=dat['objects'],
        key=["hitval", "sprite", "drop", "drop_min", "drop_max"],
        rule="""//{0}.object
if argument0=="{0}"\\(
ds_map_add(obj, "hitval", {1});
ds_map_add(obj, "sprite", {2});
ds_map_add(obj, "drop", "{3}");
ds_map_add(obj, "drop_min", {4});
ds_map_add(obj, "drop_max", {5});
return obj
\\)""",
        pre="""//setup vars
obj=ds_map_create()
"""))
    open("build/get_pew.gml", "w").write(mforge(
        dat=dat['pews'],
        key=["reload", "speed", "pershot", "rounds", "bullet"],
        rule="""//{0}.pew
if argument0=="{0}"\\(
ds_map_add(pew, "reload", {1});
ds_map_add(pew, "speed", {2});
ds_map_add(pew, "ps", {3});
ds_map_add(pew, "mxr", {4});
ds_map_add(pew, "bullet", "{5}");
return pew
\\)""",
        pre="""//setup vars
pew=ds_map_create()
"""))


def dumpdat():
    open("dat-dump.json", "w").write(dumps(dat, indent=2))
    print("DAT Dump")
    pass


""""foop"""


def makefoop():
    global addf
    global f1
    addf = Window(app,
                  title="add script",
                  height=140,
                  width=200)
    Text(addf, "add script")
    f1 = TextBox(addf)
    PushButton(addf,
               text="add script",
               command=makefoop_done)


def makefoop_done():
    dat['foop'][f1.value] = ""
    update_index()
    addf.hide()


def frename():
    global renf
    global fr1
    renf = Window(app,
                  title="rename script",
                  height=140,
                  width=200)
    Text(renf, "rename script '{}'".format(indexx.value))
    fr1 = TextBox(renf)
    PushButton(renf,
               text="rename script",
               command=frename_done)


def frename_done():
    dat['foop'][fr1.value] = dat['foop'][indexx.value]
    del dat['foop'][indexx.value]
    update_index()
    indexx.value = fr1.value
    renf.hide()


def ftitlechange():
    dat['foop'][foopeditertitle.value] = dat['foop'][indexx.value]
    del dat['foop'][indexx.value]
    quick_update()
    indexx.value = foopeditertitle.value


"""imports"""


def impitems():  # import items from a json
    fn = app.select_file(
        filetypes=[
            ["items.json", "items.json"],
            ["json", "*.json"],
            ["All files", "*.*"]
        ])
    if len(fn) <= 2:
        print("Cancel")
        return ""
    itm = loads(open(fn, "r").read())
    for i in list(itm.keys()):
        dat['items'][i] = itm[i]
    update_index()


def impobjs():
    fn = app.select_file(
        filetypes=[
            ["objects.json", "objects.json"],
            ["json", "*.json"],
            ["All files", "*.*"]
        ])
    if len(fn) <= 2:
        print("Cancel")
        return ""
    itm = loads(open(fn, "r").read())
    for i in list(itm.keys()):
        dat['objects'][i] = itm[i]
    update_index()


def imppews():
    fn = app.select_file(
        filetypes=[
            ["pews.json", "pews.json"],
            ["json", "*.json"],
            ["All files", "*.*"]
        ])
    if len(fn) <= 2:
        print("Cancel")
        return ""
    itm = loads(open(fn, "r").read())
    for i in list(itm.keys()):
        dat['pews'][i] = itm[i]
    update_index()


def implang():
    fn = app.select_file(
        filetypes=[
            ["lang", "lang**.json"],
            ["lang.json", "lang.json"],
            ["json", "*.json"],
            ["All files", "*.*"]
        ])
    if len(fn) <= 2:
        print("Cancel")
        return ""
    dat['lang'] = load(open(fn, "r"))
    update_index()


def fixP():
    err = False
    cata = ["items", "objects", "pews", "foop", "lang", "files"]
    for i in cata:
        try:
            dat[i]
        except:
            print("MISSING ({})".format(i))
            err = True
            dat[i] = {}
            print("FIXED ({})".format(i))
    if err == True:
        app.warn("Pewmine-moding", "fixed errors with Project\n look at console for more info")


def exlang():
    fn = app.select_file(
        filetypes=[
            ["as ini", "lang.ini"],
            ["as json", "lang.json"],
            ["All files", "*.*"]
        ],
        save=True,
        filename="lang.ini")
    if fn.endswith('.ini'):
        print("export lang.ini")
    if fn.endswith('.json'):
        print("export lang.json")


def DEL(path):
    print("DEL {}".format(path))
    remove(path)


def loadP():
    global dat, path
    # loger.append("load")
    fn = app.select_file(
        filetypes=[["pewmine", "*.prjmap*"], ["All files", "*.*"]])
    if len(fn) <= 2:
        return None
    if len(fn) >= 3:
        dat = loads(open(fn, "r").read())
        print("LOAD({})".format(fn))
        cac = load(open('cache/cache', 'r'))
        if fn in cac['opens']:
            cac['opens'].append(fn)
            dump(cac, open('cache/cache', 'w'))
        path = fn
        fixP()
        update_index()
        startt.hide()
        rm_cache(userreq=False)


"""CACHE"""


def gen_cache():
    dump(dat["lang"], open("cache/lang.json", "w"))
    jsontoini("cache/lang.json", "cache/lang.ini")


def rm_cache(userreq=True):
    if userreq == True:
        if app.yesno("Clear Cache",
                     "if some changes are not showing, clearing the Cache will help") == False:
            return ""
    siz = 0
    print("CLEAR CACHE")
    for root, dirs, files in walk("cache/",
                                  topdown=False):
        # print(root)
        # print(dirs)
        for i in files:
            print("DEL cache/{}".format(i))
            siz += getsize("cache/{}".format(i))
            remove("cache/{}".format(i))
    if userreq == True:
        app.info("Cache Clear",
                 "Cleared ({}) bytes".format(siz))
    update_index()
    del siz
    del root
    del dirs
    del files


"""OMNI SEARCH"""


def omni_searched():
    found = list()
    eror = 0
    noname = 0
    c = omni_in.value
    print(c)
    for i in dat:  # type
        for j in dat[i]:  # thing
            try:
                if c in dat[i][j]['name']:
                    try:
                        a = dat['lang']['dyns'][j]
                    except:
                        noname += 1
                        raise error()
                    found.append(str(j) + ':' + str(a))
            except:
                eror += 1
    if True:
        rtr = ""
        print("ID(s) found:")
        for i in found:
            rtr += f'{i}\n'
        omni_out.value = rtr


def omni_search():
    global search
    global omni_in
    global omni_out
    search = Window(app,
                    title="omni search",
                    height=200,
                    width=200)
    a1 = Box(search)
    a2 = Box(search)
    Text(a1, "omni search")
    PushButton(a1,
               text="search",
               align="right",
               command=omni_searched)
    omni_in = TextBox(a1, width="fill")
    omni_out = TextBox(a2, width="fill", height="fill",
                       multiline=True,
                       scrollbar=True)

    print(indexx.value)


"""dupe check"""


def dupcheck(dict, key):
    if key in dict:
        return True
    else:
        return False


# def dupecheckUI():

"""SAVES"""


def save():  # force save
    if True == True:
        print("SAVE")
        open(path, "w").write(dumps(dat, indent=2))


def fsave():
    dat[indexx.value] = Sinitojson(dexout.value)
    try:
        DEL(f"cache/cv_{indexx.value}.ini")
    except:
        pass


def lsave():
    dat["lang"][indexx.value] = Sinitojson(dexout.value)
    try:
        DEL(f"cache/cv_{indexx.value}.ini")
    except:
        pass


def gsave():
    spl = indexx.value.split("|")[0]
    dat[selt.value][spl] = Sinitojson(dexout.value)
    try:
        DEL(f"cache/cv_{spl}.ini")
    except:
        pass


def ssave():
    dat["foop"][indexx.value] = foopediterput.value


def autosaver():
    sel = selt.value
    if sel == "foop": ssave()


"""REMOVER"""


def remover():
    global removrw
    global removrbox
    global dexer
    dexer = indexx.value
    removrw = Window(app, title="remove {}".format(indexx.value)
                     , height=140, width=200)
    PushButton(removrw,
               text="remove",
               command=remover_done)
    removrwb = Box(removrw)
    removrbox = ListBox(removrwb,
                        align="left",
                        # height="",
                        items=list(
                            dat[selt.value].keys()),
                        command=update_index)
    print(indexx.value)


def remover_done():
    dat[selt.value].pop(removrbox.value)
    removrw.hide()
    try:
        DEL("cache/cv_{}.ini".format(indexx.value))
    except:
        pass
    update_index()


"""LANG KEYS"""


def remove_key():
    global addr
    global rmkey
    global dexer
    dexer = indexx.value
    addr = Window(app, title="remove key", height=140, width=200)
    PushButton(addr,
               text="remove key",
               command=remove_key_done)
    a1 = Box(addr)
    rmkey = ListBox(a1,
                    align="left",
                    # height="",
                    items=list(
                        dat['lang'][indexx.value].keys()),
                    command=update_index)

    print(indexx.value)


def remove_key_done():
    print(rmkey.value)
    print(dexer)
    dat['lang'][dexer].pop(rmkey.value)
    try:
        DEL("cache/cv_{}.ini".format(dexer))
    except:
        pass
    dex_show(dexer)
    addr.hide()
    print("done - key remove")


def add_key():
    global addk
    global b1
    global b2
    addk = Window(app,
                  title="add key",
                  height=140,
                  width=200)
    a1 = Box(addk)
    a2 = Box(addk)
    Text(a1, "Key")
    b1 = TextBox(a1)
    Text(a2, "Val")
    b2 = TextBox(a2)
    PushButton(addk,
               text="add key",
               command=add_key_done)
    print(indexx.value)


def add_key_done():
    global dat
    print("add_key")
    a = b1.value
    b = b2.value
    print("dat['lang'][{0}][{1}]={2}".format(
        indexx.value, a, b))
    dat['lang'][indexx.value][a] = b
    print(dat['lang'][indexx.value][a])
    try:
        DEL("cache/cv_{}.ini".format(indexx.value))
    except:
        pass
    dex_show(indexx.value)
    addk.hide()
    print("done - key add")


"""INDEX"""


def dex_show(value):
    putt = value.split("|")[0]
    sel = selt.value
    if putt == "lol none":
        dexout.value = """the big F
looks like there is nothing here, but what if there was?
go create a thing of that type and it may help.
if you are haveing a hard time look under help."""
        return None
    if sel == "extra":
        if putt == "meta":
            dexout.value = Sjsontoini(
                dat['meta'],
                putt)
            filebox.show()
    elif sel == "lang":
        dexout.value = Sjsontoini(
            dat['lang'][putt],
            putt)

    elif sel == "foop":
        foopediterput.value = dat["foop"][putt]
        # foopeditertitle.value=putt
    elif sel in ["items", "objects", "pews"]:
        dexout.value = Sjsontoini(
            dat[selt.value][putt],
            putt)
    else:
        dexout.value = Sjsontoini(
            dat[selt.value][putt],
            putt)
        filebox.show()


def check(ch="all"):
    warn = []
    error = []
    note = []
    v = ''
    ldyn = dat["lang"]['dyns']
    # Foop check
    if ch == "foop" or ch == "all":
        if "none" not in dat["foop"]:
            error.append(f'foop had no none script')
            dat["foop"]["none"] = """#this is a no op script"""
    # ITEMS
    if ch == "item" or ch == "all":
        for i in dat["items"]:
            if dat["items"][i]['sprite'] not in []:
                error.append(f'{i} has sprite ID but not linked')
            if i not in ldyn:
                warn.append(f'{i} is not in lang| FIXED')
                dat["lang"]['dyns'][i] = i
            if "foop" not in dat["items"][i]:
                warn.append(f'{i} has no foop| FIXED')
                dat["items"][i]['foop'] = "none"
            if "value" not in dat["items"][i]:
                warn.append(f'{i} has no value| FIXED')
                dat["items"][i]['value'] = "0"
    # OBJECTS
    if ch == "object" or ch == "all":
        for i in dat["objects"]:
            if dat["objects"][i]['sprite'] not in []:
                error.append(f'{i} has sprite ID but not linked')
            if i not in ldyn:
                warn.append(f'{i} is not in lang')
            if "foop" not in dat["objects"][i]:
                warn.append(f'{i} has no foop')
                dat["objects"][i]['foop'] = "none"

    che = Window(app,
                 title="check",
                 height=200, width=340)
    Text(che, "WARN/ERROR/NOTE")
    PushButton(che, text='close', command=che.hide)
    chk = TextBox(che, width="fill", height="fill",
                  multiline=True,
                  scrollbar=True)
    v += "[ERROR]\n"
    for i in error:
        v += f'{i}\n'
    v += "[WARN]\n"
    for i in warn:
        v += f'{i}\n'
    v += "[NOTE]\n"
    for i in note:
        v += f'{i}\n'
    error = []
    if len(error + warn + note) == 0:
        chk.value = "nothing wrong found.\ncool"
    else:
        chk.value = v


def update_index(quick=False):
    indexx.clear()
    if "CHECK" in selt.options:
        selt.value = "items"
        selt.remove("CHECK")
    try:
        a = list(dat[selt.value].keys())
    except:
        a = []

    langbox.hide()
    deflbox.hide()
    foopbox.hide()
    filebox.hide()
    dexout.visible = False
    foopedit.visible = False
    if selt.value in ["lang"]:
        dexout.visible = True
        langbox.show()
    if selt.value in ["items", "objects", "pews"]:
        dexout.visible = True
        deflbox.show()
    if selt.value in ["foop"]:
        if quick != True:
            foopedit.visible = True
            foopbox.show()
    if selt.value in ["extra"]:
        dexout.visible = True
        filebox.show()
        indexx.append("meta")
    if len(a) != 0:
        for i in a:
            try:
                a = dat['lang']['dyns'][i]
                indexx.append(f'{i}|{a}')
            except:
                indexx.append(i)
    else:
        indexx.append("lol none")


def quick_update():
    indexx.clear()
    for i in list(dat[selt.value].keys()):
        indexx.append(i)


######DEX GLOBALS
global index
global dexout
global indexx
global selt
global langbox
global filebox
print("DEX INIT")
menubar = MenuBar(app,
                  toplevel=["File", "Import", "Utils", "Help", "Cache", "Export"],
                  options=[
                      [
                          ["New", new],
                          ["Save", save],
                          ["Load", loadP],
                          ["Build", build],
                          ["Raw Build", raw_build]
                      ],
                      [
                          ["items.json", impitems],
                          ["pews.json", imppews],
                          ["objects.json", impobjs],
                          ["lang.json", implang]
                      ],
                      [
                          ["Omni-Search", omni_search],
                          ["Check", check],
                          ["Dat-Dump", dumpdat]
                      ],
                      [
                          ["Help", null],
                          ["Docs", null],
                          ["Foop docs", null]
                      ],
                      [
                          ["Create Cache", gen_cache],
                          ["Clear Cache", rm_cache]
                      ],
                      [
                          ["lang", exlang]
                      ]

                  ])
indexx = ListBox(app,
                 height="fill",
                 width=120,
                 items=["lol none"],
                 scrollbar=True,
                 align="left",
                 command=dex_show
                 )
boxx = Box(app,
           width="fill",
           align="top",
           border=True
           )
selt = Combo(boxx,
             align="left",
             height="fill",
             options=["items", "objects", "pews", "lang", "foop", "extra"],
             command=update_index)
# output
dexout = TextBox(app,
                 width="fill",
                 height="fill",
                 multiline=True,
                 scrollbar=True,
                 command=autosaver
                 )
dexout.visible = False
foopedit = Box(app,
               width="fill",
               height="fill",
               border=False
               )
"""foopeditertitle = TextBox(foopedit,
       width="fill",
       command=ftitlechange
                           )"""
foopediterput = TextBox(foopedit,
                        width="fill",
                        height="fill",
                        multiline=True,
                        scrollbar=True,
                        command=autosaver
                        )

# lang box
langbox = Box(boxx,
              width="fill",
              align="right",
              border=True
              )
PushButton(langbox,
           align="left",
           height="fill",
           text="Save",
           command=lsave
           )
PushButton(langbox,
           align="left",
           height="fill",
           text="Add Key",
           command=add_key
           )
PushButton(langbox,
           align="left",
           height="fill",
           text="Remove Key",
           command=remove_key
           )
# Basic item box
deflbox = Box(boxx,
              width="fill",
              align="right",
              border=True
              )
PushButton(deflbox,
           align="left",
           height="fill",
           text="save",
           command=gsave
           )
PushButton(deflbox,
           align="left",
           height="fill",
           text="create",
           command=null
           )
PushButton(deflbox,
           align="left",
           height="fill",
           text="deleate",
           command=null
           )
# Foop box
foopbox = Box(boxx,
              width="fill",
              align="right",
              border=True
              )
PushButton(foopbox,
           align="left",
           height="fill",
           text="save",
           command=ssave
           )
PushButton(foopbox,
           align="left",
           height="fill",
           text="create",
           command=makefoop
           )
PushButton(foopbox,
           align="left",
           height="fill",
           text="remove",
           command=remover
           )
PushButton(foopbox,
           align="left",
           height="fill",
           text="Rename",
           command=frename
           )
# file box
filebox = Box(boxx,
              width="fill",
              align="right",
              border=True
              )
PushButton(filebox,
           align="left",
           height="fill",
           text="save",
           command=fsave
           )


def onstart():
    global startt
    update_index()
    startt = Window(app,
                    title="start",
                    height=160, width=220)

    Text(startt, "load or create a project")
    # recent=ListBox(startt,recent)
    buttons = Box(startt, align="left")
    PushButton(buttons, text="load", command=loadP)
    PushButton(buttons, text="create")

    if exists("cache/cache"):
        a = load(open("cache/cache", "r"))['opens']
        recent = []
        for i in a:
            recent.append(i.split('/')[-1])
        del a
        # del i

    else:
        a = ['lol none']


onstart()


def cml():
    while True:
        a = input(">>")
        if a == "check": check()


Xcml = Thread(
    target=cml, args=(), daemon=True)
Xcml.start()
app.display()