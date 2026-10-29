# mergewatch/mergewatch.ai

⭐ 26 · TypeScript · AGPL-3.0 · 推送 2026-10-27 · [GitHub](https://github.com/mergewatch/mergewatch.ai) · [官网](https://mergewatch.ai) · 组织维护

**自托管的 GitHub App：多 AI agent 并行评审每个 PR**

MergeWatch 是一个可自托管（Docker 三服务）或使用 SaaS 的 GitHub App，对每个 pull request 运行 6 个专项评审 agent（安全、bug、风格、错误处理、测试覆盖、注释准确性）加 2 个工具 agent，由 orchestrator 去重、按严重度排序并给出 1-5 的合并就绪分。支持 Anthropic、LiteLLM、Bedrock、Ollama（实验性）作为 LLM 后端；agent 可读取 diff 之外的源码获取上下文，支持仓库级 .mergewatch.yml 与组织级自定义 agent 配置，附带 Next.js 仪表盘（分析、历史、设置）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 6 个评审 agent + 2 个工具并行运行，orchestrator 去重并输出 1-5 合并就绪分
- 支持 Anthropic / LiteLLM(100+ providers) / Bedrock / Ollama 四类 LLM 后端
- GitHub Checks 集成、@mergewatch 评论按需复审与问答、自动生成 Mermaid 架构图
- 智能跳过琐碎 PR（锁文件、文档、配置）以节省成本

## 适用场景

- 在私有云/Docker 中自托管 AI 代码评审，代码不出本地
- 为开源或团队仓库的每个 PR 自动获取结构化评审与合并评分
- 组织管理员通过自定义 agent 在全组织强制执行评审规则

## 场景标签

`代码审查` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L15: MergeWatch is a GitHub App that reviews every pull request with a team of specialized AI agents running in parallel
> L23: - **Any LLM** — Anthropic, AWS Bedrock, LiteLLM (100+ providers), or Ollama for fully local/air-gapped

## 星数曲线

```mermaid
xychart-beta
    title "mergewatch/mergewatch.ai 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-27", "2026-10-29"]
    y-axis "stars" 23 --> 27
    line [24, 25, 26, 26]
```

2026-10-18 24 → 2026-10-29 26（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `d1f9c9e2998e` · [字段定义](../../DATASET.md)*
