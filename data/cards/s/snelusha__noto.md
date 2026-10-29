# snelusha/noto

⭐ 59 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/snelusha/noto) · [官网](https://noto.snelusha.dev) · 个人维护

**开发者用：基于 Gemini 从暂存改动生成 commit 消息的 CLI 工具**

npm 全局安装的命令行工具，读取 Git 暂存区改动，调用 Google Generative API（Gemini 模型，默认 gemini-2.5-flash 可配置）生成 commit 消息，默认自动提交，也提供预览、复制到剪贴板、提交前行内编辑等模式。支持从提交历史生成或用自然语言描述生成项目级 commit 规范（.noto/commit-prompt.md），并提供 prev 命令取用上次生成的消息、amend 修改上次提交。使用前需配置 Google Generative API key（环境变量或 noto config key）。

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

- 基于暂存改动生成上下文相关的 commit 消息，默认自动提交
- noto init 从提交历史或自然语言描述生成项目 commit 规范
- 消息可预览（--preview）、复制（--copy）、提交前行内编辑
- 模型可经 --model / NOTO_MODEL 环境变量 / 配置文件切换

## 适用场景

- 我在终端一条命令生成并提交 commit 消息
- 我按团队提交规范用历史记录生成 commit 模板约束生成结果
- 我用 prev 命令复用或 amend 上次生成的提交消息

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L7: - **Instant Commit Messages**: Generate clear, context-aware messages based on staged changes.
> L27: Before using noto, you must configure your Google Generative API key. You can now provide your API key in two ways:

## 星数曲线

```mermaid
xychart-beta
    title "snelusha/noto 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 58 --> 60
    line [59, 59]
```

2026-10-18 59 → 2026-10-29 59（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1e93980c063b` · [字段定义](../../DATASET.md)*
