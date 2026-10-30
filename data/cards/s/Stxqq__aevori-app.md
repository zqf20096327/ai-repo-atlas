# Stxqq/aevori-app

⭐ 16 · TypeScript · NOASSERTION · 推送 2026-09-30 · [GitHub](https://github.com/Stxqq/aevori-app) · [官网](https://github.com/Stxqq/aevori-app/releases) · 个人维护

**macOS 本地 AI 聊天与个人 agent 工作区（Ollama 驱动）**

运行在 Mac 上、通过浏览器访问的个人 AI 工作区：基于本地 Ollama 模型进行流式对话，提供四种可选角色的 agent、可增删并可关闭的记忆（存储上下文而非微调权重）、笔记与任务管理、成员邀请与隔离工作区、Mac 池请求路由。提供 Apple silicon 与 Intel 的免构建下载包（内含 Node 运行时），也可用 Node 22.13+ 从源码运行。限制：未签名 preview，数据存储未加密，云端 API 为可选项，移动端仅 PWA 不跑模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 本地 Ollama 推理，无需账号或 API key 即可聊天
- 四种角色 agent，记忆可增删/检查/关闭，笔记任务需用户批准
- 成员邀请、撤销与隔离工作区；Mac 池跨主机路由请求
- 响应式 PWA 可添加到手机主屏（模型仍跑在 Mac 上）

## 适用场景

- 在 Mac 上与本地模型进行隐私可控的对话
- 给 agent 设定角色并维护长期记忆、笔记与任务
- 小团队在各自硬件上隔离使用共享的本地 AI 工作区
- 手机通过 HTTPS 访问 Mac 上运行的实例

## 场景标签

`AI 助手` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L18: AEVORI is a personal AI workspace that runs on your Mac and opens in your browser.
> L22: **Preview 0.3.0 · macOS · Local Ollama inference · English interface**
> L93: - Local agent inference always uses Ollama. Optional cloud chat sends its messages

## 星数曲线

```mermaid
xychart-beta
    title "Stxqq/aevori-app 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `7773ebaef0a3` · [字段定义](../../DATASET.md)*
