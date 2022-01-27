var modules;

// var window = new Proxy(global, {
//     get: function (target, key, receiver) {
//         console.log("window.get", key, target[key]);
//         if (key == "location") {
//             location = new Proxy(target[key], {
//                 get: function (_target, _key, _receiver) {
//                     console.log("window.get", key, _key, _target[_key]);
//                     if (_key == "port") {
//                         console.log("_key ", _key)
//                     }
//                     return _target[_key];
//                 }
//             })
//         }
//         return target[key];
//     },
//     set: function (target, key, value, receiver) {
//         console.log("window.set", key, value);
//         target[key] = value;
//     }
// });
var window = global;
window.name = ''
window.webpackJsonp = []
window.navigator = {
    appCodeName: "Mozilla",
    appMinorVersion: "0",
    appName: "Netscape",
    appVersion: "5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    browserLanguage: "zh-CN",
    cookieEnabled: true,
    cpuClass: "x86",
    language: "zh-CN",
    maxTouchPoints: 0,
    msManipulationViewsEnabled: true,
    msMaxTouchPoints: 0,
    msPointerEnabled: true,
    onLine: true,
    platform: "Win32",
    pointerEnabled: true,
    product: "Gecko",
    systemLanguage: "zh-CN",
    userAgent: "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    userLanguage: "zh-CN",
    vendor: "",
    vendorSub: "",
    webdriver: false
}


var atob = function (val) {
    return Buffer.from(val, 'base64').toString('binary')
}
var btoa = function (val) {
    return Buffer.from(val).toString('base64')
}


