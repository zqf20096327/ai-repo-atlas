# xiwan/acp-bridge

⭐ 96 · Python · Apache-2.0 · 推送 2026-09-28 · [GitHub](https://github.com/xiwan/acp-bridge) · [官网](https://aws.amazon.com/cn/blogs/china/enable-kiro-and-claude-code-for-im-with-acp-bridge-async-ai-workflow/) · 个人维护 · 中文 README

**把本地 CLI 编程 agent 暴露为 HTTP 服务的多 agent 编排平台**

面向团队与机器人场景的多 agent 编排平台：通过 ACP 协议将本机 CLI agent（Kiro、Claude Code、Codex、Qwen、OpenCode、Hermes、AWS DevOps Agent 等）封装为 HTTP 服务，支持顺序/并行/竞争/对话式流水线编排、IM（Discord/飞书）驱动的异步任务、webhook 回调，以及虚拟 agent auto 的自动路由。零配置启动时自动探测已安装的 agent CLI；配套 bridge-ctl/stack-ctl 控制脚本与 litellm/mantle-proxy 组成的服务栈。Apache 2.0 许可，提供 Docker 与 systemd 部署文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将多种 CLI agent 经 ACP 暴露为统一 HTTP 服务
- 顺序/并行/竞争/对话式多 agent 流水线编排
- Discord/飞书 IM 驱动的异步任务与 webhook 回调
- 零配置启动：自动探测已安装的 agent CLI

## 适用场景

- 一台 EC2 跑 Kiro+Claude+Codex，团队经 HTTP 共同调用
- 在 Discord/飞书发消息让 agent 执行任务并回推结果
- 把多个 agent 串成流水线做重构或代码审查的异步任务

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L17: A multi-agent orchestration platform that exposes local CLI agents (Kiro, Claude Code, Codex, Qwen, OpenCode, Herme
> L25: |**Team AI gateway**|One EC2 runs Kiro + Claude + Codex; everyone calls them via HTTP — no local install needed|
> L105: |Pipelines|Multi-agent orchestration: sequence, parallel, race, conversation|

## 星数曲线

```mermaid
xychart-beta
    title "xiwan/acp-bridge 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 94 --> 97
    line [95, 96, 96]
```

2026-10-18 95 → 2026-10-27 96（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d97c4ca7cdf4` · [字段定义](../../DATASET.md)*
