# RubricLab/maige

⭐ 105 · TypeScript · AGPL-3.0 · 推送 2026-10-24 · [GitHub](https://github.com/RubricLab/maige) · [官网](https://maige.app) · 组织维护

**AI 管理 GitHub 仓库议题与标签的自然语言工作流工具**

以 GitHub App 形式接入仓库，通过 webhook 接收 issues、issue comments 与 pull requests 事件，用户在评论中以自然语言指令（如指派人员、增删标签、查询仓库包）驱动 AI 执行仓库维护操作，核心场景是议题标签的自动处理。提供托管服务（Maige.app），README 同时给出源码本地运行步骤（bun 安装依赖、Vercel 环境变量、ngrok 暴露端口），但明确声明暂不支持自助托管，继续操作需自担风险。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 以 GitHub App + webhook 方式接入仓库（issues/issue comments/pull requests 事件）
- 评论中自然语言指令执行指派、标签增删、仓库查询等操作
- 提供 Maige.app 托管服务，另有源码本地运行步骤（bun + ngrok）

## 适用场景

- 让 AI 自动处理 GitHub 议题的打标签与指派
- 在 issue 评论中用自然语言查询和管理仓库
- 通过规则指令（如提及 docker 自动加标签）简化仓库维护

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: Quickly set up Maige and let AI handle your issue labels with ease. Get started at Maige.app.
> L45: Try these commands:

## 星数曲线

```mermaid
xychart-beta
    title "RubricLab/maige 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 103 --> 105
    line [104, 104]
```

2026-10-18 104 → 2026-10-25 104（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `ddd1bbc05352` · [字段定义](../../DATASET.md)*
