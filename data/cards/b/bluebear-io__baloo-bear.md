# bluebear-io/baloo-bear

⭐ 39 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/bluebear-io/baloo-bear) · [官网](https://bluebear.io/projects/baloo-bear) · 组织维护

**面向团队的自托管 AI 代码审查 GitHub App**

开源的 GitHub App，安装到仓库后由 FastAPI 服务接收 PR webhook，使用 PI agent 运行时读取 PR diff 与仓库上下文（AGENTS.md/CONTRIBUTING.md、计划文档等），生成带严重级别分级的行内审查评论，覆盖 bug、安全风险、缺失错误处理与仓库规范违规。面向需要自托管而非 SaaS 审查服务的团队，自行部署 Docker 服务、控制 GitHub App 安装范围并提供 Anthropic、Amazon Bedrock、Google、OpenAI 或 Databricks AI Gateway 的模型凭据。支持二级 LLM 假阳性校验、Dependabot 感知审查与本地 dry-run。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 PI 的 agent 式审查：读文件、grep、探索仓库而非仅看 diff
- 多 provider：Anthropic / Amazon Bedrock / Google / OpenAI / Databricks AI Gateway
- CRITICAL/HIGH/MEDIUM/LOW 严重级别路由与二级 LLM 假阳性校验
- local_review.py 可对本地 git diff 做不发布评论的 dry-run

## 适用场景

- 团队在 PR 流程中获得自动 AI 代码与安全审查
- 强制执行 AGENTS.md / CONTRIBUTING.md 中的仓库规范
- 对依赖更新 PR（Dependabot）做专项审查
- 开 PR 前本地跑同一审查管线预检

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L9: Baloo is an open source **GitHub App for AI pull request review**. It installs on your repositories, reads PR diffs 
> L55: |**Multi-provider**|Runs every agent through the configured Anthropic, Amazon Bedrock, Google, OpenAI, or Databrick

## 星数曲线

```mermaid
xychart-beta
    title "bluebear-io/baloo-bear 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-28 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `e544240f1c39` · [字段定义](../../DATASET.md)*
