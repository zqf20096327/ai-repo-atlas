# anton-abyzov/ccx-go

⭐ 21 · Go · MIT · 推送 2026-04-02 · [GitHub](https://github.com/anton-abyzov/ccx-go) · 个人维护

**Go 实现的终端 AI 编程助手 CLI**

CCX（Community Code Extended）项目的 Go 实现：终端内的 AI 编程助手，以 9.3MB 单二进制分发，基于 Bubbletea/Charm 构建全功能 TUI。接入 Anthropic Claude API（SSE 流式响应），内置 11 个工具（Bash、FileEdit、Grep、Agent 等）与斜杠命令；多 agent 编排采用每 agent 一个 goroutine 加 channel 通信；含 4 层上下文压缩、MCP 协议客户端、基于规则 DSL 的权限系统与 markdown 技能加载。通过 git clone 编译或 go install 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 11 个内置工具：Bash/文件读写编辑/Grep/Agent/WebFetch 等
- goroutine-per-agent 多 agent 编排，channel IPC 与 context 取消
- 4 层上下文压缩（micro/auto/session/full）与 MCP 协议客户端
- 9.3MB 静态二进制，无运行时依赖

## 适用场景

- 在终端里通过对话让 AI 读写代码并执行命令
- 需要单二进制、无依赖部署的本地 AI 编程助手
- 通过 markdown 技能与 MCP 客户端扩展工具能力

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: AI coding assistant CLI in Go, part of the CCX (Community Code Extended) project. 9.3MB binary, 11 tools, full TUI. 
> L22: export ANTHROPIC_API_KEY="your-key-here"

## 星数曲线

```mermaid
xychart-beta
    title "anton-abyzov/ccx-go 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `bccb958f6273` · [字段定义](../../DATASET.md)*
