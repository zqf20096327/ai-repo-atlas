# dhy365-creator/codex-third-party-subagents

⭐ 15 · JavaScript · MIT · 推送 2026-09-01 · [GitHub](https://github.com/dhy365-creator/codex-third-party-subagents) · 个人维护 · 中文 README

**让 Codex 以有界子代理形式接入第三方/国产模型 API 的兼容层**

面向使用 OpenAI Codex Desktop 的开发者的版本限定兼容与安装验证层：在保持 Codex 主代理与 OpenAI 模型为主的前提下，将 DeepSeek、MiniMax、阿里百炼 Qwen 等第三方模型作为受审查的有界子工作进程处理单一文本/代码任务。机制包括 Keychain 凭据、版本范围 Host 门控、只读 Doctor、dry-run 优先安装器、owner-only 单槽任务桥与回退边界；Codex 保留结果审查与最终接受权。Provider 运行时仅限 macOS，Windows 仅支持配置安装；大量版本处于 HOST BLOCKED 或 UNKNOWN 状态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- DeepSeek V4 Flash Public Beta（maintainer E2E，macOS）与 MiniMax-M3 / Qwen3.7-Max 运行时已验证
- 版本范围 Host 门控：0.149.x HOST BLOCKED，未知版本 fail closed
- API key 仅从 macOS Keychain 读取，dry-run 默认、--apply 才生效
- 路由策略基于实时配额数据，配额查询失败时回退 OpenAI worker

## 适用场景

- 在 Codex 配额受限时把有界任务委派给 DeepSeek/MiniMax/Qwen 等第三方模型
- 在 macOS 上以可控方式为 Codex 配置国产模型子代理
- 用 Doctor 和 verifier 排查 Codex 多代理与跨供应商兼容状态

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L10: bounded third-party model handoffs in Codex, with **Codex retaining final
> L69: Reviewed provider packs, command-backed Keychain authentication, a

## 星数曲线

```mermaid
xychart-beta
    title "dhy365-creator/codex-third-party-subagents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `124440d10645` · [字段定义](../../DATASET.md)*
