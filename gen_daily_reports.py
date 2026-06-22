# 日报 + 前瞻 转 HTML — 2026年6月
import os

CSS = """<style>
  :root { --blue:#1d4ed8; --light:#eff6ff; --gray:#f3f4f6; --border:#d1d5db; --text:#1e293b; --muted:#64748b; --green:#059669; --red:#dc2626; }
  * { margin:0; padding:0; box-sizing:border-box; }
  body {
    max-width:960px; margin:0 auto; padding:48px 28px 80px;
    font-family:-apple-system,BlinkMacSystemFont,'Microsoft YaHei','PingFang SC',sans-serif;
    font-size:15px; line-height:1.85; color:var(--text); background:#f8fafc;
  }
  .cover {
    background:linear-gradient(135deg,#1e3a8a 0%,#2563eb 100%);
    color:#fff; padding:40px 36px; border-radius:12px; margin-bottom:36px;
  }
  .cover h1 { font-size:28px; margin-bottom:6px; }
  .cover .meta { font-size:14px; opacity:0.85; margin-top:4px; }

  h2 { font-size:20px; color:#1e40af; margin:36px 0 12px; padding-bottom:6px; border-bottom:2px solid #2563eb; padding-left:4px; }
  h3 { font-size:17px; color:#1d4ed8; margin:24px 0 8px; padding-left:10px; border-left:4px solid #2563eb; }
  h4 { font-size:15px; color:#0f172a; margin:18px 0 6px; }
  p { margin:10px 0; color:#334155; }
  strong { color:#0f172a; }
  code { background:#f1f5f9; padding:1px 6px; border-radius:3px; font-size:13px; color:#1e40af; }

  table { width:100%; border-collapse:collapse; margin:14px 0 22px; font-size:13.5px; background:#fff; border-radius:8px; overflow:hidden; box-shadow:0 1px 3px rgba(0,0,0,.06); }
  thead th { background:#1e3a8a; color:#fff; padding:10px 8px; text-align:left; font-weight:600; font-size:12.5px; }
  tbody td { padding:9px 8px; border-bottom:1px solid #e2e8f0; vertical-align:top; }
  tbody tr:nth-child(even) { background:#f8fafc; }
  tbody tr:hover { background:#dbeafe; }

  blockquote { border-left:3px solid #93c5fd; padding:10px 16px; margin:14px 0; background:#eff6ff; border-radius:0 6px 6px 0; font-size:14px; color:#1e40af; }
  hr { border:none; border-top:1px solid var(--border); margin:28px 0; }

  .insight { background:#fff; border:1px solid #e2e8f0; border-radius:10px; padding:20px 24px; margin:18px 0; box-shadow:0 1px 3px rgba(0,0,0,.04); }
  .insight h4 { color:#1e3a8a; margin-bottom:8px; }
  .insight .ref { background:#f0f9ff; border-left:4px solid #0ea5e9; padding:8px 12px; margin:10px 0; font-size:14px; color:#0c4a6e; border-radius:4px; }
  .insight .counter { background:#fef2f2; border-left:4px solid #dc2626; padding:8px 12px; margin:10px 0; font-size:14px; color:#991b1b; border-radius:4px; }

  .tag-up { color:#059669; font-weight:700; }
  .tag-down { color:#dc2626; font-weight:700; }
  .tag-flat { color:#6b7280; }

  .footer { margin-top:40px; padding-top:16px; border-top:1px solid var(--border); font-size:12px; color:var(--muted); }
  .oneliner { background:#fefce8; border-left:4px solid #eab308; padding:12px 16px; margin:20px 0; border-radius:4px; font-size:14px; color:#854d0e; font-weight:600; }

  @media print { body { font-size:12px; padding:20px; } table { font-size:11px; } }
</style>"""

# ============================================================
# 日报 1: 2026-06-20
# ============================================================
daily_0620 = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>宏观日报 — 2026年6月20日</title>
""" + CSS + """
</head>
<body>

<div class="cover">
  <h1>📰 宏观日报</h1>
  <div class="meta"><span>📅 2026年6月20日（周六）</span><span>📆 覆盖：6月17日–19日</span></div>
</div>

<h2>🇨🇳 中国线</h2>

<p><strong>央行结构性改革大礼包，但未降息。</strong> 6月17日陆家嘴论坛，潘功胜宣布多项措施：①利率走廊从70bp收窄至50bp（±25bp），增设隔夜逆回购操作，长期向价格型框架过渡；②推出FIMA人民币回购工具——境外央行/主权基金可用中债做押获取人民币流动性（7天/1月/3月），实质推动人民币国际化；③授权六大行在上海自贸区开展离岸人民币外汇交易，挑战香港离岸地位；④正研究非银机构紧急流动性支持工具。<strong>LPR连续13个月不变</strong>（1年3.00%、5年3.50%），花旗预计H2象征性降10bp。方向判断：央行选择制度开放而非传统刺激，借用人民币强势窗口推进资本账户开放。</p>

