# Zentar-Ai/Zentara-Code

⭐ 83 · TypeScript · Apache-2.0 · 推送 2026-03-17 · [GitHub](https://github.com/Zentar-Ai/Zentara-Code) · [官网](https://zentar.ai) · 组织维护

**VS Code 的 AI 编码助手扩展：聊天驱动改码与运行时调试**

Zentara Code 是一个 VS Code 扩展，把聊天指令转化为代码库变更：通过并行子代理执行独立任务（隔离上下文、opt-in 写权限、超时控制），基于 LSP 做语义级代码理解（25+ 工具，符号、引用、调用层级），并集成运行时调试（35+ 调试操作：断点、单步、状态检查）以在提交变更前验证行为。工作流为 Plan→Approvals→Execute→Analyze→Verify。推荐使用 Claude Max 订阅作为 LLM Provider，需另行安装对应语言的调试扩展（如 Python + debugpy）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 并行子代理执行，隔离上下文与严格范围分离
- 25+ LSP 语义工具用于代码理解与安全重构
- 集成运行时调试（35+ 操作）验证变更
- 审批机制：文件写入、网络等敏感操作需显式批准

## 适用场景

- 通过聊天指令实现功能、修 bug 和重构代码
- 在提交前用集成的调试器验证修改行为
- 用并行子代理加速独立任务的处理

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: Zentara Code turns chat instructions into precise, auditable changes in your codebase. It is optimized for speed, sa
> L13: - **Parallel subagents**: Independent workers run simultaneously with strict scope separation, opt‑in write permiss
> L15: - **Runtime debugging**: Launch, control, and inspect debug sessions from tasks to reproduce, instrument, step, and

## 星数曲线

```mermaid
xychart-beta
    title "Zentar-Ai/Zentara-Code 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 82 --> 84
    line [83, 83]
```

2026-10-18 83 → 2026-10-28 83（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `06570d922b1c` · [字段定义](../../DATASET.md)*
