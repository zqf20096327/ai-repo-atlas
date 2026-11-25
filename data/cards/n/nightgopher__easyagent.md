# nightgopher/easyagent

⭐ 4 · Go · MIT · 推送 2026-11-23 · [GitHub](https://github.com/nightgopher/easyagent) · 个人维护 · 中文 README

**Go 编写的个人 AI 编程助手与 Agent 工作台，多端接入**

以对话方式阅读与修改代码、执行工具并保留可继续的历史会话；底层 Agent 能力以公共 Go SDK 复用，提供桌面（macOS dmg/Linux deb）、Android 原生客户端、Web 工作区、终端 TUI、飞书对话与 MCP 工具接入等多种入口。模型通过 OpenAI 兼容环境变量配置，或经飞书登录 EasyCode 启用账号模型。安装方式包括从源码 make build、Release 二进制/安装包与官方安装脚本；Linux 桌面端需 libwebkit2gtk-4.1。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 桌面、Android、Web、TUI、飞书、MCP 多端接入同一 Agent 流程
- MCP 工具支持 stdio、Streamable HTTP、SSE 与 OAuth，逐工具过滤
- 可复用 Go SDK：模型 Provider、会话、上下文压缩、Skills、本地/SSH 执行
- 循环任务 /loop 与内置联网搜索、网页读取工具

## 适用场景

- 在终端 TUI 里对项目发起单次分析或交互式对话
- 手机/浏览器远程连接主机上的 Agent 处理任务
- 通过飞书账号发起任务并接收生成的文件
- 以 MCP 接入外部工具并按项目授权管理权限

## 场景标签

`编码 Agent` `AI 助手` · 领域:编码与开发

## 证据(README 行号)

> L3: **Go 驱动的个人 AI 编程助手与 Agent 工作台，支持桌面、Android、Web、TUI、飞书和 MCP。**
> L7: 在对话中阅读与修改代码、执行工具、查看过程与结果，并保留可继续的历史会话。日常使用以桌面或浏览器工作区为中心，也可以从终端或已配对的飞书账号发起任务。底层 Agent 能力通过公共 Go SDK 复用。
> L17: - **可复用 SDK**：模型 Provider、工具、会话、上下文压缩、Skills、本地/SSH 执行和 AgentSession。

## 星数曲线

```mermaid
xychart-beta
    title "nightgopher/easyagent 星数(近 3 点)"
    x-axis ["2026-10-26", "2026-11-13", "2026-11-25"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-26 3 → 2026-11-25 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `9b169218ec8c` · [字段定义](../../DATASET.md)*
