# guanguans/ai-commit

⭐ 394 · PHP · MIT · 推送 2026-09-17 · [GitHub](https://github.com/guanguans/ai-commit) · 个人维护 · 中文 README

**用 AI 生成约定式 git 提交信息的命令行工具**

PHP 编写的命令行工具，读取暂存的 git 变更，调用 AI 生成器（如 Bito CLI、文心一言 Ernie Bot 等）产出符合 conventional 规范的提交信息并执行提交。提供配置管理（set/get/unset/reset/list/edit）、命令列表查看与 self-update 自更新。要求 PHP >= 8.2，支持下载单文件或通过 Composer 全局/项目安装。支持配置多个生成器并按 --generator 切换。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 生成符合 conventional 规范的 git 提交信息
- 支持多种生成器（bito_cli、ernie_bot 等）并可切换
- config 配置管理与 self-update 自更新命令

## 适用场景

- 写提交信息时用 AI 自动生成约定式描述
- 团队统一提交信息格式，减少手写负担

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L7: > Automagically generate conventional git commit message with AI. - 使用 AI 自动生成约定式 git 提交信息。
> L54: ╰─ ./ai-commit commit --generator=bito_cli --no-edit --no-verify --ansi                                            

## 星数曲线

```mermaid
xychart-beta
    title "guanguans/ai-commit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 393 --> 395
    line [394, 394]
```

2026-10-18 394 → 2026-10-28 394（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `3cd1de75fd58` · [字段定义](../../DATASET.md)*
