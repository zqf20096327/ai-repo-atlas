# patmakesapps/LumaKit

⭐ 21 · Python · MIT · 推送 2026-09-15 · [GitHub](https://github.com/patmakesapps/LumaKit) · 个人维护

**自托管自主任务 Agent，可驱动机器人执行长时任务**

面向终端用户的自托管任务代理：为模型提供 shell 执行、仓库操作、网页搜索、浏览器自动化、截图、邮件、提醒、记忆与可跨重启的长时自主任务，通过 Web UI 展示实时工具活动与写前 diff 预览，对 shell/git/删除等危险步骤设 fail-closed 审批。模型层支持 Anthropic/OpenAI/xAI 及本地 Ollama，一个配置切换。可驱动 VISITOR LX-1 机器人（LumaBot），安全反射在机器人本地运行，另有零模型参与的 Remote 模式。交互面含 Web UI、Telegram 与 CLI。需 Python 3.10+，从源码 pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 持久任务运行器：跨重启的长时自主任务与自维护 todo
- shell/git/删除等危险步骤 fail-closed 审批，不可关闭
- 单一接口切换 Claude/GPT/Grok/本地 Ollama，无需重启
- 可驱动 VISITOR LX-1 机器人：Agent/Remote/Off 三模式，安全反射不依赖模型

## 适用场景

- 委托 AI 从头到尾完成多小时的编程/运维任务并在风险步骤审批
- 通过 Telegram 在手机上查看任务进度并接收完成通知
- 让 Agent 通过机器人摄像头查看并记住家中房间与物品
- 隐私敏感场景下用本地 Ollama 全离线运行

## 场景标签

`AI 助手` `编码 Agent` `浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L7: **The self-hosted autonomous task agent you can actually trust with a shell — and now with a body.** Delegate a job 
> L9: LumaKit gives a model real tools: shell execution, repository work, web search, browser automation, screenshots, ema
> L11: And LumaKit doesn't stop at the desk. It is the mind of the **VISITOR LX-1

## 星数曲线

```mermaid
xychart-beta
    title "patmakesapps/LumaKit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-28 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `bb33170906c5` · [字段定义](../../DATASET.md)*
