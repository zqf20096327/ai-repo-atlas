# ZenRows/cli

⭐ 16 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/ZenRows/cli) · [官网](https://docs.zenrows.com/cli/introduction) · 组织维护

**让 AI agent 经 Zenrows 云可靠抓取受保护网页的 CLI/MCP 工具**

ZenRows 官方开源的命令行工具：将 Fetch、Extract、Batch、Crawl、Browser Sessions 四类云端原语以 zenrows fetch/extract/batch/browser 等命令暴露给 AI agent 与开发者工作流，并附带技能、模板、工作流、配方与评测资产注册表，可为 Claude Code、Cursor、Codex 等客户端自动配置 MCP。首次云端调用自动创建免费账户并本地存储密钥，无需预置 API key。核心功能依赖 Zenrows 云端点；Browser Sessions 为按带宽与时长计费的升级路径。

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

- zenrows fetch/extract/batch/crawl/browser 覆盖单页抓取、结构化提取、批量任务与真实浏览器会话
- 首次调用自动开通 Free 计划账户，密钥以 0600 权限存于 .zenrows/secrets.json
- zenrows init --agents 一键为多种 agent 客户端配置 MCP
- 本地 spec 校验与额度估算无需 API key，Batch 任务本地策略默认上限 10,000 URL

## 适用场景

- AI agent 需要可靠抓取带反爬保护的网页数据
- 批量对成千上万 URL 执行抓取与结构化提取
- 为 Claude Code/Cursor 等客户端配置 ZenRows MCP 服务

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L3: **Zenrows CLI is the open-source command-line, MCP, skills, templates,
> L7: It makes the four Zenrows primitives — Fetch, Extract, Batch, and Browser
> L15: (skills, templates, workflows, recipes, evals) and MCP configuration for popular

## 星数曲线

```mermaid
xychart-beta
    title "ZenRows/cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `34701c832623` · [字段定义](../../DATASET.md)*