<p><strong>财政部定调"十五五"城市更新。</strong> 6月8日政策吹风会，财政部经济建设司明确：中央财政"保持较大支持力度"投入城市更新，资金来源包括保障房补助、专项债、中央预算内投资、超长期特别国债。同步实施税收优惠。这是真金白银的长期承诺，但短期无增量数字。</p>

<p><em>昨日无明显中国经济数据发布。</em></p>

<h2>🌍 国际线</h2>

<p><strong>美联储迎来Warsh时代，首秀鹰派。</strong> 6月17日FOMC一致通过维持利率3.50%-3.75%不变（连续第四次），但看点在新主席：①声明砍至约150词，削减前瞻指引；②Warsh拒交个人点阵图，称SEP"不适合当前政策形势"；③宣布成立五个工作组审查联储框架；④核心转向单一盯通胀——点阵图显示9/19票委预计年内加息一次，中位数升至3.80%。市场反应：S&P 500 -1.2%、纳指 -1.3%，10年期美债收益率逼近4.5%。高盛将首次降息预测推迟至2027年6月。</p>

<p><strong>中美贸易：从145%悬崖边退回谈判桌。</strong> 经历年初飙升至145%/125%的报复性关税后，双方在日内瓦框架下暂时退至美30%/中10%。6月14日美商务部长访华达成工作机制；6月15日中国暂停镓锗锑对美出口禁令（至11月27日）；6月下旬伦敦框架协议初步达成——中国承诺解决稀土出口限制，美国承诺放松部分芯片设计软件和化学品出口管制。<strong>关键节点：8月10日限期达成全面协议，否则关税弹回145%。</strong> 方向：双方都在借窗口降温，但结构性矛盾未解。</p>

<p><em>欧洲/日本：昨日无明显增量信号。</em></p>

<h2>💰 关键资产价格（6月20日）</h2>
<table>
<thead><tr><th>资产</th><th>水平</th><th>方向</th></tr></thead>
<tbody>
<tr><td>美国10年期国债</td><td>4.45%</td><td><span class="tag-up">↑</span> 受鹰派FOMC推升</td></tr>
<tr><td>中国10年期国债</td><td>未获取到最新</td><td>—</td></tr>
<tr><td>USD/CNY</td><td>未获取到最新</td><td>—</td></tr>
<tr><td>美元指数 DXY</td><td>~100.9</td><td><span class="tag-up">↑</span></td></tr>
<tr><td>布伦特原油</td><td>回落中</td><td><span class="tag-down">↓</span> 中东局势缓和</td></tr>
<tr><td>黄金</td><td>~$4,200</td><td><span class="tag-down">↓</span> 美元走强压制</td></tr>
<tr><td>沪深300</td><td>未获取到最新</td><td>—</td></tr>
<tr><td>S&P 500</td><td>涨1.08%</td><td><span class="tag-up">↑</span> AI乐观+地缘缓和</td></tr>
</tbody></table>

<h2>🔬 科技突破扫描</h2>
<p><strong>【真突破】</strong> 本周有四项重大科学发现值得关注：</p>

<div class="insight">
<h4>1. 线粒体-细胞核"专线"被发现</h4>
<p>亚利桑那大学等38位科学家在 <em>Nature</em> 发表：线粒体并非通过简单扩散为细胞核供能，而是VDAC1蛋白与核孔RANBP2直接物理连接形成专用能量通道。切断该连接导致小鼠胚胎死亡。改写教科书级别的发现。</p>
</div>

<div class="insight">
<h4>2. 斯坦福发现全新免疫细胞——ruptoblast</h4>
<p>发表在 <em>Cell</em>：这种"破裂母细胞"可在数分钟内爆炸性自毁并杀死周围数十个靶细胞，是已知最快的细胞死亡形式。为靶向治疗细菌感染和肿瘤提供全新思路。</p>
</div>

<div class="insight">
<h4>3. 真核细胞起源理论被改写</h4>
<p>IRB Barcelona团队在 <em>Nature</em> 发表：复杂细胞并非源自一次简单共生事件，而是多种微生物数百万年"渐进联盟"的结果，巨型病毒可能充当基因转移载体。</p>
</div>

<div class="insight">
<h4>4. 受精卵内父母基因组"分开居住"机制</h4>
<p>日本RIKEN在 <em>Nature</em> 发表：父母基因组在受精卵内分处两个原核，通过空间分离维持发育潜能。</p>
</div>

