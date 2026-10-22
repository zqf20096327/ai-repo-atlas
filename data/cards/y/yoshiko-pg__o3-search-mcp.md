# yoshiko-pg/o3-search-mcp

⭐ 286 · JavaScript · MIT · 推送 2026-07-09 · [GitHub](https://github.com/yoshiko-pg/o3-search-mcp) · [官网](https://www.npmjs.com/package/o3-search-mcp) · 个人维护 · 中文 README

**让 AI 编程 agent 咨询 OpenAI o3 网络搜索的 MCP server**

MCP 服务器：注册到 AI 编程 agent（如 Claude Code）后，agent 可自主调用 OpenAI 高端模型（o3/gpt-5/o4-mini，经环境变量选择）及其网络搜索能力，用于排查疑难报错、查阅最新库文档或做设计评审。通过环境变量配置 API Key、搜索上下文大小、推理力度、超时与重试。以 npx 方式或本地 pnpm 构建接入。限制：需 OpenAI API Key，且使用 o3 需将账户升至 Tier 4 或完成组织验证，否则调用报错。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 让 agent 在遇到难题时自主咨询 o3 并利用其网络搜索
- 支持 o3/gpt-5/o4-mini 模型选择及搜索上下文/推理力度配置
- npx 一行注册到 Claude Code，或本地 git clone + pnpm 构建
- SDK 自动在限流（429）、服务端错误与连接错误时重试

## 适用场景

- 调试卡住时让编程 agent 咨询 o3 扫描 GitHub issues 等来源
- 升级依赖库时查询最新文档与选项变更
- 让 agent 在设计复杂系统时向 o3 征求评审意见

## 场景标签

 · 领域:AI 开发者工具/MCP

## 证据(README 行号)

> L7: MCP server that enables the use of OpenAI's high-end models and their powerful web search capabilities.
> L8: By registering it with any AI coding agent, the agent can autonomously consult with OpenAI models to solve complex p

## 星数曲线

```mermaid
xychart-beta
    title "yoshiko-pg/o3-search-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 285 --> 287
    line [286, 286]
```

2026-10-18 286 → 2026-10-22 286（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `1a6f56b6f583` · [字段定义](../../DATASET.md)*
