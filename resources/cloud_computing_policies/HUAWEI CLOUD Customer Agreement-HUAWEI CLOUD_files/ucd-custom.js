!function (t, e) {
    "function" == typeof define && define.amd ? define(["jquery"], e) : "object" == typeof exports ? module.exports = e(require("jquery")) : t.UCD = e(t.jQuery)
}(this, function (t) {
    function e(e, n) {
        var i = t(e), o = t(document);
        return i.on(l.DOWN + g, function (t) {
            var e = l.getEvent(t);
            var r = e.pageX, s = e.pageY, a = r, u = s;
            n.onDragStart && n.onDragStart.call(i, t, a, u), o.on(l.MOVE + g, function (t) {
                var e = l.getEvent(t);
                a = e.pageX - r, u = e.pageY - s, n.onDragging && n.onDragging.call(i, t, a, u)
            }).on(l.UP + g, function (t) {
                o.off(l.MOVE + g + " " + l.UP + g), n.onDragEnd && n.onDragEnd.call(i, t, a, u)
            })
        }), l.DOWN + g
    }

    function n(t) {
        t = t.toLowerCase();
        var e = /(chrome)[ \/]([\w.]+)/.exec(t) || /(webkit)[ \/]([\w.]+)/.exec(t) || /(opera)(?:.*version|)[ \/]([\w.]+)/.exec(t) || /(msie) ([\w.]+)/.exec(t) || t.indexOf("compatible") < 0 && /(mozilla)(?:.*? rv:([\w.]+)|)/.exec(t) || [];
        return { browser: e[1] || "", version: e[2] || "0" }
    }

    function i(t) {
        var e = n(navigator.userAgent), i = {};
        return e.browser && (i[e.browser] = !0, i.version = e.version), i.chrome ? i.webkit = !0 : i.webkit && (i.safari = !0), t.browser = i, t[e.browser] = !0, i
    }

    function o(e) {
        var n, i, r = u.call(arguments, 1), s = 0, a = r.length;
        for (; a > s; s++)for (n in r[s]) i = r[s][n], r[s].hasOwnProperty(n) && void 0 !== i && (t.isPlainObject(i) ? e[n] = t.isPlainObject(e[n]) ? o({}, e[n], i) : o({}, i) : e[n] = i);
        return e
    }

    function r(t, e) {
        function n() {
            this.constructor = t
        }

        for (var i in e) c.call(e, i) && (t[i] = e[i]);
        return n.prototype = e.prototype, t.prototype = new n, t.__super = e.prototype, t
    }

    /*!
     * SmartUE-4.0.0 core.js
     *
     * Copyright 2016 Huawei Technology, UCD Center
     * http://interface/smartue
     */
    var s = window.UCD || (window.UCD = { Core: t });
    var a = document, u = Array.prototype.slice, c = Object.prototype.hasOwnProperty, p = Object.prototype.toString, d = 0;
    var h = s.uuid = function (t) {
        return (t || "") + ++d
    };
    s.keyCodes = {
        BACKSPACE: 8,
        COMMA: 188,
        DELETE: 46,
        DOWN: 40,
        END: 35,
        ENTER: 13,
        ESCAPE: 27,
        HOME: 36,
        LEFT: 37,
        PAGE_DOWN: 34,
        PAGE_UP: 33,
        PERIOD: 190,
        RIGHT: 39,
        SPACE: 32,
        TAB: 9,
        UP: 38
    };
    var g = ".ucd.drag";
    var l = s.Events = {
        isPad: "ontouchstart" in window,
        mouse: {
            DOWN: "mousedown", MOVE: "mousemove", UP: "mouseup", getEvent: function (t) {
                return t
            }
        },
        touch: {
            DOWN: "touchstart", MOVE: "touchmove", UP: "touchend", getEvent: function (t) {
                var e = t.originalEvent.touches;
                return e.length ? e[0] : t
            }
        }
    };
    return t.extend(l, l.isPad ? l.touch : l.mouse), s.bindDragEvent = e, s.NS_SVG = "http://www.w3.org/2000/svg", s.NS_XLINK = "http://www.w3.org/1999/xlink", s.support = {}, s.support.SVG = !!a.createElementNS && !!a.createElementNS(s.NS_SVG, "svg").createSVGRect, s.support.SMIL = !!a.createElementNS && /SVGAnimate/.test(p.call(a.createElementNS(s.NS_SVG, "animate"))), s.support.VML = !s.support.SVG, i(s.support), t.cleanData = function (e) {
        return function (n) {
            var i, o, r;
            for (r = 0; null != (o = n[r]); r++)try {
                i = t._data(o, "events"), i && i.remove && t(o).triggerHandler("remove")
            } catch (s) {
            }
            e(n)
        }
    }(t.cleanData), s.Widget = function () {
    }, s.Widget.prototype = {
        widgetName: "widget",
        defaultElement: "<div>",
        options: { disabled: !1, create: null },
        _createWidget: function (e, n) {
            t.isPlainObject(e) && (n = e, e = null), e = t(e || this.defaultElement)[0], this.element = t(e), this.uuid = h(), this.eventNamespace = "." + this.widgetName + this.uuid, this.bindings = t(), e !== this && (t.data(e, this.widgetName, this), this._on(!0, this.element, {
                remove: function (t) {
                    t.target === e && this.destroy()
                }
            }), this.document = t(e.style ? e.ownerDocument : e.document || e), this.window = t(this.document[0].defaultView || this.document[0].parentWindow)), this.options = o({}, this.options, this._getCreateOptions(), n), this._create(), this._trigger("create", null, this._getCreateEventData()), s.ChangeDetector && (this._changeDetector = new s.ChangeDetector(n)), this._init()
        },
        _getCreateOptions: t.noop,
        _getCreateEventData: function () {
            return this
        },
        _create: t.noop,
        _init: t.noop,
        destroy: function () {
            this._destroy(), this.element.unbind(this.eventNamespace).removeData(this.widgetName), this.widget().unbind(this.eventNamespace), this.bindings.unbind(this.eventNamespace)
        },
        _destroy: t.noop,
        widget: function () {
            return this.element
        },
        option: function (e, n) {
            if (t.isPlainObject(e)) this._setOptions(e); else {
                if (void 0 === n) return this.options[e];
                this._setOption(e, n)
            }
            return this
        },
        _setOptions: function (t) {
            var e;
            for (e in t) this._setOption(e, t[e]);
            return this
        },
        _setOption: function (t, e) {
            return this.options[t] = e, this
        },
        disable: function (t) {
            this.option("disabled", t !== !1)
        },
        _on: function (e, n, i) {
            var o, r = this;
            "boolean" != typeof e && (i = n, n = e, e = !1), i ? (n = o = t(n), this.bindings = this.bindings.add(n)) : (i = n, n = this.element, o = this.widget()), t.each(i, function (i, s) {
                function a() {
                    return e || r.options.disabled !== !0 && !t(this).hasClass("ucd-state-disabled") ? ("string" == typeof s ? r[s] : s).apply(r, arguments) : !1
                }

                "string" != typeof s && (a.guid = s.guid = s.guid || a.guid || t.guid++);
                var u = i.match(/^([\w:-]*)\s*(.*)$/), c = u[1] + r.eventNamespace, p = u[2];
                p ? o.delegate(p, c, a) : n.bind(c, a)
            })
        },
        _off: function (e, n) {
            n = (n || "").split(" ").join(this.eventNamespace + " ") + this.eventNamespace, e.unbind(n).undelegate(n), this.bindings = t(this.bindings.not(e).get())
        },
        _delay: function (t, e) {
            function n() {
                return ("string" == typeof t ? i[t] : t).apply(i, arguments)
            }

            var i = this;
            return setTimeout(n, e || 0)
        },
        _trigger: function (e, n, i) {
            var o, r, s = this.options[e];
            if (i = void 0 === i ? {} : i, n = t.Event(n), n.type = e.toLowerCase(), n.target = this.element[0], r = n.originalEvent) for (o in r) o in n || (n[o] = r[o]);
            return this.element.trigger(n, i), !(t.isFunction(s) && s.apply(this.element[0], [n].concat(i)) === !1 || n.isDefaultPrevented())
        }
    }, s.require = function (t) {
        var e = s[t];
        if (!e) throw new Error("module " + t + " not found");
        return e
    }, s.registerWidget = function (e, n, i) {
        function a(t, e) {
            arguments.length && this._createWidget(t, e)
        }

        i || (i = n, n = "Widget");
        var u = s.require(n), c = t.isFunction(i) ? i(u.prototype, u, e) : i;
        return r(a, u), a.version = c.version, t.extend(a.prototype, c), a.prototype.options = o({}, u.prototype.options, c.options), a.prototype.widgetName = e, s[e] = a, a
    }, s
});
//# sourceMappingURL=core.min.js.map