<h2>🧠 专家拆解：这些信息到底在说什么</h2>

<div class="insight">
<h4>第一课：为什么美联储鹰派，中国就不能降息？</h4>
<p>这是本周最重要的宏观逻辑链。链条是这样的：</p>
<p style="background:#f1f5f9; padding:12px; border-radius:6px; font-family:monospace; font-size:13px;">
美国加息/鹰派 → 美元资产收益率高 → 全球资金流向美国<br>
→ 人民币贬值压力 → 中国央行降息空间被压缩<br>
→ 如果强行降息 → 中美利差扩大 → 资本外流加速 → 汇率崩
</p>
<p>这就是为什么潘功胜在陆家嘴论坛<strong>只推改革、不降息</strong>的根本原因。不是不想刺激经济，而是<strong>外部条件不允许</strong>。他做的 FIMA 回购工具、利率走廊收窄这些，本质是在"为未来降息铺路"——先把制度框架搭好，等美联储松口了再出手。</p>
<div class="ref">💡 <strong>记住这个关系</strong>：美联储的利率是全球资产定价的「地心引力」。引力越大（利率越高），其他国家货币政策的自由度越小。</div>
</div>

<div class="insight">
<h4>第二课：怎么判断一个政策是「真金白银」还是「口号」？</h4>
<table>
<thead><tr><th>政策</th><th>真钱信号</th><th>判断</th></tr></thead>
<tbody>
<tr><td>央行陆家嘴措施</td><td>具体数字？没有。可立即操作？FIMA 回购是。预算拨付？不涉及。</td><td><span style="background:#fef3c7;padding:2px 8px;border-radius:3px;">🟡 制度改革</span>—长期重要，短期无增量资金</td></tr>
<tr><td>财政部城市更新</td><td>有专项债/特别国债/中央预算。有税收优惠。但<strong>具体额度</strong>？没给。</td><td><span style="background:#fef3c7;padding:2px 8px;border-radius:3px;">🟡 框架承诺</span>—方向确定，但钱还没落到具体项目</td></tr>
</tbody></table>
<p><strong>真金白银的判定标准</strong>：①有没有<strong>具体数字</strong>（多少钱、什么利率）；②有没有<strong>起止日期</strong>；③有没有<strong>具体受益对象</strong>。三个缺一个，就还是半成品信号。</p>
</div>

<div class="insight">
<h4>第三课：中美贸易——145% 关税是什么概念？</h4>
<p><strong>145% 关税 = 贸易禁运。</strong> 一件中国产品到美国，成本100元，加145元税 → 售价至少245元，没人会买。所以145%的时候中美贸易实质上停了。</p>
<p>这就是为什么双方要从悬崖边往回退。但退到30%/10%也只是<strong>回到了2025年初的水平</strong>——仍然很高，只是从「窒息」退到了「重伤」。</p>
<p><strong>8月10日这个日期你要圈起来</strong>：伦敦框架协议设了这个截止日。如果谈崩，瞬间弹回145%。这种「悬崖风险」会在截止日前2-3周开始被市场定价。</p>
</div>

<div class="insight">
<h4>第四课：10年期美债 4.5% 为什么重要？</h4>
<p>10年期美国国债收益率是<strong>地球上最重要的一个数字</strong>：</p>
<ul style="margin:8px 0 8px 24px; color:#334155;">
<li><strong>它是所有资产的定价分母</strong>。股票、房产、比特币——所有未来现金流的折现都用它做基准。10Y越高 → 分母越大 → 资产估值越低。</li>
<li><strong>4.5% 是一个心理阈值</strong>。历史上超过4.5%开始出问题：2018年10月达到3.2%就引发了四季度暴跌；2023年10月冲到5%时区域银行爆了一轮。</li>
<li><strong>黄金跌就是因为这个</strong>。黄金不生息，当10Y给你4.5%的无风险回报时，持有黄金的机会成本就很高。</li>
</ul>
</div>

<h2>🎯 对你意味着什么</h2>

<h3>短期（接下来 2-4 周）</h3>
<ol style="margin:8px 0 8px 24px; color:#334155;">
<li><strong>保持防御仓位。</strong> Fed 鹰 + 贸易不确定性 = 风险资产波动大。不要在这个环境下追高。</li>
<li><strong>关注 8 月 10 日前后的市场波动。</strong> 中美贸易大限是近期最大的事件风险。</li>
<li><strong>美元短期偏强。</strong> DXY 在 100+，Fed 鹰派支撑。</li>
</ol>

