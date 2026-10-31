# FTShare-Lab/agent-claim-network

⭐ 44 · Rust · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/FTShare-Lab/agent-claim-network) · [官网](https://ftshare-lab.github.io/agent-claim-network/) · 组织维护 · 中文 README

**终端通用 AI 助手，带可追溯 Claim 知识共享与分歧裁决**

Rust 编写的终端 TUI 通用 AI 助手（`acn`）：自然语言执行查资料、改文件（出 diff）、跑命令、看图片/PDF、接 MCP 工具与 Skill。核心机制是 Claim——会话压缩或结束时自动复盘生成带 holder/scope/置信度/证据的判断，写入本机 trace。单人模式即可独立使用；接入仓库内的 Router 与 Maintainer 两个可执行文件后，各 Agent 的 Claim 可互相检索、引用，冲突记为 Dispute，由 Maintainer 自动分析或人工裁决。支持 Anthropic Messages、OpenAI-compatible 与 Responses 协议。当前仅支持 macOS 与 x86_64 glibc Linux，不支持 Windows/Alpine/ARM64 Linux。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 会话自动复盘生成带 holder/scope/置信度/证据的 Claim 并写 trace
- 团队模式下 Claim 经 Router 互检、Dispute 由 Maintainer 自动或人工裁决
- 支持 MCP（stdio/Streamable HTTP）、Skill、并行子代理、后台进程
- 支持 Anthropic Messages / OpenAI Chat Completions / Responses 三种协议

## 适用场景

- 在终端用自然语言让助手查资料、改文件、跑命令
- 多 Agent 团队共享可检索、可追溯的判断并处理分歧
- 单人模式下沉淀可复用的结论，减少重复提问

## 场景标签

`AI 助手` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L31: 执行 `acn`，用自然语言交代任务：查资料、改文件、跑命令、看图片和 PDF、接外部工具。命令在你本机执行，改动会以 diff 显示。这一层和常见的终端 coding agent 同类，但不限于写代码，而是一个通用助手。
> L33: 另外一层是 Claim。压缩上下文或结束会话时，ACN 会复盘本轮里站得住、以后还用得上的结论，落成一条带适用范围和依据的判断。一个人用时，下次少重复问；多人把各自的 ACN 接入同一套团队服务后，这些判断可以互相看见、引用和质疑

## 星数曲线

```mermaid
xychart-beta
    title "FTShare-Lab/agent-claim-network 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-31 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8e10bc6d7d71` · [字段定义](../../DATASET.md)*
