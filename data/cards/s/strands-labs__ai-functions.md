# strands-labs/ai-functions

⭐ 335 · Python · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/strands-labs/ai-functions) · [官网](https://strandsagents.com) · 组织维护

**Python 库：用 AI agent 执行的函数与自校验工作流**

基于 Strands 的 Python 库，提出『AI Function』抽象：函数签名与 docstring 由库转为 prompt，交由 agent 执行并返回带类型校验的原生 Python 对象。核心机制包括 post-conditions 自纠错循环、Lean 证明的可验证模块、有状态 AI Thread、多线程协调的 agent 团队、跨进程/机器的分布式运行，以及按美元声明价值与 token 成本的模型选择。支持所有 Strands 模型提供方，默认 Amazon Bedrock；内置 Claude Code、Kiro、Codex 会话包装器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- post-conditions 校验失败自动重新提示，直到通过或达上限
- experimental.verified 模块：Lean 检查证明，ai_compile 可生成免模型调用的机器码实现
- AI Thread 协议使外部运行时（Claude Code/Kiro/Codex）作为线程加入团队
- coordinator/client 分离实现跨进程分布式执行

## 适用场景

- 把重复任务声明为函数，由 agent 执行并自动校验结果
- 构建互相发现与委派的多 agent 工作流
- 在数据管道中让 agent 处理任意格式文件返回 DataFrame

## 场景标签

 · 领域:LLM 基础设施/Agent 框架

## 证据(README 行号)

> L23: Strands AI Functions is a Python library built around a new abstraction: functions that behave like standard Python
> L43: AI Functions supports all Strands model providers and defaults to Amazon Bedrock (see Configuring Credentials). To 

## 星数曲线

```mermaid
xychart-beta
    title "strands-labs/ai-functions 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 332 --> 336
    line [333, 335, 335]
```

2026-10-18 333 → 2026-10-22 335（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `5a9732dd4183` · [字段定义](../../DATASET.md)*
