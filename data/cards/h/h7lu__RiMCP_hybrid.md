# h7lu/RiMCP_hybrid

⭐ 44 · C# · MIT · 推送 2026-02-19 · [GitHub](https://github.com/h7lu/RiMCP_hybrid) · 个人维护 · 中文 README

**RimWorld 源码与 XML 定义的混合检索 MCP 服务器，供 AI 助手调用**

面向 RimWorld Mod 开发者的代码检索与导航工具：对 C# 源码与 XML Def 建立索引，结合 Lucene/BM25 词法检索、向量语义检索与跨层图关系（继承/调用/XML-C# 绑定），以 MCP 服务器形式通过 stdio/JSON-RPC 暴露 4 个工具（rough_search、get_uses、get_used_by、get_item），可接入 Claude Desktop、VS Code Copilot 等 AI 助手，也可作为 CLI 使用。需 .NET 8 SDK 与 Python 3.9+，嵌入由本地 Python 服务（127.0.0.1:5000）或远程 API（如 OpenAI embeddings）提供；需先用 ILSpy 等导出 RimWorld C# 源码并构建索引。作者在 README 中以中文记录了大量实验过程与迭代方向。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 词法（Lucene/BM25）+ 向量语义 + 图关系三路混合检索
- 4 个 MCP 工具：rough_search / get_uses / get_used_by / get_item，两步检索减少上下文噪声
- 图边存储用位图压缩稀疏矩阵，作者记录从 6.2GB 压缩到 400MB
- v1.1.0 起支持 --api-key/--model-name 连接 OpenAI 等远程嵌入 API

## 适用场景

- 在 Claude Desktop 或 VS Code Copilot 中检索 RimWorld 源码与 XML 定义
- Mod 开发时查询某 Def 引用了哪些 C# 组件、某类被谁使用
- 让 AI 助手按符号名取回完整类/方法/Def 源码片段

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L7: - 这个项目提供了一套面向 RimWorld 源代码与 XML 定义的检索与导航工具，核心目标是把词法检索、语义检索和图结构导航结合起来，构建一个能被 AI 助手调用的服务。项目既可以作为一个命令行工具使用，也可以以 MCP 服务器
> L33: - 要启动这个系统用于交互或集成，最直接的方式是运行 MCP 服务器组件，服务进程以标准输入输出或 JSON-RPC 协议暴露接口，外部的 AI 助手可以向其发送检索与导航请求并接收结构化响应。也可以在命令行模式下运行各个工具命令

## 星数曲线

```mermaid
xychart-beta
    title "h7lu/RiMCP_hybrid 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-29 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `403012df1e21` · [字段定义](../../DATASET.md)*
