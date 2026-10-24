# tomohiro-owada/devrag

⭐ 64 · Go · 推送 2026-04-15 · [GitHub](https://github.com/tomohiro-owada/devrag) · 个人维护 · 中文 README

**面向 Claude Code 开发者的本地 Markdown 向量检索 MCP 服务器**

用 Go 编写的单二进制 RAG 工具，为使用 Claude Code 的开发者提供本地 Markdown 文档语义检索：自动索引 .md 文件，基于 multilingual-e5-small 嵌入模型（ONNX Runtime 推理，模型首次运行自动下载）与 sqlite-vec 向量库，通过 MCP 协议向 Claude Code 暴露 search/index/list/delete/reindex 等工具，也可作为独立 CLI 使用。支持 macOS CoreML GPU 加速并自动回退 CPU，支持目录与 glob 模式配置、增量同步。限制：仅索引 Markdown 文件，首次运行需联网下载模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单二进制分发，无需 Python，模型首次运行自动下载
- 基于 multilingual-e5-small 嵌入与 sqlite-vec 的本地语义检索
- MCP 服务器与独立 CLI 两种使用方式，输出 JSON 或文本
- GPU/CPU 自动检测，macOS 支持 CoreML 加速

## 适用场景

- 让 Claude Code 用向量检索代替整文件读取以节省 token
- 团队对大文档仓库做本地语义检索，Git 同步后自动更新索引
- 以 CLI 方式在脚本中查询本地 Markdown 笔记

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L29: - 💻 **CLI & MCP** - Use as MCP server or standalone CLI commands
> L147: DevRag provides the following tools via Model Context Protocol:

## 星数曲线

```mermaid
xychart-beta
    title "tomohiro-owada/devrag 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 63 --> 65
    line [64, 64]
```

2026-10-18 64 → 2026-10-24 64（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `eb21d3e60a18` · [字段定义](../../DATASET.md)*