// pager
/*!function (e, t) {
 "function" == typeof define && define.amd ? define(["jquery", "./core.js"], t) : "object" == typeof exports ? module.exports = t(require("jquery"), require("./core.js")) : e.UCD.Pager = t(e.jQuery, e.UCD)
 }(this, function (e, t) {
 return t.registerWidget("Pager", function (s) {
 var a = '<li class="ucd-pager-ellipsis"><span>...</span></li>';
 var i = {
 generate: function (e, t, s, a) {
 var i = [];
 for (var n = e; t >= n; n++)i.push(s.call(a, n, e, t));
 return i.join("")
 }, buildList: function (e, t, s) {
 return i.generate(e, t, function (e) {
 return ['<li class="ucd-pager-page', e === s ? " active" : "", '"><a href="#page-', e, '">', e, "</a></li>"].join("")
 })
 }, build: function (e, t, s, n) {
 if (s > t) return i.buildList(1, t, e);
 var o = [];
 if (s > t && (s = t), s > e) o.push(i.buildList(1, s, e)), n > 0 && t - n + 1 > s && o.push(a, i.buildList(t - n + 1, t, e)); else if (e > t - s + 1) n > 0 && t - s + 1 > n && o.push(i.buildList(1, n, e), a), o.push(i.buildList(t - s + 1, t, e)); else {
 var r = Math.floor(s / 2), g = s - r;
 n > 0 && e - r > n && o.push(i.buildList(1, n, e), a), o.push(i.buildList(e - r, e + g - 1, e)), n > 0 && t - n + 1 > e + g - 1 && o.push(a, i.buildList(t - n + 1, t, e))
 }
 return o.join("")
 }, buildDroplistData: function (e, t) {
 var s, a = [];
 for (var i = 0, n = e.length; n > i; i++)s = {}, s.text = s.value = e[i], s.value === t && (s.selected = !0), a.push(s);
 return a
 }, buildIconButton: function (e) {
 return ['<li class="ucd-pager-btn ucd-pager-', e, '"><span class="ucd-icon ucd-icon-', e, '"></span></li>'].join("")
 }
 };
 return {
 options: {
 count: 0,
 pagesize: 10,
 visiblePages: 8,
 edgePages: 1,
 page: 1,
 pageChange: null,
 sizes: [],
 formatCount: function (e) {
 return "共" + e + "条"
 },
 showCount: !1,
 showGoto: !0,
 showFirst: !1,
 showLast: !1,
 showPrev: !0,
 showNext: !0
 }, refresh: function () {
 var e = this.element, t = this.options;
 this._totalPages = Math.ceil(this._count / this._pagesize), this._page > this._totalPages && (this._page = this._totalPages);
 var s = [t.showFirst ? i.buildIconButton("first") : "", t.showPrev ? i.buildIconButton("prev") : "", i.build(this._page, this._totalPages, t.visiblePages, t.edgePages), t.showNext ? i.buildIconButton("next") : "", t.showLast ? i.buildIconButton("last") : ""].join("");
 e.children(".ucd-pager-pages").html(s), t.showFirst && e.find(".ucd-pager-first").toggleClass("disabled", 1 === this._page), t.showLast && e.find(".ucd-pager-last").toggleClass("disabled", this._page === this._totalPages), t.showPrev && e.find(".ucd-pager-prev").toggleClass("disabled", 1 === this._page), t.showNext && e.find(".ucd-pager-next").toggleClass("disabled", this._page === this._totalPages)
 }, setPageSize: function (e) {
 return this._pagesize = e, this
 }, setCount: function (e) {
 return this._count = e, this
 }, getPage: function () {
 return this._page
 }, setPage: function (e) {
 return e = parseInt(e, 10), isNaN(e) ? this : (this._updatePage(e), this)
 }, _create: function () {
 s._create.call(this);
 var a = this.element, n = this.options, o = n.sizes && n.sizes.length;
 var r = [o ? '<span class="ucd-pager-sizes"></span>' : "", n.showCount ? '<span class="ucd-pager-count"></span>' : "", '<ul class="ucd-pager-pages"></ul>', n.showGoto ? '<span class="ucd-pager-goto">跳转 <input type="text" class="ucd-pager-goto-page"><button class="ucd-pager-trigger"></button></span>' : ""];
 a.addClass("ucd-pager").append(r.join("")), o && t.Droplist && (this._pageSizes = new t.Droplist(this.element.find(".ucd-pager-sizes"), {
 dropdownClassName: "ucd-pager-sizes-options",
 data: i.buildDroplistData(n.sizes, n.pagesize),
 change: e.proxy(this._onPageSizeChange, this)
 })), n.showCount && this.element.children(".ucd-pager-count").html(n.formatCount ? n.formatCount(n.count) : n.count), this._setupEvents(), this.setCount(n.count).setPageSize(n.pagesize).setPage(n.page), n.disabled && this._toggleDisable()
 }, _setOption: function (e, t) {
 s._setOption.call(this, e, t), "disabled" === e && this._toggleDisable(t)
 }, _setupEvents: function () {
 var e = this.options, t = { "click .ucd-pager-page>a": "_gotoPage" };
 e.showGoto && (t["keyup .ucd-pager-goto-page"] = "_onGoto", t["click .ucd-pager-trigger"] = "_confirmGoto"), (e.showFirst || e.showLast || e.showPrev || e.showNext) && (t["click .ucd-pager-btn"] = "_navPage"), this._on(t)
 }, _navPage: function (t) {
 var s, a = e(t.target).closest(".ucd-pager-btn"), i = a.is(".ucd-pager-prev"), n = a.is(".ucd-pager-next"), o = a.is(".ucd-pager-first"), r = a.is(".ucd-pager-last");
 i || n ? s = this._page + (i ? -1 : 1) : o ? s = 1 : r && (s = this._totalPages), s && this._updatePage(s, !0)
 }, _gotoPage: function (t) {
 t.preventDefault(), this._updatePage(parseInt(e(t.target).text(), 10), !0)
 }, _onPageSizeChange: function (e, t) {
 this.setPageSize(parseInt(t.selected, 10)), this.refresh()
 }, _onGoto: function (s) {
 if (s.which !== t.keyCodes.ENTER) return !1;
 var a = e(s.target), i = e(s.target).val();
 this._updatePage(parseInt(i, 10), !0), i != this._page && a.val(this._page)
 }, _confirmGoto: function () {
 var e = this.element.find(".ucd-pager-goto-page"), t = e.val();
 this._updatePage(parseInt(t, 10), !0), t != this._page && e.val(this._page)
 }, _updatePage: function (e, t) {
 isNaN(e) || this._page === e || (1 > e ? e = 1 : e > this._totalPages && (e = this._totalPages), e !== this._page && (this._page = e, this.refresh(), t && this._trigger("pageChange", null, e)))
 }, _toggleDisable: function (e) {
 var t = this.element, s = e !== !1;
 t.toggleClass("disabled", s), t.find(".ucd-pager-goto-page").prop("disabled", s), t.find(".ucd-pager-trigger").prop("disabled", s), this._pageSizes && this._pageSizes.disable(s)
 }
 }
 }), t.Pager
 });*/
