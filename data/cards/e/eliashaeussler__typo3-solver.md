# eliashaeussler/typo3-solver

⭐ 30 · PHP · GPL-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/eliashaeussler/typo3-solver) · [官网](https://docs.typo3.org/p/eliashaeussler/typo3-solver/main/en-us/) · 个人维护

**TYPO3 扩展：用 AI 生成的方案解决 CMS 异常**

为 TYPO3 CMS 提供的扩展，扩展其异常处理机制：发生异常时通过 OpenAI PHP 客户端向已配置的模型发送提示词，将返回的补全内容作为解决方案展示。可配置模型、tokens、温度、补全数量等属性，支持已解决问题的缓存，并提供命令行命令，可自定义方案提供者与提示词。兼容 TYPO3 13.4 LTS 与 14.3 LTS。通过 Composer 或 TYPO3 扩展仓库（TER）安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 异常处理器扩展，展示 AI 生成的解决方案
- 可配置补全属性（模型、tokens、温度、数量）
- 已解决问题的缓存集成
- 提供命令行命令与自定义方案提供者/提示词

## 适用场景

- TYPO3 站点出错时直接在错误页看到 AI 生成的修复建议
- 从命令行求解 TYPO3 问题
- 通过自定义提示词适配团队的问题求解流程

## 场景标签

 · 领域:Web/CMS 开发工具

## 证据(README 行号)

> L10: An extension for TYPO3 CMS to solve exceptions with AI generated solutions.
> L11: It uses the [OpenAI PHP client][1] to send a prompt to a configured model

## 星数曲线

```mermaid
xychart-beta
    title "eliashaeussler/typo3-solver 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-28 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `adf7b2040d8e` · [字段定义](../../DATASET.md)*
