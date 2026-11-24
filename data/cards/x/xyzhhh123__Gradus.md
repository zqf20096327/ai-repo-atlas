# xyzhhh123/Gradus

⭐ 3 · Python · MIT · 推送 2026-11-23 · [GitHub](https://github.com/xyzhhh123/Gradus) · 个人维护

**面向开发者的分层 coding agent 运行时与 CLI/Web UI**

把模型流式输出转换为可调用工具的会话，并为每个会话提供沙箱化的 workspace 副本（git 仓库用 git worktree，否则用过滤目录树），会话关闭时合回宿主。分 ai/agent/coding/host 四层，单向依赖；支持 Anthropic Messages、OpenAI Chat Completions、OpenAI Responses、Gemini 四种协议统一为内部消息模型，历史以厂商中立格式存储，可会话中途切换 provider。提供 CLI、Web UI、Python API 与多 agent、MCP、定时任务等内置工具。限制：Gemini 协议与 docker 沙箱标注为测试中，restricted 沙箱不隔离网络。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 厂商中立的会话历史存储，可对话中途切换 Anthropic/OpenAI/Gemini 风格端点
- 每会话沙箱 workspace 副本，关闭时合回，进程被杀无损失
- 四种模型协议统一为一套消息模型与 12 个流式事件
- 9 个 hook、并行工具、steer/follow_up 的可控工具循环

## 适用场景

- 以 CLI 或 Web UI 运行编码 agent 并避免其直接修改宿主目录
- 基于 ai/agent 协议层自行构建 agent 应用
- 在沙箱副本中执行 agent 工具调用并按需合回变更

## 场景标签

`编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L8: **分层的 Coding Agent 运行时。** Gradus 把模型的流式输出变成能调用工具的会话，并给每个会话一份私有的 workspace 副本，会话结束时再合回宿主。
> L30: 3. 🧰 **它是运行时，不是应用。** 四个包，import 单向。`ai` 对其上层一无所知，所以你可以只取协议层；`agent` 给你循环与门面，不附带 CLI。
> L120: gradus/coding    产品层        配置、会话、工具、权限、沙箱、MCP、CLI


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `7504cc6979f6` · [字段定义](../../DATASET.md)*
