# schwarztim/freetaxusa-mcp

⭐ 11 · TypeScript · MIT · 推送 2026-09-29 · [GitHub](https://github.com/schwarztim/freetaxusa-mcp) · 个人维护

**让 AI 助手通过 FreeTaxUSA 代为报税的 MCP 服务器**

基于 Playwright 浏览器自动化的 MCP 服务器：驱动 Chromium 会话访问 FreeTaxUSA（无公开 API），通过无障碍树读取表单、填充字段并在各报税环节间导航，向 AI agent 返回结构化数据。提供 15 个报税工具（会话、页面交互、个人信息、收入、扣除等），其中 Phase 2/3 工具目前为占位实现。内置会话持久化、PII 输出脱敏、州税付费墙拦截、凭据不落盘等机制。需 Node.js 20+ 与 FreeTaxUSA 账户，面向使用 Claude 等 AI 助手的个人报税用户。

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

- 15 个报税工具：登录会话、页面交互、W-2/1099 收入、扣除与申报检查
- PII 自动脱敏：SSN/EIN/账号在所有工具输出中被掩码
- 凭据不存储、浏览器配置目录 0700 权限的会话安全设计
- 可配置税年支持往年补报

## 适用场景

- 通过对话让 Claude 代为在 FreeTaxUSA 填写并提交联邦报税表
- 填报 W-2、1099 等收入信息并查询退税估算
- 使用往年税年补报需纸质邮寄的税表

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L1: # FreeTaxUSA MCP Server
> L13: This MCP uses Playwright to drive a real Chromium browser session against FreeTaxUSA's web interface. It reads form
> L24: - **15 tax filing tools** across personal info, income, deductions, review, and filing

## 星数曲线

```mermaid
xychart-beta
    title "schwarztim/freetaxusa-mcp 星数(近 3 点)"
    x-axis ["2026-11-02", "2026-11-16", "2026-11-19"]
    y-axis "stars" 9 --> 12
    line [10, 11, 11]
```

2026-11-02 10 → 2026-11-19 11（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `b0df07b2d98b` · [字段定义](../../DATASET.md)*