<h3>中期（下半年）</h3>
<ol style="margin:8px 0 8px 24px; color:#334155;">
<li><strong>中国的真正刺激可能要等。</strong> 花旗预测 H2 降 10bp，但前提是 Fed 松口 + 国内数据继续走弱。<strong>盯住 PMI 和社融这两个先行指标。</strong></li>
<li><strong>黄金如果有回调可以考虑长线建仓。</strong> 地缘风险+各国央行买金趋势未变。</li>
<li><strong>科技突破层面</strong>：线粒体-细胞核和 ruptoblast 都是基础科学——短期无法交易，但标注了未来 5-10 年的方向。</li>
</ol>

<h3>你应该盯紧的三个信号</h3>
<table>
<thead><tr><th>#</th><th>信号</th><th>看到什么就行动</th></tr></thead>
<tbody>
<tr><td>1</td><td><strong>中美 8/10 大限</strong></td><td>谈成 → 港股/A 股情绪反弹；谈崩 → 减仓到防守</td></tr>
<tr><td>2</td><td><strong>中国 PMI（每月最后一天）</strong></td><td>连续 &lt; 49 → 政策必出，提前布局利率敏感资产</td></tr>
<tr><td>3</td><td><strong>美联储下次 FOMC</strong></td><td>如果实际加息 → 全球资产重估，现金为王</td></tr>
</tbody></table>

<div class="oneliner">
📌 今日一句话：中美同时在6月中旬出手——中国推制度型开放（人民币国际化），美国锁定通胀优先（鹰派Fed），贸易战从145%悬崖边拉回谈判桌但8月10日大限倒计时。全球资产定价的锚（10Y美债4.5%）正在重估。
</div>

<div class="footer">来源：PBoC · SCMP · J.P. Morgan · BBC · Nikkei Asia · Nature · Cell · Stanford News · 中科院</div>

