# damiano1996/incoder-plugin

⭐ 16 · Java · Apache-2.0 · 推送 2026-01-07 · [GitHub](https://github.com/damiano1996/incoder-plugin) · 个人维护

**为 JetBrains IDE 提供 LLM 代码补全与聊天辅助的插件**

面向 IntelliJ IDEA、PyCharm 等 JetBrains IDE 的插件，将 LLM 引入开发流程，提供代码生成、理解、补全与智能操作。聊天内内置本地工具：命令行执行（需确认）、生成 unified diff 并以合并对话框审阅、文件扫描/读取/创建；支持接入 MCP 服务器并动态发现其工具。另提供实时 ghost text 行内补全（Tab 接受），该功能处于快速迭代中。主要在 IntelliJ IDEA 与 PyCharm 上测试，兼容多数 JetBrains IDE。以 Apache License 发布，通过 JetBrains Marketplace 分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 聊天内本地工具：终端命令执行（需确认）、diff 补丁与合并审阅、文件操作
- 可附加 MCP 服务器并动态发现其工具
- 实时 ghost text 行内代码补全
- 主要测试于 IntelliJ IDEA 与 PyCharm，兼容多数 JetBrains IDE

## 适用场景

- 在 JetBrains IDE 内通过聊天生成、理解和修改代码
- 编码时获得实时行内补全建议
- 通过 MCP 服务器扩展聊天可用的工具

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L16: It seamlessly integrates advanced Large Language Models (LLMs) into your development workflow, providing you with c
> L15: **InCoder** is a powerful plugin designed for JetBrains IDEs, including IntelliJ IDEA, PyCharm, and others in the J

## 星数曲线

```mermaid
xychart-beta
    title "damiano1996/incoder-plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `5f4216d11b6f` · [字段定义](../../DATASET.md)*
