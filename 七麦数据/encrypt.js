function i(e) {
    var t, a = (t = "",
        ["66", "72", "6f", "6d", "43", "68", "61", "72", "43", "6f", "64", "65"].forEach((function (e) {
                t += unescape("%u00" + e)
            }
        )),
        t);
    return String[a](e)
}

function cv(e) {
    return function (e) {
        return Buffer.from(e).toString("base64")
    }(encodeURIComponent(e).replace(/%([0-9A-F]{2})/g, (function (e, t) {
            return i("0x" + t)
        }
    )))
}

function oZ(e, t) {
    t || (t = s());
    for (var a = (e = e.split("")).length, n = t.length, o = "charCodeAt", r = 0; r < a; r++)
        e[r] = i(e[r][o](0) ^ t[(r + 10) % n][o](0));
    return e.join("")
}

var d = "@#",
    f = 3460,
    h = "analysis",
    baseURL = "https://api.qimai.cn",
    l = "00000008d78d46a";

function getAnalysis(url, params) {
    var a, o = +new Date - (f || 0) - 1515125653845, r = [];
    void 0 === params && (params = {})
    Object.keys(params).forEach((function (t) {
            if (t == h)
                return !1;
            params.hasOwnProperty(t) && r.push(params[t])
        }
    ))
    r = r.sort().join("")
    r = cv(r)
    r += d + url.replace(baseURL, "")
    r += d + o
    r += d + 1
    a = cv(oZ(r, l))
    // console.log('analysis = ' + a)
    return a
}

url = '/andapp/appinfo'
params = {
    'market': 100,
    'appid': 5388170
}
getAnalysis(url, params)