//# sourceMappingURL=Pager.min.js.map

// droplist
!function (t, e) {
    "function" == typeof define && define.amd ? define(["jquery", "./core.js"], e) : "object" == typeof exports ? module.exports = e(require("jquery"), require("./core.js")) : t.UCD.Droplist = e(t.jQuery, t.UCD)
}(this, function (t, e) {
    return e.registerWidget("Droplist", function (i) {
        var s = {
            findSelected: function (t) {
                var e = [];
                for (var i = 0, s = t ? t.length : 0; s > i; i++)t[i].selected === !0 && e.push(String(t[i].text));
                return e
            }, firstOrDefault: function (e, i, s) {
                var o = s;
                return t.each(e, function () {
                    return i(this) ? (o = this, !1) : void 0
                }), o
            }, simpleHTML: function (e, i, s) {
                var o = t.map(s || {}, function (t, e) {
                    if ("boolean" == typeof t) return t === !0 ? e : void 0;
                    if (void 0 !== t) return e + '="' + t + '"'
                }).join(" ");
                return ["<", e, " ", o, ">", i, "</" + e + ">"].join("")
            }, intAttr: function (t, e, i) {
                var s = t.attr(e);
                return void 0 === s ? i : parseInt(s, 10)
            }, hasAttr: function (t, e) {
                var i = t.attr(e);
                return void 0 !== i
            }, parseNativeSelect: function (e) {
                var i, o = { autofocus: !1, required: !1, disabled: !1, multiple: !1, size: 0, data: [] }, n = o.data;
                return t.extend(o, {
                    autofocus: s.hasAttr(e, "autofocus"),
                    disabled: s.hasAttr(e, "disabled"),
                    multiple: s.hasAttr(e, "multiple"),
                    size: s.intAttr(e, "size", 0)
                }), e.find("option").each(function () {
                    var e = t(this), o = e.parent();
                    i = {
                        disabled: s.hasAttr(e, "disabled"),
                        selected: s.hasAttr(e, "selected"),
                        value: e.attr("value"),
                        text: e.text()
                    }, o.is("optgroup") && (i.group = o.attr("label"), t.extend(i, { disabled: s.hasAttr(o, "disabled") })), n.push(i)
                }), o
            }, buildOption: function (t, e) {
                var i = s.simpleHTML("span", t.text);
                return e && (i = '<span class="ucd-icon-checkbox"></span>' + i), s.simpleHTML("li", i, {
                    "class": "ucd-droplist-option",
                    "data-value": t.value,
                    disabled: t.disabled,
                    selected: t.selected
                })
            }, buildOptions: function (e, i) {
                var o, n = [], l = {};
                return e && e.length && e[0].group && t.each(e, function () {
                    this.group && (o = l[this.group] = l[this.group] || [], o.push(this))
                }), o ? t.each(l, function (e, o) {
                    var l = t.map(o, function (t) {
                        return s.buildOption(t, i)
                    });
                    n.push(s.simpleHTML("li", e + s.simpleHTML("ul", l.join("")), { "class": "ucd-droplist-optgroup" }))
                }) : t.each(e, function () {
                    n.push(s.buildOption(this, i))
                }), n.join("")
            }
        };
        var o = '<div class="ucd-droplist"><div class="ucd-droplist-header"> <input class="ucd-droplist-input" type="text" placeholder="请选择"> <span class="ucd-droplist-trigger"><span></span></span></div></div>';
        return {
            options: {
                droplistClassName: null,
                allowInput: !0,
                autofocus: !1,
                required: !1,
                disabled: !1,
                multiple: !1,
                size: 0,
                valueSeperator: /\s*[\uFF0C,]\s*/,
                valueJoin: ", ",
                filterMinLength: 3,
                notfoundTemplate: '<div class="ucd-droplist-notfound">Not found</div>',
                dropdownClassName: null,
                data: [],
                placeholder: null
            }, _create: function () {
                i._create.call(this);
                var e = this.options, n = this.$el = this.element;
                if (n.is("select")) {
                    this._nativeSelect = n;
                    var l = s.parseNativeSelect(this._nativeSelect);
                    t.extend(this.options, l), n.hide(), n = this.$el = t(o).insertAfter(n)
                } else n.append(o), n = this.$el = n.find(".ucd-droplist");
                this.$header = n.find(".ucd-droplist-header"), this.$input = this.$header.find(".ucd-droplist-input"), this.$trigger = this.$header.find(".ucd-droplist-trigger"), n.toggleClass("multiple", e.multiple), this._toggleDisable(e.disabled), this._toggleAllowInput(e.allowInput), e.droplistClassName && n.addClass(e.droplistClassName), this._setupEvents();
                var d = s.findSelected(e.data);
                d && d.length && this.select(d)
            }, _destroy: function () {
                this.element.is("select") ? (this.element.show(), this.$el.remove()) : this.element.empty()
            }, _toggleDisable: function (t) {
                this.$el.toggleClass("disabled", t), this.$input.prop("disabled", t)
            }, _toggleAllowInput: function (t) {
                this.$input.prop("readonly", !t)
            }, _setupEvents: function () {
                this._nativeSelect && this._on(this._nativeSelect, {
                    focus: function () {
                        this.$input.focus()
                    }
                }), this._on(this.$input, {
                    focus: "_focusValue",
                    click: "_focusOrOpen",
                    change: "_changeValue",
                    input: "_filterValue",
                    keydown: "_handleKey"
                }), this._on(this.$trigger, { click: "_toggleDropdown" }), this._on(this.window, {
                    scroll: "_adjustPosition",
                    resize: "_adjustPosition"
                })
            }, _adjustPosition: function () {
                this.isOpen() && this.close()
            }, _focusValue: function () {
            }, _focusOrOpen: function () {
                this.$input.is(":focus") ? this.open() : this.$input.focus()
            }, _handleKey: function (t) {
                var i = t.which;
                i === e.keyCodes.ENTER && this._toggleDropdown()
            }, _changeValue: function () {
                this._filterEnd(), this._updateSelection(this.$input.val())
            }, _filterValue: function () {
                var e = this.$input.val();
                if (e && !(e.length < this.options.filterMinLength)) {
                    var i = !1;
                    this.$options.children().each(function () {
                        var s = t(this), o = s.text(), n = -1 === o.indexOf(e);
                        s.toggleClass("ucd-droplist-notmatch", n), n || (i = !0)
                    }), this._toggleNotFound(!i)
                }
            }, _filterEnd: function () {
                var t = this;
                setTimeout(function () {
                    var e = "ucd-droplist-notmatch";
                    t.$options.children("." + e).removeClass(e), t._toggleNotFound(!1)
                }, 1)
            }, _toggleNotFound: function (t) {
                var e = this.$dropdown.children(".ucd-droplist-notfound");
                t ? e.length || this.$dropdown.prepend(this.options.notfoundTemplate) : e.length && e.remove()
            }, _toggleDropdown: function () {
                this.isOpen() ? this.close() : this.open()
            }, _selectOption: function (e) {
                var i = this.options, s = t(e.target), o = s.closest(".ucd-droplist-option");
                if (o.is(":disabled") || o.is(".disabled")) return !1;
                if (i.multiple) o.toggleClass("selected"), o.children(".ucd-icon-checkbox").toggleClass("checked"); else {
                    o.addClass("selected");
                    var n = o.siblings(".selected").removeClass("selected");
                    o.children(".ucd-icon-checkbox").addClass("checked"), n.children(".ucd-icon-checkbox.checked").removeClass("checked")
                }
                this._updateValue(e.ctrlKey)
            }, _updateSelection: function (t) {
                t && 0 !== t.length ? this.toggle(t.trim().split(this.options.valueSeperator), !0) : this.unselectAll()
            }, _updateValue: function (e) {
                this.$input.val(this.getSelected(!0).join(this.options.valueJoin));
                var i = this.getSelected();
                this._nativeSelect && this._nativeSelect.children("option").each(function () {
                    var e = this.value;
                    this.selected = i.length && -1 !== t.inArray(e, i)
                }), this._trigger("change", null, { selected: this.options.multiple ? i : i[0] }), e || (this.close(), this.$input.focus())
            }, _tryClose: function (e) {
                var i = t(e.target), s = i.closest(".ucd-droplist-content");
                this.$dropdown && s.is(this.$dropdown) || this.close()
            }, _toggle: function (t, e) {
                var i = e ? "addClass" : "removeClass";
                var s = t[i]("selected");
                this.options.multiple && s.children(".ucd-icon-checkbox")[i]("checked");
                this._updateValue(false);
            }, _setOption: function (t, e) {
                if (i._setOption.call(this, t, e), "data" === t && this.$options) {
                    var o = this.options, n = s.buildOptions(o.data, o.multiple);
                    this.$options.html(n)
                } else "disabled" === t ? this._toggleDisable(e) : "allowInput" === t && this._toggleAllowInput(e);
                return this
            }, setData: function (t) {
                this.option("data", t)
            }, getSelected: function (e) {
                if (!this.$options) {
                    this._renderDropdown();
                }
                ;
                return this.$options.find(".selected").map(function () {
                    return e ? t(this).text() : t(this).data("value")
                }).toArray()
            }, toggleAll: function (t) {
                if (!this.$dropdown) {
                    this._renderDropdown();
                }
                ;
                this._toggle(this.$options.children(), t)
            }, selectAll: function () {
                this.toggleAll(!0)
            }, unselectAll: function () {
                this.toggleAll(!1)
            }, toggle: function (e, i) {
                var s = t.isArray(e);
                if (!s || e.length) {
                    var o = function () {
                        var i = t(this).text();
                        return s ? -1 !== t.inArray(i, e) : i === e
                    };
                    this.$dropdown || this._renderDropdown();
                    var n = this.$options.children();
                    this._toggle(n.filter(o), i), this._toggle(n.not(o), !i), this._updateValue(!0)
                }
            }, select: function (t) {
                this.toggle(t, !0)
            }, unselect: function (t) {
                this.toggle(t, !1)
            }, isOpen: function () {
                return this.$el.hasClass("open")
            }, _renderDropdown: function () {
                var e = this.options;
                if (!this.$dropdown) {
                    this.$dropdown = t('<div class="ucd-droplist-content"></div>').appendTo(this.document[0].body), e.dropdownClassName && this.$dropdown.addClass(e.dropdownClassName);
                    var i = s.buildOptions(e.data, e.multiple);
                    this.$options = t('<ul class="ucd-droplist-options"></ul>').html(i).appendTo(this.$dropdown), this._on(this.$dropdown, { "click .ucd-droplist-option": "_selectOption" }), this._updatePosition()
                }
            }, _updatePosition: function () {
                var t = this.$el, e = t.offset(), i = t.height(), s = this.document.height(), o = this.$dropdown.height(), n = e.top + i, l = n + o > s && e.top >= o;
                return this.$dropdown.css({ width: t.css("width"), left: e.left, top: l ? e.top - o : n }), l
            }, open: function () {
                this.$dropdown || this._renderDropdown();
                var t = this._updatePosition();
                this.$el.addClass("open").toggleClass("open-up", t), this.$dropdown.addClass("open").toggleClass("open-up", t), this._on(this.document, {
                    mousedown: "_tryClose",
                    mousewheel: "_tryClose"
                })
            }, close: function () {
                this.$el.removeClass("open open-up"), this.$dropdown.removeClass("open open-up"), this._off(this.document, "mousedown mousewheel")
            }
        }
    }), e.Droplist
});
//# sourceMappingURL=Droplist.min.js.map

