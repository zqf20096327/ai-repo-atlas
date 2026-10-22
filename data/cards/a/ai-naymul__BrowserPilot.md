# ai-naymul/BrowserPilot

⭐ 180 · TypeScript · MIT · 推送 2026-07-26 · [GitHub](https://github.com/ai-naymul/BrowserPilot) · [官网](https://pilotbrowser.vercel.app/) · 个人维护

**自然语言驱动的浏览器抓取 agent，绕过反爬并输出结构化数据**

用自然语言提示控制浏览器导航与数据抽取的工具：AI 基于截图决策而非 CSS 选择器，输出 JSON/CSV/PDF/HTML/Markdown 等格式。抓取基于 Patchright（Playwright 分支）、完整 Chromium + xvfb、指纹轮换与拟人行为，README 列出对 DataDome/Akamai/Cloudflare/PerimeterX 等反爬系统的加载测试结果。支持 10 并发 worker 的批量抓取（断点续传、自适应限速、上下文轮换）。需配置 GOOGLE_API_KEY（Gemini），可选代理。提供 Docker 与源码两种安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言提示驱动浏览器导航，AI 基于截图决策而非选择器
- 输出 JSON/CSV/PDF/HTML/Markdown 等多种结构化格式
- 10 并发批量抓取引擎：断点续传、自适应限速、上下文轮换
- 提供针对 Pixelscan/Sannysoft 等检测工具的可复现 benchmark 命令

## 适用场景

- 跨电商平台监控价格并导出结构化 JSON
- 从 LinkedIn、G2 等带登录墙或无限滚动的站点抽取线索数据
- 批量抓取受 DataDome/Akamai/Cloudflare 保护的站点

## 场景标签

 · 领域:网页抓取/浏览器自动化

## 证据(README 行号)

> L12:  Type what you want → AI navigates any website → get structured data back.
> L206: The AI doesn't rely on CSS selectors or DOM structure — it looks at a screenshot and decides what to do. When a si

## 星数曲线

```mermaid
xychart-beta
    title "ai-naymul/BrowserPilot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 179 --> 181
    line [180, 180]
```

2026-10-18 180 → 2026-10-22 180（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `35f7c18290ce` · [字段定义](../../DATASET.md)*
