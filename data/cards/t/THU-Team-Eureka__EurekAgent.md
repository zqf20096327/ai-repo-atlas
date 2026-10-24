# THU-Team-Eureka/EurekAgent

⭐ 85 · Python · AGPL-3.0 · 推送 2026-08-10 · [GitHub](https://github.com/THU-Team-Eureka/EurekAgent) · 组织维护 · 中文 README

**驱动 Claude Code 做指标驱动自主科学发现的 agent 系统**

面向度量驱动任务的自主科研系统：用户以 INSTRUCTION.md、SUBMISSION_FORMAT.md 与私有 evaluate.py 定义问题与评分标准，系统协调现成 CLI agent（Claude Code）提出方案、实现代码、运行实验并循环迭代。agent 与评分在独立 Docker 容器中隔离执行，私有评估器不挂载进 agent 容器以防篡改；支持中断恢复、TUI 对话与 Web 实时监控。需安装 Docker、Node.js 22+、Claude Code，GPU 可选（默认 auto，支持 CPU-only）。AGPL-3.0，另设商业授权条目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以用户提供的 evaluate.py 为评分唯一来源（grade_submission + is_better 契约）
- agent 与 grader 双容器隔离执行，私有评估器对 agent 不可见
- 可中断恢复的长时运行与 Web 实时监控/离线快照
- /generate-inputs 技能从自然语言描述交互生成问题文件

## 适用场景

- 定义优化问题与评分函数，让 agent 自主迭代寻找更优解
- 数学、内核工程、机器学习任务的自动化实验循环
- 通过 TUI 介入指导、监控长时运行的成本与得分演化

## 场景标签

`编码 Agent` `科研工具` · 领域:编码与开发

## 证据(README 行号)

> L14:  Define your problem and evaluation criteria — EurekAgent coordinates off-the-shelf CLI agents (i.e. Claude Code) t
> L25: We present **EurekAgent**, an agent system for metric-driven autonomous scientific discovery. Define your problem a

## 星数曲线

```mermaid
xychart-beta
    title "THU-Team-Eureka/EurekAgent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 83 --> 86
    line [84, 85]
```

2026-10-18 84 → 2026-10-24 85（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `24c435e276f6` · [字段定义](../../DATASET.md)*
