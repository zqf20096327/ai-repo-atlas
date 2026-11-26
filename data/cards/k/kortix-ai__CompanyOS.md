# kortix-ai/CompanyOS

⭐ 20,798 · TypeScript · NOASSERTION · 推送 2026-11-25 · [GitHub](https://github.com/kortix-ai/CompanyOS) · [官网](https://kortix.com) · 组织维护

**面向 AI-native 公司的开源公司操作系统：托管与编排 agent**

Kortix CompanyOS 将企业的数据源、agent、技能、记忆与连接器收进一个自有的 git 仓库（company as code），提供事件驱动的触发器、名为 My Kortix 的对话入口 agent、多 agent 并行（swarm）、每个会话独立的云端沙箱计算机、结果驱动（Outcome）工作流与审批/审计/SSO 等团队管控。用户通过 CLI、Web、Slack/Teams/邮件/MCP 接入；自托管经由 Docker Compose 栈部署到自有 VPC 或本地服务器，模型可自带 key 接任意 provider。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- agent、技能、记忆与连接器以文件形式存于单一自有 git 仓库
- 事件驱动触发：定时、签名 webhook、连接器与应用事件、合并的变更请求
- 每个会话独立云计算机，空闲休眠、状态持久，数千 agent 可按一份配置并行
- 支持 Kortix Cloud、VPC 或本地自托管，模型 provider 与 key 自选

## 适用场景

- 把公司的 agent、技能与连接器作为代码集中管理并版本化
- 让 agent 7×24 小时按定时/webhook 自主推进带完成定义的目标
- 在自有 VPC 或本地网络中自托管企业 AI agent 平台
- 团队多人共享同一套 agent、公司记忆与权限体系

## 场景标签

`多智能体` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L35: Kortix CompanyOS takes the session out of the person's hands. It is a **cloud-native agent harness**: you
> L76: |**Models**|Kortix-managed models, your own provider keys, a ChatGPT subscription or a Claude subscription. Every r
> L105: |**Company as code** Extensible to the core.|Every agent, skill, rule, connector and piece of context is a file in

## 星数曲线

```mermaid
xychart-beta
    title "kortix-ai/CompanyOS 星数(近 16 点)"
    x-axis ["2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 20551 --> 20820
    line [20573, 20635, 20654, 20670, 20692, 20715, 20738, 20751, 20758, 20762, 20773, 20779, 20782, 20785, 20789, 20798]
```

2026-11-08 20,573 → 2026-11-26 20,798（+225）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `3d6b41a50e34` · [字段定义](../../DATASET.md)*
