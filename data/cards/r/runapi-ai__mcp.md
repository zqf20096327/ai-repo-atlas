# runapi-ai/mcp

⭐ 56 · TypeScript · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/runapi-ai/mcp) · [官网](https://runapi.ai) · 组织维护

**连接 RunAPI 的 MCP 服务器：模型发现、定价查询与媒体任务创建**

面向 MCP 兼容编码工具的 RunAPI 客户端：提供 9 个工具，涵盖浏览 160+ 模型目录（图像/视频/音频/实用 4 种模态）、查看模型输入约束与运行时定价、提示词搜索、创建媒体任务（需幂等键）、查询任务状态与账户余额。目录类工具无需 API key（使用构建时内嵌合约数据），认证操作通过浏览器登录、RUNAPI_API_KEY 或共享配置完成。本包为纯客户端，不运行本地生成后端；提供本地 stdio 与托管远程 MCP 两种接入方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 个工具覆盖模型目录、定价、提示词搜索、任务创建与余额查询
- 目录/定价/提示词工具无需 API key，基于内嵌合约数据
- create_task 支持幂等键与等待/非等待两种模式
- 提供 Claude Code、Cursor、VS Code、Windsurf、Roo Code 配置生成

## 适用场景

- 在编码助手中按模态查找并比较 RunAPI 生成模型与当前定价
- 让助手选好模型并直接创建图像/视频/音乐生成任务
- CI 或无头环境通过 RUNAPI_API_KEY 查询任务状态与余额

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L20: RunAPI MCP Server connects MCP-compatible coding tools to RunAPI.
> L26: This package is a pure client.

## 星数曲线

```mermaid
xychart-beta
    title "runapi-ai/mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 54 --> 57
    line [55, 56, 56]
```

2026-10-18 55 → 2026-10-31 56（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `63f682138d76` · [字段定义](../../DATASET.md)*