</body></html>"""

# ============================================================
# 日报 2: 2026-06-21
# ============================================================
daily_0621 = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>宏观日报 — 2026年6月21日</title>
""" + CSS + """
</head>
<body>

<div class="cover">
  <h1>📰 宏观日报</h1>
  <div class="meta"><span>📅 2026年6月21日（周日）</span><span>📆 覆盖：6月19日–21日</span></div>
</div>

<h2>🇨🇳 中国线</h2>

<p><strong>LPR连续13月按兵不动。</strong> 6月21日，央行公布1年期LPR维持3.0%、5年期LPR维持3.5%，自2025年5月以来未作调整。尽管内需疲弱（5月社零同比-0.6%），央行选择"稳汇率优先"——在美联储鹰派、美元走强的背景下，降息空间被压缩。</p>

<p><strong>陆家嘴论坛释放金融开放信号。</strong> 央行行长潘功胜宣布六大举措：①完善短端利率调控机制；②设立境外央行回购工具；③上海自贸区启动离岸人民币外汇交易试点，工、农、中、建、交、中信六大行首批获批。证监会主席吴清宣布深化科创板改革，将AI、量子技术、生物制造、具身智能纳入优先上市赛道。</p>

<p><strong>"AI+消费"与平台经济新政连发。</strong> 八部门联合发布《关于加快"AI+消费"发展的意见》，布局人形机器人消费产品赛道。七部门发布《平台经济中小企业发展行动计划(2026-2028)》，推进算法透明化、引导平台降费、打击"内卷式"竞争。</p>

<p><strong>国新办6月22日高调发布会。</strong> 商务部、发改委、财政部联合亮相，推出"利用外资固稳促优"一揽子政策。</p>

<h2>🌍 国际线</h2>

<p><strong>美联储：沃什首秀，鹰派亮剑。</strong> 6月FOMC维持利率3.50-3.75%不变，但删除了"宽松倾向"措辞。点阵图巨变：9/18官员预计年内至少加息一次（3月为零）。新任主席沃什承诺"不惜代价恢复价格稳定"。市场定价12月加息概率升至89%。</p>

<p><strong>ECB与BOJ跟进紧缩。</strong> 欧洲央行6月11日加息25bp至2.25%（2023年以来首次），拉加德称"这只是开始"。日本央行6月16日加息25bp至1.00%（1995年以来最高），日元贬值压力是重要催化剂。</p>

<p><strong>中美制裁升级。</strong> 中国商务部6月22日宣布对10家美国军工/稀土企业实施出口管制（含MP Materials、USA Rare Earth），财政部禁止政府采购46家美国防务公司产品——直接反制美国6月初将阿里巴巴、百度、比亚迪等列入1260H清单。双方"缓和窗口"正在收窄。</p>

<p><strong>美伊和平协议脆弱不堪。</strong> 6月15日签署的MOU（含60天谈判窗口、分阶段重开霍尔木兹海峡、解除伊朗石油制裁、3000亿美元重建基金）一度推动布油暴跌至$77。但周末伊朗以以色列违反黎巴嫩停火为由，威胁重新封锁海峡。</p>

<h2>💰 关键资产价格</h2>
<table>
<thead><tr><th>资产</th><th>最新水平</th><th style="width:60px">周涨跌</th><th>背景驱动</th></tr></thead>
<tbody>
<tr><td>10Y美债</td><td>4.48%</td><td class="tag-down">-2bp</td><td>鹰派美联储+油价下跌对冲</td></tr>
<tr><td>10Y中债</td><td>1.73%</td><td class="tag-down">-4bp</td><td>弱基本面+资金面转松</td></tr>
<tr><td>USDCNH（离岸）</td><td>6.7838</td><td class="tag-up">+0.5%</td><td>美元走强+中美利差扩大</td></tr>
<tr><td>DXY</td><td>100.75</td><td class="tag-up">+1.0%</td><td>美联储鹰派转向+避险需求</td></tr>
<tr><td>布油</td><td>$77.0</td><td class="tag-down">-10%</td><td>美伊和平协议压低风险溢价</td></tr>
<tr><td>金价</td><td>$4,160</td><td class="tag-down">-1.5%</td><td>强势美元+加息预期压制</td></tr>
<tr><td>沪深300</td><td>4,942</td><td class="tag-up">+0.2%</td><td>AI+科创板改革提振情绪</td></tr>
<tr><td>S&P 500</td><td>7,501</td><td class="tag-up">+0.9%</td><td>AI驱动纳斯达克+2.5%</td></tr>
</tbody></table>

<h2>🔬 科技突破扫描</h2>
<p><em>今日无重大科技突破。6月中旬值得关注的科学进展：江门中微子实验(JUNO)首批物理成果（<em>Nature</em>封面）；宾州州立大学世界首个全二维材料CMOS计算机（<em>Nature</em>）。均为超过一周的突破。</em></p>

<h2>🧠 专家拆解</h2>

<div class="insight">
<h4>第一课：为什么美联储鹰派，中国就不能降息？——"利率不可能三角"</h4>
<p>中国经济这么弱，为什么央行不降息？答案是：<strong>在资本流动开放的世界上，一个国家的利率，从来不是自己说了算。</strong></p>
<p style="background:#f1f5f9; padding:12px; border-radius:6px; font-size:13px;">
<strong>美联储鹰派 → 美债收益率升至4.5% → 中美10年期利差扩大至277bp（4.48% - 1.73%）→ 套利资金卖出人民币买美元 → 人民币贬值压力 → 央行若要降息，利差进一步扩大 → 贬值加速 → 资本外流 + 进口通胀</strong>
</p>
<div class="ref">💡 <strong>大国降息通常发生在全球利率下行周期中。</strong> 当美联储在加息，你逆势降息，本质上是在告诉全世界"我的货币不如他的值钱"。</div>
</div>

<div class="insight">
<h4>第二课：美伊和平协议——为什么油跌了40%但事情还没完？</h4>
<table>
<thead><tr><th style="background:#059669;color:#fff">乐观情景（概率~40%）</th><th style="background:#d97706;color:#fff">基准情景（概率~40%）</th><th style="background:#dc2626;color:#fff">悲观情景（概率~20%）</th></tr></thead>
<tbody>
<tr><td>60天内达成正式和平协议，伊朗石油全面回归，布油跌至$60-65</td><td>谈判反复拉锯，部分进展但无最终协议，布油在$70-85震荡</td><td>谈判破裂，海峡再次封锁，布油迅速弹回$100+</td></tr>
</tbody></table>
<p><strong>你应该关注什么？</strong> 不要只看油价——要关注：<strong>①每周CPI/PCE是否因油价下跌而回落、②美联储官员是否提及"油价下跌缓解通胀压力"、③伊朗实际出口量是否回升</strong>。只有当油价下跌通过通胀数据"传导"到央行政策路径上，才算真正落定。</p>
</div>

<div class="insight">
<h4>第三课：中美"制裁对等化"——从"我打你忍"到"你打我还"</h4>
<p>这一次中国反制有两个质的区别：<strong>①覆盖面扩大</strong>——一次性制裁56家美国企业；<strong>②工具更丰富</strong>——出口管制+政府采购禁令+不可靠实体清单组合使用。</p>
<div class="counter">⚠️ 中美"5月北京峰会缓和窗口"正在关闭。如果你在考虑任何涉及跨境的投资或生意，要把"中美关系不确定性溢价"重新计入判断。</div>
</div>

<h2>🎯 对你意味着什么</h2>

<h3>短期（2-4周）</h3>
<ul style="margin:8px 0 8px 24px; color:#334155;">
<li><strong>盯紧6月25日（周四）美国5月PCE数据。</strong> 核心PCE若≥3.4%：加息概率跳升，美元继续走强。若≤3.2%：市场重定价"鹰派过度"，风险资产反弹。</li>
<li><strong>关注6月23-25日夏季达沃斯论坛。</strong> 中国高层常在达沃斯释放政策信号。</li>
<li><strong>警惕美伊谈判的周末风险。</strong> 不要在周五满仓风险资产。</li>
</ul>

<h3>中期（下半年）</h3>
<ul style="margin:8px 0 8px 24px; color:#334155;">
<li><strong>全球利率环境的底层逻辑已经改变。</strong> 三大央行（Fed+ECB+BOJ）同步收紧为2022年以来首次。</li>
<li><strong>中国的政策路径：财政发力 > 货币宽松。</strong> 央行降息空间被封堵，真金白银会从财政口出。</li>
<li><strong>如果美伊和平协议落地，油价中枢下移至$60-75。</strong> 这将是全球通胀缓解的最大单一利好。</li>
</ul>

<h3>你应该盯紧的 2-3 个信号</h3>
<table>
<thead><tr><th>信号名</th><th>看到什么就行动</th></tr></thead>
<tbody>
<tr><td><strong>美国核心PCE</strong></td><td>连续两月回落至3.0%以下 → 加息预期降温；连续两月≥3.5% → 加息定局，防御优先</td></tr>
<tr><td><strong>USDCNH 是否突破 7.0</strong></td><td>接近7.0无干预 → 央行容忍更大贬值空间；6.8处大面积干预 → 汇率风险可控</td></tr>
<tr><td><strong>美伊谈判新闻标题</strong></td><td>出现"breakthrough"→ 油价下探$65；出现"collapse"→ 油价反弹至$100+</td></tr>
</tbody></table>

<div class="oneliner">📌 今日一句话：全球央行从"放水"到"收水"的同步转向已成定局，而美伊和平协议是唯一可能打破这个方向的变量——一个脆弱的和平，撑着一个脆弱的希望。</div>

<div class="footer">来源：Reuters · Bloomberg · CNBC · MarketWatch · Trading Economics · 中国人民银行 · 国新办 · 东方财富 · 21世纪经济报道 · Barclays Research · TD Economics</div>

</body></html>"""

