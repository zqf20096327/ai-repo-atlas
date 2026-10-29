# magicdrive/ark

⭐ 25 · Go · MIT · 推送 2026-10-28 · [GitHub](https://github.com/magicdrive/ark) · 个人维护 · 中文 README

**面向 AI 编码 agent 的代码智能引擎（MCP 服务器）**

静态单二进制程序，解析代码仓库、抽取声明与引用、按各语言作用域规则解析引用指向，构建代码图谱并通过 MCP 协议的 21 个工具供编码 agent 查询调用关系、变更影响与符号上下文。分析 Go/TypeScript/TSX/PHP/Terraform/Rust/Java/JavaScript/Python 等，不执行仓库代码。每个答案带置信级别与未解析计数；不做类型推断，模块解析不等价于编译器。附 Claude Code/Cursor/Codex/Cline/Copilot 等客户端一键接入与仓库转储、秘密屏蔽功能。

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

- 21 个 MCP 工具：调用者/被调用者追踪、变更影响分析、token 预算控制的符号上下文
- 引用解析附 exact/strong/candidate/unresolved 置信级别，歧义名返回声明列表而非静默选择
- 静态单二进制，不执行仓库代码，无出站网络连接
- 秘密屏蔽与 .arkignore 排除机制

## 适用场景

- 让编码 agent 在大仓库中查函数调用关系与变更影响范围
- 编辑前为 agent 提供聚焦的符号级上下文而非整文件
- 将仓库结构转储为单文本供 agent 阅读

## 场景标签

 · 领域:开发工具/代码智能

## 证据(README 行号)

> L10: what each reference points to, and serves the resulting graph to coding
> L11: agents over the Model Context Protocol.
> L81: `setup` adds Ark's entry to the client's MCP configuration and leaves every

## 星数曲线

```mermaid
xychart-beta
    title "magicdrive/ark 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-29 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `43a6a7b8e426` · [字段定义](../../DATASET.md)*
