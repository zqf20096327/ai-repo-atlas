# Eternal-Xstar/workbuddy2api-plus

⭐ 3 · Go · MIT · 推送 2026-11-26 · [GitHub](https://github.com/Eternal-Xstar/workbuddy2api-plus) · [官网](https://github.com/Eternal-Xstar/workbuddy2api-plus/wiki) · 个人维护 · 中文 README

**把 WorkBuddy/CodeBuddy 账号包装成 OpenAI 兼容 API 的多账号网关**

Go 编写的自托管反向代理网关，通过 OAuth 设备授权获取腾讯 CodeBuddy 账号凭证，对外暴露 /v1/chat/completions 接口，现有 OpenAI SDK 客户端可零改造接入。核心机制包括多账号池加权选号、熔断与冷却、会话粘性、token 自动刷新，以及签到/活跃/保活等定时任务。附带内嵌 Web 管理面板与 smoke/doctor 运维命令。README 声明仅限个人自用账号，禁止批量小号分发额度与收费售卖，并提示上游策略收紧可能导致不可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多账号池调度：快过期积分加权 + 成本分层 + 加权随机选号
- 熔断与冷却：429 指数退避、402 硬冷却、连续失败熔断、会话粘性
- 内嵌单文件 Web 管理面板：账号运维、用量分析、在线改配置（热生效）
- 成长任务一键完成（17/18）：行为事件上报后轮询计分并自动领奖

## 适用场景

- 给自己的本地工具提供 OpenAI 兼容入口，管理自己的 CodeBuddy 账号
- 多账号场景下自动签到、保活与积分任务推进
- DSH 等客户端通过一条命令同步网关模型清单
- 面板上排查单个账号健康状态与错误日志

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L65: WorkBuddy2API 是一个自托管的 **OpenAI 兼容反向代理网关**，将腾讯 CodeBuddy（`copilot.tencent.com`）账号包装为统一的 `/v1/chat/completions` 服务。
> L67: - 官方不提供 OpenAI 形态的开放 API，本项目通过 **OAuth 设备授权**（面板「添加账号」或 `login.sh`）获取账号凭证，在网关侧做 token 自动刷新、账号池调度与流量治理；
> L69: - 对客户端只暴露 OpenAI 兼容接口，现有 SDK / 前端 / 工具 **零改造接入**。

## 星数曲线

```mermaid
xychart-beta
    title "Eternal-Xstar/workbuddy2api-plus 星数(近 2 点)"
    x-axis ["2026-11-27", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-27 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `c85867c4d394` · [字段定义](../../DATASET.md)*
