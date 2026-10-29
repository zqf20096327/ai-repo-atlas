# dweekly/ai-content-disclosure

⭐ 23 · MIT · 推送 2026-03-19 · [GitHub](https://github.com/dweekly/ai-content-disclosure) · 个人维护

**面向网页作者与标准参与者的 HTML AI 内容披露规范提案**

由 David E. Weekly 撰写的 W3C 社区组规范说明文档（explainer）：提出 ai-disclosure HTML 属性与配套 meta 标签，让作者在页面元素级粒度声明 AI 参与程度。取值（none/ai-assisted/ai-generated/autonomous）对齐 IETF AI-Disclosure 头与 IPTC Digital Source Type 词表，可选元数据包括 ai-model、ai-provider、ai-prompt-url，并给出 schema.org JSON-LD 表达与继承规则。这是规范文本而非可安装软件，无安装命令；文档明确该机制为自愿声明、无完整性保护。

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

- 元素级 ai-disclosure 属性 + 页面级 meta 标签双层声明
- 四档取值对齐 IETF AI-Disclosure 与 IPTC Digital Source Type
- 可选 ai-model/ai-provider/ai-prompt-url 元数据与 schema.org JSON-LD 集成
- 文档包含隐私、无障碍、国际化考量与备选方案分析

## 适用场景

- 出版方在混合内容页面（人写正文 + AI 摘要）中分区块标注 AI 参与度
- 标准参与者跟踪 W3C AI 内容披露规范的提案讨论
- 面向 EU AI Act 第 50 条机器可读标注要求探索 HTML 层实现

## 场景标签

 · 领域:Web 标准/内容透明度

## 证据(README 行号)

> L9: - W3C AI Content Disclosure Community Group
> L23: This explainer proposes an `ai-disclosure` HTML attribute and a companion

## 星数曲线

```mermaid
xychart-beta
    title "dweekly/ai-content-disclosure 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `b30f1a9e4079` · [字段定义](../../DATASET.md)*
