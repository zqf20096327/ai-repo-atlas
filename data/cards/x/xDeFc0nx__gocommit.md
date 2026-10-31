# xDeFc0nx/gocommit

⭐ 16 · Go · MIT · 推送 2026-10-21 · [GitHub](https://github.com/xDeFc0nx/gocommit) · 个人维护

**调用 Gemini 自动生成 git commit 信息的 CLI 工具**

用 Go 编写的命令行工具：用户设置 API key 后，在 git 仓库中运行 gocommit 即调用 Gemini 生成提交信息，免去手写。安装方式为 go install，配置仅需 set-api 一条命令保存密钥。README 极简，未说明生成信息的语言、格式控制或如何处理暂存区差异等细节，作者自述为个人使用的简单工具。

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

- 单命令运行：gocommit 生成 commit 信息
- gocommit set-api 子命令配置 API key
- 通过 go install 一行安装

## 适用场景

- 不想手写 commit message 的开发者快速提交
- 在个人项目中自动化生成提交描述

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: GoCommit is a simple "bad" CLI tool i made to use Gemini to generate git commit messages
> L18: gocommit set-api --key yourapikeyhere

## 星数曲线

```mermaid
xychart-beta
    title "xDeFc0nx/gocommit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `5837e55fd43a` · [字段定义](../../DATASET.md)*