# ============================================================
# 前瞻周报: 2026-06-28
# ============================================================
preview_0628 = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>前瞻周报 — 2026年6月28日</title>
""" + CSS + """
</head>
<body>

<div class="cover">
  <h1>🔮 前瞻周报</h1>
  <div class="meta"><span>📅 2026年6月28日</span><span>📆 覆盖：6月22日–27日</span></div>
</div>

<h2>📅 下周核心事件日历</h2>

<table>
<thead><tr><th>日期</th><th>时间</th><th>事件</th><th>前值</th><th>预期</th><th>为什么重要</th><th>超预期意味</th><th>不及预期意味</th></tr></thead>
<tbody>
<tr>
  <td><strong>6/22 周一</strong></td><td>09:15</td><td>🇨🇳 中国6月LPR（1Y/5Y）</td><td>3.0%/3.5%</td><td>不变</td><td>货币政策风向标；在Fed鹰派+内需走弱矛盾中，央行是否松动？</td><td>—</td><td>若意外下调：A股和地产股大幅反弹</td>
</tr>
<tr>
  <td><strong>6/23 周二</strong></td><td>16:00</td><td>🇪🇺 欧元区6月制造业PMI初值</td><td>48.7</td><td>49.0</td><td>ECB刚加息25bp，经济能否承受？</td><td>回到50以上：ECB加息底气足</td><td>跌破48：滞胀担忧升温</td>
</tr>
<tr>
  <td>6/23 周二</td><td>21:45</td><td>🇺🇸 美国6月标普全球制造业PMI</td><td>55.1</td><td>54.5</td><td>美国制造业是否延续扩张？</td><td>保持55+：支持Fed鹰派</td><td>跌至52以下：抑制加息预期</td>
</tr>
<tr>
  <td>6/23 周二</td><td>全天</td><td>🌐 夏季达沃斯论坛开幕（大连）</td><td>—</td><td>—</td><td>中国高层常借机释放政策信号</td><td>暗示"加大财政力度"→A股催化剂</td><td>基调偏紧→市场情绪回落</td>
</tr>
<tr>
  <td><strong>6/24 周三</strong></td><td>盘后</td><td>🇺🇸 美光科技(MU) Q3财报</td><td>—</td><td>—</td><td>AI/HBM存储需求核心晴雨表</td><td>双超预期→AI/半导体继续高歌</td><td>指引不及预期→纳斯达克承压</td>
