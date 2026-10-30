# warengonzaga/magic-commit

⭐ 37 · JavaScript · GPL-3.0 · 推送 2026-05-09 · [GitHub](https://github.com/warengonzaga/magic-commit) · 个人维护

**用 AI 逐文件生成提交信息的 git 提交 CLI 工具**

Magic Commit 是一个 npm 分发的命令行工具：运行 magicc 后自动按文件暂存改动并逐个提交，提交信息由 OpenAI 模型（默认 gpt-4o-mini）生成，用户逐条确认。使用前需通过 magicc -s=<api-key> 配置 OpenAI API key。作者声明项目处于早期阶段，可能存在 bug；README 提及 aicommits、ai-commit、opencommit 等同类型项目作为灵感来源。GPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 按文件自动暂存并逐个提交改动
- 调用 OpenAI gpt-4o-mini 生成提交信息
- 通过 magicc -s=<api-key> 配置 API key
- npm/yarn 全局安装

## 适用场景

- 懒得写提交信息时自动生成
- 按文件拆分提交并逐条确认提交信息
- 保持统一的 git 提交信息格式

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L9: **Magic Commit** is a simple and easy-to-use tool that helps you to automatically stage your changes by file and com
> L33: > To be able to make it work it requires API key from OpenAI to use the GPT-3 model. You can get your API key by si

## 星数曲线

```mermaid
xychart-beta
    title "warengonzaga/magic-commit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-30 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0bac713373f3` · [字段定义](../../DATASET.md)*
