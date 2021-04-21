var md5 = require("./md5.js");

function ascp() {
    var nowTime = Math.floor(new Date().getTime() / 1e3);
    var t_hex = nowTime.toString(16).toUpperCase();
    var t_md5 = md5(nowTime).toString().toUpperCase();
    if (t_hex.length !== 8) {
        return {
            as: "479BB4B7254C150",
            cp: "7E0AC8874BB0985"
        };
    }
    var pre = t_md5.slice(0, 5);
    var last = t_md5.slice(-5);
    var as_cy = "";
    for (var i = 0; i < 5; i++) {
        as_cy += pre[i] + t_hex[i];
    }
    var cp_cy = "";
    for (var j = 0; j < 5; j++) {
        cp_cy += t_hex[j + 3] + last[j];
    }
    return {
        as: "A1" + as_cy + t_hex.slice(-3),
        cp: t_hex.slice(0, 3) + cp_cy + "E1"
    };
}

console.log(ascp())
