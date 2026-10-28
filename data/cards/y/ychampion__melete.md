# ychampion/melete

⭐ 19 · TypeScript · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/ychampion/melete) · [官网](https://melete.si) · 个人维护

**自托管的常驻个人 AI agent，代管邮件日历文件并持续工作**

运行在用户自己设备上的个人 agent：接入工作与个人邮箱、日历、文件、浏览器和服务器，全天候监控并代为处理事务，如代拟改期邮件、读取银行账单核对发票、跟进订位等。模型无关，支持 Fireworks（默认）、Anthropic、OpenAI、Google、openai-compatible 及 ChatGPT 登录；代码执行放入 E2B/Modal/Daytona 沙箱，出站消息需用户批准并留回执可撤销，隐私路由器可阻止敏感数据发往云端模型。通过一键脚本加 Docker 安装，或 git clone 源码自行部署；自称处于 early beta，另有托管版候补名单。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 一个 agent 跨邮箱、日历、Drive、浏览器与任意 MCP 服务器统一工作
- 模型无关：Fireworks/Anthropic/OpenAI/Google/openai-compatible/ChatGPT 登录
- 代码与命令在 E2B/Modal/Daytona 沙箱执行，隔离浏览器填表
- 消息发送需批准、动作留回执可撤销，记忆可查看或遗忘
- 可作为 MCP 服务器被 ChatGPT/Claude/Claude Code 等当作连接器使用

## 适用场景

- 让 agent 监控多个邮箱和日历并代拟/跟进事务
- 用自己登录态的浏览器读取账单、核对发票等私密数据
- 长期任务交给 agent 分班持续执行，回来查看简报
- 通过对话、语音与它交互，并审批外发消息

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5: Melete lives on your own computers and works in every account you're signed
> L7: servers. It keeps watch over all of it, day and night, notices what needs you,
> L75: - **It can afford to watch everything.** It runs on hardware you already have,

## 星数曲线

```mermaid
xychart-beta
    title "ychampion/melete 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `506ec0423446` · [字段定义](../../DATASET.md)*
