# linq-team/kalshi-agent

⭐ 16 · TypeScript · MIT · 推送 2026-06-18 · [GitHub](https://github.com/linq-team/kalshi-agent) · 组织维护

**通过 iMessage 交易 Kalshi 预测市场的 AI agent**

基于 Linq Blue 与 Claude 构建的 Kalshi 预测市场交易代理：用户通过 iMessage 发消息，经 Linq Blue webhook 转发到本地 Node.js 服务，Claude 通过工具调用执行下单、撤单、行情查询与持仓查询。每个用户经 magic link 绑定自己的 Kalshi 账户，API 密钥以 AES-256-GCM 加密存于内存，重启即失。需 Node.js 20+、ngrok（本地开发）、Kalshi API 权限与 Anthropic API key；支持 Docker 与 Railway/Fly.io 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- iMessage 对话式下单、撤单与行情/持仓查询
- 多用户 magic link 各自绑定 Kalshi 账户，凭据 AES-256-GCM 加密仅存内存
- 全部组件本地运行，无远程数据库与外部认证服务
- 提供 Dockerfile 与 Procfile 支持 Docker/Railway/Fly.io 部署

## 适用场景

- 用手机短信直接操作 Kalshi 预测市场交易
- 通过对话让 AI 查询行情、下单和管理持仓
- 多用户共用一个 agent 但各自绑定自己的 Kalshi 账户

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3: A prediction market trading agent for Kalshi, accessible via iMessage. Built on Linq Blue and powered by Claude (Ant
> L17: User ──iMessage──▶ Linq Blue ──webhook──▶ kalshi-agent ──▶ Claude (Anthropic)
> L89: 4. The agent sends the message to Claude with Kalshi tools available

## 星数曲线

```mermaid
xychart-beta
    title "linq-team/kalshi-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `4d5028115978` · [字段定义](../../DATASET.md)*