</tr>
<tr style="background:#fef2f2;">
  <td><strong>⭐ 6/25 周四</strong></td><td>20:30</td><td>🇺🇸 <strong>美国5月核心PCE年率</strong></td><td>3.3%</td><td><strong>3.4%</strong></td><td><strong>Fed最看重通胀指标；鹰派转向后第一个验证数据</strong></td><td>≥3.5%：12月加息概率破90%，美债破4.6%，美元冲101+</td><td>≤3.2%：市场重定价"鹰派过度"，风险资产全面反弹</td>
</tr>
<tr style="background:#fef2f2;">
  <td>6/25 周四</td><td>20:30</td><td>🇺🇸 <strong>美国Q1 GDP终值</strong></td><td>1.6%</td><td>1.7%</td><td>一季度经济全貌</td><td>高于1.8%：经济韧性支撑加息</td><td>低于1.5%：滞胀担忧浮现</td>
</tr>
<tr>
  <td>6/25 周四</td><td>20:30</td><td>🇺🇸 5月耐用品订单月率</td><td>+8.0%</td><td>-4.7%</td><td>企业投资意愿关键指标</td><td>降幅小于-3%：企业投资信心好</td><td>降幅大于-6%：前景堪忧</td>
</tr>
<tr>
  <td>6/25 周四</td><td>20:30</td><td>🇺🇸 初请失业金（截至6/20）</td><td>22.2万</td><td>22.5万</td><td>劳动力市场是否出现裂痕？</td><td>高于24万：加息空间受限</td><td>低于21万：加息更有底气</td>
</tr>
<tr>
  <td>6/25 周四</td><td>凌晨</td><td>🏦 美联储银行压力测试结果</td><td>—</td><td>—</td><td>决定大银行资本缓冲要求</td><td>全部通过→金融股正面</td><td>部分未通过→信贷收紧担忧</td>
</tr>
<tr>
  <td>6/25 周四</td><td>盘后</td><td>🎮 英伟达股东大会</td><td>—</td><td>—</td><td>AI总龙头战略方向</td><td>积极展望→AI领涨</td><td>保守表述→短期回调</td>
</tr>
<tr>
  <td><strong>6/26 周五</strong></td><td>22:00</td><td>🇺🇸 6月密歇根消费者信心终值</td><td>60.5</td><td>60.8</td><td>消费者真实感受+通胀预期</td><td>信心回升+通胀预期降→软着陆</td><td>信心降+通胀预期升→滞胀</td>
</tr>
<tr>
  <td>6/26 周五</td><td>全天</td><td>🎤 FOMC三票委密集讲话</td><td>—</td><td>—</td><td>威廉姆斯+古尔斯比+<strong>卡什卡利（鹰派）</strong></td><td>若提"油价缓解通胀"→鸽派</td><td>若坚持"需要更多证据"→鹰派</td>
</tr>
<tr>
  <td><strong>6/27 周六</strong></td><td>09:30</td><td>🇨🇳 中国5月规上工业企业利润</td><td>4.0% YoY</td><td>—</td><td>企业盈利最直接衡量指标</td><td>利润增速回升→制造业信心改善</td><td>增速放缓→政策刺激呼声增强</td>
</tr>
</tbody></table>

<h2>🧠 专家拆解：下周真正的焦点</h2>

<div class="insight">
<h4>焦点一：6月25日美国核心PCE——"一个数字决定下半年的利率叙事"</h4>
<p><strong>为什么PCE比CPI更重要？</strong> CPI是劳工统计局发布的"消费者价格指数"，而<strong>PCE是美联储官方钦定的通胀目标指标</strong>。区别在于PCE考虑了消费者的"替代效应"，覆盖范围更广，通常比CPI低0.3-0.5个百分点。</p>

<p><strong>当前环境的特殊性：</strong> 新任美联储主席沃什删除了政策声明中的"宽松倾向"措辞，并以"不惜代价恢复价格稳定"结尾。<strong>美联储从"想降息但不敢"变成了"准备好加息"。</strong></p>

<table>
<thead><tr><th>PCE结果</th><th>市场推演</th></tr></thead>
<tbody>
<tr style="background:#fef2f2;"><td><strong>≥3.5%（高于预期）</strong></td><td>核心通胀连续两月加速 → 7月FOMC可能直接加息 → 美债10Y破4.6% → 美元指数冲向102 → 全球risk-off</td></tr>
<tr><td><strong>3.3-3.4%（符合预期）</strong></td><td>通胀"停滞在3%+" → 维持现状但鹰派不改 → 区间震荡</td></tr>
<tr style="background:#f0fdf4;"><td><strong>≤3.2%（低于预期）</strong></td><td>通胀意外回落 → 12月加息概率骤降 → 美债回落至4.3% → 风险资产狂欢</td></tr>
</tbody></table>

