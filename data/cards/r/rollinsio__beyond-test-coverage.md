# rollinsio/beyond-test-coverage

⭐ 52 · Python · MIT · 推送 2026-07-02 · [GitHub](https://github.com/rollinsio/beyond-test-coverage) · 个人维护

**测试质量评分基准与 Claude Code 技能：按多维准则生成/加固测试套件**

包含两部分：跨语言基准实验与两个捆绑的 Claude Code 技能。基准部分对 9 个开源库（Python/JS/TS/Go，另含 Kotlin/Swift 矩阵）删除人工测试套件，经 read→build→evaluate 循环再生，并按反脆弱性、严谨性、mock 纪律、复用、正确性、覆盖率下限六组评分轴与人工基线对比。技能部分提供 test-quality 评分器/循环定义与 results-dashboard 仪表盘渲染，可经插件市场或直接运行 score.py 使用；非 Python 语言档位为启发式规则，未经 Python 同等实证验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 六组质量评分轴（反脆弱/严谨/mock/复用/正确性/覆盖率下限）与自动计数脚本
- read→build→evaluate 循环从源码再生成测试套件并与人工基线逐轴对比
- 9 库 × 3 语言（另含 Kotlin/Swift 6 库矩阵）的对比实验与交互式结果仪表盘
- 以 Claude Code 技能形式提供，可直接运行 score.py 评分任意套件

## 适用场景

- 审计或加固现有测试套件的质量（而非仅看覆盖率）
- 用 LLM 循环再生成测试套件并与人工基线逐轴对比
- 查阅 LLM 生成测试与人工测试质量对比的实验数据

## 场景标签

`模型评测` `代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: **A Claude Code skill that hardens test *quality*, not coverage** — packaged
> L178: Or score any suite directly, without the skill harness:

## 星数曲线

```mermaid
xychart-beta
    title "rollinsio/beyond-test-coverage 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-28 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `648aed41eaa2` · [字段定义](../../DATASET.md)*
