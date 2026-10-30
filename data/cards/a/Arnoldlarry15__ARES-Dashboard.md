# Arnoldlarry15/ARES-Dashboard

⭐ 16 · TypeScript · MIT · 推送 2026-07-05 · [GitHub](https://github.com/Arnoldlarry15/ARES-Dashboard) · [官网](https://ares-dashboard-mauve.vercel.app) · 个人维护

**企业安全团队用于规划与审计 AI 红队测试的操作台**

面向安全团队、合规人员与 AI 安全研究者的全栈红队作战控制台：以活动（campaign）形式构建攻击清单，对齐 OWASP LLM Top 10、MITRE ATLAS/ATT&CK 框架，导出 JSON 清单供测试使用，但不自动执行漏洞利用。提供 RBAC、JWT 会话、审计日志与多租户隔离等企业治理功能；AI 部分为可选的载荷生成（Gemini/OpenAI/Anthropic/本地 LLM），另有无需 API key 的静态回退与演示模式。部署方式为 Vercel 一键部署或本地 Node.js 20.x 运行。

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

- campaign 式攻击清单构建与 OWASP/MITRE 框架对齐
- 可选 AI 载荷生成（Gemini/OpenAI/Anthropic/本地 OpenAI 兼容端点），带静态回退模式
- 企业功能：RBAC、JWT 会话、SSO（Auth0/Azure AD/Clerk/Okta）、审计日志与多租户
- Vercel 一键部署与无需 API key 的演示模式

## 适用场景

- AI 产品上线前做结构化、可审计的红队风险评估
- 为 SOC 2/ISO 27001 审计导出带时间戳的安全测试证据
- 分布式红队团队按角色协作管理与共享攻击场景

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L4: ARES is an AI Red Team Operations Dashboard for planning, executing, and auditing structured adversarial testing of 
> L8: ARES provides a centralized workspace for building attack manifests, managing red team campaigns, aligning assessmen
> L45: ARES provides a governance-ready AI red-teaming and audit platform that:

## 星数曲线

```mermaid
xychart-beta
    title "Arnoldlarry15/ARES-Dashboard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `2205f65e293d` · [字段定义](../../DATASET.md)*