/***
 * 复选框、单选框、
 ***/
Array.prototype.removeByValue = function (val) {
    //删除数组中的某一项
    for (var i = 0; i < this.length; i++) {
        if (this[i] == val) {
            this.splice(i, 1);
            break;
        }
    }
};
String.prototype.trim = function () {
    // 去掉字符串两端空白
    return this.replace(/(^\s*)|(\s*$)/g, "");
}
var RemWidth = parseFloat($('html').css('font-size'));
if (!(RemWidth % 1)) { RemWidth = parseInt(RemWidth) };
var common = {
    into: function () {
        //单复选框
        this.checkboxAndradio();
    },

    /**** 单复选框样式跨平台统一 ****/
    checkboxAndradio: function (id) {
        common.id = id + ' ' ? id : '';
        common.checkboxAndRadioStates();
        common.checkboxAndRadioClick();
    },
    checkboxAndRadioStates: function (fu) {
        var _this = common;
        _this.time = setTimeout(function () {
            // 判断id是否存在，确定查找范围
            if (_this.id) {
                var $inputBox = $('#' + _this.id + ' input[type="checkbox"],#' + _this.id + ' input[type="radio"]');
            } else {
                var $inputBox = $('input[type="checkbox"],input[type="radio"]');
            }
            $inputBox.each(function (i, e) {
                // 循环查找到相应的单复选框，并过滤掉影藏的部分
                if ($(this).css('display') != 'none') {

                    if ($(this).attr('type') == 'checkbox') {
                        //复选框

                        /**
                         * 新建 class="checkboxInput" 的label标签，并把当前复选框包裹到当前label中.
                         * 若当前复选框其父及元素就是 class="checkboxInput" 的label标签，则跳过，并删除lable的class值 disabled与active、若存在此类名
                         * */
                        if (!$(this).parent().is('.checkboxInput')) {
                            $(this).wrap('<label class="checkboxInput"></label>');
                        } else {
                            $(this).parent().css({ 'display': 'inline-block' }).removeClass('disabled active');
                        };

                        // 复选框为选中状态其父及元素lable添加 active class值
                        if ($(this).prop('checked')) {
                            $(this).parent().addClass('active');
                        };
                        // 复选框为disabled状态其父及元素lable添加 disabled class值
                        if ($(this).prop('disabled')) {
                            $(this).parent().addClass('disabled');
                        };
                    } else {
                        //单选框

                        if (!$(this).parent().is('.radioInput')) {
                            $(this).wrap('<label class="radioInput"></label>');
                        } else {
                            $(this).parent().removeClass('disabled active');
                        };

                        /**
                         * 单选框被选中时其父及元素lable添加active class值，并且全局单选框name与其一致的单选框父元素label 删掉 active class值
                         * 单选框为 disabled 态时其父及元素lable添加disabled class值
                         * */
                        if ($(this).prop('checked')) {
                            $('input[type="radio"][name="' + $(this).attr('name') + '"]').parent('.radioInput').removeClass('active');
                            $(this).parent('.radioInput').addClass('active');
                        };
                        if ($(this).prop('disabled')) {
                            $(this).parent().addClass('disabled');
                        }
                    };

                    if ($(this).hasClass('min')) {
                        $(this).parent().addClass('min');
                    } else { $(this).parent().removeClass('min'); }

                } else {
                    // 单复选框隐藏时也使其父元素label也隐藏
                    if ($(this).parent().is('.checkboxInput') || $(this).parent().is('.radioInput')) {
                        $(this).parent().css({ 'display': 'none' });
                    }
                }

            });

            //再次运行确保在新加入input时能有 change 事件
            common.checkboxAndRadioClick();

            $('.checkboxInput,.radioInput').each(function (index, el) {
                $(this).unbind('click');
                $(this).click(function (e) {
                    e.stopPropagation();
                })
            })
        }, 30)

    },
    checkboxAndRadioClick: function () {
        var _this = common;
        // 判断id是否存在，确定查找范围
        if (_this.id) {
            var $inputBox = $('#' + _this.id + ' input[type="checkbox"],#' + _this.id + ' input[type="radio"]');
        } else {
            var $inputBox = $('input[type="checkbox"],input[type="radio"]');
        }

        $inputBox.each(function (i, e) {
            $(this).unbind('change', common.checkboxAndRadioStates).bind('change', common.checkboxAndRadioStates);
        })

    },
    /**** 单复选框样式跨平台统一 *end*/
};
/***
 * 弹窗控件
 ***/
