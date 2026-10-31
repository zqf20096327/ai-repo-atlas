# Neuradock/eeg-workstation-agent

⭐ 16 · Python · MIT · 推送 2026-09-22 · [GitHub](https://github.com/Neuradock/eeg-workstation-agent) · [官网](https://neuradock.com) · 组织维护

**面向开发者的 EEG 认知负荷信号工具包与本地 API**

本地优先的 Python 工具包：读取 NeuraDock 7 通道（250Hz）EEG 的 TCP 实时流，做确定性解析、预处理与信号质量门控，计算后部 Alpha 动态、峰值频率、不对称性与 Rest/Task 视觉认知负荷对比，通过 GET /api/status 与本地仪表盘供应用消费。面向自适应界面、XR、车载 HMI、康复训练等开发者；提供无硬件合成回放演示与三个浏览器示例。声明非医疗设备；LLM 仅用于可选的工作流选择与解释，且不发送原始 EEG，无 API key 也可运行仪表盘。另附带 Kimi 技能包集成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性 EEG 解析、预处理与信号质量门控
- 后部 Alpha 动态/抑制/峰值频率/不对称性与 Rest/Task 负荷对比
- 实时 TCP 采集 + 本地 API（GET /api/status）+ 仪表盘
- 无硬件合成回放演示与三个浏览器示例（视觉搜索/自适应 HMI/负荷游戏）
- 可选 LLM 工作流选择，原始 EEG 不发送给模型

## 适用场景

- 为自适应界面或车载 HMI 接入实时认知负荷信号
- 教学与研究中演示 Alpha 动态与信号反馈
- 无硬件阶段用合成回放验证集成流程

## 场景标签

 · 领域:神经科学工程/BCI 工具

## 证据(README 行号)

> L25: NeuraDock Agent is a local-first Python toolkit for turning NeuraDock
> L53: - Optional privacy-bounded LLM workflow selection and result explanation.
> L128: No LLM API key is needed to run the dashboard. Its connection action explains

## 星数曲线

```mermaid
xychart-beta
    title "Neuradock/eeg-workstation-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `982ed474ed30` · [字段定义](../../DATASET.md)*
