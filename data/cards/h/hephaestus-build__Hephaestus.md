# hephaestus-build/Hephaestus

⭐ 23 · Java · MIT · 推送 2026-11-27 · [GitHub](https://github.com/hephaestus-build/Hephaestus) · [官网](https://hephaestus.build) · 组织维护

**给软件团队提供工程实践反馈的 GitHub/GitLab 自托管应用**

面向软件团队的工程实践反馈平台：对 pull request、issue、代码评审与团队讨论实时生成反馈，反馈以评论、每周摘要和个人 Practice 档案（按实践维度展示长期进展）三种形式呈现。实践条目来自预置目录或自定义，反馈可配置 Off/Approve first/Automatic 模式。通过 GitHub App 形式接入 GitHub 与 GitLab，可连接 Slack 与 Outline；用 Helm 部署在 Kubernetes 上，MIT 许可，支持自带模型提供方。项目处于 pre-1.0 阶段，次版本可能引入需要动作的配置或 API 变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 对 PR、issue、代码评审与团队讨论生成带引用和下一步建议的反馈
- 个人 Practice 档案按实践维度展示长期进展，管理员可查看观察记录
- 反馈模式可按工作区/实践组/实践配置 Off、Approve first 或 Automatic
- 支持自带模型提供方（OpenAI、Azure OpenAI 或 OpenAI 兼容端点）

## 适用场景

- 团队希望对每条 PR 和 issue 自动给出工程实践反馈
- 为开发者提供按实践维度跟踪的个人成长档案
- 在自有 Kubernetes 集群上自托管并接入自己的模型端点

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L18: It reviews pull requests, issues, code reviews and team discussions as the work happens.
> L54:  Your own model provider: OpenAI, Azure OpenAI, or any OpenAI-compatible endpoint.

## 星数曲线

```mermaid
xychart-beta
    title "hephaestus-build/Hephaestus 星数(近 2 点)"
    x-axis ["2026-11-19", "2026-11-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-11-19 23 → 2026-11-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `5712a73a79a0` · [字段定义](../../DATASET.md)*
