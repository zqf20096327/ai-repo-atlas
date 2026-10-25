# lingcoder/crab-code

⭐ 76 · Rust · MIT · 推送 2026-10-14 · [GitHub](https://github.com/lingcoder/crab-code) · [官网](https://github.com/lingcoder/crab-code) · 组织维护 · 中文 README

**Rust 实现的开源 Claude Code 替代品：可接任意 LLM 的 Agentic 编程 CLI**

用 Rust 从零构建的终端 Agentic 编程工具，对齐 Claude Code 的工具集、权限模型与交互模式，支持 Anthropic/OpenAI/DeepSeek/Bedrock/Vertex 等多种 LLM 提供商接入。提供多层配置合并（defaults→plugin→user→project→local→CLI→env）、MCP 三种传输、Agent Teams 协作模式与会话间后台记忆整理。代码规模为 25 个 crate、约 16.1 万行、4940 个测试；通过 git clone 加 cargo build 从源码构建，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 Anthropic / OpenAI / DeepSeek / Bedrock / Vertex 等多提供商接入
- 与 Claude Code 工具集、权限模型、交互模式兼容
- 25 个 Rust crate 分四层架构，4940 个测试
- MCP 三种传输与 Agent Teams 协调模式

## 适用场景

- 在终端里让任意 LLM 执行思考、规划与编码任务
- 从 Claude Code 迁移到开源方案并复用原有工作流
- 按项目/用户/环境变量分层管理多提供商配置

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L14: Crab Code is a Rust-native agentic coding CLI. It aligns with Claude Code's toolset, permission model, and interact
> L3: **Open-source alternative to Claude Code, built from scratch in Rust.**

## 星数曲线

```mermaid
xychart-beta
    title "lingcoder/crab-code 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 75 --> 77
    line [76, 76]
```

2026-10-18 76 → 2026-10-25 76（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `5c4c7fb6e367` · [字段定义](../../DATASET.md)*
