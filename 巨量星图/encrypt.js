var p = function (e, t, n, i, r, o, a) {
    var s = e + (t & n | ~t & i) + (r >>> 0) + a;
    return (s << o | s >>> 32 - o) + t
}
var g = function (e, t, n, i, r, o, a) {
    var s = e + (t & i | n & ~i) + (r >>> 0) + a;
    return (s << o | s >>> 32 - o) + t
}
var v = function (e, t, n, i, r, o, a) {
    var s = e + (t ^ n ^ i) + (r >>> 0) + a;
    return (s << o | s >>> 32 - o) + t
}
var m = function (e, t, n, i, r, o, a) {
    var s = e + (n ^ (t | ~i)) + (r >>> 0) + a;
    return (s << o | s >>> 32 - o) + t
}
var n = {
    utf8: {
        stringToBytes: function (e) {
            return n.bin.stringToBytes(unescape(encodeURIComponent(e)))
        },
        bytesToString: function (e) {
            return decodeURIComponent(escape(n.bin.bytesToString(e)))
        }
    },
    bin: {
        stringToBytes: function (e) {
            for (var t = [], n = 0; n < e.length; n++)
                t.push(255 & e.charCodeAt(n));
            return t
        },
        bytesToString: function (e) {
            for (var t = [], n = 0; n < e.length; n++)
                t.push(String.fromCharCode(e[n]));
            return t.join("")
        }
    }
}

var r = n.utf8

var i = {
    rotl: function (e, t) {
        return e << t | e >>> 32 - t
    },
    rotr: function (e, t) {
        return e << 32 - t | e >>> t
    },
    endian: function (e) {
        if (e.constructor == Number)
            return 16711935 & i.rotl(e, 8) | 4278255360 & i.rotl(e, 24);
        for (var t = 0; t < e.length; t++)
            e[t] = i.endian(e[t]);
        return e
    },
    randomBytes: function (e) {
        for (var t = []; e > 0; e--)
            t.push(Math.floor(256 * Math.random()));
        return t
    },
    bytesToWords: function (e) {
        for (var t = [], n = 0, i = 0; n < e.length; n++,
            i += 8)
            t[i >>> 5] |= e[n] << 24 - i % 32;
        return t
    },
    wordsToBytes: function (e) {
        for (var t = [], n = 0; n < 32 * e.length; n += 8)
            t.push(e[n >>> 5] >>> 24 - n % 32 & 255);
        return t
    },
    bytesToHex: function (e) {
        for (var t = [], n = 0; n < e.length; n++)
            t.push((e[n] >>> 4).toString(16)),
                t.push((15 & e[n]).toString(16));
        return t.join("")
    },
    hexToBytes: function (e) {
        for (var t = [], n = 0; n < e.length; n += 2)
            t.push(parseInt(e.substr(n, 2), 16));
        return t
    },
    bytesToBase64: function (e) {
        for (var t = [], i = 0; i < e.length; i += 3)
            for (var r = e[i] << 16 | e[i + 1] << 8 | e[i + 2], o = 0; o < 4; o++)
                8 * i + 6 * o <= 8 * e.length ? t.push(n.charAt(r >>> 6 * (3 - o) & 63)) : t.push("=");
        return t.join("")
    },
    base64ToBytes: function (e) {
        e = e.replace(/[^A-Z0-9+\/]/gi, "");
        for (var t = [], i = 0, r = 0; i < e.length; r = ++i % 4)
            0 != r && t.push((n.indexOf(e.charAt(i - 1)) & Math.pow(2, -2 * r + 8) - 1) << 2 * r | n.indexOf(e.charAt(i)) >>> 6 - 2 * r);
        return t
    }
}


