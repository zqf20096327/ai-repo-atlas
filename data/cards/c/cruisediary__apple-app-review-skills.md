# cruisediary/apple-app-review-skills

⭐ 19 · Swift · MIT · 推送 2026-05-02 · [GitHub](https://github.com/cruisediary/apple-app-review-skills) · 个人维护 · 中文 README

**面向 Claude Code 的 App Store 审核风险检查技能与 agent 集合**

将 Apple App Store Review Guidelines 全部 5 个章节与 Stack Overflow、Apple Developer Forums、RevenueCat 社区等来源的真实拒审案例，编码为 31 个可复用的 Claude Code skills 和自治 agent：覆盖布局与 UI、权限申请、UGC 安全、隐私（含隐私清单、账号删除、AI 数据披露）、质量（崩溃风险、私有 API）、IAP 与订阅披露、元数据等类别，提交前运行可产出按优先级排序的拒审风险报告。提供 curl 一键安装、git clone 手动安装与项目级安装三种方式，附 Swift 反例代码与 5 个 agent。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 31 个 skills 覆盖 App Store 审核指南 5 个章节
- 基于真实开发者拒审案例构建检查项
- /appstore-full-audit 一键运行全部 skills 并输出优先级风险报告
- skills 为原子化设计，可在自定义 agent 中组合使用

## 适用场景

- iOS/macOS 应用提交 App Store 前做全量拒审风险自查
- 针对 iPad 布局、隐私合规、订阅披露等专项审计
- 团队在项目仓库内共享审核检查技能

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: > A curated collection of Claude Code skills and agents to eliminate App Store rejections — built from **real-world 
> L15: This project encodes Apple's full App Store Review Guidelines — combined with **dozens of real developer rejection 
> L217: |`appstore-full-audit`|All 31 skills|Final pre-submission check|

## 星数曲线

```mermaid
xychart-beta
    title "cruisediary/apple-app-review-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `eee5cb7c115d` · [字段定义](../../DATASET.md)*
