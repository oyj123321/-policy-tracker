# Policy Tracker — AI 驱动的政策与产业周报<br><sub>AI-Powered Policy & Industry Weekly Report</sub>

每周自动聚合中国 & 国际产业政策、宏观信号、AI/半导体/新能源行业动态。
<br>*Weekly aggregation of China & global industrial policy, macro signals, AI/semiconductor/clean energy developments.*

---

## 📸 效果预览 / Preview

### 周报 · Weekly Policy Report
![Weekly](screenshot.png)

### 日报 · Daily Macro Brief
| June 20 | June 21 |
|---------|---------|
| ![Daily0620](screenshot-daily-0620.png) | ![Daily0621](screenshot-daily-0621.png) |

### 下周前瞻 · Weekly Preview
![Preview](screenshot-preview-0628.png)

---

## 🚀 快速开始 / Quick Start

本项目由 **Claude Code + 人工审核** 驱动。生成一期报告共三步。
<br>*This project is powered by Claude Code with human review. Three steps per report.*

### 1. 启动研究 Agent / Launch Research
```
搜索上周全球产业政策，按行业分中+国际汇总，保存到 D:\news\周报-政策追踪-YYYY-MM-DD.html（用本周一的日期）。
```
Claude 会自动 / *Claude will*：
- 并行搜索中国/美国/欧盟/日韩等区域政策 · *Parallel search across CN/US/EU/JP/KR*
- 按行业分类整理 · *Categorize by sector*
- 生成带完整 CSS 的 HTML 报告 · *Generate styled HTML*

### 2. 审核 & 迭代 / Review & Iterate
- 浏览器打开 HTML · *Open in browser, check completeness*
- 缺漏则追问 Claude 补充 · *Ask Claude to fill gaps*
- 排版不满意可当场改 CSS · *Tweak CSS live*

### 3. 发布 / Publish
```bash
git add -A && git commit -m "周报 YYYY-MM-DD" && git push
```

---

## 📋 报告体系 / Report Types

| 报告 Report | 频率 Freq | 内容 Content |
|-------------|-----------|---------------|
| **周报-政策追踪** Weekly Policy | 每周一 Mon | 中+国际产业政策、深度拆解、下周关注<br>*CN & global policy, deep analysis, next-week watch* |
| **日报-宏观** Daily Macro | 不定期 Ad-hoc | 当日重大宏观事件、资产价格、科技突破<br>*Daily macro events, asset prices, sci-tech breakthroughs* |
| **周报-前瞻** Weekly Preview | 每周日 Sun | 下周事件日历、核心数据预期、决策矩阵<br>*Next-week event calendar, data expectations, decision matrix* |

---

## 🎨 报告特性 / Features

| 特性 Feature | 说明 Description |
|-------------|------------------|
| 纯 HTML | 表格列宽精确，`Ctrl+P` 导出 PDF · *Pixel-perfect tables, print-to-PDF* |
| 变动标记 | 每行政策标注 vs 上周 ↑↓→ · *Week-over-week change indicators* |
| 市场映射 | 表格后附黄底斜体市场反应行 · *Market reaction rows after each table* |
| 深度拆解 | 历史参照 + 反对观点 + 量化预测 · *Historical refs + counter-views + projections* |
| 来源分级 | 🟢 官方一手 / 🔵 权威媒体 / ⚪ 券商智库 · *Tiered source credibility* |

---

## 🤖 Claude 默认搜索流程 / Default Search Pipeline

每次生成周报前执行以下搜索（同组并行）：
<br>*The following searches run before each report (groups run in parallel):*

### 第一轮 / Round 1（并行 4 路）
| # | 搜索内容 Search Query |
|---|----------------------|
| 1 | 中国产业政策最新：新能源/电动车/半导体/房地产/消费/农业 |
| 2 | US CHIPS Act / IRA / semiconductor export controls latest |
| 3 | EU CBAM / green industrial policy / critical raw materials latest |
| 4 | 全球电动车关税 + 芯片管制 + 日韩半导体投资 |

### 第二轮 / Round 2（按需补充 / On-demand）
| # | 搜索内容 Search Query |
|---|----------------------|
| 5 | 中国专项债发行进度 + 以旧换新补贴具体数据 |
| 6 | EU-China EV tariff / anti-subsidy latest |
| 7 | 日韩东南亚半导体投资：TSMC熊本、三星、SK海力士 |
| 8 | 下周全球经济数据发布日历（仅前瞻周报需要） |

### 写作规范 / Writing Standards
- 政策名 + 类型（新政/续期/加码/收紧）+ 金额 + 有效期 + 要点 + 市场映射
- 金额列不能写"—"，必须填具体数字或解释无法获取 · *No empty amount cells*
- 每条深度拆解含：为什么现在出 + 历史参照 + 反对观点 + 后续演化 · *Why now + history + counter-view + what's next*
- 来源分级：官方一手公告 > 权威媒体报道 > 券商/智库分析 · *Official > Media > Analyst*

---

## 📁 文件结构 / File Structure

```
D:\news\
├── gen_report_v2.py              # 周报 HTML 模板 / Weekly template
├── gen_daily_reports.py          # 日报+前瞻模板 / Daily + Preview template
├── CLAUDE.md                     # Claude Code 自动加载的 prompt
├── 周报-政策追踪-YYYY-MM-DD.html  # 每周报告 / Weekly report
├── 日报-YYYY-MM-DD.html          # 日报 / Daily macro brief
├── 周报-前瞻-YYYY-MM-DD.html      # 下周前瞻 / Weekly preview
├── screenshot*.png               # 效果图 / Screenshots
└── README.md
```

---

## ⚠️ 免责 / Disclaimer

市场数据仅作信息参考，不构成投资建议。
<br>*Market data is for informational purposes only and does not constitute investment advice.*