var AUI = AUI || {};
/***
 * 支持检测浏览器及版本信息
 * Chrome/Safari/Firefox/IE
 ***/
(function (window, $, NS, undefined) {
    "use strict";
    NS.Dialog = function (obj, opt) {
        this.options = {
            obj: obj,
            position: 'center'
        }

        var that = this,
            options = this.options,
            $dialog = $('<div class="aui-dialog"></div>'),
            $main = $('<div class="aui-dialog-main hidden"></div>'),
            $mask = $('<div class="aui-dialog-mask"></div>'),
            $close = '<div class="dialog-close-btn">&#10006;</div>',
            $content, mainWid, mainHei, position;

        _setOption(opt);

        if (options.className) {
            $dialog.addClass(options.className);
        }

        $main.append($close);
        $dialog.append($main);

        if (options.model) {
            $dialog.append($mask);
        }

        if ($(obj).length > 0) {
            $content = $(obj).clone();
            $content.removeClass('aui-dialog-layer');
            $main.append($content);
        }

        $dialog.appendTo('body');
        _bindEvent();
        _setStyle();

        // 初始化对话框z-index
        that.zIndex.max = options.zIndex || 100;

        function _setOption(key, val) {
            if (typeof key === 'object') {
                var opt = key;
                for (var i in opt) {
                    that.options[i] = opt[i];
                }
            } else {
                this.options[key] = val
            }
        }
        function _setZIndex() {
            var z = $main.css('zIndex');
            if (z === 'auto' || Number(z) < that.zIndex.max - 1) {
                $mask.css('zIndex', that.zIndex.max);
                $main.css('zIndex', that.zIndex.max + 1);

                that.zIndex.max += 2;
            }
        }
        function _showDialog() {
            $main.removeClass('hidden');
            _setZIndex();
            if (position != options.position) {
                position = options.position;
                _setPosition(position);
            }
            if (!$dialog.hasClass('show')) {
                $dialog.addClass('show');
            } else {
                $dialog.addClass('shown');
                setTimeout(function () {
                    $dialog.removeClass('shown');
                }, 500);
            }

            if (!options.model && options.closeAfter && typeof options.closeAfter === 'number') {
                setTimeout(_closeDialog, options.closeAfter);
            }
            if (options.model == false) {
                $mask.remove()
            }
            if (options.model == true) {
                if ($dialog.find('.aui-dialog-mask').length == 0) {
                    $dialog.append($mask);
                }
            }

        }

        function _closeDialog() {
            var z = $main.css('zIndex');
            if (z == 'auto' || Number(z) == that.zIndex.max - 1) {
                that.zIndex.max -= 2;
            }

            $dialog.removeClass('show');
            setTimeout(function () {
                $main.addClass('hidden');
                $mask.css('zIndex', 0);
                $main.css('zIndex', 1);
            }, 300);
            options.onClose && typeof options.onClose === 'function' && options.onClose(that);
        }

        function _bindEvent() {
            $dialog.on('click', '.dialog-close-btn, .dialog-cancel', function (event) {
                _closeDialog();
                options.onCancel && typeof options.onCancel === 'function' && options.onCancel(that);
            });
            $dialog.on('click', '.dialog-ok', function (event) {
                _closeDialog();
                options.onOk && typeof options.onOk === 'function' && options.onOk(that);
            });
            $main.scrollUnique();
            $mask.scrollUnique();
        }

        function _setPosition(pos) {
            var win_width = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth,
                win_height = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight,
                l, t, r, b, ml, mt;
            if (pos === 'center' || pos === 'top' || pos === 'bottom') {
                ml = -1 * mainWid / 2;

                if (mainWid > win_width) {
                    l = ml = 0;
                }
            }

            if (pos === 'center' || pos === 'left' || pos === 'right') {
                mt = -1 * mainHei / 2;

                if (mainHei > win_height) {
                    t = mt = 0;
                }
            }

            if (pos === 'center') {
                b = "auto";
                r = "auto"
            }
            if (pos === 'top') {
                t = '80px';
                b = "auto";
                mt = 0;
            }
            if (pos === 'bottom') {
                t = 'auto';
                b = "80px";
                mt = 0;
            }
            if (pos === 'left') {
                l = '80px';
                r = 'auto';
                ml = 0;
            }
            if (pos === 'right') {
                l = 'auto';
                r = '80px';
                ml = 0;
            }

            $main.css({
                left: l,
                top: t,
                bottom: b,
                right: r,
                "marginLeft": ml + 'px',
                "marginTop": mt + 'px'
            });
        }
        function _setStyle() {
            // 设置对话框宽度
            if (options.width && Number(options.width)) {
                mainWid = options.width;
            } else {
                mainWid = $main.outerWidth();
            }
            // 设置对话框高度
            if (options.height && Number(options.height)) {
                mainHei = options.height;
            } else {
                mainHei = $main.outerHeight();
            }

            position = options.position;
            _setPosition(position);

            $main.css({
                width: options.width,
                height: options.height
            });

        }

        that.close = _closeDialog;
        that.show = _showDialog;
        that.setOptions = _setOption;
    }

    NS.Dialog.prototype.zIndex = {
        max: 100
    }

})(window, jQuery, AUI);

function createDialog(obj, opt) {
    var dialog;
    if (typeof obj === 'object') {
        opt = obj;
        obj = $('<div class="aui-dialog-layer requirement-dialog"></div>')
        if (opt.head) {
            obj.append('<div class="dialog-head"><h2 class="caption">' + opt.head + '</h2></div>')
        }
        if (opt.content) {
            obj.append('<div class="dialog-content">' + opt.content + '</div>')
        }

        opt.className = "aui-tip-dialog";

    }

    if ($(obj).length > 0) {
        dialog = new AUI.Dialog(obj, opt);
    }

    return dialog;
}

function isIE() { //ie?
    if (!!window.ActiveXObject || "ActiveXObject" in window) {
        return true;
    } else { return false; }
}

/*------------------------------*/
