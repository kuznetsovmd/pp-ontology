function msSchemaLoader() {
    try {
        var e = new XMLHttpRequest
          , t = (new XMLHttpRequest,
        "https://schema.milestoneinternet.com/schema/" + extractSubdomain(encodeURI(window.location.href)) + "/schema.json?t=" + Math.floor(1e4 * Math.random()) + 1);
        e.onreadystatechange = function() {
            4 == e.readyState && 200 == e.status && "[]" != e.responseText && (
            jsonld = document.createElement("script"),
            jsonld.type = "application/ld+json",
            jsonld.id = "ms-jsonblock",
            jsonld.innerHTML = e.responseText,
            appendschema(jsonld))
        }
        ,
        e.open("GET", t, !0),
        e.setRequestHeader("x-ms-blob-type", "BlockBlob"),
        e.send()
    } catch (e) {
        console.log(e)
    }
}
function appendschema(jsonld) {
    "[]" != jsonld.innerHTML && (document.getElementsByTagName("head")[0].appendChild(jsonld));
     console.log("schema added to head");
}
function extractSubdomain(e) {
    var t = "";
    return null != (e = (e = (e = (e = e.replace(new RegExp(/^http\:\/\/|^https\:\/\/|^ftp\:\/\//i), "")).replace(new RegExp(/^uat\.|^www\./i), "")).split("?").shift()).split("#").shift()) && (t = trimTrailingChars(e, "/")),
    t
}
function trimTrailingChars(e, t) {
    var n = new RegExp(t + "+$");
    return e.replace(n, "")
}
var msFilter = {
    onLoad: "load"
};
