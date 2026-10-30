# NihadMemmedli/quorvex_ai

⭐ 45 · Python · MIT · 推送 2026-08-02 · [GitHub](https://github.com/NihadMemmedli/quorvex_ai) · [官网](https://nihadmemmedli.github.io/quorvex_ai/) · 个人维护

**自托管 AI 测试平台：把规格/PRD 转成 Playwright 测试并自愈**

面向团队的自托管测试平台：输入自然语言流程、PRD 或 OpenAPI 文件，或让 agent 探索真实应用，系统规划流程、生成 Playwright TypeScript 代码，在浏览器中验证并修复选择器/时序失败；产出的测试代码可审查、提交并在 CI 中运行，无需运行时 AI 依赖。生成时需配置 AI provider 凭证。功能扩展至 API/负载/安全/数据库/移动冒烟/LLM 评测测试，附带仪表盘、队列、浏览器池、RBAC、CI 集成等运维面。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言规格/PRD/OpenAPI 转可审查的 Playwright TypeScript 代码
- 浏览器验证与选择器/时序失败的自动修复（hybrid healing）
- 覆盖 API/K6 负载/Nuclei/ZAP 安全扫描/数据库/LLM 评测等专项测试
- 自托管部署：dashboard、Redis 队列、MinIO 存储、RBAC、浏览器池

## 适用场景

- 用自然语言描述用户流程，自动生成可提交 CI 的 Playwright 测试
- 上传 PRD 提取需求并做覆盖缺口分析
- 让 agent 自主探索应用发现测试点并长时间运行任务
- 在自有基础设施内运行带凭据管控的测试平台

## 场景标签

`浏览器自动化` `代码生成` `模型评测` `网络安全` · 领域:效率与自动化

## 证据(README 行号)

> L21: Quorvex AI is a self-hosted testing platform for teams that want AI-assisted test authoring without giving up norma
> L29: - **AI speed, standard test code**: agents help plan, generate, validate, and heal tests while your team keeps read
> L103: |Test generation|Plain-English specs to Playwright, browser-backed planning, validation, Smart Check reuse, hybrid

## 星数曲线

```mermaid
xychart-beta
    title "NihadMemmedli/quorvex_ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-30 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `382248e93154` · [字段定义](../../DATASET.md)*
