# scanaislop/aislop

⭐ 772 · TypeScript · MIT · 推送 2026-11-22 · [GitHub](https://github.com/scanaislop/aislop) · [官网](https://scanaislop.com) · 组织维护

**AI 辅助开发代码质量扫描器：确定性规则检出 slop 模式**

针对 AI 编码助手留下的代码模式（叙事性注释、被吞异常、隐藏 fallback、as any 断言、幻觉导入、重复辅助函数、死代码等）的本地扫描 CLI：50+ 规则覆盖 12 种语言目标，对每次变更打 0–100 分，亚秒级运行；运行路径不含 LLM，输入相同代码输出相同分数。支持 scan/fix/agent/ci 命令、编辑钩子、行内忽略指令与 YAML 规则配置，可选捆绑 Ruff、golangci-lint、PMD 等外部工具，MIT 许可，通过 npm/Homebrew/PyPI 分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 50+ 确定性规则覆盖 12 种语言目标，运行时不含 LLM
- 0–100 评分，支持 CI 模式（JSON + gate）与 README 徽章
- aislop agent 在 git worktree 中调用本地编码代理修复并复检
- 行内 aislop-ignore 指令、规则级 severity 覆写与 .aislopignore

## 适用场景

- 在 CI 中对 AI 生成代码变更打分并设质量门槛
- 安装编辑钩子让编码代理在每次修改后自动修复 slop
- 对多语言仓库扫描死代码、重复代码与安全问题

## 场景标签

 · 领域:开发者工具/代码质量

## 证据(README 行号)

> L9: aislop catches them. 50+ rules across 12 language targets (TypeScript, JavaScript, Expo / React Native, Python, Go, 
> L50: aislop ci                    # CI mode (JSON + gate)
> L218: `aislop agent` keeps the deterministic scanner in charge while using the coding agent you already have installed. 

## 星数曲线

```mermaid
xychart-beta
    title "scanaislop/aislop 星数(近 25 点)"
    x-axis ["2026-10-22", "2026-10-23", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-24"]
    y-axis "stars" 691 --> 779
    line [698, 699, 700, 702, 706, 707, 711, 714, 716, 717, 700, 732, 737, 739, 742, 744, 745, 746, 748, 752, 755, 766, 769, 772, 772]
```

2026-10-22 698 → 2026-11-24 772（+74）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `36959eff3ded` · [字段定义](../../DATASET.md)*