!function (e) {
    function t(t) {
        for (var n, r, o = t[0], a = t[1], c = 0, u = []; c < o.length; c++)
            r = o[c],
            Object.prototype.hasOwnProperty.call(i, r) && i[r] && u.push(i[r][0]),
                i[r] = 0;
        for (n in a)
            Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
        for (s && s(t); u.length;)
            u.shift()()
    }

    var n = {}
        , r = {
        35: 0
    }
        , i = {
        35: 0
    };

    function o(t) {
        // console.log('index:', t)
        if (n[t])
            return n[t].exports;
        var r = n[t] = {
            i: t,
            l: !1,
            exports: {}
        };
        return e[t].call(r.exports, r, r.exports, o),
            r.l = !0,
            r.exports
    }

    modules = o;
    o.e = function (e) {
        var t = [];
        r[e] ? t.push(r[e]) : 0 !== r[e] && {
            8: 1,
            21: 1,
            22: 1,
            23: 1,
            24: 1,
            25: 1,
            26: 1,
            27: 1,
            29: 1,
            31: 1,
            37: 1,
            39: 1,
            40: 1,
            41: 1,
            42: 1,
            44: 1,
            45: 1,
            46: 1,
            47: 1,
            49: 1,
            53: 1,
            54: 1,
            55: 1,
            57: 1,
            70: 1,
            71: 1,
            72: 1,
            74: 1,
            75: 1,
            76: 1,
            77: 1,
            78: 1,
            81: 1,
            82: 1,
            83: 1,
            84: 1,
            85: 1,
            86: 1,
            87: 1,
            88: 1,
            89: 1,
            91: 1,
            92: 1,
            93: 1,
            94: 1,
            95: 1
        }[e] && t.push(r[e] = new Promise((function (t, n) {
                for (var i = "main." + ({
                    0: "shared_5cac3ab8a563f9bbb56eca3256b8ed78b8d955b6",
                    1: "lib_0ad37f8a",
                    2: "shared_ddb69a58413b8324ef696dc6cfa9d1ea4c7519cc",
                    3: "lib_79b5cf47",
                    4: "shared_1257c3c9568bb2a3f62d5ecd308c048e4bf1bfcd",
                    5: "shared_92f99629e986751c8921c57c658e5e3ebe23d234",
                    6: "shared_66e7ebb3246404a2feb1adb7bed7e4117e5b4363",
                    7: "shared_f30f7459f944e851b885959dfde412e92f3a8d2e",
                    8: "shared_f30f7459f944e851b885959dfde412e92f3a8d2e_CSS",
                    9: "shared_3254bd1931ca333a5c274ba01dd8e55e0d0915f7",
                    10: "shared_1679dafdec5942113b512c7479f90fe8c8cc0c34",
                    11: "shared_6389524d82c312e7d98e40d6619dd28305142472",
                    12: "shared_d1ef5af0010fdbecda3e7215eeb794b639ace47a",
                    13: "griffith-player",
                    14: "lib_16a524cd",
                    15: "lib_330004dc",
                    16: "shared_02f2a87bf33ecb38af7b19dfbca195a9fc2fb430",
                    17: "shared_29883da17f6edf7dc61a1cad7e21ec8752a5040e",
                    18: "shared_4be4eabe8cccf0f9dd1e84435900f6b53ad5b687",
                    19: "shared_b59f4818030bb32444355928d14a422ae90a2e9b",
                    20: "shared_daaa4a126208fc5f5a863f08a363ab54d49aaa6e",
                    21: "shared_daaa4a126208fc5f5a863f08a363ab54d49aaa6e_CSS",
                    22: "Carousel",
                    23: "Chart",
                    24: "ECommerceAd",
                    25: "EcommerceAdCard",
                    26: "FeeConsultCard",
                    27: "GoodsRecommendGoodsCardList",
                    28: "HistoricalScore",
                    29: "InlineVideo",
                    30: "KnowledgeForm",
                    31: "Labels",
                    32: "ScoreLineChart",
                    33: "VideoAnswerLabel",
                    34: "VideoController",
                    36: "biz-co-creation",
                    37: "campaign-routes",
                    38: "collection-Scroller",
                    39: "collection-routes",
                    40: "collections-routes",
                    41: "comment-manage-footer",
                    42: "comments-modals",
                    43: "contribution-modal",
                    44: "creation-manage-action-list",
                    45: "creator-routes",
                    46: "creator-salt-routes",
                    47: "email-register-routes",
                    48: "empty-view-svg",
                    49: "explore-routes",
                    50: "flv.js",
                    51: "gaokao-pray-cheer-animation-data",
                    52: "gaokao-pray-kanshan-animation-data",
                    53: "globalOrgReport",
                    54: "help-center-routes",
                    55: "host-routes",
                    56: "image-editor",
                    57: "knowledge-plan-routes",
                    58: "lib_0bf4e2b2",
                    59: "lib_29107295",
                    60: "lib_5c8e84aa",
                    61: "lib_620696dc",
                    62: "lib_75fc9c18",
                    63: "lib_9974496f",
                    64: "lib_a0a3d150",
                    65: "lib_a4c92b5b",
                    66: "lib_c3f561e3",
                    67: "lib_f3cf1418",
                    68: "liveplus-routes",
                    69: "lottie-web",
                    70: "mcn-routes",
                    71: "messages-routes",
                    72: "modals",
                    73: "mqtt",
                    74: "navbar-messages",
                    75: "navbar-notifications",
                    76: "notifications-routes",
                    77: "people-routes",
                    78: "question-routes",
                    79: "react-draggable-tags",
                    80: "react-id-swiper",
                    81: "report_modals",
                    82: "richinput",
                    83: "richinputV2",
                    84: "roundtable-routes",
                    85: "search-routes",
                    86: "settings-routes",
                    87: "sign-page",
                    88: "signflow",
                    89: "special-routes",
                    90: "theater-player",
                    91: "topic-routes",
                    92: "topstory-routes",
                    93: "user-hover-card",
                    94: "vessay-routes",
                    95: "wiki-routes",
                    96: "zswsdid"
                }[e] || e) + ".216a26f4." + {
                    0: "31d6cfe0d16ae931b73c",
                    1: "31d6cfe0d16ae931b73c",
                    2: "31d6cfe0d16ae931b73c",
                    3: "31d6cfe0d16ae931b73c",
                    4: "31d6cfe0d16ae931b73c",
                    5: "31d6cfe0d16ae931b73c",
                    6: "31d6cfe0d16ae931b73c",
                    7: "31d6cfe0d16ae931b73c",
                    8: "fbfcafd2e60655535340",
                    9: "31d6cfe0d16ae931b73c",
                    10: "31d6cfe0d16ae931b73c",
                    11: "31d6cfe0d16ae931b73c",
                    12: "31d6cfe0d16ae931b73c",
                    13: "31d6cfe0d16ae931b73c",
                    14: "31d6cfe0d16ae931b73c",
                    15: "31d6cfe0d16ae931b73c",
                    16: "31d6cfe0d16ae931b73c",
                    17: "31d6cfe0d16ae931b73c",
                    18: "31d6cfe0d16ae931b73c",
                    19: "31d6cfe0d16ae931b73c",
                    20: "31d6cfe0d16ae931b73c",
                    21: "89971b0e4e3977395f29",
                    22: "6c92d300e158ac1b00bc",
                    23: "1225590f22ec86bcb10b",
                    24: "752a48f8cba9087b6345",
                    25: "6aff1abff3181c4be4b7",
                    26: "f8e68f066fec0a9d4928",
                    27: "17268c49036e63718bcd",
                    28: "31d6cfe0d16ae931b73c",
                    29: "7ed1c89d2a44c4e39cfa",
                    30: "31d6cfe0d16ae931b73c",
                    31: "7d19d2afdc588e36471f",
                    32: "31d6cfe0d16ae931b73c",
                    33: "31d6cfe0d16ae931b73c",
                    34: "31d6cfe0d16ae931b73c",
                    36: "31d6cfe0d16ae931b73c",
                    37: "16472a0d92600947beb8",
                    38: "31d6cfe0d16ae931b73c",
                    39: "b30e2f98301de0bbfdd3",
                    40: "448f973abe02454e248e",
                    41: "e1e2513512bf9513c082",
                    42: "6436c2f2c7fab1a849cd",
                    43: "31d6cfe0d16ae931b73c",
                    44: "623b9dc04e975e96ee9b",
                    45: "b94f1604c7fbc60cc303",
                    46: "347ddd4980702811af8b",
                    47: "fa6109c8620289ef3a82",
                    48: "31d6cfe0d16ae931b73c",
                    49: "206a39de43ed49d917cb",
                    50: "31d6cfe0d16ae931b73c",
                    51: "31d6cfe0d16ae931b73c",
                    52: "31d6cfe0d16ae931b73c",
                    53: "c75d6b4598f4e5f0b035",
                    54: "a6b7f66e1ac360d0369b",
                    55: "e0162ac20dadb7fc7597",
                    56: "31d6cfe0d16ae931b73c",
                    57: "ac3683c9a66fd47d1e9a",
                    58: "31d6cfe0d16ae931b73c",
                    59: "31d6cfe0d16ae931b73c",
                    60: "31d6cfe0d16ae931b73c",
                    61: "31d6cfe0d16ae931b73c",
                    62: "31d6cfe0d16ae931b73c",
                    63: "31d6cfe0d16ae931b73c",
                    64: "31d6cfe0d16ae931b73c",
                    65: "31d6cfe0d16ae931b73c",
                    66: "31d6cfe0d16ae931b73c",
                    67: "31d6cfe0d16ae931b73c",
                    68: "31d6cfe0d16ae931b73c",
                    69: "31d6cfe0d16ae931b73c",
                    70: "1958ed6d9ebc835b9680",
                    71: "25da3bb89bf32b689fbf",
                    72: "251a0d613c85b74b6ede",
                    73: "31d6cfe0d16ae931b73c",
                    74: "1a2c2f71435526e5bfc9",
                    75: "604b9ac194e31a18c984",
                    76: "89027cf3bed5ec959d7a",
                    77: "861e64977fa6851b13f7",
                    78: "74acd617ee019bb5995f",
                    79: "31d6cfe0d16ae931b73c",
                    80: "31d6cfe0d16ae931b73c",
                    81: "d5e0c613991be273e216",
                    82: "aa0e589d891dbc77501f",
                    83: "7c1d877a99aeaeb97f56",
                    84: "0db447eadea0aa469879",
                    85: "f5fa2b301c861ce8da73",
                    86: "b23eb9ffdf65a3348e34",
                    87: "842ddf25986733b9d1ee",
                    88: "86dbb919c9ba1353a6c0",
                    89: "969f85fee5b260820c26",
                    90: "31d6cfe0d16ae931b73c",
                    91: "e533e447c77488b4e02d",
                    92: "837d61d6bfd253e72e2b",
                    93: "16cb5177954ad9841393",
                    94: "7fdd87db3c673dbfa53b",
                    95: "5a138013ab3ec06b20b5",
                    96: "31d6cfe0d16ae931b73c"
                }[e] + ".css", a = o.p + i, c = document.getElementsByTagName("link"), u = 0; u < c.length; u++) {
                    var s = (d = c[u]).getAttribute("data-href") || d.getAttribute("href");
                    if ("stylesheet" === d.rel && (s === i || s === a))
                        return t()
                }
                var l = document.getElementsByTagName("style");
                for (u = 0; u < l.length; u++) {
                    var d;
                    if ((s = (d = l[u]).getAttribute("data-href")) === i || s === a)
                        return t()
                }
                var f = document.createElement("link");
                f.rel = "stylesheet",
                    f.type = "text/css";
                f.onerror = f.onload = function (i) {
                    if (f.onerror = f.onload = null,
                    "load" === i.type)
                        t();
                    else {
                        var o = i && ("load" === i.type ? "missing" : i.type)
                            , c = i && i.target && i.target.href || a
                            , u = new Error("Loading CSS chunk " + e + " failed.\n(" + c + ")");
                        u.code = "CSS_CHUNK_LOAD_FAILED",
                            u.type = o,
                            u.request = c,
                            delete r[e],
                            f.parentNode.removeChild(f),
                            n(u)
                    }
                }
                    ,
                    f.href = a,
                0 !== f.href.indexOf(window.location.origin + "/") && (f.crossOrigin = "anonymous"),
                    document.head.appendChild(f)
            }
        )).then((function () {
                r[e] = 0
            }
        )));
        var n = i[e];
        if (0 !== n)
            if (n)
                t.push(n[2]);
            else {
                var a = new Promise((function (t, r) {
                        n = i[e] = [t, r]
                    }
                ));
                t.push(n[2] = a);
                var c, u = document.createElement("script");
                u.charset = "utf-8",
                    u.timeout = 120,
                o.nc && u.setAttribute("nonce", o.nc),
                    u.src = function (e) {
                        return o.p + "main." + ({
                            0: "shared_5cac3ab8a563f9bbb56eca3256b8ed78b8d955b6",
                            1: "lib_0ad37f8a",
                            2: "shared_ddb69a58413b8324ef696dc6cfa9d1ea4c7519cc",
                            3: "lib_79b5cf47",
                            4: "shared_1257c3c9568bb2a3f62d5ecd308c048e4bf1bfcd",
                            5: "shared_92f99629e986751c8921c57c658e5e3ebe23d234",
                            6: "shared_66e7ebb3246404a2feb1adb7bed7e4117e5b4363",
                            7: "shared_f30f7459f944e851b885959dfde412e92f3a8d2e",
                            8: "shared_f30f7459f944e851b885959dfde412e92f3a8d2e_CSS",
                            9: "shared_3254bd1931ca333a5c274ba01dd8e55e0d0915f7",
                            10: "shared_1679dafdec5942113b512c7479f90fe8c8cc0c34",
                            11: "shared_6389524d82c312e7d98e40d6619dd28305142472",
                            12: "shared_d1ef5af0010fdbecda3e7215eeb794b639ace47a",
                            13: "griffith-player",
                            14: "lib_16a524cd",
                            15: "lib_330004dc",
                            16: "shared_02f2a87bf33ecb38af7b19dfbca195a9fc2fb430",
                            17: "shared_29883da17f6edf7dc61a1cad7e21ec8752a5040e",
                            18: "shared_4be4eabe8cccf0f9dd1e84435900f6b53ad5b687",
                            19: "shared_b59f4818030bb32444355928d14a422ae90a2e9b",
                            20: "shared_daaa4a126208fc5f5a863f08a363ab54d49aaa6e",
                            21: "shared_daaa4a126208fc5f5a863f08a363ab54d49aaa6e_CSS",
                            22: "Carousel",
                            23: "Chart",
                            24: "ECommerceAd",
                            25: "EcommerceAdCard",
                            26: "FeeConsultCard",
                            27: "GoodsRecommendGoodsCardList",
                            28: "HistoricalScore",
                            29: "InlineVideo",
                            30: "KnowledgeForm",
                            31: "Labels",
                            32: "ScoreLineChart",
                            33: "VideoAnswerLabel",
                            34: "VideoController",
                            36: "biz-co-creation",
                            37: "campaign-routes",
                            38: "collection-Scroller",
                            39: "collection-routes",
                            40: "collections-routes",
                            41: "comment-manage-footer",
                            42: "comments-modals",
                            43: "contribution-modal",
                            44: "creation-manage-action-list",
                            45: "creator-routes",
                            46: "creator-salt-routes",
                            47: "email-register-routes",
                            48: "empty-view-svg",
                            49: "explore-routes",
                            50: "flv.js",
                            51: "gaokao-pray-cheer-animation-data",
                            52: "gaokao-pray-kanshan-animation-data",
                            53: "globalOrgReport",
                            54: "help-center-routes",
                            55: "host-routes",
                            56: "image-editor",
                            57: "knowledge-plan-routes",
                            58: "lib_0bf4e2b2",
                            59: "lib_29107295",
                            60: "lib_5c8e84aa",
                            61: "lib_620696dc",
                            62: "lib_75fc9c18",
                            63: "lib_9974496f",
                            64: "lib_a0a3d150",
                            65: "lib_a4c92b5b",
                            66: "lib_c3f561e3",
                            67: "lib_f3cf1418",
                            68: "liveplus-routes",
                            69: "lottie-web",
                            70: "mcn-routes",
                            71: "messages-routes",
                            72: "modals",
                            73: "mqtt",
                            74: "navbar-messages",
                            75: "navbar-notifications",
                            76: "notifications-routes",
                            77: "people-routes",
                            78: "question-routes",
                            79: "react-draggable-tags",
                            80: "react-id-swiper",
                            81: "report_modals",
                            82: "richinput",
                            83: "richinputV2",
                            84: "roundtable-routes",
                            85: "search-routes",
                            86: "settings-routes",
                            87: "sign-page",
                            88: "signflow",
                            89: "special-routes",
                            90: "theater-player",
                            91: "topic-routes",
                            92: "topstory-routes",
                            93: "user-hover-card",
                            94: "vessay-routes",
                            95: "wiki-routes",
                            96: "zswsdid"
                        }[e] || e) + "." + {
                            0: "2f5028b07ccc699203a0",
                            1: "47119428df8d27119f28",
                            2: "211b5b9d40176a6d5888",
                            3: "f934f94d9e94b9eb4baf",
                            4: "db30a1295cf2e77ed198",
                            5: "5f17d902c23d030daa8e",
                            6: "683cea530b9ac0e7e45f",
                            7: "3e9ab33fc5217e8cc625",
                            8: "14f6e79e0d009abbd1a6",
                            9: "25171096d0e3c4cea189",
                            10: "bb4fc50b2165e07d6e55",
                            11: "0d92e8cbec0af97d933b",
                            12: "6c011ff07d1980525b83",
                            13: "7b8fe72e2f671a026b2d",
                            14: "6024905eb69de19f5d5a",
                            15: "cba5d8694883d412b0c3",
                            16: "ca485275ae38a06f52b9",
                            17: "ac5e1796bee87dc8cd4c",
                            18: "39cab951497327f42b03",
                            19: "f692616783cf8d7385a6",
                            20: "48ab60c044e71e64b93d",
                            21: "66a6354f9781a5fec884",
                            22: "346684a32da7806c51cb",
                            23: "6fd4b004119d0cba612f",
                            24: "c757706277fdf8043926",
                            25: "8bab9964c9b6bd6b1e51",
                            26: "ac28a4ced4e6f0fbbe13",
                            27: "725ba654dc0d5e0ede75",
                            28: "21f052214621bb8c9abc",
                            29: "e568777bb4d737986a0f",
                            30: "8602e31b2100f71333da",
                            31: "00b3692f335a699641a4",
                            32: "2c0156d44271cd16e48e",
                            33: "314b11db707ef9c0a7e9",
                            34: "1cdeaddbd3aab75f7a10",
                            36: "05e822ae6db50d71e91e",
                            37: "ba5acdc33e89392ad9d3",
                            38: "b48ff61d92655f288b20",
                            39: "e2993e9df6bdd6ad9b80",
                            40: "76605ffebd7a03722194",
                            41: "d7fefe3f7ef91a333002",
                            42: "3abe198cb0c0c2bc6177",
                            43: "3b85b1874650d12f63ba",
                            44: "c6492790693fc40f1f97",
                            45: "7b3de1663fbf3672dece",
                            46: "04f77055e034ff126a02",
                            47: "3c89b74e07160dceb411",
                            48: "ee6679a5b9132f07e3a9",
                            49: "c6fd01ae8cc9c9bc4a29",
                            50: "d6a80028c9a23ee9ae69",
                            51: "1ab4e52d2e69be05a611",
                            52: "fe4946976cbca410cf45",
                            53: "b1ca848869ace0fba550",
                            54: "a4108b30b8370c8049c1",
                            55: "3f2948fe00e0b30301a6",
                            56: "af2f61feada8a8ab2105",
                            57: "447d05e5bd1b9d8b9927",
                            58: "cb5fa31c50dc08b41961",
                            59: "1cae45b5f24b3683e506",
                            60: "2ae117ce1176f2530e4e",
                            61: "d01816291b9551b436bf",
                            62: "bc7dfb1604171a2b4fdc",
                            63: "61dcf67d0310601cfcf9",
                            64: "b3497148bef1d008e532",
                            65: "06f46ef8603547930ef0",
                            66: "8bd5c40b5b665038c74f",
                            67: "6e874f7f6e4141167b9e",
                            68: "91ad0af851a90bbea40a",
                            69: "133f7a22383c358871e2",
                            70: "c6f1a3a5cb6a1507e6fe",
                            71: "50c4a72d396744531daf",
                            72: "10af8df1da2bb32ece4d",
                            73: "c63a3e6e4db629eb2559",
                            74: "bae55c89873fa3f6f471",
                            75: "9ed76eb5c25c1235385d",
                            76: "f4f5dbad4b5a711d97fd",
                            77: "fdef2d6af006ab6ddbc1",
                            78: "103a7b6fa45fba9d5a27",
                            79: "c0255c9b12438540d1f3",
                            80: "02ca90c31a2f92654b04",
                            81: "47c07b3f058616291fb2",
                            82: "7aaffef26a9d25958763",
                            83: "3161a227d71f4b23de5e",
                            84: "5de9c0264874147558da",
                            85: "32a3f7f5b3c8266f1a4c",
                            86: "fa3dd785d8916d2001de",
                            87: "c39410703487d0e83ce6",
                            88: "4edcd6e6b67790af1c22",
                            89: "4a644e322daee8e707ed",
                            90: "5023289474a284152c24",
                            91: "33a56bc3ee23e38bfbfc",
                            92: "d02283e6f0ad18665ea7",
                            93: "9e7496aaca760236524f",
                            94: "b0198141fbe885ee2f02",
                            95: "7f03f5a7bc4a38a9d738",
                            96: "9b661482bd2fb378fc98"
                        }[e] + ".js"
                    }(e),
                0 !== u.src.indexOf(window.location.origin + "/") && (u.crossOrigin = "anonymous");
                var s = new Error;
                c = function (t) {
                    u.onerror = u.onload = null,
                        clearTimeout(l);
                    var n = i[e];
                    if (0 !== n) {
                        if (n) {
                            var r = t && ("load" === t.type ? "missing" : t.type)
                                , o = t && t.target && t.target.src;
                            s.message = "Loading chunk " + e + " failed.\n(" + r + ": " + o + ")",
                                s.name = "ChunkLoadError",
                                s.type = r,
                                s.request = o,
                                n[1](s)
                        }
                        i[e] = void 0
                    }
                }
                ;
                var l = setTimeout((function () {
                        c({
                            type: "timeout",
                            target: u
                        })
                    }
                ), 12e4);
                u.onerror = u.onload = c,
                    document.head.appendChild(u)
            }
        return Promise.all(t)
    }
        ,
        o.m = e,
        o.c = n,
        o.d = function (e, t, n) {
            o.o(e, t) || Object.defineProperty(e, t, {
                enumerable: !0,
                get: n
            })
        }
        ,
        o.r = function (e) {
            "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
                value: "Module"
            }),
                Object.defineProperty(e, "__esModule", {
                    value: !0
                })
        }
        ,
        o.t = function (e, t) {
            if (1 & t && (e = o(e)),
            8 & t)
                return e;
            if (4 & t && "object" == typeof e && e && e.__esModule)
                return e;
            var n = Object.create(null);
            if (o.r(n),
                Object.defineProperty(n, "default", {
                    enumerable: !0,
                    value: e
                }),
            2 & t && "string" != typeof e)
                for (var r in e)
                    o.d(n, r, function (t) {
                        return e[t]
                    }
                        .bind(null, r));
            return n
        }
        ,
        o.n = function (e) {
            var t = e && e.__esModule ? function () {
                    return e.default
                }
                : function () {
                    return e
                }
            ;
            return o.d(t, "a", t),
                t
        }
        ,
        o.o = function (e, t) {
            return Object.prototype.hasOwnProperty.call(e, t)
        }
        ,
        o.p = "https://static.zhihu.com/heifetz/",
        o.oe = function (e) {
            throw console.error(e),
                e
        }
    ;
    var a = window.webpackJsonp = window.webpackJsonp || []
        , c = a.push.bind(a);
    a.push = t,
        a = a.slice();
    for (var u = 0; u < a.length; u++)
        t(a[u]);
    var s = c;
    // o(o.s = 844)
}({
    243: function (module, exports, __webpack_require__) {
        "use strict";

        function t(e) {
            return (t = "function" == typeof Symbol && "symbol" == typeof Symbol.A ? function (e) {
                return typeof e
            } : function (e) {
                return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
            })(e)
        }

        Object.defineProperty(exports, "__esModule", {
            value: !0
        });
        var A = "2.0",
            __g = {};

        function s() {
        }

        function i(e) {
            this.t = (2048 & e) >> 11, this.s = (1536 & e) >> 9, this.i = 511 & e, this.h = 511 & e
        }

        function h(e) {
            this.s = (3072 & e) >> 10, this.h = 1023 & e
        }

        function a(e) {
            this.a = (3072 & e) >> 10, this.c = (768 & e) >> 8, this.n = (192 & e) >> 6, this.t = 63 & e
        }

        function c(e) {
            this.s = e >> 10 & 3, this.i = 1023 & e
        }

        function n() {
        }

        function e(e) {
            this.a = (3072 & e) >> 10, this.c = (768 & e) >> 8, this.n = (192 & e) >> 6, this.t = 63 & e
        }

        function o(e) {
            this.h = (4095 & e) >> 2, this.t = 3 & e
        }

        function r(e) {
            this.s = e >> 10 & 3, this.i = e >> 2 & 255, this.t = 3 & e
        }

        s.prototype.e = function (e) {
            e.o = !1
        }, i.prototype.e = function (e) {
            switch (this.t) {
                case 0:
                    e.r[this.s] = this.i;
                    break;
                case 1:
                    e.r[this.s] = e.k[this.h]
            }
        }, h.prototype.e = function (e) {
            e.k[this.h] = e.r[this.s]
        }, a.prototype.e = function (e) {
            switch (this.t) {
                case 0:
                    e.r[this.a] = e.r[this.c] + e.r[this.n];
                    break;
                case 1:
                    e.r[this.a] = e.r[this.c] - e.r[this.n];
                    break;
                case 2:
                    e.r[this.a] = e.r[this.c] * e.r[this.n];
                    break;
                case 3:
                    e.r[this.a] = e.r[this.c] / e.r[this.n];
                    break;
                case 4:
                    e.r[this.a] = e.r[this.c] % e.r[this.n];
                    break;
                case 5:
                    e.r[this.a] = e.r[this.c] == e.r[this.n];
                    break;
                case 6:
                    e.r[this.a] = e.r[this.c] >= e.r[this.n];
                    break;
                case 7:
                    e.r[this.a] = e.r[this.c] || e.r[this.n];
                    break;
                case 8:
                    e.r[this.a] = e.r[this.c] && e.r[this.n];
                    break;
                case 9:
                    e.r[this.a] = e.r[this.c] !== e.r[this.n];
                    break;
                case 10:
                    e.r[this.a] = t(e.r[this.c]);
                    break;
                case 11:
                    e.r[this.a] = e.r[this.c] in e.r[this.n];
                    break;
                case 12:
                    e.r[this.a] = e.r[this.c] > e.r[this.n];
                    break;
                case 13:
                    e.r[this.a] = -e.r[this.c];
                    break;
                case 14:
                    e.r[this.a] = e.r[this.c] < e.r[this.n];
                    break;
                case 15:
                    e.r[this.a] = e.r[this.c] & e.r[this.n];
                    break;
                case 16:
                    e.r[this.a] = e.r[this.c] ^ e.r[this.n];
                    break;
                case 17:
                    e.r[this.a] = e.r[this.c] << e.r[this.n];
                    break;
                case 18:
                    e.r[this.a] = e.r[this.c] >>> e.r[this.n];
                    break;
                case 19:
                    e.r[this.a] = e.r[this.c] | e.r[this.n];
                    break;
                case 20:
                    e.r[this.a] = !e.r[this.c]
            }
        }, c.prototype.e = function (e) {
            e.Q.push(e.C), e.B.push(e.k), e.C = e.r[this.s], e.k = [];
            for (var t = 0; t < this.i; t++) e.k.unshift(e.f.pop());
            e.g.push(e.f), e.f = []
        }, n.prototype.e = function (e) {
            e.C = e.Q.pop(), e.k = e.B.pop(), e.f = e.g.pop()
        }, e.prototype.e = function (e) {
            switch (this.t) {
                case 0:
                    e.u = e.r[this.a] >= e.r[this.c];
                    break;
                case 1:
                    e.u = e.r[this.a] <= e.r[this.c];
                    break;
                case 2:
                    e.u = e.r[this.a] > e.r[this.c];
                    break;
                case 3:
                    e.u = e.r[this.a] < e.r[this.c];
                    break;
                case 4:
                    e.u = e.r[this.a] == e.r[this.c];
                    break;
                case 5:
                    e.u = e.r[this.a] != e.r[this.c];
                    break;
                case 6:
                    e.u = e.r[this.a];
                    break;
                case 7:
                    e.u = !e.r[this.a]
            }
        }, o.prototype.e = function (e) {
            switch (this.t) {
                case 0:
                    e.C = this.h;
                    break;
                case 1:
                    e.u && (e.C = this.h);
                    break;
                case 2:
                    e.u || (e.C = this.h);
                    break;
                case 3:
                    e.C = this.h, e.w = null
            }
            e.u = !1
        }, r.prototype.e = function (e) {
            switch (this.t) {
                case 0:
                    for (var t = [], n = 0; n < this.i; n++) t.unshift(e.f.pop());
                    e.r[3] = e.r[this.s](t[0], t[1]);
                    break;
                case 1:
                    for (var r = e.f.pop(), i = [], o = 0; o < this.i; o++) i.unshift(e.f.pop());
                    e.r[3] = e.r[this.s][r](i[0], i[1]);
                    break;
                case 2:
                    for (var a = [], c = 0; c < this.i; c++) a.unshift(e.f.pop());
                    e.r[3] = new e.r[this.s](a[0], a[1])
            }
        };
        var k = function (e) {
            for (var t = 66, n = [], r = 0; r < e.length; r++) {
                var i = 24 ^ e.charCodeAt(r) ^ t;
                n.push(String.fromCharCode(i)), t = i
            }
            return n.join("")
        };

        function Q(e) {
            this.t = (4095 & e) >> 10, this.s = (1023 & e) >> 8, this.i = 1023 & e, this.h = 63 & e
        }

        function C(e) {
            this.t = (4095 & e) >> 10, this.a = (1023 & e) >> 8, this.c = (255 & e) >> 6
        }

        function B(e) {
            this.s = (3072 & e) >> 10, this.h = 1023 & e
        }

        function f(e) {
            this.h = 4095 & e
        }

        function g(e) {
            this.s = (3072 & e) >> 10
        }

        function u(e) {
            this.h = 4095 & e
        }

        function w(e) {
            this.t = (3840 & e) >> 8, this.s = (192 & e) >> 6, this.i = 63 & e
        }

        function G() {
            this.r = [0, 0, 0, 0], this.C = 0, this.Q = [], this.k = [], this.B = [], this.f = [], this.g = [], this.u = !1, this.G = [], this.b = [], this.o = !1, this.w = null, this.U = null, this.F = [], this.R = 0, this.J = {
                0: s,
                1: i,
                2: h,
                3: a,
                4: c,
                5: n,
                6: e,
                7: o,
                8: r,
                9: Q,
                10: C,
                11: B,
                12: f,
                13: g,
                14: u,
                15: w
            }
        }

        Q.prototype.e = function (e) {
            switch (this.t) {
                case 0:
                    e.f.push(e.r[this.s]);
                    break;
                case 1:
                    e.f.push(this.i);
                    break;
                case 2:
                    e.f.push(e.k[this.h]);
                    break;
                case 3:
                    e.f.push(k(e.b[this.h]))
            }
        }, C.prototype.e = function (A) {
            switch (this.t) {
                case 0:
                    var t = A.f.pop();
                    A.r[this.a] = A.r[this.c][t];
                    break;
                case 1:
                    var s = A.f.pop(),
                        i = A.f.pop();
                    A.r[this.c][s] = i;
                    break;
                case 2:
                    var h = A.f.pop();
                    A.r[this.a] = eval(h)
            }
        }, B.prototype.e = function (e) {
            e.r[this.s] = k(e.b[this.h])
        }, f.prototype.e = function (e) {
            e.w = this.h
        }, g.prototype.e = function (e) {
            throw e.r[this.s]
        }, u.prototype.e = function (e) {
            var t = this,
                n = [0];
            e.k.forEach((function (e) {
                n.push(e)
            }));
            var r = function (r) {
                var i = new G;
                return i.k = n, i.k[0] = r, i.v(e.G, t.h, e.b, e.F), i.r[3]
            };
            r.toString = function () {
                return "() { [native code] }"
            }, e.r[3] = r
        }, w.prototype.e = function (e) {
            switch (this.t) {
                case 0:
                    for (var t = {}, n = 0; n < this.i; n++) {
                        var r = e.f.pop();
                        t[e.f.pop()] = r
                    }
                    e.r[this.s] = t;
                    break;
                case 1:
                    for (var i = [], o = 0; o < this.i; o++) i.unshift(e.f.pop());
                    e.r[this.s] = i
            }
        }, G.prototype.D = function (e) {
            for (var t = atob(e), n = t.charCodeAt(0) << 8 | t.charCodeAt(1), r = [], i = 2; i < n + 2; i += 2) r.push(t.charCodeAt(i) << 8 | t.charCodeAt(i + 1));
            this.G = r;
            for (var o = [], a = n + 2; a < t.length;) {
                var c = t.charCodeAt(a) << 8 | t.charCodeAt(a + 1),
                    u = t.slice(a + 2, a + 2 + c);
                o.push(u), a += c + 2
            }
            this.b = o
        }, G.prototype.v = function (e, t, n) {
            for (t = t || 0, n = n || [], this.C = t, "string" == typeof e ? this.D(e) : (this.G = e, this.b = n), this.o = !0, this.R = Date.now(); this.o;) {
                var r = this.G[this.C++];
                if ("number" != typeof r) break;
                var i = Date.now();
                if (500 < i - this.R) return;
                this.R = i;
                try {
                    this.e(r)
                } catch (e) {
                    this.U = e, this.w && (this.C = this.w)
                }
            }
        }, G.prototype.e = function (e) {
            var t = (61440 & e) >> 12;
            new this.J[t](e)
                .e(this)
        }, "undefined" != typeof window && (new G)
            .v("AxjgB5MAnACoAJwBpAAAABAAIAKcAqgAMAq0AzRJZAZwUpwCqACQACACGAKcBKAAIAOcBagAIAQYAjAUGgKcBqFAuAc5hTSHZAZwqrAIGgA0QJEAJAAYAzAUGgOcCaFANRQ0R2QGcOKwChoANECRACQAsAuQABgDnAmgAJwMgAGcDYwFEAAzBmAGcSqwDhoANECRACQAGAKcD6AAGgKcEKFANEcYApwRoAAxB2AGcXKwEhoANECRACQAGAKcE6AAGgKcFKFANEdkBnGqsBUaADRAkQAkABgCnBagAGAGcdKwFxoANECRACQAGAKcGKAAYAZx+rAZGgA0QJEAJAAYA5waoABgBnIisBsaADRAkQAkABgCnBygABoCnB2hQDRHZAZyWrAeGgA0QJEAJAAYBJwfoAAwFGAGcoawIBoANECRACQAGAOQALAJkAAYBJwfgAlsBnK+sCEaADRAkQAkABgDkACwGpAAGAScH4AJbAZy9rAiGgA0QJEAJACwI5AAGAScH6AAkACcJKgAnCWgAJwmoACcJ4AFnA2MBRAAMw5gBnNasCgaADRAkQAkABgBEio0R5EAJAGwKSAFGACcKqAAEgM0RCQGGAYSATRFZAZzshgAtCs0QCQAGAYSAjRFZAZz1hgAtCw0QCQAEAAgB7AtIAgYAJwqoAASATRBJAkYCRIANEZkBnYqEAgaBxQBOYAoBxQEOYQ0giQKGAmQABgAnC6ABRgBGgo0UhD/MQ8zECALEAgaBxQBOYAoBxQEOYQ0gpEAJAoYARoKNFIQ/zEPkAAgChgLGgkUATmBkgAaAJwuhAUaCjdQFAg5kTSTJAsQCBoHFAE5gCgHFAQ5hDSCkQAkChgBGgo0UhD/MQ+QACAKGAsaCRQCOYGSABoAnC6EBRoKN1AUEDmRNJMkCxgFGgsUPzmPkgAaCJwvhAU0wCQFGAUaCxQGOZISPzZPkQAaCJwvhAU0wCQFGAUaCxQMOZISPzZPkQAaCJwvhAU0wCQFGAUaCxQSOZISPzZPkQAaCJwvhAU0wCQFGAkSAzRBJAlz/B4FUAAAAwUYIAAIBSITFQkTERwABi0GHxITAAAJLwMSGRsXHxMZAAk0Fw8HFh4NAwUABhU1EBceDwAENBcUEAAGNBkTGRcBAAFKAAkvHg4PKz4aEwIAAUsACDIVHB0QEQ4YAAsuAzs7AAoPKToKDgAHMx8SGQUvMQABSAALORoVGCQgERcCAxoACAU3ABEXAgMaAAsFGDcAERcCAxoUCgABSQAGOA8LGBsPAAYYLwsYGw8AAU4ABD8QHAUAAU8ABSkbCQ4BAAFMAAktCh8eDgMHCw8AAU0ADT4TGjQsGQMaFA0FHhkAFz4TGjQsGQMaFA0FHhk1NBkCHgUbGBEPAAFCABg9GgkjIAEmOgUHDQ8eFSU5DggJAwEcAwUAAUMAAUAAAUEADQEtFw0FBwtdWxQTGSAACBwrAxUPBR4ZAAkqGgUDAwMVEQ0ACC4DJD8eAx8RAAQ5GhUYAAFGAAAABjYRExELBAACWhgAAVoAQAg/PTw0NxcQPCQ5C3JZEBs9fkcnDRcUAXZia0Q4EhQgXHojMBY3MWVCNT0uDhMXcGQ7AUFPHigkQUwQFkhaAkEACjkTEQspNBMZPC0ABjkTEQsrLQ==");
        var b = function (e) {
            return __g._encrypt(encodeURIComponent(e))
        };
        exports.ENCRYPT_VERSION = A, exports.default = b
    },
    371: function (e, t, n) {
        var r;
        !function (i) {
            "use strict";

            function o(e, t) {
                var n = (65535 & e) + (65535 & t);
                return (e >> 16) + (t >> 16) + (n >> 16) << 16 | 65535 & n
            }

            function a(e, t, n, r, i, a) {
                return o((c = o(o(t, e), o(r, a))) << (u = i) | c >>> 32 - u, n);
                var c, u
            }

            function c(e, t, n, r, i, o, c) {
                return a(t & n | ~t & r, e, t, i, o, c)
            }

            function u(e, t, n, r, i, o, c) {
                return a(t & r | n & ~r, e, t, i, o, c)
            }

            function s(e, t, n, r, i, o, c) {
                return a(t ^ n ^ r, e, t, i, o, c)
            }

            function l(e, t, n, r, i, o, c) {
                return a(n ^ (t | ~r), e, t, i, o, c)
            }

            function d(e, t) {
                var n, r, i, a, d;
                e[t >> 5] |= 128 << t % 32, e[14 + (t + 64 >>> 9 << 4)] = t;
                var f = 1732584193,
                    p = -271733879,
                    h = -1732584194,
                    b = 271733878;
                for (n = 0; n < e.length; n += 16) r = f, i = p, a = h, d = b, f = c(f, p, h, b, e[n], 7, -680876936), b = c(b, f, p, h, e[n + 1], 12, -389564586), h = c(h, b, f, p, e[n + 2], 17, 606105819), p = c(p, h, b, f, e[n + 3], 22, -1044525330), f = c(f, p, h, b, e[n + 4], 7, -176418897), b = c(b, f, p, h, e[n + 5], 12, 1200080426), h = c(h, b, f, p, e[n + 6], 17, -1473231341), p = c(p, h, b, f, e[n + 7], 22, -45705983), f = c(f, p, h, b, e[n + 8], 7, 1770035416), b = c(b, f, p, h, e[n + 9], 12, -1958414417), h = c(h, b, f, p, e[n + 10], 17, -42063), p = c(p, h, b, f, e[n + 11], 22, -1990404162), f = c(f, p, h, b, e[n + 12], 7, 1804603682), b = c(b, f, p, h, e[n + 13], 12, -40341101), h = c(h, b, f, p, e[n + 14], 17, -1502002290), f = u(f, p = c(p, h, b, f, e[n + 15], 22, 1236535329), h, b, e[n + 1], 5, -165796510), b = u(b, f, p, h, e[n + 6], 9, -1069501632), h = u(h, b, f, p, e[n + 11], 14, 643717713), p = u(p, h, b, f, e[n], 20, -373897302), f = u(f, p, h, b, e[n + 5], 5, -701558691), b = u(b, f, p, h, e[n + 10], 9, 38016083), h = u(h, b, f, p, e[n + 15], 14, -660478335), p = u(p, h, b, f, e[n + 4], 20, -405537848), f = u(f, p, h, b, e[n + 9], 5, 568446438), b = u(b, f, p, h, e[n + 14], 9, -1019803690), h = u(h, b, f, p, e[n + 3], 14, -187363961), p = u(p, h, b, f, e[n + 8], 20, 1163531501), f = u(f, p, h, b, e[n + 13], 5, -1444681467), b = u(b, f, p, h, e[n + 2], 9, -51403784), h = u(h, b, f, p, e[n + 7], 14, 1735328473), f = s(f, p = u(p, h, b, f, e[n + 12], 20, -1926607734), h, b, e[n + 5], 4, -378558), b = s(b, f, p, h, e[n + 8], 11, -2022574463), h = s(h, b, f, p, e[n + 11], 16, 1839030562), p = s(p, h, b, f, e[n + 14], 23, -35309556), f = s(f, p, h, b, e[n + 1], 4, -1530992060), b = s(b, f, p, h, e[n + 4], 11, 1272893353), h = s(h, b, f, p, e[n + 7], 16, -155497632), p = s(p, h, b, f, e[n + 10], 23, -1094730640), f = s(f, p, h, b, e[n + 13], 4, 681279174), b = s(b, f, p, h, e[n], 11, -358537222), h = s(h, b, f, p, e[n + 3], 16, -722521979), p = s(p, h, b, f, e[n + 6], 23, 76029189), f = s(f, p, h, b, e[n + 9], 4, -640364487), b = s(b, f, p, h, e[n + 12], 11, -421815835), h = s(h, b, f, p, e[n + 15], 16, 530742520), f = l(f, p = s(p, h, b, f, e[n + 2], 23, -995338651), h, b, e[n], 6, -198630844), b = l(b, f, p, h, e[n + 7], 10, 1126891415), h = l(h, b, f, p, e[n + 14], 15, -1416354905), p = l(p, h, b, f, e[n + 5], 21, -57434055), f = l(f, p, h, b, e[n + 12], 6, 1700485571), b = l(b, f, p, h, e[n + 3], 10, -1894986606), h = l(h, b, f, p, e[n + 10], 15, -1051523), p = l(p, h, b, f, e[n + 1], 21, -2054922799), f = l(f, p, h, b, e[n + 8], 6, 1873313359), b = l(b, f, p, h, e[n + 15], 10, -30611744), h = l(h, b, f, p, e[n + 6], 15, -1560198380), p = l(p, h, b, f, e[n + 13], 21, 1309151649), f = l(f, p, h, b, e[n + 4], 6, -145523070), b = l(b, f, p, h, e[n + 11], 10, -1120210379), h = l(h, b, f, p, e[n + 2], 15, 718787259), p = l(p, h, b, f, e[n + 9], 21, -343485551), f = o(f, r), p = o(p, i), h = o(h, a), b = o(b, d);
                return [f, p, h, b]
            }

            function f(e) {
                var t, n = "",
                    r = 32 * e.length;
                for (t = 0; t < r; t += 8) n += String.fromCharCode(e[t >> 5] >>> t % 32 & 255);
                return n
            }

            function p(e) {
                var t, n = [];
                for (n[(e.length >> 2) - 1] = void 0, t = 0; t < n.length; t += 1) n[t] = 0;
                var r = 8 * e.length;
                for (t = 0; t < r; t += 8) n[t >> 5] |= (255 & e.charCodeAt(t / 8)) << t % 32;
                return n
            }

            function h(e) {
                var t, n, r = "";
                for (n = 0; n < e.length; n += 1) t = e.charCodeAt(n), r += "0123456789abcdef".charAt(t >>> 4 & 15) + "0123456789abcdef".charAt(15 & t);
                return r
            }

            function b(e) {
                return unescape(encodeURIComponent(e))
            }

            function v(e) {
                return function (e) {
                    return f(d(p(e), 8 * e.length))
                }(b(e))
            }

            function O(e, t) {
                return function (e, t) {
                    var n, r, i = p(e),
                        o = [],
                        a = [];
                    for (o[15] = a[15] = void 0, i.length > 16 && (i = d(i, 8 * e.length)), n = 0; n < 16; n += 1) o[n] = 909522486 ^ i[n], a[n] = 1549556828 ^ i[n];
                    return r = d(o.concat(p(t)), 512 + 8 * t.length), f(d(a.concat(r), 640))
                }(b(e), b(t))
            }

            function g(e, t, n) {
                return t ? n ? O(t, e) : h(O(t, e)) : n ? v(e) : h(v(e))
            }

            void 0 === (r = function () {
                return g
            }.call(t, n, t, e)) || (e.exports = r)
        }()
    }
})


