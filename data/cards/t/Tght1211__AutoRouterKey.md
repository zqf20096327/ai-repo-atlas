# Tght1211/AutoRouterKey

⭐ 20 · Python · MIT · 推送 2026-03-17 · [GitHub](https://github.com/Tght1211/AutoRouterKey) · 个人维护 · 中文 README

**自动化批量注册 Outlook 与 OpenRouter 账号并创建 API Key 的工具**

基于 Playwright 的浏览器自动化工具，覆盖 Outlook 邮箱批量注册、OpenRouter 账号注册、邮件验证、2FA、API Key 创建全流程，并附带 Flask Web 管理平台（统计面板、账号表格、Key 日报、导出、REST API）、邮件通知与每日 9:30 定时日报。针对 macOS 优化，要求 Chrome 无痕模式与代理。内置 .cursor/skills 下的 Agent Skill 文件，可供 Cursor 等 AI 智能体读取后自主执行流程；不带 AI 时仍可通过 CLI 完整使用。README 附免责声明：仅供学习研究。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Outlook 注册 → OpenRouter 注册 → 邮件验证 → 2FA → API Key 创建全链路自动化
- Flask Web 管理平台：统计面板、账号表格、Key 日报、搜索导出与 REST API
- 每日 9:30 定时汇总日报与即时邮件通知（SMTP）
- 内置 AI Agent Skill（openrouter-register），Cursor 等智能体可读取后自主执行

## 适用场景

- 批量注册 Outlook 与 OpenRouter 账号并自动创建 API Key
- 通过 Web 面台集中管理账号与 Key 记录
- 让 Cursor 等 AI 智能体读取 Skill 后引导配置并执行流程

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L9: 基于 Playwright 浏览器自动化，完整实现：Outlook 邮箱注册 → OpenRouter 账号注册 → 邮件验证 → 2FA 验证码 → API Key 创建 → 邮件通知 → Web 管理平台。针对 macOS 优化
> L15: 本项目内置可被 AI 智能体直接使用的 Skill。AI 读取 Skill 文件后，可自主执行全部自动化流程并引导用户配置。
> L25: **Cursor IDE：** Skill 会被自动发现，AI 可直接读取并执行。

## 星数曲线

```mermaid
xychart-beta
    title "Tght1211/AutoRouterKey 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `06138ae399cd` · [字段定义](../../DATASET.md)*