var s = function (e, t) {
    e.constructor == String ? e = t && "binary" === t.encoding ? a.stringToBytes(e) : r.stringToBytes(e) : o(e) ? e = Array.prototype.slice.call(e, 0) : Array.isArray(e) || e.constructor === Uint8Array || (e = e.toString());
    for (var n = i.bytesToWords(e), l = 8 * e.length, u = 1732584193, c = -271733879, d = -1732584194, f = 271733878, h = 0; h < n.length; h++)
        n[h] = 16711935 & (n[h] << 8 | n[h] >>> 24) | 4278255360 & (n[h] << 24 | n[h] >>> 8);
    n[l >>> 5] |= 128 << l % 32,
        n[14 + (l + 64 >>> 9 << 4)] = l;
    // var p = s._ff
    //     , g = s._gg
    //     , v = s._hh
    //     , m = s._ii;
    for (h = 0; h < n.length; h += 16) {
        var y = u
            , A = c
            , b = d
            , w = f;
        u = p(u, c, d, f, n[h + 0], 7, -680876936),
            f = p(f, u, c, d, n[h + 1], 12, -389564586),
            d = p(d, f, u, c, n[h + 2], 17, 606105819),
            c = p(c, d, f, u, n[h + 3], 22, -1044525330),
            u = p(u, c, d, f, n[h + 4], 7, -176418897),
            f = p(f, u, c, d, n[h + 5], 12, 1200080426),
            d = p(d, f, u, c, n[h + 6], 17, -1473231341),
            c = p(c, d, f, u, n[h + 7], 22, -45705983),
            u = p(u, c, d, f, n[h + 8], 7, 1770035416),
            f = p(f, u, c, d, n[h + 9], 12, -1958414417),
            d = p(d, f, u, c, n[h + 10], 17, -42063),
            c = p(c, d, f, u, n[h + 11], 22, -1990404162),
            u = p(u, c, d, f, n[h + 12], 7, 1804603682),
            f = p(f, u, c, d, n[h + 13], 12, -40341101),
            d = p(d, f, u, c, n[h + 14], 17, -1502002290),
            c = p(c, d, f, u, n[h + 15], 22, 1236535329),
            u = g(u, c, d, f, n[h + 1], 5, -165796510),
            f = g(f, u, c, d, n[h + 6], 9, -1069501632),
            d = g(d, f, u, c, n[h + 11], 14, 643717713),
            c = g(c, d, f, u, n[h + 0], 20, -373897302),
            u = g(u, c, d, f, n[h + 5], 5, -701558691),
            f = g(f, u, c, d, n[h + 10], 9, 38016083),
            d = g(d, f, u, c, n[h + 15], 14, -660478335),
            c = g(c, d, f, u, n[h + 4], 20, -405537848),
            u = g(u, c, d, f, n[h + 9], 5, 568446438),
            f = g(f, u, c, d, n[h + 14], 9, -1019803690),
            d = g(d, f, u, c, n[h + 3], 14, -187363961),
            c = g(c, d, f, u, n[h + 8], 20, 1163531501),
            u = g(u, c, d, f, n[h + 13], 5, -1444681467),
            f = g(f, u, c, d, n[h + 2], 9, -51403784),
            d = g(d, f, u, c, n[h + 7], 14, 1735328473),
            c = g(c, d, f, u, n[h + 12], 20, -1926607734),
            u = v(u, c, d, f, n[h + 5], 4, -378558),
            f = v(f, u, c, d, n[h + 8], 11, -2022574463),
            d = v(d, f, u, c, n[h + 11], 16, 1839030562),
            c = v(c, d, f, u, n[h + 14], 23, -35309556),
            u = v(u, c, d, f, n[h + 1], 4, -1530992060),
            f = v(f, u, c, d, n[h + 4], 11, 1272893353),
            d = v(d, f, u, c, n[h + 7], 16, -155497632),
            c = v(c, d, f, u, n[h + 10], 23, -1094730640),
            u = v(u, c, d, f, n[h + 13], 4, 681279174),
            f = v(f, u, c, d, n[h + 0], 11, -358537222),
            d = v(d, f, u, c, n[h + 3], 16, -722521979),
            c = v(c, d, f, u, n[h + 6], 23, 76029189),
            u = v(u, c, d, f, n[h + 9], 4, -640364487),
            f = v(f, u, c, d, n[h + 12], 11, -421815835),
            d = v(d, f, u, c, n[h + 15], 16, 530742520),
            c = v(c, d, f, u, n[h + 2], 23, -995338651),
            u = m(u, c, d, f, n[h + 0], 6, -198630844),
            f = m(f, u, c, d, n[h + 7], 10, 1126891415),
            d = m(d, f, u, c, n[h + 14], 15, -1416354905),
            c = m(c, d, f, u, n[h + 5], 21, -57434055),
            u = m(u, c, d, f, n[h + 12], 6, 1700485571),
            f = m(f, u, c, d, n[h + 3], 10, -1894986606),
            d = m(d, f, u, c, n[h + 10], 15, -1051523),
            c = m(c, d, f, u, n[h + 1], 21, -2054922799),
            u = m(u, c, d, f, n[h + 8], 6, 1873313359),
            f = m(f, u, c, d, n[h + 15], 10, -30611744),
            d = m(d, f, u, c, n[h + 6], 15, -1560198380),
            c = m(c, d, f, u, n[h + 13], 21, 1309151649),
            u = m(u, c, d, f, n[h + 4], 6, -145523070),
            f = m(f, u, c, d, n[h + 11], 10, -1120210379),
            d = m(d, f, u, c, n[h + 2], 15, 718787259),
            c = m(c, d, f, u, n[h + 9], 21, -343485551),
            u = u + y >>> 0,
            c = c + A >>> 0,
            d = d + b >>> 0,
            f = f + w >>> 0
    }
    return i.endian([u, c, d, f])
}

// var e = "author_id6774914600774139912num10service_methodGetAuthorHotCommentTokensservice_namedata.AdStarDataServicewithout_emojiwithout_emoji"

var getSign = function (e) {
    var u = "e39539b8836fb99e1538974d3ac1fe98",
        t = undefined;
    var nn = i.wordsToBytes(s(e + u, t));
    sign = i.bytesToHex(nn)
    return sign
}
