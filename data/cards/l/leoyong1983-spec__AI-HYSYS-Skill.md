# leoyong1983-spec/AI-HYSYS-Skill

⭐ 10 · Python · MIT · 推送 2026-11-11 · [GitHub](https://github.com/leoyong1983-spec/AI-HYSYS-Skill) · 个人维护 · 中文 README

**让 AI 智能体接管已有 Aspen HYSYS 仿真的技能库**

面向化工/流程工程师的 Codex skill：通过 COM（HYSYS.Application）或 spreadsheet/workbook 桥接管人工已建且可运行的 HYSYS case，覆盖环境就绪检查、版本选择（V14/V15）、有边界参数修改、强制收敛验收循环、机器可读导出、PFD 视觉清理与审查阶段基础工艺包生成。明确不宣称从零建模或无人批准的生产写回；要求 Windows 本地安装 Aspen HYSYS 并配置 COM 注册。脚本优先、每步可审计，缺验证能力时报 UNVERIFIED/BLOCKED。

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

- 接管已有可运行 HYSYS case，支持 V14/V15 显式版本选择
- 强制收敛验收循环：求解-等待-回读-全项判断，fail-closed 且带迭代历史
- 三条示例提示词覆盖环境验证、有边界修改导出、基线冻结与工艺包生成
- 可作 Codex skill 安装，或直接复用 SKILL.md/AGENTS.md 等参考资料

## 适用场景

- 让 AI 助手接管已有的气体处理/LNG/炼厂 HYSYS 模型做验证与导出
- 对现有 case 做有边界的参数调优与敏感性计算
- 为审查阶段冻结基线并生成基础工艺包交付物
- 在已配置监控/数孪测试床场景下做监督级桥接（需明确读写审批）

## 场景标签

 · 领域:化工/流程工程自动化

## 证据(README 行号)

> L10: This repository packages a reusable skill, source pack, and workflow for engineers who want to let an AI agent take
> L29: **中文**：AI-HYSYS-Skill 是面向 Aspen HYSYS 的 AI 技能库，核心目标是接管人工已建、已经能运行的 HYSYS case，而不是让 AI 从零盲目建模。它帮助智能体检查 Windows/HYSYS 
> L129: - Python with `pywin32` (`pythoncom` and `win32com.client`) for direct COM automation

## 星数曲线

```mermaid
xychart-beta
    title "leoyong1983-spec/AI-HYSYS-Skill 星数(近 2 点)"
    x-axis ["2026-11-25", "2026-11-27"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-25 10 → 2026-11-27 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 mid · 依据 README sha `828632f287c2` · [字段定义](../../DATASET.md)*