var o = modules(243)
    , a = modules.n(o)
    , s = modules(371)
    , l = modules.n(s);

function get_signature(e) {
    var U = function (e) {
        var t = new URL(e, "https://www.zhihu.com");
        return "" + t.pathname + t.search
    }
        , M = function (e) {
        return null == e ? "" : "string" == typeof e ? e : "undefined" != typeof URLSearchParams && e instanceof URLSearchParams ? e.toString() : u()(e) ? JSON.stringify(e) : ("object" == typeof (t = e) ? null === t : "function" != typeof t) ? String(e) : "";
        var t
    }
        , B = function (e, t) {
        return void 0 === t && (t = 4096),
        !!e && function (e) {
            return new Blob([e]).size
        }(e) <= t
    }

    var n = {
        dc0: "\"ALDQODSHZhSPTpHFSuIP0qp7puKVHbZjuFw=|1643257930\"",
        xZst81: null,
        zse93: "101_3_2.0"
    }, t = null;

    var r = n.zse93
        , i = n.dc0
        , o = n.xZst81
        , c = U(e)
        , u = M(t)
        , s = [r, c, i, B(u) && u, o].filter(Boolean).join("+");
    var signature = '2.0_' + a()(l()(s))
    signature = signature.slice(0, signature.length - 4)
    console.log('signature:', signature)
    return signature
}

// var ee = '/api/v4/search_v3?t=general&q=%E7%90%86%E8%B4%A2&correction=1&offset=0&limit=20&filter_fields=&lc_idx=0&show_all_topics=0&search_source=Normal'
// var nn = {
//     dc0: "\"ALDQODSHZhSPTpHFSuIP0qp7puKVHbZjuFw=|1643257930\"",
//     xZst81: null,
//     zse93: "101_3_2.0"
// }
// get_signature(ee, null, nn)


module.exports = {
    get_signature: get_signature
}
