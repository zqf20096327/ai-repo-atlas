# greenticai/greentic

⭐ 16 · Rust · 推送 2026-10-30 · [GitHub](https://github.com/greenticai/greentic) · [官网](https://greentic.ai) · 组织维护

**面向企业的数字工人操作系统：确定性编排+受控 AI**

Greentic 是一个用于构建和运行『数字工人』的平台/运行时：以 WebAssembly 组件（WASIp2 沙箱）为执行单元，采用图式确定性流程编排，能力需显式声明，支持策略控制层与 Observer 审计监控层。AI 以显式、受限步骤嵌入（Chat2Flow 意图路由、Chat2Data 自然语言转系统方言等），可运行 MCP 式集成。数字工人可接入 Slack/Teams/WhatsApp/Telegram/WebChat/Webhook 等渠道，支持多租户与 50+ 语言交互，通过 gtc CLI（wizard/setup/start/up）创建与部署，可部署到 AWS/GCP/Azure（AWS 路径需 aws CLI）。用 Rust 实现，经 cargo-binstall 安装。限制：行业方案 Greentic-X 等标注 coming soon。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- WebAssembly 组件 + WASIp2 沙箱执行，能力显式声明
- 图式确定性流程编排与策略/审计（Control/Observer）层
- Chat2Flow/Chat2Data 等 LLM 步骤显式声明权限嵌入
- gtc CLI 一条命令创建/部署数字工人，支持 AWS/GCP/Azure

## 适用场景

- 搭建 IT 服务台等跨渠道（Teams/Slack/Telegram 等）的确定性自动化数字工人
- 在受监管流程中以显式声明权限的方式嵌入 AI 路由/转换步骤
- 为数字工人执行附加策略控制与审计追踪

## 场景标签

`工作流自动化` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L169: Greentic is built from self-describing executable units.
> L154: - optional AI steps for routing, interpretation, or transformation
> L222: - **Chat2Flow** for routing intent to the right flow

## 星数曲线

```mermaid
xychart-beta
    title "greenticai/greentic 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `4852c27468b0` · [字段定义](../../DATASET.md)*
