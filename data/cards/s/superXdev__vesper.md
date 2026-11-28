# superXdev/vesper

⭐ 3 · TypeScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/superXdev/vesper) · [官网](https://vesper.frd.lol) · 个人维护

**面向市场/营销人员：调研公司与竞对，产出增长渠道与实验建议**

Vesper 从公开信息调研一家公司及最多 4 个竞品，输出客户获取渠道信号强度、市场缺口与可执行的营销实验；每条洞察附带证据引用（如 `A3`），无法核验的内容标记为 Not checked。技术栈为 Vue 3 + Hono + BullMQ + PostgreSQL/Drizzle，含 CLI 与 MCP 服务器。默认走规则分析（免费），配置 AI_PROVIDER 后叠加跨来源洞察，AI 调用失败时回退到规则结果；无鉴权，仅建议绑定本机回环地址。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 调研公司与最多 4 个竞品，输出各增长渠道信号强度对比表
- 每条洞察附带证据引用，不可核验项标记为 Not checked
- 默认规则分析免费，可选 anthropic/openai/openai-compatible/claude-code/codex 引擎
- 提供 web 界面、CLI 与 MCP 服务器三种使用方式

## 适用场景

- 调研竞品在各营销渠道的表现并寻找市场缺口
- 为下一个增长实验筛选机会点
- 通过 MCP 客户端在对话中调用公司调研结果

## 场景标签

 · 领域:商业情报/营销分析

## 证据(README 行号)

> L5: Vesper researches a company and up to 4 competitors from public information, then shows how they appear to acquire c
> L189: Vesper always runs a rule-based analysis. An AI engine, when configured, adds positioning and cross-source insight


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `3ebd6ae8e0c9` · [字段定义](../../DATASET.md)*
