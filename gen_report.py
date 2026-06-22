import os

html = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>政策周报 — 2026年06月22日</title>
<style>
  :root { --blue: #1d4ed8; --light: #eff6ff; --gray: #f3f4f6; --border: #d1d5db; --text: #1e293b; --muted: #64748b; }
  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    max-width: 1040px; margin: 0 auto; padding: 48px 28px 80px;
    font-family: -apple-system,BlinkMacSystemFont,'Microsoft YaHei','PingFang SC',sans-serif;
    font-size: 15px; line-height: 1.75; color: var(--text); background: #f8fafc;
  }

  .cover {
    background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
    color: #fff; padding: 48px 40px; border-radius: 12px; margin-bottom: 40px;
  }
  .cover h1 { font-size: 30px; margin-bottom: 8px; letter-spacing: 1px; }
  .cover .meta { font-size: 14px; opacity: 0.85; }
  .cover .meta span { margin-right: 24px; }

  .section-title {
    font-size: 22px; font-weight: 700; color: #1e3a8a;
    margin: 44px 0 8px; padding-bottom: 8px;
    border-bottom: 3px solid #2563eb;
  }
  .subsection-title {
    font-size: 17px; font-weight: 700; color: #1d4ed8;
    margin: 28px 0 10px; padding-left: 12px;
    border-left: 4px solid #2563eb;
  }

  .table-wrap { overflow-x: auto; margin: 12px 0 28px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,.08); }
  table { width: 100%; border-collapse: collapse; font-size: 13.5px; background: #fff; }
  thead th {
    background: #1e3a8a; color: #fff; padding: 11px 10px; text-align: left;
    font-weight: 600; font-size: 13px; white-space: nowrap;
  }
  tbody td { padding: 10px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
  tbody tr:nth-child(even) { background: #f8fafc; }
  tbody tr:hover { background: #dbeafe; }

  .tag-new  { display:inline-block; background:#d1fae5; color:#065f46; padding:1px 7px; border-radius:3px; font-size:12px; font-weight:600; }
  .tag-renew{ display:inline-block; background:#dbeafe; color:#1e40af; padding:1px 7px; border-radius:3px; font-size:12px; font-weight:600; }
  .tag-warn { display:inline-block; background:#fee2e2; color:#991b1b; padding:1px 7px; border-radius:3px; font-size:12px; font-weight:600; }

  .insight { background: #fff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 24px 28px; margin: 20px 0; box-shadow: 0 1px 3px rgba(0,0,0,.04); }
  .insight h3 { font-size: 16px; color: #1e3a8a; margin-bottom: 10px; }
  .insight p  { margin: 8px 0; color: #334155; }
  .insight .q { font-weight: 700; color: #0f172a; }

  .dirs { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 12px 0 24px; }
  .dir-card { background: #fff; border-left: 4px solid #2563eb; border-radius: 6px; padding: 16px 20px; box-shadow: 0 1px 3px rgba(0,0,0,.04); }
  .dir-card .num { font-size: 22px; font-weight: 800; color: #2563eb; }
  .dir-card h4 { font-size: 15px; margin: 4px 0 6px; color: #0f172a; }
  .dir-card p { font-size: 13px; color: #475569; line-height: 1.6; }

  .footer { margin-top: 48px; padding-top: 20px; border-top: 1px solid var(--border); font-size: 12px; color: var(--muted); }
</style>
</head>
<body>

<div class="cover">
  <h1>政策周报</h1>
  <div class="meta">
    <span>2026年06月22日</span>
    <span>覆盖：6月15日 – 6月21日</span>
    <span>下期：6月29日</span>
  </div>
</div>

<div class="section-title">中国产业政策</div>

<div class="subsection-title">新能源 / 电动车</div>
<div class="table-wrap"><table>
<thead><tr><th>政策</th><th>类型</th><th>金额/规模</th><th>有效期</th><th>要点</th></tr></thead>
<tbody>
<tr>
  <td>五部门启动 2026 年新能源汽车下乡</td>
  <td><span class="tag-renew">续期加码</span></td>
  <td>累计销量已破 2000 万辆</td>
  <td>2026 全年</td>
  <td>落实车购税/车船税减免、县域充换电设施补短板；覆盖千县万镇</td>
</tr>
<tr>
  <td>工信部等三部门召开新能源车企座谈会</td>
  <td><span class="tag-new">新政</span></td>
  <td>—</td>
  <td>长期</td>
  <td>补齐<strong>汽车芯片及基础软件</strong>短板；推动新能源重卡规模化；督促 60 天账期；规范竞争秩序</td>
</tr>
<tr>
  <td>工信部《2026 年汽车标准化工作要点》</td>
  <td><span class="tag-new">新政</span></td>
  <td>—</td>
  <td>2026–2030</td>
  <td>四大方向：质量安全、绿色低碳、车路云一体化+汽车芯片标准、<strong>固态电池标准体系</strong>预研</td>
</tr>
<tr>
  <td>国家能源局：可再生能源消费考核扩围</td>
  <td><span class="tag-new">新政</span></td>
  <td>—</td>
  <td>即日</td>
  <td>算力设施、多晶硅、锂离子电池制造纳入考核—"以绿造绿"</td>
</tr>
<tr>
  <td>新能源车购置税减半</td>
  <td><span class="tag-renew">退坡续期</span></td>
  <td>全免 → <strong>减半</strong></td>
  <td>2026 全年</td>
  <td>购车成本增加数千元，多家车企已涨价</td>
</tr>
</tbody></table></div>

<div class="subsection-title">半导体 / 科技</div>
<div class="table-wrap"><table>
<thead><tr><th>政策</th><th>类型</th><th>金额/规模</th><th>有效期</th><th>要点</th></tr></thead>
<tbody>
<tr>
  <td>汽车芯片国产替代提速</td>
  <td><span class="tag-new">新政加码</span></td>
  <td>—</td>
  <td>长期</td>
  <td>工信部明确扩大国产汽车芯片应用规模；北京此前已非正式要求车企最大化使用国产芯片</td>
</tr>
<tr>
  <td>芯联集成 12 英寸车规晶圆厂</td>
  <td><span class="tag-new">重大投资</span></td>
  <td><strong>200 亿元</strong>（约 30 亿美元）</td>
  <td>2026 起建设</td>
  <td>浙江绍兴；月产 5 万片；覆盖新能源车、AI 服务器、机器人芯片</td>
</tr>
<tr>
  <td>七部门：平台经济协同发展行动方案</td>
  <td><span class="tag-new">新政</span></td>
  <td>—</td>
  <td>2026–2028</td>
  <td>培育制造业单项冠军；平台企业向产业互联网转型</td>
</tr>
<tr>
  <td>研发费用加计扣除</td>
  <td><span class="tag-renew">续期</span></td>
  <td>—</td>
  <td>长期</td>
  <td>科技企业研发费用 <strong>100% 加计扣除</strong></td>
</tr>
<tr>
  <td>商务部/中央网信办联合发文</td>
  <td><span class="tag-new">新政</span></td>
  <td>—</td>
  <td>长期</td>
  <td>推动半导体、AI、数字经济；6/16 多只半导体股涨停</td>
</tr>
</tbody></table></div>

<div class="subsection-title">房地产 / 基建 / 城市更新</div>
<div class="table-wrap"><table>
<thead><tr><th>政策</th><th>类型</th><th>金额/规模</th><th>有效期</th><th>要点</th></tr></thead>
<tbody>
<tr>
  <td>财政部：十五五中央财政支持城市更新</td>
  <td><span class="tag-new">新政定调</span></td>
  <td><strong>2026 年中央预算 970 亿元</strong></td>
  <td>2026–2030</td>
  <td>保障房、城中村改造、老旧小区改造、地下管网；惠及约 800 万户</td>
</tr>
<tr>
  <td>地方政府专项债</td>
  <td><span class="tag-renew">续期加码</span></td>
  <td>未披露</td>
  <td>十五五期间</td>
  <td>50 个重点城市连续 3 年获定额补助；东中西部分别补助</td>
</tr>
<tr>
  <td>超长期特别国债</td>
  <td><span class="tag-new">新渠道</span></td>
  <td>未披露</td>
  <td>2026 起</td>
  <td>新增渠道：地下管网 + 老旧小区改造</td>
</tr>
<tr>
  <td>城镇保障性安居工程补助</td>
  <td><span class="tag-renew">续期</span></td>
  <td>持续拨付</td>
  <td>长期</td>
  <td>城中村、危旧房改造；对东中西部分别定额补助</td>
</tr>
</tbody></table></div>

<div class="subsection-title">消费 / 以旧换新</div>
<div class="table-wrap"><table>
<thead><tr><th>政策</th><th>类型</th><th>金额/规模</th><th>有效期</th><th>要点</th></tr></thead>
<tbody>
<tr>
  <td>2026 年消费品以旧换新总盘子</td>
  <td><span class="tag-renew">续期减量</span></td>
  <td>超长期国债 <strong>~2500 亿</strong>（↓16.7%）</td>
  <td>2026 全年</td>
  <td>6 月底前下达 2000 亿设备更新 + 第三批 625 亿消费品资金</td>
</tr>
<tr>
  <td>汽车报废更新</td>
  <td><span class="tag-renew">优化</span></td>
  <td>最高 <strong>2 万/辆</strong>（改按车价比例）</td>
  <td>2026 全年</td>
  <td>置换更新最高 1.5 万；30 个工作日内兑付</td>
</tr>
<tr>
  <td>家电以旧换新</td>
  <td><span class="tag-renew">收紧</span></td>
  <td><strong>15%</strong> / 单件 ≤1500 元</td>
  <td>2026 全年</td>
  <td>仅补贴 <strong>1 级能效</strong>（冰箱/洗衣机/电视/空调/电脑/热水器，共 6 类）</td>
</tr>
<tr>
  <td>数码及智能产品购新补贴</td>
  <td><span class="tag-new">新增</span></td>
  <td><strong>15%</strong> / 单件 ≤500 元</td>
  <td>2026 全年</td>
  <td>手机、平板、智能手表/手环、<strong>智能眼镜</strong>（4 类）；单价 ≤6000 元</td>
</tr>
<tr>
  <td><span class="tag-warn">⚠ 效果预警</span></td>
  <td>—</td>
  <td>—</td>
  <td>—</td>
  <td>1–5 月社零同比 <strong>-0.6%</strong>（2023 年来首次转负）；家电拉动系数 0.9→0.6；汽车由正转负</td>
</tr>
</tbody></table></div>

<div class="subsection-title">农业 / 粮食</div>
<div class="table-wrap"><table>
<thead><tr><th>政策</th><th>类型</th><th>金额/规模</th><th>有效期</th><th>要点</th></tr></thead>
<tbody>
<tr>
  <td>2026 中央一号文件：粮食最低收购价</td>
  <td><span class="tag-renew">续期</span></td>
  <td>小麦 1.19 元/斤 · 粳稻 1.31 元/斤</td>
  <td>2026 全年</td>
  <td>连续 22 年执行兜底收购；粮食产销区省际横向补偿</td>
</tr>
<tr>
  <td>耕地地力保护补贴</td>
  <td><span class="tag-renew">续期</span></td>
  <td>全国 105–150 元/亩</td>
  <td>6 月底前发放</td>
  <td>不撂荒方可领取；黑龙江 ≥75 元/亩，江西 112 元/亩</td>
</tr>
<tr>
  <td>玉米/大豆生产者补贴</td>
  <td><span class="tag-renew">续期</span></td>
  <td>玉米 ≈120 · 大豆 ≈200 元/亩</td>
  <td>2026 全年</td>
  <td>东北主产区更高（吉林大豆高达 550 元/亩）</td>
</tr>
<tr>
  <td>农机购置补贴</td>
  <td><span class="tag-renew">续期</span></td>
  <td><strong>30%–40%</strong>（重点机具 ≤50%）</td>
  <td>长期</td>
  <td>覆盖主要农作物全程机械化</td>
</tr>
<tr>
  <td>水稻完全成本保险</td>
  <td><span class="tag-renew">续期</span></td>
  <td>保额 <strong>1100 元/亩</strong>，保费财政全补</td>
  <td>2026 全年</td>
  <td>50 亩以下小农户免缴保费</td>
</tr>
</tbody></table></div>

<div class="section-title">国际产业政策</div>

<div class="subsection-title">美国 CHIPS / IRA / 半导体</div>
<div class="table-wrap"><table>
<thead><tr><th>政策</th><th>类型</th><th>金额/规模</th><th>要点</th><th>对华溢出</th></tr></thead>
<tbody>
<tr>
  <td>CHIPS Act 拨款基本完成</td>
  <td>执行中</td>
  <td>已拨付逾 <strong>360 亿美元</strong></td>
  <td>Intel $78.6亿+$35亿国防；TSMC $66亿；三星 $47亿；美光 $61.7亿</td>
  <td>受资助企业 <strong>10 年内不得在华扩产</strong>先进制程</td>
</tr>
<tr>
  <td>35% 投资税收抵免</td>
  <td><span class="tag-new">加码</span></td>
  <td>25% → <strong>35%</strong></td>
  <td>2026/12/31 前未破土动工则作废；可退税直接支付</td>
  <td>全球产能进一步向美集中</td>
</tr>
<tr>
  <td>Intel 18A（1.8nm）量产</td>
  <td>里程碑</td>
  <td>—</td>
  <td>亚利桑那 Fab 52 — 美国首次超越 2nm</td>
  <td>美国先进逻辑从 0%→~15%</td>
</tr>
<tr>
  <td>TSMC 亚利桑那良率 ≥92%</td>
  <td>里程碑</td>
  <td>$650 亿</td>
  <td>Fab 1 满载；Fab 2 在建（3nm/2nm，2027）</td>
  <td>最先进制程首次在美达到台湾同级良率</td>
</tr>
<tr>
  <td>三星德州 2nm GAA</td>
  <td>在建</td>
  <td>$370 亿+</td>
  <td>锁定 Tesla/Google；2026 年底量产</td>
  <td>先进制程供应链向北美集中</td>
</tr>
<tr>
  <td>美国政府持有 Intel ~10%</td>
  <td><span class="tag-new">新政</span></td>
  <td>~$89 亿估值</td>
  <td>股权置换拨款；正与 TSMC/三星/美光探讨</td>
  <td>政府成半导体股东—史无前例</td>
</tr>
<tr>
  <td>美光 HBM/DRAM 扩产</td>
  <td>在建</td>
  <td>$61.7 亿拨款</td>
  <td>纽约 + 爱达荷；AI 数据中心驱动</td>
  <td>HBM 产能仍集中在亚洲</td>
</tr>
<tr>
  <td><span class="tag-warn">⚠ 劳动力缺口</span></td>
  <td>风险</td>
  <td>2030 年缺 ~7 万人</td>
  <td>技术员/工程师严重不足</td>
  <td>可能延缓产能爬坡</td>
</tr>
</tbody></table></div>

<div class="subsection-title">欧盟 CBAM / 绿色工业 / 关键原材料</div>
<div class="table-wrap"><table>
<thead><tr><th>政策</th><th>类型</th><th>要点</th><th>对华溢出</th></tr></thead>
<tbody>
<tr>
  <td>CBAM 全面执行</td>
  <td>2026/1/1 起</td>
  <td>覆盖钢铁、铝、水泥、化肥、电力、氢</td>
  <td>中国对欧钢铁/铝出口面临额外碳成本</td>
</tr>
<tr>
  <td><strong>ECOFIN 扩大 CBAM 范围</strong></td>
  <td><span class="tag-new">重大加码</span></td>
  <td>纳入 <strong>下游制成品</strong>：叉车、输送设备、机械零件、电动机部件、货车、医疗设备；废钢/废铝防规避</td>
  <td>中国机械/机电出口欧盟成本显著上升</td>
</tr>
<tr>
  <td>CBAM 扩展共识达成</td>
  <td>里程碑</td>
  <td>理事会范围比欧委会原提案 <strong>扩大一倍</strong>；年度复审强制扩围；收紧"资源洗白"</td>
  <td>出口商需建立完整碳足迹追溯</td>
</tr>
<tr>
  <td>CRMA 联动</td>
  <td>政策协同</td>
  <td>钢铝与关键/战略原材料清单重叠；废金属条款推循环经济</td>
  <td>中国铝/钢出口商绿色溢价能力成关键</td>
</tr>
<tr>
  <td>间接排放纳入预告</td>
  <td>2027 提案</td>
  <td>芬兰智库报告（6/10）建议扩展</td>
  <td>电解铝等高电力成本产品首当其冲</td>
</tr>
</tbody></table></div>

<div class="subsection-title">芯片出口管制 / 实体清单</div>
<div class="table-wrap"><table>
<thead><tr><th>政策</th><th>类型</th><th>要点</th><th>对华溢出</th></tr></thead>
<tbody>
<tr>
  <td>美对华芯片管制第三轮</td>
  <td>持续收紧</td>
  <td>此前已限制 140 家中国科技公司；豁免部分盟友设备商</td>
  <td>AI/超算芯片获取持续受限</td>
</tr>
<tr>
  <td>中芯国际/长鑫存储等 15 家入列</td>
  <td><span class="tag-new">加码</span></td>
  <td>存储 + Foundry 龙头被列入</td>
  <td>国产替代紧迫性进一步上升</td>
</tr>
<tr>
  <td>日本/荷兰协同管制</td>
  <td>持续</td>
  <td>日本限制 23 种设备；荷兰限制先进 DUV</td>
  <td>设备进口渠道全面收窄</td>
</tr>
</tbody></table></div>

<div class="subsection-title">全球电动车关税</div>
<div class="table-wrap"><table>
<thead><tr><th>政策</th><th>类型</th><th>要点</th><th>对华溢出</th></tr></thead>
<tbody>
<tr>
  <td>欧盟对华 BEV 反补贴关税</td>
  <td>执行中（5 年）</td>
  <td>BYD 17% · 吉利 18.8% · 上汽 35.3% · Tesla 中 7.8%（均+10% 基础）</td>
  <td>中国 BEV 欧洲市占率从 ~8% 回落</td>
</tr>
<tr>
  <td><strong>中欧"价格承诺"共识</strong></td>
  <td><span class="tag-new">重大缓和</span></td>
  <td>以最低进口价替代关税（2026/1/12）；需可追溯+反规避</td>
  <td>MIP 计算方法是 2026 年最关键中欧贸易议题</td>
</tr>
<tr>
  <td>中国车企对策</td>
  <td>市场适应</td>
  <td>PHEV 出口激增；比亚迪/沃尔沃在欧建厂</td>
  <td>"以价代税"能否持续取决于 MIP 谈判</td>
</tr>
<tr>
  <td>美国 301 条款</td>
  <td>持续</td>
  <td>中国 EV <strong>100% 关税</strong></td>
  <td>中国 EV 基本不进入美国</td>
</tr>
</tbody></table></div>

<div class="subsection-title">日韩 / 东南亚科技投资</div>
<div class="table-wrap"><table>
<thead><tr><th>项目</th><th>状态</th><th>金额</th><th>要点</th></tr></thead>
<tbody>
<tr>
  <td><strong>台积电熊本二厂拟升级 3nm</strong></td>
  <td>重大升级</td>
  <td>—</td>
  <td>若成行将是日本首次量产 3nm</td>
</tr>
<tr>
  <td>台积电熊本一厂</td>
  <td>量产</td>
  <td>$86 亿+</td>
  <td>22/28nm + 12/16nm；月产 5.5 万片；2026Q4 满产</td>
</tr>
<tr>
  <td>台积电全球布局</td>
  <td>扩张</td>
  <td>年 CapEx >$300 亿</td>
  <td>亚利桑那 + 熊本 + 德累斯顿（2027）三线并进</td>
</tr>
<tr>
  <td>三星平泽/华城</td>
  <td>持续</td>
  <td>—</td>
  <td>P3/P4 推 2nm GAA；华城 DRAM/HBM</td>
</tr>
<tr>
  <td>SK 海力士 HBM</td>
  <td>扩张</td>
  <td>—</td>
  <td>HBM3E 供 NVIDIA；2026 HBM4 研发</td>
</tr>
<tr>
  <td>马来西亚槟城/居林</td>
  <td>扩张</td>
  <td>—</td>
  <td>英特尔、英飞凌封测扩产——中美脱钩最大受益方之一</td>
</tr>
</tbody></table></div>

<div class="section-title">专家拆解：本周政策背后的逻辑</div>

<div class="insight">
  <h3>1. 欧盟 CBAM 扩大化——碳关税从「原材料的墙」变成「制成的网」</h3>
  <p><span class="q">为什么现在出？</span> CBAM 全面执行后，出口商通过将高碳钢材/铝材加工成下游制成品（机械零件、电动机壳）再出口即可绕开碳关税。6 月 12 日 ECOFIN 扩围的核心目的就是<strong>封堵这个"下游套利"漏洞</strong>——范围从约 200 个海关编码可能扩大至 600–800 个。</p>
  <p><span class="q">和中国政策的联动？</span> 中国正在大力补贴 1 级能效家电（15%），推动制造商使用更低碳的钢铝。如果中国企业能建立从原料到成品的碳足迹追溯体系，未来对欧出口可能获得 CBAM 下的碳成本优势——<strong>碳竞争力正在成为新贸易壁垒</strong>。</p>
  <p><span class="q">历史参照？</span> CBAM 架构参考了 EU-ETS（2005 年启动）的经验：先上游，后下游。ETS 花了 15 年才覆盖当前范围；CBAM 正在以极高加速度复现这条路径。</p>
  <p><span class="q">后续？</span> 9 月欧洲议会将给更激进立场。2026 年底三方谈判定最终形态。大概率从 2028 年起绝大多数金属密集型制成品都被纳入。</p>
</div>

<div class="insight">
  <h3>2. 中国 EV「以价代税」——从关税对抗到价格管制</h3>
  <p><span class="q">为什么值得关注？</span> 1 月 12 日中欧达成的"价格承诺"共识本质上是<strong>双方各退一步</strong>：中国车企承诺不低于最低价倾销，欧盟暂停关税。MIP 的具体计算方法是当前博弈焦点。</p>
  <p><span class="q">对中国国内的影响？</span> 如果 MIP 以温和方式设定——国内 EV 品牌在欧洲实现"量价齐升"；如果 MIP 过高——加速中国车企在欧洲建厂，国内二线品牌承压更重。</p>
  <p><span class="q">历史参照？</span> 1980 年代日美汽车贸易摩擦——日本接受"自愿出口限制"后，倒逼产品线从低价车升级到高端车（雷克萨斯、讴歌由此诞生），反而提升了利润率。<strong>MIP 如果利用得当，可以倒逼品牌向上</strong>。</p>
  <p><span class="q">后续？</span> MIP 谈判结果将决定中国 EV 在欧洲未来五年的定价权。</p>
</div>

<div class="insight">
  <h3>3. 美国 CHIPS Act 进入量产时代——但劳动力缺口是致命伤</h3>
  <p><span class="q">里程碑意义？</span> Intel 18A 量产、TSMC 良率 92%、三星 2nm GAA 即将投产——美国先进逻辑从 <strong>0%（2022）→ ~15%（2025）</strong>。但所有项目面临同一个瓶颈：<strong>缺人</strong>。</p>
  <p><span class="q">对中国半导体的镜像启示？</span> 中国半导体人才缺口据行业协会估计超过 <strong>20 万</strong>。如果不解决培养问题，大基金三期 3000 亿砸下去也会遇到同样的"有设备没人操作"困境。<strong>半导体人才正在成为比芯片本身更稀缺的战略资源</strong>。</p>
  <p><span class="q">后续？</span> 2027 年可能爆发更严重劳动力危机。解决方案：国会追加学徒拨款、放宽 H-1B 工程师限制、部分项目回流亚洲（台积电熊本 3nm 正是此背景产物）。</p>
</div>

<div class="section-title">本周值得关注的产业方向</div>

<div class="dirs">
  <div class="dir-card">
    <div class="num">1</div>
    <h4>车用芯片国产替代加速</h4>
    <p>工信部明确"加快补齐汽车芯片短板"+ 芯联集成 200 亿车规晶圆厂投资。国内车规 MCU、IGBT、SiC 功率器件供应商可能迎来新一轮订单潮。</p>
  </div>
  <div class="dir-card">
    <div class="num">2</div>
    <h4>CBAM 扩围：碳成本冲击中国机械出口</h4>
    <p>CBAM 从基础材料扩大到叉车、电动机、医疗设备等下游制成品。所有对欧出口金属密集型产品的中国企业需尽快建立产品级碳足迹核算能力。</p>
  </div>
  <div class="dir-card">
    <div class="num">3</div>
    <h4>中欧 EV 价格承诺谈判走向</h4>
    <p>MIP 谈判将决定中国新能源车在欧洲未来几年的定价空间。直接关联 BYD、吉利、上汽的欧洲出口策略，间接影响锂电、动力电池回收、充电桩出口。</p>
  </div>
</div>

<div class="footer">
  数据来源：新华社 · 财政部 · 发改委 · 工信部 · 商务部 · 欧盟理事会 · European Commission · Business Times · Brussels Times · ESG Today · Carbon Herald · Yicai · 21 世纪经济报道 · WisdomTree · Wedbush · Georgetown CSET · 各地方农业农村局公告。数据截至 2026-06-22。
</div>

</body>
</html>'''

with open(r'D:\news\周报-政策追踪-2026-06-22.html', 'w', encoding='utf-8') as f:
    f.write(html)

sz = os.path.getsize(r'D:\news\周报-政策追踪-2026-06-22.html')
print(f'Done: {sz} bytes ({sz//1024} KB)')
