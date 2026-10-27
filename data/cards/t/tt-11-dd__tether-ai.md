# tt-11-dd/tether-ai

⭐ 95 · TypeScript · MIT · 推送 2026-10-09 · [GitHub](https://github.com/tt-11-dd/tether-ai) · [官网](https://tether-code.xyz) · 个人维护 · 中文 README

**本地优先的 AI 编程工作台，让模型安全地检视和修改代码库**

基于 Pi 生态（tether-agent-core 封装）构建的 Electron 桌面 AI 编程代理，面向真实代码库：将模型调用、工作区工具、终端命令、权限确认、会话历史与 diff 审查集于一处。默认聚焦 DeepSeek，兼容 OneAPI、Ollama、vLLM 等 OpenAI 兼容端点。提供 Plan/Ask/Auto/Full 四种权限模式、macOS Seatbelt 沙箱、补丁检查点与 /undo 恢复、MCP/Hooks/Skills 支持。UI 与会话数据留存本地 ~/.tether，无遥测、无中继代理；macOS（arm64）与 Windows 10/11 提供下载包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- DeepSeek 优先，支持 OneAPI/Ollama/vLLM 等 OpenAI 兼容端点
- Plan/Ask/Auto/Full 四种权限模式与 macOS Seatbelt 沙箱
- 补丁检查点支持 /undo 恢复上一轮文件变更
- MCP、Hooks、Skills、规划与子代理集成

## 适用场景

- 让 DeepSeek 等模型在权限边界内检视、编辑并验证我的仓库
- 在本地桌面端跟踪工具调用、diff 与上下文用量的编码任务
- 通过 /skill:name 调用项目或全局 agent 技能

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: **A local-first AI coding workbench built on the Pi ecosystem**
> L15: Tether is an Electron desktop agent for real codebases. It brings model calls, workspace tools, terminal commands, 

## 星数曲线

```mermaid
xychart-beta
    title "tt-11-dd/tether-ai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 93 --> 96
    line [94, 95, 95]
```

2026-10-18 94 → 2026-10-27 95（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `26cfd8d46a82` · [字段定义](../../DATASET.md)*
