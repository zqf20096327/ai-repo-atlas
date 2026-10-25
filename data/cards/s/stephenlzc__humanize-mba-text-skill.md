# stephenlzc/humanize-mba-text-skill

⭐ 55 · Python · MIT · 推送 2026-07-08 · [GitHub](https://github.com/stephenlzc/humanize-mba-text-skill) · 个人维护 · 中文 README

**面向中国 MBA 论文的 AI 写作痕迹检测与改写建议工具**

针对中国 MBA 毕业论文的 AI 写作痕迹检测与去除工具：通过规则匹配（TOML 外置规则识别 AI 词汇、模糊归因、套话等）、散文统计（段落级句长 CV、指纹分析）与语义链（10 维跨段/跨章检测）三层叠加识别 AI 生成特征，输出结构化改写计划（location/skeleton/替换短语/目标字数）、按句聚合的高风险标注与 Before/After 对比报告。支持针对绪论到结论 5 个章节的优化策略，可自动修复中英文混排空格，可作为 Claude Code Skill 使用。 transformers 为可选依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三层叠加检测：规则匹配 + 散文统计（句长 CV）+ 语义链（10 维跨段/跨章）
- 结构化改写计划：每条 issue 含 location、改写骨架、推荐替换短语与目标字数
- 按句聚合的高风险标注（含字符偏移、触发规则、改写示例），可直接对接 LLM 改写流程
- 可作为 Claude Code 的 Skill 直接使用

## 适用场景

- 检测 MBA 论文中的 AI 写作痕迹并获取修改建议
- 对比改写前后的句长 CV 变化验证效果
- 按章节类型获取针对性的写作改进策略

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L19: 这是一个专门为**中国 MBA 毕业论文**设计的 AI 写作痕迹检测与去除工具。基于 MBA 论文的学术规范和实践要求，通过多维度检测方法识别文本中的 AI 生成特征，并提供具体的修改建议，帮助你将 AI 生成的文本改写为自然、
> L36: - ✅ **多层级 AI 检测**：从规则匹配（regex）→ 散文统计（5 维 CV/指纹）→ 语义链（10 维跨段/跨章）三层叠加
> L103: python scripts/detect_ai_patterns.py your_text.txt --format markdown --output report.md

## 星数曲线

```mermaid
xychart-beta
    title "stephenlzc/humanize-mba-text-skill 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23", "2026-10-25"]
    y-axis "stars" 51 --> 56
    line [52, 53, 55, 55]
```

2026-10-18 52 → 2026-10-25 55（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `824734819c64` · [字段定义](../../DATASET.md)*
