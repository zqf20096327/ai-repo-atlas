# voight-dev/voight

⭐ 37 · TypeScript · MIT · 推送 2026-04-09 · [GitHub](https://github.com/voight-dev/voight) · [官网](https://voight.dev) · 个人维护

**在 VS Code 中追踪并审阅 AI 生成代码的扩展**

VS Code 扩展，检测 AI 助手插入的代码并组织为可审阅片段：提供时间线视图、全文件视图、片段级 Diff、圈复杂度指标与上下文笔记，附编辑统计与导出等命令。检测基于插入字符数/行数阈值与排除规则，适用于任意文本文件；复杂度分析支持 TypeScript/JavaScript/Python/Go（移植自 Lizard）。可选 BYOK 功能允许用自己的 API key（gemini/anthropic/openai）请求片段解释。可从扩展市场安装或源码打包安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按时间线/全文件视图组织检测到的 AI 代码片段，附 Diff 展开
- 片段显示圈复杂度指标（分析移植自 Lizard）
- BYOK AI 解释：支持 gemini/anthropic/openai，自带 API key
- 检测阈值与排除模式可配置，检测适用于任意文本文件

## 适用场景

- AI 辅助开发中回顾和定位 AI 生成的代码段
- 按复杂度指标筛选需要重点审阅或重构的 AI 代码
- 为片段附加笔记并标记待审阅项

## 场景标签

 · 领域:开发工具/IDE 扩展

## 证据(README 行号)

> L5:  Track and review AI-generated code in VS Code.
> L11: Voight detects code insertions from AI assistants and organizes them into reviewable segments. When you're moving f
> L39: ### AI Explanations (BYOK)

## 星数曲线

```mermaid
xychart-beta
    title "voight-dev/voight 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-25 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `c88a41c6750b` · [字段定义](../../DATASET.md)*
