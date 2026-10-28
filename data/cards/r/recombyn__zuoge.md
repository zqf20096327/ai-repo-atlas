# recombyn/zuoge

⭐ 56 · TypeScript · Apache-2.0 · 推送 2026-09-11 · [GitHub](https://github.com/recombyn/zuoge) · [官网](https://recombyn.com) · 组织维护 · 中文 README

**自托管的开源 AI 设计工作台：无限画布+设计 Agent**

开源（Apache-2.0）AI 设计工作区，主体是文档驱动的无限矢量画布（CanvasKit + SceneDocument），内置基于 LangGraph 的 Design Agent，通过流式对话在画布上执行 plan→Skills→tool_ops 流程；提供 MCP server 供 Codex 等外部客户端读写同一项目，支持 Yjs 实时协作、技能/画布插件、Tauri 桌面壳。通过 Docker Compose 自托管（MySQL、Redis、MinIO、API、worker、collab），需自备 LLM API key（DeepSeek/Doubao/OpenRouter 等）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无限矢量画布：形状/文本/图片/布尔运算/导出，SceneDocument 协议
- LangGraph Design Agent：流式对话在画布上执行 tool_ops，AgentProfile YAML 可定制
- MCP canvas：Codex 等外部客户端经同一 tool_ops 契约读写项目（live/headless/离线队列）
- Yjs 实时协作、技能与画布插件系统、Tauri 桌面端

## 适用场景

- 团队自托管一个可通过对话生成和编辑设计的协作画布
- 让 Codex 等 MCP 客户端直接读写设计项目文档
- 通过技能包和画布插件扩展设计能力

## 场景标签

 · 领域:设计工具/AI 应用

## 证据(README 行号)

> L19: An open-source AI design workspace. Document-backed infinite artboard (CanvasKit + SceneDocument), LangGraph Design
> L29: 🤖 **Design Agent** — Streaming chat on the same canvas: plan → Skills → `tool_ops` → apply. Fixed LangGraph kernel;
> L31: 🔌 **MCP canvas** — External clients use the same `tool_ops` contract as the built-in Agent. Live mode applies ops i

## 星数曲线

```mermaid
xychart-beta
    title "recombyn/zuoge 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-28"]
    y-axis "stars" 54 --> 57
    line [55, 56, 56]
```

2026-10-18 55 → 2026-10-28 56（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `631273694a4b` · [字段定义](../../DATASET.md)*
