# The-Best-Codes/ai-model-directory

⭐ 44 · TypeScript · 推送 2026-10-28 · [GitHub](https://github.com/The-Best-Codes/ai-model-directory) · [官网](https://models.agent-one.dev/) · 个人维护

**自动更新的 AI 模型元数据目录（22,000+ 模型，125+ 供应商）**

由个人开发者（AgentOne 作者）维护的 AI 模型元数据聚合仓库：GitHub Actions 每小时运行，通过各供应商适配器（OpenRouter、OpenAI、Anthropic 等）拉取模型元数据，规范化为统一 TOML 树存储，并生成扁平化的 all.json / all.min.json。元数据涵盖定价、上下文与 token 限制、模态、功能开关、开放权重等。支持 metadata.toml 覆盖与继承定制，文档了针对第三方数据的输入校验与安全措施。自述处于 beta 阶段，数据可信度受限于上游供应商。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 每小时 GitHub Actions 自动拉取 125+ 供应商的模型元数据
- 统一 schema 覆盖定价/上下文/模态/功能开关/开放权重
- metadata.toml 支持 manual_data、extends、priorities、preserve 覆盖机制
- Zod 严格校验、端点硬编码、超时与路径限制等安全措施

## 适用场景

- 为 AI 应用查询各供应商模型的定价与上下文限制
- 路由或计费决策的默认数据源（README 提示需自行核实）
- 以 JSON/TOML 形式订阅全量模型目录做集成

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L6: The AI model directory is the most comprehensive, automatically updated list of AI models and their metadata like pr
> L21: A GitHub Actions workflow runs every hour and re-fetches model metadata from every supported provider (OpenRouter, 

## 星数曲线

```mermaid
xychart-beta
    title "The-Best-Codes/ai-model-directory 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-28", "2026-10-29"]
    y-axis "stars" 40 --> 45
    line [41, 42, 44, 44]
```

2026-10-18 41 → 2026-10-29 44（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8b09385066c8` · [字段定义](../../DATASET.md)*
