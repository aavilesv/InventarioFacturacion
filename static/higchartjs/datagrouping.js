/*
 Highstock JS v8.0.0 (2019-12-10)

 Data grouping module

 (c) 2010-2019 Torstein Hnsi

 License: www.highcharts.com/license
*/
(function(b){"object"===typeof module&&module.exports?(b["default"]=b,module.exports=b):"function"===typeof define&&define.amd?define("highcharts/modules/datagrouping",["highcharts"],function(k){b(k);b.Highcharts=k;return b}):b("undefined"!==typeof Highcharts?Highcharts:void 0)})(function(b){function k(e,b,k,B){e.hasOwnProperty(b)||(e[b]=B.apply(null,k))}b=b?b._modules:{};k(b,"parts/DataGrouping.js",[b["parts/Globals.js"],b["parts/Utilities.js"]],function(e,b){var k=b.arrayMax,B=b.arrayMin,J=b.correctFloat,
D=b.defined,K=b.extend,x=b.isNumber,A=b.pick;b=e.addEvent;var y=e.Axis,L=e.defaultPlotOptions,M=e.format,E=e.merge,N=e.Point,F=e.Series,O=e.Tooltip,v=e.approximations={sum:function(a){var d=a.length;if(!d&&a.hasNulls)var c=null;else if(d)for(c=0;d--;)c+=a[d];return c},average:function(a){var d=a.length;a=v.sum(a);x(a)&&d&&(a=J(a/d));return a},averages:function(){var a=[];[].forEach.call(arguments,function(d){a.push(v.average(d))});return"undefined"===typeof a[0]?void 0:a},open:function(a){return a.length?
a[0]:a.hasNulls?null:void 0},high:function(a){return a.length?k(a):a.hasNulls?null:void 0},low:function(a){return a.length?B(a):a.hasNulls?null:void 0},close:function(a){return a.length?a[a.length-1]:a.hasNulls?null:void 0},ohlc:function(a,d,c,b){a=v.open(a);d=v.high(d);c=v.low(c);b=v.close(b);if(x(a)||x(d)||x(c)||x(b))return[a,d,c,b]},range:function(a,d){a=v.low(a);d=v.high(d);if(x(a)||x(d))return[a,d];if(null===a&&null===d)return null}},G=function(a,d,c,b){var f=this,e=f.data,P=f.options&&f.options.data,
l=[],m=[],q=[],p=a.length,r=!!d,t=[],g=f.pointArrayMap,k=g&&g.length,w=["x"].concat(g||["y"]),y=0,z=0,u;b="function"===typeof b?b:v[b]?v[b]:v[f.getDGApproximation&&f.getDGApproximation()||"average"];k?g.forEach(function(){t.push([])}):t.push([]);var B=k||1;for(u=0;u<=p&&!(a[u]>=c[0]);u++);for(u;u<=p;u++){for(;"undefined"!==typeof c[y+1]&&a[u]>=c[y+1]||u===p;){var h=c[y];f.dataGroupInfo={start:f.cropStart+z,length:t[0].length};var C=b.apply(f,t);f.pointClass&&!D(f.dataGroupInfo.options)&&(f.dataGroupInfo.options=
E(f.pointClass.prototype.optionsToObject.call({series:f},f.options.data[f.cropStart+z])),w.forEach(function(a){delete f.dataGroupInfo.options[a]}));"undefined"!==typeof C&&(l.push(h),m.push(C),q.push(f.dataGroupInfo));z=u;for(h=0;h<B;h++)t[h].length=0,t[h].hasNulls=!1;y+=1;if(u===p)break}if(u===p)break;if(g)for(h=f.cropStart+u,C=e&&e[h]||f.pointClass.prototype.applyOptions.apply({series:f},[P[h]]),h=0;h<k;h++){var A=C[g[h]];x(A)?t[h].push(A):null===A&&(t[h].hasNulls=!0)}else h=r?d[u]:null,x(h)?t[0].push(h):
null===h&&(t[0].hasNulls=!0)}return{groupedXData:l,groupedYData:m,groupMap:q}},H={approximations:v,groupData:G},w=F.prototype,Q=w.processData,R=w.generatePoints,z={groupPixelWidth:2,dateTimeLabelFormats:{millisecond:["%A, %b %e, %H:%M:%S.%L","%A, %b %e, %H:%M:%S.%L","-%H:%M:%S.%L"],second:["%A, %b %e, %H:%M:%S","%A, %b %e, %H:%M:%S","-%H:%M:%S"],minute:["%A, %b %e, %H:%M","%A, %b %e, %H:%M","-%H:%M"],hour:["%A, %b %e, %H:%M","%A, %b %e, %H:%M","-%H:%M"],day:["%A, %b %e, %Y","%A, %b %e","-%A, %b %e, %Y"],
week:["Week from %A, %b %e, %Y","%A, %b %e","-%A, %b %e, %Y"],month:["%B %Y","%B","-%B %Y"],year:["%Y","%Y","-%Y"]}},I={line:{},spline:{},area:{},areaspline:{},arearange:{},column:{groupPixelWidth:10},columnrange:{groupPixelWidth:10},candlestick:{groupPixelWidth:10},ohlc:{groupPixelWidth:5}},S=e.defaultDataGroupingUnits=[["millisecond",[1,2,5,10,20,25,50,100,200,500]],["second",[1,2,5,10,15,30]],["minute",[1,2,5,10,15,30]],["hour",[1,2,3,4,6,8,12]],["day",[1]],["week",[1]],["month",[1,3,6]],["year",
null]];w.getDGApproximation=function(){return e.seriesTypes.arearange&&this instanceof e.seriesTypes.arearange?"range":e.seriesTypes.ohlc&&this instanceof e.seriesTypes.ohlc?"ohlc":e.seriesTypes.column&&this instanceof e.seriesTypes.column?"sum":"average"};w.groupData=G;w.processData=function(){var a=this.chart,d=this.options.dataGrouping,c=!1!==this.allowDG&&d&&A(d.enabled,a.options.isStock),b=this.visible||!a.options.chart.ignoreHiddenSeries,f,e=this.currentDataGrouping,n=!1;this.forceCrop=c;this.groupPixelWidth=
null;this.hasProcessed=!0;c&&!this.requireSorting&&(this.requireSorting=n=!0);c=!1===Q.apply(this,arguments)||!c;n&&(this.requireSorting=!1);if(!c){this.destroyGroupedData();c=d.groupAll?this.xData:this.processedXData;var l=d.groupAll?this.yData:this.processedYData,m=a.plotSizeX;a=this.xAxis;var q=a.options.ordinal,p=this.groupPixelWidth=a.getGroupPixelWidth&&a.getGroupPixelWidth();if(p){this.isDirty=f=!0;this.points=null;n=a.getExtremes();var r=n.min;n=n.max;q=q&&a.getGroupIntervalFactor(r,n,this)||
1;p=p*(n-r)/m*q;m=a.getTimeTicks(a.normalizeTimeTickInterval(p,d.units||S),Math.min(r,c[0]),Math.max(n,c[c.length-1]),a.options.startOfWeek,c,this.closestPointRange);l=w.groupData.apply(this,[c,l,m,d.approximation]);c=l.groupedXData;q=l.groupedYData;var t=0;if(d.smoothed&&c.length){var g=c.length-1;for(c[g]=Math.min(c[g],n);g--&&0<g;)c[g]+=p/2;c[0]=Math.max(c[0],r)}for(g=1;g<m.length;g++)m.info.segmentStarts&&-1!==m.info.segmentStarts.indexOf(g)||(t=Math.max(m[g]-m[g-1],t));r=m.info;r.gapSize=t;this.closestPointRange=
m.info.totalRange;this.groupMap=l.groupMap;if(D(c[0])&&c[0]<a.min&&b){if(!D(a.options.min)&&a.min<=a.dataMin||a.min===a.dataMin)a.min=Math.min(c[0],a.min);a.dataMin=Math.min(c[0],a.dataMin)}d.groupAll&&(d=this.cropData(c,q,a.min,a.max,1),c=d.xData,q=d.yData);this.processedXData=c;this.processedYData=q}else this.groupMap=null;this.hasGroupedData=f;this.currentDataGrouping=r;this.preventGraphAnimation=(e&&e.totalRange)!==(r&&r.totalRange)}};w.destroyGroupedData=function(){this.groupedData&&(this.groupedData.forEach(function(a,
d){a&&(this.groupedData[d]=a.destroy?a.destroy():null)},this),this.groupedData.length=0)};w.generatePoints=function(){R.apply(this);this.destroyGroupedData();this.groupedData=this.hasGroupedData?this.points:null};b(N,"update",function(){if(this.dataGroup)return e.error(24,!1,this.series.chart),!1});b(O,"headerFormatter",function(a){var d=this.chart,c=d.time,b=a.labelConfig,f=b.series,e=f.tooltipOptions,n=f.options.dataGrouping,l=e.xDateFormat,m=f.xAxis,q=e[(a.isFooter?"footer":"header")+"Format"];
if(m&&"datetime"===m.options.type&&n&&x(b.key)){var p=f.currentDataGrouping;n=n.dateTimeLabelFormats||z.dateTimeLabelFormats;if(p)if(e=n[p.unitName],1===p.count)l=e[0];else{l=e[1];var r=e[2]}else!l&&n&&(l=this.getXDateFormat(b,e,m));l=c.dateFormat(l,b.key);r&&(l+=c.dateFormat(r,b.key+p.totalRange-1));f.chart.styledMode&&(q=this.styledModeFormat(q));a.text=M(q,{point:K(b.point,{key:l}),series:f},d);a.preventDefault()}});b(F,"destroy",w.destroyGroupedData);b(F,"afterSetOptions",function(a){a=a.options;
var d=this.type,c=this.chart.options.plotOptions,b=L[d].dataGrouping,e=this.useCommonDataGrouping&&z;if(I[d]||e)b||(b=E(z,I[d])),a.dataGrouping=E(e,b,c.series&&c.series.dataGrouping,c[d].dataGrouping,this.userOptions.dataGrouping)});b(y,"afterSetScale",function(){this.series.forEach(function(a){a.hasProcessed=!1})});y.prototype.getGroupPixelWidth=function(){var a=this.series,b=a.length,c,e=0,f=!1,k;for(c=b;c--;)(k=a[c].options.dataGrouping)&&(e=Math.max(e,A(k.groupPixelWidth,z.groupPixelWidth)));
for(c=b;c--;)(k=a[c].options.dataGrouping)&&a[c].hasProcessed&&(b=(a[c].processedXData||a[c].data).length,a[c].groupPixelWidth||b>this.chart.plotSizeX/e||b&&k.forced)&&(f=!0);return f?e:0};y.prototype.setDataGrouping=function(a,b){var c;b=A(b,!0);a||(a={forced:!1,units:null});if(this instanceof y)for(c=this.series.length;c--;)this.series[c].update({dataGrouping:a},!1);else this.chart.options.series.forEach(function(b){b.dataGrouping=a},!1);this.ordinalSlope=null;b&&this.chart.redraw()};e.dataGrouping=
H;"";return H});k(b,"masters/modules/datagrouping.src.js",[b["parts/DataGrouping.js"]],function(b){return b})});
//# sourceMappingURL=datagrouping.js.map