# yaowen51888-rich/lumencode

⭐ 41 · JavaScript · 推送 2026-08-24 · [GitHub](https://github.com/yaowen51888-rich/lumencode) · 个人维护 · 中文 README

**统计 15 款 AI 编码工具用量与行级 AI 代码归因的分析工具**

读取 Claude Code、Codex、Copilot CLI 等 15 款 AI 编码工具的本地会话日志，汇总 Token 消耗、费用、模型分布与项目分布；通过工具 hook 记录编辑步骤，把 AI 贡献从提交级细化到行级，每个提交可下钻查看逐行归因证据。内置 600+ 模型定价库（含 GLM/Kimi/Qwen/DeepSeek）加 Portkey API 兜底估算成本，可生成详报/简报/智能报告三种周报，输出 Markdown/飞书/钉钉格式。形态为 npm CLI + Web UI + MCP Server，需 Node.js >= 20 并编译原生 SQLite 依赖，零配置自动检测日志目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 15 款 AI 编码工具日志统一读取与汇总统计
- 行级 AI 归因：hook 步骤追踪 + step 证据，可下钻查看逐行来源
- 600+ 模型定价库（本地 590 条 + Portkey API 兜底）成本估算
- CLI + Web UI + MCP Server（7 个工具）三种使用形态
- 一键生成 Markdown/飞书/钉钉格式的详报/简报/智能报告

## 适用场景

- 统计我每周用了多少 AI 编码额度、花了多少钱
- 向负责人汇报 AI 辅助编码的产出与 ROI
- 多工具并用时对比各 AI 编码工具的使用情况
- 量化某个仓库中 AI 写的代码占比

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L54: 15 款 AI 编码工具，全部 ✅ 完整支持（会话级 / Token 级 / 模型级统计）。
> L95: |🎯 **行级 AI 归因**|不止"AI 帮了这个提交"，而是"这行代码是 AI 写的"——hook 步骤追踪 + step 证据，精确到每一行|
> L185: |`mcp`|启动 MCP Server，供 Claude Code / Cursor 等调用（详见 MCP Server）|

## 星数曲线

```mermaid
xychart-beta
    title "yaowen51888-rich/lumencode 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24", "2026-10-30"]
    y-axis "stars" 38 --> 42
    line [39, 40, 41, 41]
```

2026-10-18 39 → 2026-10-30 41（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f2c302162154` · [字段定义](../../DATASET.md)*
