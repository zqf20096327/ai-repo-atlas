# ayazelrico/Milyonus-Phone-Control

⭐ 4 · Python · Apache-2.0 · 推送 2026-11-01 · [GitHub](https://github.com/ayazelrico/Milyonus-Phone-Control) · [官网](https://www.milyonus.com) · 个人维护

**让 AI agent 本地与远程控制真实 Android/iPhone 设备的基础设施**

Milyonus agent 的手机控制基础设施：Android 侧提供 adb 与 Companion App 通道，iOS 侧通过 iPhone Mirroring 与 WebDriverAgent 接入，中间由 Gateway 处理设备租用、策略、审批与审计，并以 MCP server 形式向 agent 暴露能力。仓库处于 P0 阶段，README 明确说明尚无实际控制手机的代码，首个真实设备控制在 P2 阶段；当前内容为架构/协议/安全文档、开发规范与测试、lint 工具链（pytest/ruff/pyright/pre-commit）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Android 走 adb + Companion App，iOS 走 iPhone Mirroring + WebDriverAgent
- Gateway 提供设备租用（kiralama）、策略、审批与审计
- 内置 MCP server 供 agent 调用
- 文档体系：Plan.md、Phases.md、ADR、PITFALLS、runbook

## 适用场景

- 让 AI agent 在本地或远程操作真实手机完成自动化任务
- 以带审批与审计的网关管理设备租用与权限
- 按阶段计划跟踪该项目手机控制能力的开发进度

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L9: Milyonus Agent'ın gerçek telefonları **bağlı (yerel)** ve **uzaktan** kontrol etmesini sağlayan sistem: Android (adb
> L28: Durum: **P0 — Temel ve Kararlar**. Henüz telefon kontrol eden kod yok; ilk gerçek cihaz kontrolü P2'de (Plan-Action


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `c2ae2bedc021` · [字段定义](../../DATASET.md)*
