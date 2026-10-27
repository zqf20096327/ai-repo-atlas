# oopsie-data/oopsie-data-tools

⭐ 24 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/oopsie-data/oopsie-data-tools) · [官网](https://oopsie-data.com) · 组织维护

**机器人操作数据集的录制、标注与提交工具包**

OopsieData Tools 服务于 Oopsie Data 计划：该计划收集实验室真实机器人操作轨迹（含失败、次优与成功样本）构建共享大规模数据集。工具包提供 HDF5 形式的回合录制（EpisodeRecorder）、Web 标注流程、策略 rollout 过程中的在环标注，并附带验证、质量检查（oopsie-data qa）、检查与上传到官方仓库的工具。面向需要向数据集贡献数据的机器人实验室，可通过 issue 请求接入评估管线的帮助。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- HDF5 回合录制（EpisodeRecorder）
- Web 标注与策略 rollout 中的在环标注
- oopsie-data qa 质量检查、验证与上传官方仓库的工具

## 适用场景

- 实验室录制机器人操作轨迹并贡献到共享数据集
- 在策略评估过程中同步进行数据标注
- 对贡献数据做质量检查后上传

## 场景标签

 · 领域:机器人/数据集工具

## 证据(README 行号)

> L5: Oopsie Data is an initative to build a large-scale dataset of real robot manipulation failures (along with other mix
> L13: - HDF5 episode recording (`EpisodeRecorder`)

## 星数曲线

```mermaid
xychart-beta
    title "oopsie-data/oopsie-data-tools 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `10028ffe6742` · [字段定义](../../DATASET.md)*
