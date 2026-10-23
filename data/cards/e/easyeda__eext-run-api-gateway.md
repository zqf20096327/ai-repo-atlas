# easyeda/eext-run-api-gateway

⭐ 94 · TypeScript · Apache-2.0 · 推送 2026-09-07 · [GitHub](https://github.com/easyeda/eext-run-api-gateway) · 组织维护 · 中文 README

**嘉立创EDA扩展：为 AI 编程工具提供 WebSocket 网关桥接**

嘉立创EDA专业版扩展，作为 AI 编程工具与 EDA 环境之间的 WebSocket 桥接端：启动时自动扫描端口 49620-49629 发现 Bridge Server，经握手验证服务身份（easyeda-bridge）后连接，接收 AI 发来的代码请求并在 EDA 环境中执行、返回结果；支持心跳检测与断线自动重连。需配合 easyeda-api Skill 使用，该 Skill 负责启动 Bridge Server 并提供 API 文档与调用约定。安装需先装 Node.js 22 LTS 与任一 AI 编程工具，再在 EDA 扩展管理器中勾选允许外部交互。

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

- 自动扫描端口 49620-49629 发现并连接 Bridge Server
- WebSocket 握手验证服务身份（easyeda-bridge）
- 接收 AI 代码请求，在 EDA 环境中执行并返回结果
- 心跳检测与断线自动重连

## 适用场景

- 让 AI 编程工具直接操作嘉立创EDA专业版进行原理图检查与绘制
- 通过 OpenCode、Claude Code 等工具用自然语言驱动 EDA 工作流
- 在 EDA 与 AI Agent 之间建立本地 WebSocket 通道

## 场景标签

 · 领域:电子设计自动化（EDA）/AI 工具桥接

## 证据(README 行号)

> L5: 嘉立创EDA 专业版扩展 — 为 AI 编程工具（OpenCode、Claude Code、Cursor、Cline、Continue、Windsurf、WorkBuddy、QwenCode、KimiCode、Trae 等）提供 W
> L12: - 🤖 **代码执行** — 接收来自 AI 的代码请求，在 EDA 环境中执行并返回结果
> L25: 本扩展需要配合 **easyeda-api** Skill 一起使用。该 Skill 负责启动 Bridge Server、提供 EasyEDA API 文档与调用约定，并负责 AI 与 EDA 之间的完整工作流。

## 星数曲线

```mermaid
xychart-beta
    title "easyeda/eext-run-api-gateway 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23"]
    y-axis "stars" 92 --> 95
    line [93, 94, 94]
```

2026-10-18 93 → 2026-10-23 94（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `ed98a2f28741` · [字段定义](../../DATASET.md)*
