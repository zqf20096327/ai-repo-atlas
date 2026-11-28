# tbphp/gpt-load

⭐ 7,250 · Go · MIT · 推送 2026-11-27 · [GitHub](https://github.com/tbphp/gpt-load) · [官网](https://gpt-load.com) · 个人维护 · 中文 README

**自托管 AI 网关：多渠道多凭据统一接入与调度**

以 Go 编写、Docker Compose 部署的自托管 AI 网关：应用侧仅需一个 base URL 与 AccessKey，上游渠道、凭据、模型与路由策略在管理 UI 中配置。支持 OpenAI/Anthropic/Gemini 原生协议入口，内置官方云平台、模型服务与订阅账号（Codex/Claude/Antigravity/Grok）渠道，提供多凭据调度、权重、重试、冷却、黑名单与会话亲和，并含请求日志、用量与成本统计，数据落 SQLite/MySQL/PostgreSQL，凭据本地加密存储。2.0 为完全重写，不能原地迁移 1.x 数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单入口统一接入官方 API、云平台、模型服务与兼容中转，客户端保持原生协议
- API key 与订阅账号共享凭据管理、调度与健康处理机制
- 多凭据调度含权重、重试、冷却、黑名单与会话亲和
- 内嵌管理 UI，支持 SQLite/MySQL/PostgreSQL 与凭据本地加密

## 适用场景

- 为多个上游账号和密钥做统一接入与轮询调度
- 应用不改代码切换 OpenAI/Anthropic/Gemini 协议后端
- 集中查看请求日志、用量与成本估算

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: **A self-hosted AI gateway for multi-channel, multi-credential setups**
> L7: API keys, subscription accounts, traffic scheduling, failure handling, request logs, and usage accounting — behind a
> L23: Your application only needs one base URL and one AccessKey. Providers, accounts, credentials, models, and routing p

## 星数曲线

```mermaid
xychart-beta
    title "tbphp/gpt-load 星数(近 26 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 7157 --> 7261
    line [7165, 7170, 7172, 7176, 7180, 7187, 7189, 7194, 7168, 7200, 7207, 7209, 7214, 7215, 7218, 7219, 7224, 7228, 7232, 7241, 7243, 7245, 7248, 7252, 7253, 7250]
```

2026-10-26 7,165 → 2026-11-28 7,250（+85）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `2369458e8d45` · [字段定义](../../DATASET.md)*
