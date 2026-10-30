# TalentOS-AI/claude-code-source-analysis

⭐ 17 · 推送 2026-10-16 · [GitHub](https://github.com/TalentOS-AI/claude-code-source-analysis) · [官网](https://talentos-ai.github.io/claude-code-source-analysis/) · 组织维护 · 中文 README

**分析 Claude Code 泄露源码的中文技术手册（14 章）**

基于 2026 年 3 月通过 npm source map 泄露的 Claude Code TypeScript 源码（约 1,902 个文件 / 512,000 行）编写的中文分析手册，共 14 章，附 13 张架构图，覆盖架构、安全、多 Agent 设计逻辑与正反示例，并附录一键复制配置集。仓库本身不提供泄露源码，仅做分析引用，声明源码版权归 Anthropic 所有，仅用于教育与安全研究。以 GitBook 形式发布，由 TalentOS 维护并提供定制 Agent / 技能开发服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于约 51 万行泄露 TypeScript 源码的分析
- 14 章内容与 13 张架构图
- 附录提供一键复制配置集

## 适用场景

- 系统学习 Claude Code 的架构与多 Agent 设计
- 日常使用 Claude Code 时查快捷键、隐藏参数与权限配置
- 了解泄露源码中的安全与设计逻辑

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L17: 本书分析基于 2026 年 3 月 31 日通过 npm source map 泄露的 Claude Code TypeScript 源码（约 1,902 个文件 / 512,000 行）。原始泄露经 @Fried_rice 公开
> L5: ### 三种读法

## 星数曲线

```mermaid
xychart-beta
    title "TalentOS-AI/claude-code-source-analysis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `558c36747dfc` · [字段定义](../../DATASET.md)*
