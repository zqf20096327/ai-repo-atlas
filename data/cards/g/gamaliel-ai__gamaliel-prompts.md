# gamaliel-ai/gamaliel-prompts

⭐ 16 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/gamaliel-ai/gamaliel-prompts) · [官网](https://gamaliel.ai) · 组织维护

**开源 AI 圣经研读应用的提示词模板与神学准则集合**

Gamaliel.ai 是免费、无需登录的 AI 圣经研读伴侣，本仓库是其开源部分：提供 Jinja 提示词模板、用户画像 YAML、宗派神学准则及面向教会等组织的合作伙伴配置，并附带本地测试验证这些模板的 CLI 参考实现。系统要求回答以圣经为依据并遵循尼西亚传统教义约束，每个 AI 回答可审计（披露完整提示词、上下文与所用模型）。项目自述处于早期开发阶段，暂未接受 PR；当前使用公有领域的 WEB 与 KJV 译本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Jinja 提示词模板驱动 Gamaliel agents 的系统与用户提示生成
- 用户画像 YAML 调整 AI 的语气、深度与面向受众
- 宗派/教义神学准则（YAML）与合作伙伴配置体系
- CLI 工具用于本地测试验证模板、画像与神学配置

## 适用场景

- 审阅或改进 AI 圣经研读应用的提示词逻辑与神学边界
- 为教会或机构定制专属的 Gamaliel 合作伙伴配置
- 本地测试提示词模板变更后再提交 PR

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: Gamaliel Prompts is the open-source heart of the Gamaliel.ai project—a free, Open, AI-powered Bible study companion.
> L38: - `templates/` — Jinja prompt templates that are used to generate instructions (system prompts) and input (user pro

## 星数曲线

```mermaid
xychart-beta
    title "gamaliel-ai/gamaliel-prompts 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-30 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `15ca0722bbe9` · [字段定义](../../DATASET.md)*
