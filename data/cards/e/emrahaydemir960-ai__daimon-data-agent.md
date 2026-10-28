# emrahaydemir960-ai/daimon-data-agent

⭐ 58 · HTML · 推送 2026-10-27 · [GitHub](https://github.com/emrahaydemir960-ai/daimon-data-agent) · 个人维护

**加入 Discord/Slack/Teams 的数据科学 Agent，线程内做贝叶斯分析**

自托管的开源数据科学 agent，以机器人形式加入团队的 Discord、Slack 或 Microsoft Teams 工作区：在频道中 @提及即在线程中写代码并运行、用 PyMC 拟合贝叶斯模型，回复图表、不确定性解读与可复现的 marimo notebook，支持定时例程与 MCP 服务器接入。构建于 Anthropic Managed Agents 之上，按每服务器/工作区一个租户隔离，单次部署可用一个 API key 服务多个社区；也可配置为 OpenAI 后端。以多服务 Docker Compose 栈部署，Postgres 存储元数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 线程内运行分析并用 PyMC 拟合贝叶斯模型，回复图表与 marimo notebook
- 租户级隔离（tenant_id 层），单部署多 Discord 服务器/Slack 工作区
- 定时例程支持定期分析自动发帖，可接入 Notion/Linear/GitHub 等 MCP 服务器
- 默认 Anthropic Managed Agents，可按 agent 切换 OpenAI 后端

## 适用场景

- 在团队频道里直接提问，让 bot 做数据分析并给出不确定性解读
- 设置每周定时报表例程自动发到指定频道
- 自托管一个实例服务多个社区，各自记忆与数据隔离

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L5: daimon is an open source data science agent that joins your team's Discord, Slack, or Microsoft Teams workspace and 
> L43: daimon is built on Anthropic Managed Agents. Every adapter — Discord, Slack, Teams, the CLI, the MCP server and the
> L165: `daimon` can run on Anthropic Managed Agents (default) or on OpenAI. Provider choice is per agent and is configure

## 星数曲线

```mermaid
xychart-beta
    title "emrahaydemir960-ai/daimon-data-agent 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-28"]
    y-axis "stars" 57 --> 59
    line [58, 58]
```

2026-10-26 58 → 2026-10-28 58（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `ced9a1bda3c1` · [字段定义](../../DATASET.md)*
