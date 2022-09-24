(function(t) {
  function s(s) {
      for (var i, n, r = s[0], o = s[1], c = s[2], m = 0, u = []; m < r.length; m++) n = r[m], Object.prototype.hasOwnProperty.call(a, n) && a[n] && u.push(a[n][0]), a[n] = 0;
      for (i in o) Object.prototype.hasOwnProperty.call(o, i) && (t[i] = o[i]);
      d && d(s);
      while (u.length) u.shift()();
      return l.push.apply(l, c || []), e()
  }

  function e() {
      for (var t, s = 0; s < l.length; s++) {
          for (var e = l[s], i = !0, r = 1; r < e.length; r++) {
              var o = e[r];
              0 !== a[o] && (i = !1)
          }
          i && (l.splice(s--, 1), t = n(n.s = e[0]))
      }
      return t
  }
  var i = {},
      a = {
          app: 0
      },
      l = [];

  function n(s) {
      if (i[s]) return i[s].exports;
      var e = i[s] = {
          i: s,
          l: !1,
          exports: {}
      };
      return t[s].call(e.exports, e, e.exports, n), e.l = !0, e.exports
  }
  n.m = t, n.c = i, n.d = function(t, s, e) {
      n.o(t, s) || Object.defineProperty(t, s, {
          enumerable: !0,
          get: e
      })
  }, n.r = function(t) {
      "undefined" !== typeof Symbol && Symbol.toStringTag && Object.defineProperty(t, Symbol.toStringTag, {
          value: "Module"
      }), Object.defineProperty(t, "__esModule", {
          value: !0
      })
  }, n.t = function(t, s) {
      if (1 & s && (t = n(t)), 8 & s) return t;
      if (4 & s && "object" === typeof t && t && t.__esModule) return t;
      var e = Object.create(null);
      if (n.r(e), Object.defineProperty(e, "default", {
              enumerable: !0,
              value: t
          }), 2 & s && "string" != typeof t)
          for (var i in t) n.d(e, i, function(s) {
              return t[s]
          }.bind(null, i));
      return e
  }, n.n = function(t) {
      var s = t && t.__esModule ? function() {
          return t["default"]
      } : function() {
          return t
      };
      return n.d(s, "a", s), s
  }, n.o = function(t, s) {
      return Object.prototype.hasOwnProperty.call(t, s)
  }, n.p = "/";
  var r = window["webpackJsonp"] = window["webpackJsonp"] || [],
      o = r.push.bind(r);
  r.push = s, r = r.slice();
  for (var c = 0; c < r.length; c++) s(r[c]);
  var d = o;
  l.push([0, "chunk-vendors"]), e()
})({
  0: function(t, s, e) {
      t.exports = e("56d7")
  },
  "034f": function(t, s, e) {
      "use strict";
      e("85ec")
  },
  "1db9": function(t, s, e) {
      t.exports = e.p + "img/c1.2d2dcf21.jpg"
  },
  "215d": function(t, s) {
      t.exports = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMIAAAAyCAYAAAAOcwQoAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyZpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMDY3IDc5LjE1Nzc0NywgMjAxNS8wMy8zMC0yMzo0MDo0MiAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTUgKFdpbmRvd3MpIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjJDNTQ4NTM3REI5MDExRTlCNDhGQTIwRjNGQTc1N0EzIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjJDNTQ4NTM4REI5MDExRTlCNDhGQTIwRjNGQTc1N0EzIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6MkM1NDg1MzVEQjkwMTFFOUI0OEZBMjBGM0ZBNzU3QTMiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6MkM1NDg1MzZEQjkwMTFFOUI0OEZBMjBGM0ZBNzU3QTMiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz4FAS0XAAAJWElEQVR42uxd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"
  },
  2413: function(t, s, e) {
      t.exports = e.p + "img/coding_.e8413cbf.svg"
  },
  4541: function(t, s, e) {
      t.exports = e.p + "img/handshake.34250d54.svg"
  },
  4851: function(t, s, e) {
      t.exports = e.p + "img/c2.0a3b2b89.jpg"
  },
  "56d7": function(t, s, e) {
      "use strict";
      e.r(s);
      e("e260"), e("e6cf"), e("cca6"), e("a79d");
      var i = e("2b0e"),
          a = function() {
              var t = this,
                  s = t.$createElement,
                  e = t._self._c || s;
              return e("div", {
                  attrs: {
                      id: "app"
                  }
              }, [e("navbar"), e("home"), t._m(0)], 1)
          },
          l = [function() {
              var t = this,
                  s = t.$createElement,
                  e = t._self._c || s;
              return e("footer", {
                  staticClass: "gradient"
              }, [e("div", {
                  staticClass: "container-fluid text-center"
              }, [e("span", [t._v("Made by "), e("a", {
                  attrs: {
                      href: "https://horizontall.htb"
                  }
              }, [t._v("Horizontall.htb")])])])])
          }],
          n = e("bc3a"),
          r = e.n(n),
          o = function() {
              var t = this,
                  s = t.$createElement,
                  i = t._self._c || s;
              return i("div", [i("b-navbar", {
                  attrs: {
                      toggleable: "lg",
                      type: "light",
                      variant: "light"
                  }
              }, [i("b-container", [i("b-navbar-brand", {
                  attrs: {
                      href: "#"
                  }
              }, [i("a", {
                  attrs: {
                      href: "/"
                  }
              }, [i("img", {
                  attrs: {
                      src: e("cc09"),
                      alt: ""
                  }
              })])]), i("b-navbar-toggle", {
                  attrs: {
                      target: "nav-collapse"
                  }
              }), i("b-collapse", {
                  attrs: {
                      id: "nav-collapse",
                      "is-nav": ""
                  }
              }, [i("b-navbar-nav", {
                  staticClass: "ml-auto"
              }, [i("b-nav-item", {
                  attrs: {
                      href: "#"
                  }
              }, [t._v("Home")]), i("b-nav-item", {
                  attrs: {
                      href: "#"
                  }
              }, [t._v("Feature")]), i("b-nav-item", {
                  attrs: {
                      href: "#"
                  }
              }, [t._v("About")])], 1)], 1)], 1)], 1)], 1)
          },
          c = [],
          d = {},
          m = d,
          u = e("2877"),
          p = Object(u["a"])(m, o, c, !1, null, null, null),
          v = p.exports,
          g = function() {
              var t = this,
                  s = t.$createElement,
                  e = t._self._c || s;
              return e("div", [e("header", {
                  staticClass: "page-header gradient"
              }, [t._m(0), e("svg", {
                  attrs: {
                      xmlns: "http://www.w3.org/2000/svg",
                      viewBox: "0 0 1440 250"
                  }
              }, [e("path", {
                  attrs: {
                      fill: "#fff",
                      "fill-opacity": "1",
                      d: "M0,128L48,117.3C96,107,192,85,288,80C384,75,480,85,576,112C672,139,768,181,864,181.3C960,181,1056,139,1152,122.7C1248,107,1344,117,1392,122.7L1440,128L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"
                  }
              })])]), t._m(1), e("section", {
                  staticClass: "feature gradient"
              }, [e("svg", {
                  attrs: {
                      xmlns: "http://www.w3.org/2000/svg",
                      viewBox: "0 0 1440 320"
                  }
              }, [e("path", {
                  attrs: {
                      fill: "#fff",
                      "fill-opacity": "1",
                      d: "M0,224L48,213.3C96,203,192,181,288,154.7C384,128,480,96,576,117.3C672,139,768,213,864,208C960,203,1056,117,1152,101.3C1248,85,1344,139,1392,165.3L1440,192L1440,0L1392,0C1344,0,1248,0,1152,0C1056,0,960,0,864,0C768,0,672,0,576,0C480,0,384,0,288,0C192,0,96,0,48,0L0,0Z"
                  }
              })]), t._m(2), e("svg", {
                  attrs: {
                      xmlns: "http://www.w3.org/2000/svg",
                      viewBox: "0 0 1440 320"
                  }
              }, [e("path", {
                  attrs: {
                      fill: "#fff",
                      "fill-opacity": "1",
                      d: "M0,224L48,213.3C96,203,192,181,288,154.7C384,128,480,96,576,117.3C672,139,768,213,864,208C960,203,1056,117,1152,101.3C1248,85,1344,139,1392,165.3L1440,192L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"
                  }
              })])]), e("section", {
                  staticClass: "icons"
              }, [e("div", {
                  staticClass: "container"
              }, [e("div", {
                  staticClass: "row text-center"
              }, [e("div", {
                  staticClass: "col-md-4"
              }, [e("div", {
                  staticClass: "icon gradient mb-4"
              }, [e("svg", {
                  staticClass: "feather feather-layers",
                  attrs: {
                      xmlns: "http://www.w3.org/2000/svg",
                      width: "24",
                      height: "24",
                      viewBox: "0 0 24 24",
                      fill: "none",
                      stroke: "currentColor",
                      "stroke-width": "2",
                      "stroke-linecap": "round",
                      "stroke-linejoin": "round"
                  }
              }, [e("polygon", {
                  attrs: {
                      points: "12 2 2 7 12 12 22 7 12 2"
                  }
              }), e("polyline", {
                  attrs: {
                      points: "2 17 12 22 22 17"
                  }
              }), e("polyline", {
                  attrs: {
                      points: "2 12 12 17 22 12"
                  }
              })])]), e("h3", [t._v("Built for developers")]), e("p", [t._v(" Our customizable, block-based build system makes creating your next project fast and easy! ")])]), e("div", {
                  staticClass: "col-md-4"
              }, [e("div", {
                  staticClass: "icon gradient mb-4"
              }, [e("svg", {
                  staticClass: "feather feather-smartphone",
                  attrs: {
                      xmlns: "http://www.w3.org/2000/svg",
                      width: "24",
                      height: "24",
                      viewBox: "0 0 24 24",
                      fill: "none",
                      stroke: "currentColor",
                      "stroke-width": "2",
                      "stroke-linecap": "round",
                      "stroke-linejoin": "round"
                  }
              }, [e("rect", {
                  attrs: {
                      x: "5",
                      y: "2",
                      width: "14",
                      height: "20",
                      rx: "2",
                      ry: "2"
                  }
              }), e("line", {
                  attrs: {
                      x1: "12",
                      y1: "18",
                      x2: "12.01",
                      y2: "18"
                  }
              })])]), e("h3", [t._v("Modern responsive design")]), e("p", {
                  staticClass: "mb-0"
              }, [t._v(" Featuring carefully crafted, mobile-first components, your end product will function beautifully on any device! ")])]), e("div", {
                  staticClass: "col-md-4"
              }, [e("div", {
                  staticClass: "icon gradient mb-4"
              }, [e("svg", {
                  staticClass: "feather feather-code",
                  attrs: {
                      xmlns: "http://www.w3.org/2000/svg",
                      width: "24",
                      height: "24",
                      viewBox: "0 0 24 24",
                      fill: "none",
                      stroke: "currentColor",
                      "stroke-width": "2",
                      "stroke-linecap": "round",
                      "stroke-linejoin": "round"
                  }
              }, [e("polyline", {
                  attrs: {
                      points: "16 18 22 12 16 6"
                  }
              }), e("polyline", {
                  attrs: {
                      points: "8 6 2 12 8 18"
                  }
              })])]), e("h3", [t._v("Complete documentation")]), e("p", {
                  staticClass: "mb-0"
              }, [t._v(" All of the layouts, page sections, components, and utilities are fully covered in this products docs. ")])])])])]), e("section", {
                  staticClass: "gallery"
              }, [e("svg", {
                  attrs: {
                      xmlns: "http://www.w3.org/2000/svg",
                      viewBox: "0 0 1440 160"
                  }
              }, [e("path", {
                  attrs: {
                      fill: "#fff",
                      "fill-opacity": "1",
                      d: "M0,128L120,128C240,128,480,128,720,122.7C960,117,1200,107,1320,101.3L1440,96L1440,0L1320,0C1200,0,960,0,720,0C480,0,240,0,120,0L0,0Z"
                  }
              })]), t._m(3), e("svg", {
                  attrs: {
                      xmlns: "http://www.w3.org/2000/svg",
                      viewBox: "0 0 1440 320"
                  }
              }, [e("path", {
                  attrs: {
                      fill: "#fff",
                      "fill-opacity": "1",
                      d: "M0,128L120,128C240,128,480,128,720,122.7C960,117,1200,107,1320,101.3L1440,96L1440,320L1320,320C1200,320,960,320,720,320C480,320,240,320,120,320L0,320Z"
                  }
              })])]), e("section", {
                  staticClass: "services gradient"
              }, [e("svg", {
                  attrs: {
                      xmlns: "http://www.w3.org/2000/svg",
                      viewBox: "0 0 1440 220"
                  }
              }, [e("path", {
                  attrs: {
                      fill: "#fff",
                      "fill-opacity": "1",
                      d: "M0,96L34.3,106.7C68.6,117,137,139,206,122.7C274.3,107,343,53,411,53.3C480,53,549,107,617,117.3C685.7,128,754,96,823,96C891.4,96,960,128,1029,154.7C1097.1,181,1166,203,1234,202.7C1302.9,203,1371,181,1406,170.7L1440,160L1440,0L1405.7,0C1371.4,0,1303,0,1234,0C1165.7,0,1097,0,1029,0C960,0,891,0,823,0C754.3,0,686,0,617,0C548.6,0,480,0,411,0C342.9,0,274,0,206,0C137.1,0,69,0,34,0L0,0Z"
                  }
              })]), t._m(4), e("svg", {
                  attrs: {
                      xmlns: "http://www.w3.org/2000/svg",
                      viewBox: "0 0 1440 210"
                  }
              }, [e("path", {
                  attrs: {
                      fill: "#fff",
                      "fill-opacity": "1",
                      d: "M0,96L34.3,106.7C68.6,117,137,139,206,122.7C274.3,107,343,53,411,53.3C480,53,549,107,617,117.3C685.7,128,754,96,823,96C891.4,96,960,128,1029,154.7C1097.1,181,1166,203,1234,202.7C1302.9,203,1371,181,1406,170.7L1440,160L1440,320L1405.7,320C1371.4,320,1303,320,1234,320C1165.7,320,1097,320,1029,320C960,320,891,320,823,320C754.3,320,686,320,617,320C548.6,320,480,320,411,320C342.9,320,274,320,206,320C137.1,320,69,320,34,320L0,320Z"
                  }
              })])]), t._m(5)])
          },
          f = [function() {
              var t = this,
                  s = t.$createElement,
                  i = t._self._c || s;
              return i("div", {
                  staticClass: "container"
              }, [i("div", {
                  staticClass: "row align-items-center justify-content-center"
              }, [i("div", {
                  staticClass: "col-md-5"
              }, [i("h2", [t._v("Build website using HT")]), i("p", [t._v(" It's crafted with the latest trend of design & coded with all modern approaches. It's a robust & multi-dimensional usable template. ")]), i("button", {
                  staticClass: "btn btn-outline-success btn-lg",
                  attrs: {
                      type: "button"
                  }
              }, [t._v(" Read more ")]), i("button", {
                  staticClass: "btn btn-outline-warning btn-lg",
                  attrs: {
                      type: "button"
                  }
              }, [t._v(" Play video ")])]), i("div", {
                  staticClass: "col-md-5"
              }, [i("img", {
                  attrs: {
                      src: e("e891"),
                      alt: "Header image"
                  }
              })])])])
          }, function() {
              var t = this,
                  s = t.$createElement,
                  i = t._self._c || s;
              return i("section", {
                  staticClass: "companies"
              }, )
          }, function() {
              var t = this,
                  s = t.$createElement,
                  i = t._self._c || s;
              return i("div", {
                  staticClass: "container"
              }, [i("div", {
                  staticClass: "row align-items-center"
              }, [i("div", {
                  staticClass: "col-md-6"
              }, [i("img", {
                  attrs: {
                      src: e("fd7d"),
                      alt: ""
                  }
              })]), i("div", {
                  staticClass: "col-md-6"
              }, [i("h1", {
                  staticClass: "my-3"
              }, [t._v("Introducing HT")]), i("p", {
                  staticClass: "my-4"
              }, [t._v(" It's crafted with the latest trend of design & coded with all modern approaches. It's a robust & multi-dimensional usable template. ")]), i("ul", [i("li", [t._v("Best for Creative Agency")]), i("li", [t._v("Built with Latest Technology")]), i("li", [t._v("Super Responsive")]), i("li", [t._v("Creative Design")])])])])])
          }, function() {
              var t = this,
                  s = t.$createElement,
                  i = t._self._c || s;
              return i("div", {
                  staticClass: "container"
              }, [i("div", {
                  staticClass: "row"
              }, [i("div", {
                  staticClass: "col-md-10"
              }, [i("h1", [t._v("Check our latest awesome creative work")]), i("p", [t._v(" It's crafted with the latest trend of design & coded with all modern approaches. It's a robust & multi-dimensional usable template ")])])]), i("div", {
                  staticClass: "row my-3 g-3"
              }, [i("div", {
                  staticClass: "col-md-4"
              }, [i("img", {
                  staticClass: "img-fluid",
                  attrs: {
                      src: e("1db9"),
                      alt: "Gallery image"
                  }
              })]), i("div", {
                  staticClass: "col-md-4"
              }, [i("img", {
                  staticClass: "img-fluid",
                  attrs: {
                      src: e("4851"),
                      alt: "Gallery image"
                  }
              })]), i("div", {
                  staticClass: "col-md-4"
              }, [i("img", {
                  staticClass: "img-fluid",
                  attrs: {
                      src: e("f3ea"),
                      alt: "Gallery image"
                  }
              })])]), i("div", {
                  staticClass: "row mt-5 justify-content-end"
              }, [i("div", {
                  staticClass: "col-md-2"
              }, [i("button", {
                  staticClass: "btn btn-outline-secondary",
                  attrs: {
                      type: "button"
                  }
              }, [t._v(" See all works ")])])])])
          }, function() {
              var t = this,
                  s = t.$createElement,
                  i = t._self._c || s;
              return i("div", {
                  staticClass: "container"
              }, [i("div", {
                  staticClass: "row align-items-center justify-content-center"
              }, [i("div", {
                  staticClass: "col-md-5"
              }, [i("button", {
                  staticClass: "btn btn-outline-warning mb-3",
                  attrs: {
                      type: "button"
                  }
              }, [t._v(" Coding ")]), i("h1", [t._v("We code.")]), i("p", [t._v(" Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus, tempore placeat corrupti enim, cumque ex? Mollitia nihil sint cumque omnis iure nisi. ")])]), i("div", {
                  staticClass: "col-md-5"
              }, [i("img", {
                  attrs: {
                      src: e("2413"),
                      alt: ""
                  }
              })]), i("div", {
                  staticClass: "col-md-5"
              }, [i("img", {
                  attrs: {
                      src: e("99c0"),
                      alt: ""
                  }
              })]), i("div", {
                  staticClass: "col-md-5"
              }, [i("button", {
                  staticClass: "btn btn-outline-success mb-3",
                  attrs: {
                      type: "button "
                  }
              }, [t._v(" Marketing ")]), i("h1", [t._v("We promote.")]), i("p", [t._v(" Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus, tempore placeat corrupti enim, cumque ex? Mollitia nihil sint cumque omnis iure nisi. ")])]), i("div", {
                  staticClass: "col-md-5"
              }, [i("button", {
                  staticClass: "btn btn-outline-light mb-3",
                  attrs: {
                      type: "button"
                  }
              }, [t._v(" Selling ")]), i("h1", [t._v("We sell.")]), i("p", [t._v(" Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus, tempore placeat corrupti enim, cumque ex? Mollitia nihil sint cumque omnis iure nisi. ")])]), i("div", {
                  staticClass: "col-md-5"
              }, [i("img", {
                  attrs: {
                      src: e("6ba1"),
                      alt: ""
                  }
              })])])])
          }, function() {
              var t = this,
                  s = t.$createElement,
                  i = t._self._c || s;
              return i("section", {
                  staticClass: "contact"
              }, [i("div", {
                  staticClass: "container"
              }, [i("div", {
                  staticClass: "row"
              }, [i("div", {
                  staticClass: "col-md-5"
              }, [i("h1", [t._v("Contact us:")]), i("div", {
                  staticClass: "mb-3"
              }, [i("label", {
                  staticClass: "form-label",
                  attrs: {
                      for: "exampleFormControlInput1"
                  }
              }, [t._v("Email address")]), i("input", {
                  staticClass: "form-control",
                  attrs: {
                      type: "email",
                      id: "exampleFormControlInput1",
                      placeholder: "name@example.com"
                  }
              })]), i("div", {
                  staticClass: "mb-3"
              }, [i("label", {
                  staticClass: "form-label",
                  attrs: {
                      for: "exampleFormControlTextarea1"
                  }
              }, [t._v("Example textarea")]), i("textarea", {
                  staticClass: "form-control",
                  attrs: {
                      id: "exampleFormControlTextarea1",
                      rows: "3"
                  }
              })]), i("button", {
                  staticClass: "btn btn-outline-secondary",
                  attrs: {
                      type: "button"
                  }
              }, [t._v(" Send ")])]), i("div", {
                  staticClass: "col-md-5"
              }, [i("img", {
                  attrs: {
                      src: e("4541"),
                      alt: "Contact image"
                  }
              })])])])])
          }],
          C = {},
          h = C,
          b = (e("8b71"), Object(u["a"])(h, g, f, !1, null, null, null)),
          w = b.exports,
          y = {
              name: "App",
              components: {
                  Navbar: v,
                  Home: w
              },
              data: function() {
                  return {
                      reviews: []
                  }
              },
              methods: {
                  getReviews: function() {
                      var t = this;
                      r.a.get("http://api-prod.horizontall.htb/reviews").then((function(s) {
                          return t.reviews = s.data
                      }))
                  }
              }
          },
          x = y,
          A = (e("034f"), Object(u["a"])(x, a, l, !1, null, null, null)),
          E = A.exports,
          M = e("8c4f"),
          L = e("5f5b"),
          I = e("b1e0");
      e("f9e3"), e("2dd8");
      i["default"].use(L["a"]), i["default"].use(I["a"]), i["default"].use(M["a"]), i["default"].config.productionTip = !1, new i["default"]({
          render: function(t) {
              return t(E)
          }
      }).$mount("#app")
  },
  "6ba1": function(t, s, e) {
      t.exports = e.p + "img/revenue_.71587b74.svg"
  },
  "85ec": function(t, s, e) {},
  "88d7": function(t, s, e) {},
  "8a45": function(t, s, e) {
      t.exports = e.p + "img/5.5b9914d5.png"
  },
  "8b71": function(t, s, e) {
      "use strict";
      e("88d7")
  },
  9689: function(t, s, e) {
      t.exports = e.p + "img/4.52389c77.png"
  },
  "99c0": function(t, s, e) {
      t.exports = e.p + "img/marketing.4b7dfec0.svg"
  },
  ac5a: function(t, s, e) {
      t.exports = e.p + "img/1.cecf2cc1.png"
  },
  cc09: function(t, s, e) {
      t.exports = e.p + "img/horizontall.2db2bc37.png"
  },
  e611: function(t, s, e) {
      t.exports = e.p + "img/3.25f11f60.png"
  },
  e891: function(t, s, e) {
      t.exports = e.p + "img/email_campaign_monochromatic.f0faa6a4.svg"
  },
  eafb: function(t, s, e) {
      t.exports = e.p + "img/2.76afc074.png"
  },
  f3ea: function(t, s, e) {
      t.exports = e.p + "img/c3.1a5adf9b.jpg"
  },
  fd7d: function(t, s, e) {
      t.exports = e.p + "img/seo_monochromatic.5fce4827.svg"
  }
});
//# sourceMappingURL=app.c68eb462.js.map