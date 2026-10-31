# ucmao/unisearch

⭐ 15 · TypeScript · NOASSERTION · 推送 2026-09-16 · [GitHub](https://github.com/ucmao/unisearch) · [官网](https://unisearch.ucmao.cn/) · 个人维护 · 中文 README

**面向创作者与分析师的 AI 多平台采集与深度研报桌面工具**

基于 Electron/TypeScript 的本地优先桌面应用，面向内容创作者、市场运营、行业分析师与学生研究员。用户用自然语言描述调研目标，AI 自动规划任务流程，并发调度底层连接器在 32+ 平台（小红书、抖音、B站、arXiv 等）采集公开数据、清洗排重并生成带来源引用标注的深度研报。内置本地 ONNX 向量语义检索，数据与 Cookie 存本地 SQLite；大模型通过配置 API Key 接入（DeepSeek/OpenAI/Kimi/Ollama 等）。提供 macOS/Windows 安装包或源码运行，源码路径需 Node.js >= 22.12.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言驱动任务规划，32+ 平台并发采集与清洗排重
- 研报观点标注原始网页引用来源与段落编号
- 内置本地 ONNX 向量语义检索，数据与 Cookie 全部留存在本地 SQLite
- 13+ 场景技能（@ 快捷调度），支持导出 Excel/Word/PDF/Markdown/Obsidian

## 适用场景

- 我调研小红书/抖音热门选题并生成有据可查的研报
- 我向多个大模型提问相同问题对比品牌回答与负面风险
- 我批量采集博主主页公开作品与互动指标并导出 Excel

## 场景标签

`网页抓取` `浏览器自动化` `科研工具` · 领域:效率与自动化

## 证据(README 行号)

> L5: **一句话搞定全网调研：AI 驱动的多平台数据采集与深度研报桌面工作台**
> L22: **无需编写任何爬虫代码**，只需在输入框里像聊天一样提出需求，AI 就会自动前往全网数十个平台抓取数据、清洗排重，并为你生成一份结构严谨、有据可查的**深度洞察研报**。
> L103: 1. **填写大模型 API**：输入你常用的大模型 API Key（支持 **DeepSeek、MiniMax、OpenAI、Kimi**，或者本地运行的 **Ollama**）。

## 星数曲线

```mermaid
xychart-beta
    title "ucmao/unisearch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `e6cd48125fe7` · [字段定义](../../DATASET.md)*
