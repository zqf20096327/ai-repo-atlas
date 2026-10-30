# fhhyyp/serein-flow

⭐ 188 · C# · 推送 2026-10-14 · [GitHub](https://github.com/fhhyyp/serein-flow) · 个人维护 · 中文 README

**Web 端工作流编排引擎，内置 MCP 供 AI 客户端安全操作流程**

面向需要创建、维护和运行项目工作流的开发者：由 Vue+Vite 可视化 Web 控制台、ASP.NET Core API、隔离的 Worker Runner 进程与 HTTP/stdio MCP 服务组成。Web 控制台管理项目、流程、版本、运行与环境设置；不受信的脚本与插件仅在独立 Worker 进程中运行。内置 MCP 服务以访问密钥鉴权，向 AI 客户端暴露受控的 tools/resources/prompts，并附 Skill 素材包供 AI 工具生成本地技能。从源码本地运行：dotnet 启动 API（默认 127.0.0.1:8188），npm 启动前端；环境假定 Windows，需 .NET SDK 10 与 Node.js。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可视化 Web 控制台管理项目、流程、版本、运行与环境设置
- 不受信脚本与插件在独立 Worker Runner 进程中隔离运行
- 内置 HTTP/stdio MCP 服务，密钥鉴权，向 AI 客户端暴露受控 tools/resources/prompts
- 提供类型化 HTTP 客户端 SDK（SereinFlow.SDK）与本地 MCP Skill 素材包

## 适用场景

- 在可视化界面中创建并运行项目工作流
- 让 AI 工具通过 MCP 接入，安全地操作流程与节点
- 在隔离进程中运行第三方脚本与插件

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L16: and plugins run only in separate Worker Runner processes. The MCP service
> L17: exposes controlled tools, resources, and prompts so AI clients can work with
> L22: |`src/SereinFlow.Api`|ASP.NET Core API and the HTTP/stdio MCP host.|

## 星数曲线

```mermaid
xychart-beta
    title "fhhyyp/serein-flow 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 186 --> 189
    line [187, 188, 188]
```

2026-10-18 187 → 2026-10-30 188（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `92b06fd012b1` · [字段定义](../../DATASET.md)*
