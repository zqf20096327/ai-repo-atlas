# fancyyan/xiaohongshu-content-collector

⭐ 29 · JavaScript · MIT · 推送 2026-10-01 · [GitHub](https://github.com/fancyyan/xiaohongshu-content-collector) · 个人维护 · 中文 README

**小红书笔记被动采集与多模态 AI 分析的 Chrome 扩展 + MCP 工具箱**

由 Chrome 扩展与本地 MCP server 组成：扩展被动拦截浏览过的小红书公开笔记，存入本地 IndexedDB，支持 JSON/JSONL/Markdown/训练数据导出；可调用自配 API Key 的模型做图文/视频分析、爆款拆解、仿写、标签与博主画像。MCP server 提供 6 个本地语料工具与 5 个经本机 xiaohongshu-cli 的实时只读工具，可接入 Claude Desktop/Cursor/Cline。不配置 AI Key 采集与导出仍可用；项目声明仅限个人学习研究，平台风控风险由使用者承担。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 被动采集推荐流/搜索/详情页数据并存本地 IndexedDB
- 多模态 AI 分析：爆款潜力、仿写、标签、选题、博主画像
- MCP 提供 11 个工具（6 个本地语料 + 5 个实时只读 CLI）
- 多格式导出含训练数据格式；CLI 调用强制串行、只读白名单、脱敏

## 适用场景

- 浏览小红书时顺带收集笔记并批量整理导出
- 用 AI 拆解爆款笔记、获取仿写与标签建议
- 把本地语料接入 Claude Desktop/Cursor 等 MCP 客户端做检索分析
- 导出训练数据格式用于模型微调

## 场景标签

`网页抓取` `多模态` · 领域:效率与自动化

## 证据(README 行号)

> L9: 本地优先的小红书内容采集、AI 分析与 MCP 工具箱。
> L47: - 支持图文分析、视频多帧分析、爆款潜力、仿写、标签、选题和博主画像。
> L201: **不配置 AI API Key 可以使用吗？** 可以。采集、导出和 MCP 本地语料工具不需要 AI API Key。

## 星数曲线

```mermaid
xychart-beta
    title "fancyyan/xiaohongshu-content-collector 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-28 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `d17bdc71f5d1` · [字段定义](../../DATASET.md)*
