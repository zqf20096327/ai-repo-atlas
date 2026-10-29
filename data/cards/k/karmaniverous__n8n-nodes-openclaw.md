# karmaniverous/n8n-nodes-openclaw

⭐ 19 · TypeScript · BSD-3-Clause · 推送 2026-06-10 · [GitHub](https://github.com/karmaniverous/n8n-nodes-openclaw) · [官网](https://www.npmjs.com/package/n8n-nodes-openclaw) · 个人维护

**n8n 社区节点包：在 n8n 工作流中调用 OpenClaw Gateway API**

面向 n8n 自动化平台的社区节点包，通过 OpenClaw Gateway 的 POST /tools/invoke 端点暴露 20 个工具：会话管理、跨渠道消息收发（Slack/Discord/Telegram 等）、定时任务、浏览器控制、Shell 命令执行、网页抓取与 Brave 搜索、图像分析、语音合成、子 agent 派生与记忆检索。每个资源支持 Raw Mode 直发任意 JSON 参数。以凭据形式配置 Gateway URL 与 Token，经 n8n 社区节点面板或 npm 安装；另有可导入的示例工作流。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 20 个工具覆盖会话、消息、定时任务、浏览器、命令执行与子 agent 派生
- Raw Mode 支持直发任意 JSON 参数
- 调用 Gateway 的 POST /tools/invoke，由网关执行工具策略与认证
- 提供 4 个可导入的示例 n8n 工作流

## 适用场景

- 在 n8n 工作流中管理 OpenClaw 会话与发送消息
- 用定时任务触发 agent 或跨渠道推送消息
- 把网页搜索、抓取结果接入自动化流程

## 场景标签

`工作流自动化` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L3: n8n community nodes for the OpenClaw Gateway API.
> L5: Control your OpenClaw instance from n8n workflows — manage sessions, send messages, run cron jobs, search the web, e
> L103: This node calls the OpenClaw Gateway's `POST /tools/invoke` endpoint. Each resource/action combination maps to a t

## 星数曲线

```mermaid
xychart-beta
    title "karmaniverous/n8n-nodes-openclaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `0282a51f9994` · [字段定义](../../DATASET.md)*
