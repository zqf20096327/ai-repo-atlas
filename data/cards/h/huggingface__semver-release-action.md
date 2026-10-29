# huggingface/semver-release-action

⭐ 20 · JavaScript · Apache-2.0 · 推送 2026-09-23 · [GitHub](https://github.com/huggingface/semver-release-action) · 组织维护

**Hugging Face 维护的语义化发布 GitHub Action**

基于 Semantic Release 封装的 GitHub Action，用于自动化软件包发布流程：依据 Conventional Commits 提交信息确定下一版本号（feat→MINOR、fix→PATCH、BREAKING CHANGE→MAJOR）、生成发布说明并发布包。支持指定发布分支、dryRun 预览模式（跳过发布步骤并打印下一版本与说明）、通过 commitAnalyzerPluginOpts 自定义提交规则；输出 tag、version、changelog 与 released 布尔值。注意：本仓库本身不涉及 AI 功能，仅由 Hugging Face 组织维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按 Conventional Commits 规则自动确定版本号增量（MAJOR/MINOR/PATCH）
- dryRun 预览模式跳过发布步骤并打印下一版本与发布说明
- commitAnalyzerPluginOpts 自定义提交类型与版本增量规则
- 输出 tag/version/changelog/released 四个结果变量

## 适用场景

- 在 CI 流水线中自动完成版本号判定与发布
- 发布前用 dryRun 预览待发布版本与说明
- 自定义提交规则控制何种提交触发发布

## 场景标签

 · 领域:开发者工具/CI-CD

## 证据(README 行号)

> L13: This github action automates the whole package release workflow including: determining the next version number, gen
> L66: This action uses Conventional Commits to determine the next version number. The commit message format determines wh

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/semver-release-action 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 low · 依据 README sha `69eaa1264e60` · [字段定义](../../DATASET.md)*
