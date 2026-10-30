# martinopedal/linkedin-auto-poster

⭐ 15 · Python · MIT · 推送 2026-06-29 · [GitHub](https://github.com/martinopedal/linkedin-auto-poster) · 个人维护

**从行业 RSS 自动生成并经 PR 审批发布 LinkedIn 帖子的工具**

面向希望维持 LinkedIn 活跃度的从业者的 Python 自动化工具：定时抓取 RSS 订阅源与 GitHub Releases，按关键词打分筛选新闻，AI agent 抓取原文并核验事实，随后按用户声明的写作风格（voice_profile.md）生成草稿，经敏感信息检查与违禁短语过滤后以 GitHub PR 形式提交，人工添加 approve-post 标签并合并后自动发布到 LinkedIn。AI 模型（Claude Opus、GPT）通过 GitHub Copilot SDK 访问，需 Copilot 订阅，无需单独 API key；LinkedIn 侧需自建开发者应用并通过审核，这是主要门槛。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- RSS 抓取→关键词打分→AI 调研与草稿→PR 审批→自动发布的完整流水线
- AI 模型经 GitHub Copilot SDK 访问，无需单独 OpenAI/Anthropic API key
- 写作风格、订阅源与关键词均可通过 config.yaml 与 voice_profile.md 配置
- 草稿经违禁短语过滤、PII 检查与技术事实核验

## 适用场景

- 每天自动把行业新闻变成个人风格的 LinkedIn 帖子
- 在手机上通过 PR 审核 AI 生成的草稿再发布
- 换一套订阅源与关键词后用于其他技术领域的内容运营

## 场景标签

`AI 写作` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: Automatically generate and publish LinkedIn posts from industry news, powered by AI.
> L25: 4. **Drafting** - Claude Opus generates a post in my writing style; GPT-5.4 critiques it
> L27: 6. **PR created** - One PR per draft with full preview. I review on my phone

## 星数曲线

```mermaid
xychart-beta
    title "martinopedal/linkedin-auto-poster 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 13 --> 16
    line [14, 15]
```

2026-10-18 14 → 2026-10-30 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `5b5b4d19cdc7` · [字段定义](../../DATASET.md)*
