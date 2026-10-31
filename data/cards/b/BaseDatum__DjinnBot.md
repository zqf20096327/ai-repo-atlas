# BaseDatum/DjinnBot

⭐ 15 · TypeScript · NOASSERTION · 推送 2026-03-08 · [GitHub](https://github.com/BaseDatum/DjinnBot) · [官网](https://docs.djinn.bot/) · 组织维护

**自托管多 agent 协作编排平台：容器化运行自主 AI 团队**

Docker Compose 部署的自托管 agent 编排平台：内置 11 个带人格与持久记忆的 agent（产品、架构、开发、测试、SRE、营销、财务等），通过看板认领任务、在隔离容器中执行工作并互相评审。机制上提供 Tree-sitter+KuzuDB 的代码知识图谱、程序化工具调用（Python 签名替代 JSON schema）、swarm 并行 DAG 执行，支持 Slack/Discord/Telegram/WhatsApp/Signal 接入。一行 curl 脚本安装，Linux/macOS 可用；模型密钥默认配置 OpenRouter。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 11 个预置人格 agent，可按目录自定义扩展
- Tree-sitter 代码知识图谱存 KuzuDB，供 agent 查询而非读文件
- 每步在隔离 Docker 容器中执行，完成后销毁，无宿主访问
- Slack/Discord/Telegram/WhatsApp/Signal 消息桥接入

## 适用场景

- 自建一个 7x24 小时处理工程、研究、运营任务的 AI agent 团队
- 通过 Slack/Telegram 等聊天工具指挥和接收 agent 工作结果
- 在自有服务器上运行带多用户认证的 agent 工作台

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L10: Deploy a team of AI agents that collaborate autonomously — engineering, research, content, operations, finance, or 
> L167: **Services:** PostgreSQL (state), Redis (event bus via Streams + Pub/Sub, JuiceFS metadata), FastAPI (REST API + S

## 星数曲线

```mermaid
xychart-beta
    title "BaseDatum/DjinnBot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `97995475d0fc` · [字段定义](../../DATASET.md)*
