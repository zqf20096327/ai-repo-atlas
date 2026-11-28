# hthoene/plainboard

⭐ 163 · Python · MIT · 推送 2026-11-27 · [GitHub](https://github.com/hthoene/plainboard) · 个人维护

**自托管多智能体团队：经理 Agent 规划、专职 Agent 构建软件**

自托管的多 Agent 软件开发平台：用户在聊天或看板中提出需求，manager agent 拆解工单并分配给专职 agent，agent 在独立容器中构建与测试，完成的分支合并为一次检查（train），通过后落入 main 分支。支持多人协作（角色权限、@提及）、订阅共享、Ideas 看板、MCP 服务器接入外部 AI 客户端。运行于 Docker 三容器（应用、runner、PostgreSQL+pgvector），面向想用自然语言驱动软件开发的个人与小团队。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- manager agent 拆解工单并分配给专职 agent，完成的分支合并检查后自动落入 main
- agent 运行在独立容器中，PlainBoard 数据库与密钥在容器外且静态加密
- 多人协作：角色权限（Viewer/Member/Owner）、@提及、订阅共享
- agent 可运行于 Claude、Codex 订阅、API key 或自托管模型服务器（Ollama、LM Studio、llama.cpp、vLLM）

## 适用场景

- 用自然语言提出需求，让 agent 团队直接产出并合并代码
- 小团队多人共享同一个经理 agent 协作开发项目
- 把看板进度通过公开 API 展示到自己的网站

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L5: You say what you want. A manager agent plans the work, specialised agents build it,
> L6: and PlainBoard checks and lands what they finish. Self-hosted, started with one command.
> L19: 2. **The manager plans it.** It writes the tickets, builds the team and gives each piece of work to
> L21: 3. **The agents build it, PlainBoard lands it.** Finished branches are merged together, checked once,

## 星数曲线

```mermaid
xychart-beta
    title "hthoene/plainboard 星数(近 8 点)"
    x-axis ["2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-28"]
    y-axis "stars" 0 --> 178
    line [6, 57, 119, 129, 138, 146, 160, 163]
```

2026-11-19 6 → 2026-11-28 163（+157）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `abeab1472b5e` · [字段定义](../../DATASET.md)*
