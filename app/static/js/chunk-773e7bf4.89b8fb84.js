(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-773e7bf4"],{2299:function(e,t,c){"use strict";c("b1ee")},b1ee:function(e,t,c){},b983:function(e,t,c){"use strict";c.r(t);var r=c("f2bf"),o=Object(r["withScopeId"])("data-v-5edee113");Object(r["pushScopeId"])("data-v-5edee113");var a={class:"row"};Object(r["popScopeId"])();var b=o((function(e,t,c,b,n,i){var d=Object(r["resolveComponent"])("SubHeader"),l=Object(r["resolveComponent"])("Member"),s=Object(r["resolveComponent"])("router-link");return Object(r["openBlock"])(),Object(r["createBlock"])(r["Fragment"],null,[Object(r["createVNode"])(d),Object(r["createVNode"])("div",a,[(Object(r["openBlock"])(!0),Object(r["createBlock"])(r["Fragment"],null,Object(r["renderList"])(e.getMembers,(function(e){return Object(r["openBlock"])(),Object(r["createBlock"])("div",{class:"col-md-3",key:e.user_id},[Object(r["createVNode"])(s,{to:{name:"StaticProfile",params:{user_code:e.user_id}}},{default:o((function(){return[Object(r["createVNode"])(l,{member:e},null,8,["member"])]})),_:2},1032,["to"])])})),128))])],64)})),n=c("5530"),i=c("5502"),d=c("e096"),l=Object(r["withScopeId"])("data-v-34a7a591");Object(r["pushScopeId"])("data-v-34a7a591");var s={id:"card"},p={class:"image-crop"},m={id:"bio"},j={style:{color:"white"}},O={style:{color:"white"}},u={id:"links"},v=Object(r["createVNode"])("i",{title:"LinkedIn link",class:"fab fa-linkedin"},null,-1),f=Object(r["createVNode"])("i",{title:"Github link",class:"fab fa-github"},null,-1);Object(r["popScopeId"])();var k=l((function(e,t,c,o,a,b){return Object(r["openBlock"])(),Object(r["createBlock"])("div",s,[Object(r["createVNode"])("h4",null,Object(r["toDisplayString"])(c.member["username"]),1),Object(r["createVNode"])("div",p,[Object(r["createVNode"])("img",{id:"avatar",src:"/api_v1/get_profile/".concat(c.member["profile_picture"]||"avatar.png","?")+(new Date).getTime()},null,8,["src"])]),Object(r["createVNode"])("div",m,[Object(r["createVNode"])("h3",j,"Division: "+Object(r["toDisplayString"])(c.member["Division"]),1),Object(r["createVNode"])("span",O,"Role: "+Object(r["toDisplayString"])(e.getRole(c.member["Role"])),1),Object(r["createVNode"])("p",null,Object(r["toDisplayString"])(c.member["Discription"]),1)]),Object(r["createVNode"])("div",u,[Object(r["createVNode"])("a",{href:c.member["Linkden"]},[v],8,["href"]),Object(r["createVNode"])("a",{href:c.member["Github"]},[f],8,["href"])])])})),g={name:"Member",props:{member:{required:!0,type:Object}},computed:Object(n["a"])({},Object(i["c"])({getRole:"getRoleByKey"}))};c("2299");g.render=k,g.__scopeId="data-v-34a7a591";var h=g,N={name:"Members",components:{SubHeader:d["a"],Member:h},computed:Object(n["a"])({},Object(i["c"])({getMembers:"home/getMembers"}))};N.render=b,N.__scopeId="data-v-5edee113";t["default"]=N}}]);
//# sourceMappingURL=chunk-773e7bf4.89b8fb84.js.map