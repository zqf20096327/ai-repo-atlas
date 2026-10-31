# ahmdd4vd/Fable5res

⭐ 13 · JavaScript · NOASSERTION · 推送 2026-06-16 · [GitHub](https://github.com/ahmdd4vd/Fable5res) · [官网](https://www.npmjs.com/package/fable5-skills) · 个人维护

**从 4,665 条 Claude Fable 5 推理轨迹蒸馏出的 5 个 agent 技能文件包**

npm 包 fable5-skills：从 HuggingFace 公开数据集 Kuberwastaken/Fable-5-traces（4,665 条真实 Claude Fable 5 思维链轨迹、60 个会话）中做统计分析，将可度量的推理行为（87.7% 动作后验证率、93.5% 先读后编率等）提炼为 5 个 SKILL.md 文件（fable-think/fable-code/fable-debug/fable-architect/fable-verify），供读取 markdown 的编码 agent（Claude Code、Cursor、Cline 等）通过 npx 一条命令安装。附 CLI 安装器（Node.js 零依赖）与 31 项声明核验报告；采用 AGPL-3.0 许可，作者表示可联系商谈双许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 个自包含可组合的 SKILL.md 推理技能（每文件含量化行为指标）
- 技能中的 31 项量化声明均对照源数据集核验（100% 通过）
- npx fable5-skills init 支持 6 种 agent 目录布局及 skills.sh 市场安装（70+ 编码 agent）
- 附 7 场景跨模型仿真基准（MiniMax M3，9 轮迭代测试）

## 适用场景

- 给我的编码 agent 安装结构化推理循环（ACKNOWLEDGE→OBSERVE→EXECUTE→VERIFY）
- 在调试时引入假设驱动的根因分析方法论
- 为不同编码 agent（Cursor/Cline/Windsurf 等）批量部署同一套推理技能

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: **AI reasoning skills, mathematically distilled from 4,665 real Claude Fable 5 chain-of-thought traces.**
> L27: `fable5-skills` packages these measurable behaviors into **5 drop-in `SKILL.md` files** so any agent that reads mar
> L244: Distilled from the public HuggingFace dataset `Kuberwastaken/Fable-5-traces` — 4,665 rows, 60 sessions of real Cla

## 星数曲线

```mermaid
xychart-beta
    title "ahmdd4vd/Fable5res 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `46ae29e2f245` · [字段定义](../../DATASET.md)*
