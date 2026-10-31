# Corning-AI/PCBai

⭐ 31 · 推送 2026-01-05 · [GitHub](https://github.com/Corning-AI/PCBai) · 组织维护

**对话式 PCB 设计 agent：用自然语言生成与优化电路板**

面向物联网、嵌入式、原型与教育场景的智能 PCB 设计代理：从高层规格说明生成电路原理图，用考虑信号完整性、散热与制造约束的算法优化元件布局，进行多目标自动布线，执行设计规则检查与信号完整性分析，支持 2/4/6+ 层板，并导出 Gerber、钻孔、网表、BOM 等生产文件。技术栈为 Python 3.8+，计划集成 KiCAD 与 OpenAI 对话接口。README 中安装、基础用法、CLI 与架构均标注 Coming Soon，尚未交付可用版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 从规格说明自动生成电路原理图
- 考虑信号完整性/散热/制造约束的元件布局优化与自动布线
- DRC 设计规则检查与信号完整性分析（阻抗匹配/串扰检测等）
- 支持 2/4/6+ 层板并导出 Gerber/钻孔/BOM 生产文件

## 适用场景

- 用自然语言描述需求后自动生成 PCB 原理图与布局
- 物联网与嵌入式设备的控制板设计
- 学生与爱好者在 AI 辅助工作流中学习 PCB 设计基础

## 场景标签

 · 领域:电子设计自动化（EDA）/硬件设计

## 证据(README 行号)

> L14: PCBai is an intelligent PCB (Printed Circuit Board) design agent that leverages conversational AI and advanced algo
> L21: Automatically generate circuit schematics from high-level specifications. Simply describe your circuit requirements
> L131: - **OpenAI**: AI-powered conversational interface (coming soon)

## 星数曲线

```mermaid
xychart-beta
    title "Corning-AI/PCBai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-31 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `9d26a0ba6cd7` · [字段定义](../../DATASET.md)*
