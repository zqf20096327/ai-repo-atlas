# Snehil-Shah/LibreSprite-MCP

⭐ 38 · JavaScript · GPL-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/Snehil-Shah/LibreSprite-MCP) · [官网](https://pypi.org/project/libresprite-mcp) · 个人维护

**让 LLM 通过 MCP 远程操作 LibreSprite 的服务器**

面向 LibreSprite 像素画软件的 Model Context Protocol (MCP) 服务器：通过在 LibreSprite scripts 目录运行远程脚本 mcp.js，与 MCP 服务器（默认端口 64823）建立连接，使 Claude Desktop / Cursor 等 MCP 客户端能用自然语言进行提示词辅助的编辑、设计与脚本编写。以 PyPI 包发布，推荐用 uv/uvx 运行。限制：仅支持单实例、实现未被广泛测试，MCP 资源文档与示例有限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- MCP 协议接入，自然语言驱动 LibreSprite 编辑/设计/脚本
- PyPI 发布，uvx libresprite-mcp 一行启动
- 通过 mcp.js 远程脚本与 LibreSprite 建立连接
- 支持 Claude Desktop 与 Cursor 作为客户端

## 适用场景

- 用对话方式让 Claude 帮我在 LibreSprite 里画像素图
- 通过 MCP 客户端远程脚本化 LibreSprite 的编辑操作

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L8: Model Context Protocol (MCP) server for prompt-assisted editing, designing, and scripting inside LibreSprite.
> L44: - **Claude Desktop & Cursor**

## 星数曲线

```mermaid
xychart-beta
    title "Snehil-Shah/LibreSprite-MCP 星数(近 4 点)"
    x-axis ["2026-10-23", "2026-10-25", "2026-10-29", "2026-10-30"]
    y-axis "stars" 35 --> 39
    line [36, 37, 38, 38]
```

2026-10-23 36 → 2026-10-30 38（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c903496cd02f` · [字段定义](../../DATASET.md)*
