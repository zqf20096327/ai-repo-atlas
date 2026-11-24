# davebream/claude-of-alexandria

⭐ 10 · TypeScript · GPL-3.0 · 推送 2026-11-21 · [GitHub](https://github.com/davebream/claude-of-alexandria) · [官网](https://github.com/davebream/claude-of-alexandria) · 个人维护

**面向圣经研究的 Claude Code 技能插件：产出严谨解经分析**

为 Claude Code 提供的插件，含 7 个技能与 13 个子代理，覆盖全部 66 卷正典；核心是 /coa:deep-study 流程（校验→检索→边界→并行分析→验证→修复→综合）。通过 204 个自动化行为测试（含 87 个 RED 相位测试）记录并防止模型伪造语言学数据、体裁误判、道德化漂移等失效模式。模型策略规定默认 Sonnet、不支持 Haiku，MCP 服务器运行在 Cloudflare Workers 上。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 技能 + 13 子代理覆盖 66 卷正典圣经研究
- 204 个自动化行为测试（87 RED + 80 GREEN 等）验证失效模式修正
- deep-study 工作流限制最多 8 次代理调用与 1 次修复循环
- 解析器验证的词汇数据与四级解释置信度标注

## 适用场景

- 讲道与教学的段落解经笔记准备
- 验证某段经文作为话语单元的完整性
- 对经文进行词汇与话语标记的学术问答与交叉引用

## 场景标签

`工作流自动化` `知识库管理` · 领域:效率与自动化

## 证据(README 行号)

> L1: Claude of Alexandria — rigorous biblical study for AI agents
> L8: Structured frameworks that prevent AI agents from committing exegetical malpractice. Every skill is built with Test-
> L141: Runs a bounded, evidence-first exegetical study as a native Claude Code workflow:

## 星数曲线

```mermaid
xychart-beta
    title "davebream/claude-of-alexandria 星数(近 2 点)"
    x-axis ["2026-11-23", "2026-11-24"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-23 10 → 2026-11-24 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `66e047a77790` · [字段定义](../../DATASET.md)*
