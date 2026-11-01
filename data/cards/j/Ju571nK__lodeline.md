# Ju571nK/lodeline

⭐ 15 · Rust · Apache-2.0 · 推送 2026-10-31 · [GitHub](https://github.com/Ju571nK/lodeline) · [官网](https://lodeline.dev) · 个人维护

**扫描 AI 编程 agent 配置并评分暴露风险的安全工具**

用 Rust 编写的本地配置扫描器，读取 Claude Code、Codex、Cursor、Gemini CLI、Antigravity、Continue.dev、Claude Desktop 等编码 agent 的 sandbox、hooks、MCP、权限与指令文件配置，检测无沙箱、通配 hooks、本地命令 MCP、空 deny 列表、提示注入等问题并输出评分。默认只测量不拦截，拦截为可选。可选 fleet 模式通过 mTLS 汇聚多机事件至中央服务器，供 SIEM 接入与策略下发。作者声明处于 alpha 阶段、单人维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 读取 7 种编码 agent 的配置并输出暴露评分
- 检测规则覆盖 sandbox/hooks/MCP/权限 deny 列表/提示注入
- 可选 fleet 模式：mTLS 事件上报、SIEM 接入、签名策略下发
- lodeline-mcp 让 agent 通过 MCP 读取自身风险评分

## 适用场景

- 在 agent 运行前检查本机编码 agent 配置的暴露面
- 多机无人值守跑编码 agent 时汇总各主机风险态势
- 把 agent 配置风险事件接入 SIEM 做监控

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: **A config scanner for AI coding agents.** Claude Code, Codex, and Cursor can run
> L49: Across the agents you actually run: **Claude Code, Codex, Cursor, Gemini CLI, Antigravity, Continue.dev, Claude Des
> L91: `lodeline-mcp` exposes the score over plain MCP, so an AI client can read its own


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `88ba212513df` · [字段定义](../../DATASET.md)*
