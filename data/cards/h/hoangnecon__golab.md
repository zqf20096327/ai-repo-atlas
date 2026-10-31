# hoangnecon/golab

⭐ 15 · Go · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/hoangnecon/golab) · 个人维护

**Go 编写的本地 MCP Server：让 AI 客户端控制与读写 Google Colab**

以 Go 从零实现的 Model Context Protocol 服务器，通过 WebSocket 连接本地浏览器与远程 Colab 虚拟机，向 AI 客户端暴露 23 个工具：打开笔记本、读取/编辑/执行单元格、读写 Colab VM 与已挂载 Google Drive 上的文件、查询环境信息等。静态工具架构不依赖 tools/list_changed 通知，可在 Cursor、Claude Desktop、Gemini Code Assist 等 MCP 客户端使用。支持 go run 直接从 GitHub 拉取运行或下载预编译二进制，需本机安装 Go；Drive 挂载需用户在 Colab UI 手动完成 OAuth 确认。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 23 个 MCP 工具覆盖单元格读写执行、文件 I/O、环境查询
- 静态工具架构，不要求客户端支持 tools/list_changed 通知
- 三种运行方式：go run 云端模块、预编译二进制等
- 通过 WebSocket 连接本地代理与 Colab，COLAB_TOKEN 鉴权

## 适用场景

- 在 Cursor/Claude Desktop 等 IDE 中让 AI 直接操作我的 Colab 笔记本
- 让 agent 在 Colab GPU 环境上远程执行代码并读取输出
- 通过 AI 读写已挂载的 Google Drive 文件

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L10: GoLab is a highly optimized, cross-platform server implementing the Model Context Protocol (MCP) for Google Colab. 
> L17: - **Universal Compatibility**: Works fluently with Cursor, Claude Desktop, Gemini Code Assist, Windsurf, and Antigr
> L72: GoLab exposes **23 tools** to grant your AI comprehensive control over remote execution pipelines.

## 星数曲线

```mermaid
xychart-beta
    title "hoangnecon/golab 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `753185dc54a2` · [字段定义](../../DATASET.md)*
