# jakemgold/github-release-posts-wordpress

⭐ 19 · PHP · 推送 2026-10-05 · [GitHub](https://github.com/jakemgold/github-release-posts-wordpress) · 个人维护

**监控 GitHub 发布并用 AI 自动生成 WordPress 博客帖的插件**

WordPress 插件：通过 WP-Cron 每日检查所监控的 GitHub 仓库新发布版本，调用 WordPress 7.0 的 AI Client API 与 Connectors（Anthropic/OpenAI/Google 等）研究发布内容并生成面向读者的博客帖，可自动发布或存为草稿并邮件通知。支持 monorepo 多包监控（识别 npm/changesets 等标签形态）、发布级别差异化文风、两种研究深度（含 commit 与文件变更）、历史版本按需生成、防重复的幂等机制。要求 WordPress 7.0+、PHP 8.2+，AI 服务在 WordPress Connectors 层配置，插件自身不管理 API key；读取 GitHub 发布数据需 PAT（公开仓库可选）。提供 zip 上传与 Composer 两种安装方式及十余个 filter 扩展钩子。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 WordPress 7.0 Connectors 接入 Anthropic/OpenAI/Google 等 AI 提供方，插件内无需管理 API key
- monorepo 多包监控：自动识别 npm/changesets 等标签形态，按包各生成帖子且支持 fnmatch 模式筛选
- Standard/Deep 两档研究深度，Deep 含 commit 信息与文件变更
- 幂等去重、历史发布按需补生成并自动回填日期保持归档时序

## 适用场景

- 为自己的开源项目新版本自动产出更新公告博客
- 聚合跟踪多个关注的 GitHub 仓库发布动态并生成可读文章
- 在草稿审核流程下由 AI 起稿、人工把关后发布

## 场景标签

`AI 写作` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: Monitors GitHub repositories for new releases and uses AI to research each release and generate a human-readable blo
> L7: Built on the **AI Client API and Connectors** introduced in WordPress 7.0 — configure your AI provider (Anthropic, O
> L14: 2. **Generate** — When a new release is detected, the AI researches the release and writes a blog post tailored to 

## 星数曲线

```mermaid
xychart-beta
    title "jakemgold/github-release-posts-wordpress 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `03bcd0557dd8` · [字段定义](../../DATASET.md)*
