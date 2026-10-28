# unicodeveloper/competitor-analysis

⭐ 37 · TypeScript · 推送 2026-04-20 · [GitHub](https://github.com/unicodeveloper/competitor-analysis) · [官网](https://competitor-analysis.up.railway.app) · 个人维护

**输入竞品网址自动生成深度调研报告的 Web 应用**

基于 Next.js 与 Valyu Deep Research API 构建的竞品分析 Web 应用：用户输入竞品网站 URL 与背景信息，系统调用 Valyu 的 AI 深度研究能力检索多来源并生成含公司概况、产品、市场定位与近期动态的报告，过程带实时进度（fast 模型约 5 分钟，heavy 最长 90 分钟）。支持 Markdown 展示、可点击来源引用与 PDF 导出。提供自托管（需 Node.js 20+ 与 Valyu API key，pnpm 安装运行）和 Valyu 平台 OAuth 两种模式，可部署到 Railway。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 调用 Valyu Deep Research API 生成竞品调研报告
- 异步架构+客户端轮询，实时分步进度与百分比展示
- 报告支持 Markdown 渲染、来源引用与 PDF 导出
- 自托管与 Valyu 平台 OAuth 两种运行模式

## 适用场景

- 输入竞品网址快速获得产品与市场定位调研报告
- 团队自托管部署后做竞品研究
- 导出带来源引用的 PDF 调研报告

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: A competitor analysis tool built with Next.js and Valyu Deep Research API.
> L17: - **Deep Research**: Leverages Valyu's AI to search multiple sources and analyze content
> L145: - **AI Research**: Valyu Deep Research API

## 星数曲线

```mermaid
xychart-beta
    title "unicodeveloper/competitor-analysis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-28 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b09792ef59b6` · [字段定义](../../DATASET.md)*
