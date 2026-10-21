# MiniMax-AI/Mini-Agent

⭐ 3,057 · Python · MIT · 推送 2026-02-14 · [GitHub](https://github.com/MiniMax-AI/Mini-Agent) · [官网](https://www.minimax.io/) · 组织维护 · 中文 README

**基于 MiniMax M2.5 的单 Agent CLI 示例项目，展示 Agent 执行管线**

MiniMax 官方发布的最小化单 Agent 演示项目：通过 Anthropic 兼容 API 调用 MiniMax-M2.5 模型，提供完整 Agent 执行循环（文件系统与 shell 工具）、跨会话持久记忆的 Session Note Tool、按 token 上限自动摘要的上下文管理、15 个 Claude Skills、MCP 工具集成（知识图谱、网页搜索）与全量日志。面向想参考生产级 Agent 实践的开发者，提供 uv tool 安装与源码开发两种模式，另支持 ACP 协议接入 Zed 编辑器。需自备 MiniMax API Key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 完整 Agent 执行循环，内置文件系统与 shell 基础工具集
- Session Note Tool 跨会话持久记忆，历史自动摘要支持长任务
- 内置 15 个 Claude Skills，原生支持 MCP 工具集成
- 支持 ACP 协议，可接入 Zed 编辑器的 agent 面板

## 适用场景

- 作为模板学习和构建生产级 LLM Agent
- 在终端用自然语言驱动文件、shell 与网页搜索任务
- 在 Zed 编辑器内通过 agent 面板直接对话使用

## 场景标签

`Agent 框架` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L5: **Mini Agent** is a minimal yet professional demo project that showcases the best practices for building agents with
> L9: * ✅ **Full Agent Execution Loop**: A complete and reliable foundation with a basic toolset for file system and shell

## 星数曲线

```mermaid
xychart-beta
    title "MiniMax-AI/Mini-Agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-21"]
    y-axis "stars" 3056 --> 3058
    line [3057, 3057]
```

2026-10-18 3,057 → 2026-10-21 3,057（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-20 · 置信度 mid · 依据 README sha `cad8b33f748c` · [字段定义](../../DATASET.md)*
