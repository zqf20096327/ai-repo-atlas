# virtualsms-io/codex-sms-verification

⭐ 26 · MIT · 推送 2026-07-19 · [GitHub](https://github.com/virtualsms-io/codex-sms-verification) · [官网](https://virtualsms.io/mcp) · 组织维护

**给 OpenAI Codex CLI 接入 VirtualSMS 短信验证 MCP 的配置示例**

本仓库是一个 .codex/config.toml 配置示例，使 OpenAI Codex CLI 通过 MCP 接入 VirtualSMS 账号验证平台，获得 40 个 virtualsms_* 工具：一次性短信验证码接收、号码租用（1-30 天）、配匹国家代理、私密云浏览器会话（beta）与账户查询，覆盖 2500+ 服务和 145+ 国家。提供托管（零安装，服务端运行于 mcp.virtualsms.io）与本地 stdio（经 npm 包 virtualsms-mcp）两种接入方式。号码为运营商实体 SIM 卡号码，非 VoIP。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单个 config.toml 即可为 Codex CLI 挂载 40 个 MCP 工具
- 托管模式零安装，无需客户端 Node.js
- 短信验证、号码租用、代理、云浏览器会话统一在一套 API 与预付余额下
- 号码为 Vodafone/O2/T-Mobile 等运营商实体 SIM 卡号码

## 适用场景

- 让 Codex agent 在注册流程中自动接收短信验证码
- 为自动化任务租用专属手机号与匹配国家代理
- 跨 145+ 国家、2500+ 服务查找可用号码并轮换未送达的订单

## 场景标签

 · 领域:开发者工具/账号验证服务

## 证据(README 行号)

> L3: > Drop-in `.codex/config.toml` example that wires VirtualSMS MCP into the OpenAI Codex CLI for account verification,
> L13: This repo is a single `.codex/config.toml` example that gives the OpenAI Codex CLI access to the VirtualSMS MCP ser

## 星数曲线

```mermaid
xychart-beta
    title "virtualsms-io/codex-sms-verification 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-31 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `973fa51bc2fb` · [字段定义](../../DATASET.md)*
