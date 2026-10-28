# yeuxuan/Ace-Mcp-Node

⭐ 359 · TypeScript · 推送 2026-04-20 · [GitHub](https://github.com/yeuxuan/Ace-Mcp-Node) · 个人维护 · 中文 README

**为 AI 助手提供代码库索引与语义搜索的 MCP Server**

Acemcp 的 Node.js/TypeScript 实现，作为 MCP 服务器向 Claude、GPT 等 AI 助手提供代码库索引与语义搜索能力：提供 search_context 工具，接收项目根目录与自然语言查询，自动增量索引（SHA-256 哈希去重、批量上传、大文件分块），返回带文件路径和行号的代码片段。支持 stdio 传输与仅绑定 localhost 的 Web 管理界面（配置编辑、实时日志、工具调试、中英双语）。与 Python 版共享配置与数据格式。需配置外部索引/搜索 API（BASE_URL/TOKEN）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- search_context 工具：自然语言语义搜索并返回带行号的代码片段
- 增量索引、SHA-256 哈希缓存、批量上传与大文件分块
- WSL 完整路径支持（UNC 与 /mnt 自动转换）与多编码检测（UTF-8/GBK/GB2312/Latin-1）
- Web 管理界面：配置编辑、实时日志、工具调试、中英双语

## 适用场景

- 让 Claude 等 MCP 客户端理解并搜索大型代码库
- 在 WSL 与 Windows 混合环境下检索项目代码
- 通过 Web 界面调试 MCP 工具调用与查看日志

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L17: **Acemcp** 是一个高性能的 MCP (Model Context Protocol) 服务器，专为 AI 助手（如 Claude、GPT 等）提供**代码库索引**和**语义搜索**能力。通过 Acemcp，AI 助手可
> L56: - ✅ **search_context 工具** - 语义搜索代码片段
> L57: - ✅ **stdio 传输** - 标准输入输出通信


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `01d0e3acb7fa` · [字段定义](../../DATASET.md)*
