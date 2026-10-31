# KeyID-AI/sdk-py

⭐ 302 · Python · 推送 2026-03-13 · [GitHub](https://github.com/KeyID-AI/sdk-py) · [官网](https://keyid.ai) · 组织维护

**为 AI agent 提供免注册免费邮箱的 Python SDK**

KeyID.ai 官方 Python SDK：agent 生成 Ed25519 密钥对后调用 provision() 即可获得真实邮箱地址，无需注册与人工介入；由服务端托管域名管理、轮换、信誉监控与送达性。SDK 封装完整邮件能力：收发/回复/转发/搜索、会话线程、草稿、签名与自动回复设置、联系人、Webhook 与送达历史、允许/屏蔽名单及用量指标，另支持定时发送与 HTML 邮件。要求 Python 3.9+，httpx 随包安装，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Ed25519 挑战-响应认证，密钥对即注册凭证
- 完整邮件 API：收发/回复/搜索/线程/草稿/联系人
- Webhook 事件订阅与送达历史查询
- 定时发送、HTML 邮件、自动回复、允许/屏蔽名单

## 适用场景

- 为自动化 agent 分配可收发邮件的真实地址
- 让 agent 通过邮件与外部系统或用户交互
- 监控 agent 邮箱的送达与用量指标

## 场景标签

 · 领域:AI agent 基础设施/通信

## 证据(README 行号)

> L3: **Free email addresses for AI agents. No signup. No human needed.**
> L7: KeyID.ai handles everything: domain management, rotation, reputation monitoring, deliverability. Your agent just gen
> L29: 2. `provision()` registers the public key and returns an email address

## 星数曲线

```mermaid
xychart-beta
    title "KeyID-AI/sdk-py 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 300 --> 303
    line [301, 302, 302]
```

2026-10-18 301 → 2026-10-31 302（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `c815f90e5c67` · [字段定义](../../DATASET.md)*
