# sgoedecke/gh-standup

⭐ 118 · Go · MIT · 推送 2026-04-23 · [GitHub](https://github.com/sgoedecke/gh-standup) · 个人维护

**给开发者的 GitHub CLI 扩展：从 GitHub 活动生成 AI 站会报告**

gh-standup 是一个 GitHub CLI 扩展，读取用户的 GitHub 活动（可回溯多天），调用 GitHub Models 生成站会报告，也可切换 GitHub Copilot 作为替代后端。面向已安装并认证 GitHub CLI 的开发者，组织场景需额外授权 read:org；使用 Copilot 后端时还需安装认证 Copilot CLI。以 gh extension install 命令安装，一条 gh standup 即可运行。

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

- 基于 GitHub 活动数据生成站会报告
- 默认使用 GitHub Models 推理，可切换 GitHub Copilot 后端
- 支持回溯多天活动（--days 参数）

## 适用场景

- 快速汇总我昨天的 GitHub 工作进展用于站会汇报
- 补写多天未汇报期间的工作总结
- 组织内使用时授权读取组织数据后生成报告

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: A GitHub CLI extension that generates AI-powered standup reports using GitHub activity data. It uses GitHub Models f

## 星数曲线

```mermaid
xychart-beta
    title "sgoedecke/gh-standup 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 116 --> 119
    line [117, 118, 118]
```

2026-10-18 117 → 2026-10-24 118（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `8acd61a4dc4e` · [字段定义](../../DATASET.md)*