<div class="ref">💡 <strong>关键联动</strong>：5月PCE数据采集期油价还在$100+，6月PCE采集期油价已跌至$77。这意味着——即使5月PCE很热，市场也可能"向前看"，因为6月数据几乎肯定会因油价暴跌而明显回落。沃什当然知道这一点。他的鹰派姿态是在为"未来"定价——确保即使油价下跌缓解通胀，Fed也不会立刻回到宽松路径。</div>
</div>

<div class="insight">
<h4>焦点二：全球PMI日（6月23日）——经济"体检报告"集体出炉</h4>
<p>周二覆盖法国、德国、欧元区、英国、美国的PMI集中发布。<strong>PMI是经济周期最灵敏的先行指标</strong>——它问的是采购经理"你觉得下个月会更好还是更差"。</p>
<table>
<thead><tr><th>全球PMI组合</th><th>含义</th></tr></thead>
<tbody>
<tr><td>美国强 + 欧元区弱</td><td>"美国例外论"继续 → 强美元、资金回流美国</td></tr>
<tr><td>美国弱 + 欧元区弱</td><td>全球同步放缓 → 大宗商品承压、避险受益</td></tr>
<tr><td>美国强 + 欧元区强</td><td>全球共振复苏 → 央行更有底气加息</td></tr>
<tr><td>美国弱 + 欧元区强</td><td>资金可能从美国流向欧洲 → 美元走弱</td></tr>
</tbody></table>
</div>

<h2>🎯 你下周应该关注什么</h2>

<h3>1. 哪个日期最值得花时间关注？</h3>
<p><strong>6月25日（周四）——"超级星期四"。</strong> 一天之内：核心PCE + Q1 GDP + 耐用品订单 + 初请失业金 + 美联储压力测试 + 英伟达股东大会。<strong>这是2026年以来信息密度最高的一天。</strong></p>

<h3>2. 什么结果会改变你对当前宏观环境的判断？</h3>
<ul style="margin:8px 0 8px 24px; color:#334155;">
<li><strong>核心PCE ≤3.2% + 初请失业金 ≥24万 →</strong> 重新评估"Fed鹰派可持续性"——通胀回落+劳动力松动=鹰派可能"过了"。</li>
<li><strong>核心PCE ≥3.5% + 初请失业金 ≤21万 →</strong> 确认"加息已成定局"——通胀和就业双双支持收紧。</li>
<li><strong>PMI（周二）全面跌破50 →</strong> 全球经济正在滑向衰退——压倒性地改变所有其他判断。</li>
</ul>

<h3>3. "如果X就做Y"决策矩阵</h3>
<table>
<thead><tr><th>情景</th><th>风险资产（股票）</th><th>避险资产（国债/黄金）</th><th>美元</th></tr></thead>
<tbody>
<tr style="background:#fef2f2;"><td>PCE热(≥3.5%) + PMI强(>54) — "高通胀+强增长"</td><td>⚠️ 短期承压</td><td>❌ 利率上行=国债跌</td><td>✅ 强美元</td></tr>
<tr style="background:#fef2f2;"><td>PCE热(≥3.5%) + PMI弱(<52) — "滞胀"</td><td>❌ 盈利+估值双杀</td><td>✅ 避险需求</td><td>⚠️ 先强后弱</td></tr>
<tr style="background:#f0fdf4;"><td>PCE冷(≤3.2%) + PMI强(>54) — "金发女孩"</td><td>✅ 估值+盈利共振</td><td>❌ 风险偏好上升</td><td>❌ 美元走弱</td></tr>
<tr style="background:#f0fdf4;"><td>PCE冷(≤3.2%) + PMI弱(<52) — "软着陆在即"</td><td>✅ 估值修复驱动</td><td>✅ 利率下行利好</td><td>❌ 美元走弱</td></tr>
</tbody></table>

<div class="oneliner">⚠️ 以上不构成投资建议。下周宏观和微观会产生叠加效应——美光财报+英伟达股东大会可能引发"AI泡沫质疑"，不要只看宏观一边。</div>

<div class="footer">来源：Reuters · Bloomberg · CNBC · MarketWatch · Trading Economics · 东方财富 · 21世纪经济报道 · Christophe Barraud · TD Economics · Smartkarma</div>

</body></html>"""

# Write all files
files = {
    r'D:\news\日报-2026-06-20.html': daily_0620,
    r'D:\news\日报-2026-06-21.html': daily_0621,
    r'D:\news\周报-前瞻-2026-06-28.html': preview_0628,
}

for path, content in files.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'{os.path.basename(path)}: {os.path.getsize(path)} bytes ({os.path.getsize(path)//1024} KB)')

print('Done!')
