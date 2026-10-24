# LSTM-Kirigaya/slidev-mcp

⭐ 91 · Jinja · MIT · 推送 2025-11-17 · [GitHub](https://github.com/LSTM-Kirigaya/slidev-mcp) · [官网](https://kirigaya.cn/openmcp) · 个人维护 · 中文 README

**面向 Slidev 的 MCP 服务器：让 LLM 生成与管理网页幻灯片**

基于 TypeScript 与 Vue 3 实现的 MCP 服务器，封装 Slidev 幻灯片流程供 AI agent 调用：提供环境检查、创建/加载 Slidev 项目、封面生成、增改查页面、网页内容抓取转 markdown 等工具，用户以自然语言描述即可让 LLM 自动生成在线 PPT。生成的项目默认存放于 `.slidev-mcp` 目录，可通过 `SLIDEV_MCP_ROOT` 环境变量（须绝对路径）自定义。详细安装步骤指向外部快速开始指南，README 本体未列出命令。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP 工具集：创建/加载 Slidev 项目、增改查幻灯片页面
- 封面生成（make_cover）与 add_page/set_page/get_page 内容管理
- websearch 工具抓取网页并输出 markdown 供幻灯片取材
- SLIDEV_MCP_ROOT 环境变量自定义项目根目录

## 适用场景

- 通过对话让 AI agent 帮我生成 Slidev 网页幻灯片
- 让 agent 加载并修改我已有的演示文稿
- 从网页内容取材自动填充幻灯片

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L16: slidev-mcp is an intelligent slide generation tool based on Slidev that integrates large language model technology,
> L48: The MCP server provides the following tools for slide creation and management:

## 星数曲线

```mermaid
xychart-beta
    title "LSTM-Kirigaya/slidev-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 90 --> 92
    line [91, 91]
```

2026-10-18 91 → 2026-10-24 91（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `270050cda85c` · [字段定义](../../DATASET.md)*
