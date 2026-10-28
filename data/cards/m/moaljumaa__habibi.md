# moaljumaa/habibi

⭐ 25 · TypeScript · NOASSERTION · 推送 2026-08-09 · [GitHub](https://github.com/moaljumaa/habibi) · [官网](https://opsily.com/hosting/habibi?utm_source=github&utm_medium=readme&utm_campaign=habibi) · 个人维护

**自托管的品牌 AI 可见性与引用追踪器**

面向 AEO/GEO 从业者的开源自托管应用：定时将一组提示词发送到 ChatGPT、Claude、Gemini、Perplexity（经单一 OpenRouter key），或驱动真实登录态浏览器 UI 抓取，解析哪个品牌被提及、哪个 URL 被引用，存储后展示逐页引用映射、提及率（每提示运行 N 次应对非确定性）、竞品份额与周度趋势。引导式向导读取用户网站并生成品牌档案与起始提示集；提供运行前成本预估与花费上限。Docker 或 Node.js 22+ 部署，采用 Sustainable Use License。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 页级引用映射：哪个 URL、哪条提示、哪个引擎
- 四引擎 API 通道 + 四个免 key 的登录态浏览器抓取引擎
- 每提示 N 次运行生成提及率，处理非确定性
- 运行前成本预估与单次/每日花费上限

## 适用场景

- 追踪品牌在 ChatGPT/Claude/Gemini/Perplexity 回答中的提及与引用
- 对比竞品在同一批答案中的曝光份额
- 按周观察 AI 搜索可见性趋势

## 场景标签

 · 领域:营销/SEO 监测

## 证据(README 行号)

> L16: **a set of prompts × a set of engines, run daily → parse who got mentioned and which URLs
> L29: - **Page-level citation mapping** — not just "we got mentioned" but *which URL got cited, for

## 星数曲线

```mermaid
xychart-beta
    title "moaljumaa/habibi 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `303b3237b321` · [字段定义](../../DATASET.md)*
