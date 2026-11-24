# Sandflow-ai/sand3d

⭐ 2,249 · HTML · Apache-2.0 · 推送 2026-11-23 · [GitHub](https://github.com/Sandflow-ai/sand3d) · [官网](https://sandflow.ai/sand3d/) · 组织维护

**为 LLM 设计的 Python 3D 建模库，用短程序描述物体**

基于 Blender bpy 的 Python 建模库：以短程序（profiles、solids、edits、joints、assemblies）声明式描述 3D 物体的构成方式，每个部分按命名而非手算坐标访问，同一程序可确定性复现同一网格。API 全量约 3,600 tokens，可放入 system prompt 供模型生成建模程序；一次导出支持 GLB、URDF、USD、IFC、OBJ、STL 六种格式，并在 Hugging Face 提供五套 CC BY 4.0 程序数据集。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 程序式 3D 建模：部件、关节与装配体以命名声明，输出确定性网格
- API 全量约 3,600 tokens 可放入 system prompt，并附 llms.txt 与装配体编写准则
- 一次导出 GLB/URDF/USD/IFC/OBJ/STL，覆盖游戏引擎、机器人仿真与 BIM 工具链
- Hugging Face 上五套程序化 3D 数据集（Objaverse/CAD/Articraft/SimReady/AutoMate）

## 适用场景

- 让 LLM 通过生成 sand3d 程序来产出可编辑、可导出的 3D 模型
- 为机器人仿真（PyBullet/MuJoCo/Isaac）生成带关节与限位的 URDF 资产
- 向 Revit/ArchiCAD 等 BIM 工具导出 IFC 格式的装配体
- 读取程序化 3D 数据集做模型训练或资产检索

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L5: **3D modeling in Python, built for LLMs.**
> L7: sand3d is a Python library for writing 3D objects as short programs: profiles, solids,
> L105: ## Give it to your LLM

## 星数曲线

```mermaid
xychart-beta
    title "Sandflow-ai/sand3d 星数(近 15 点)"
    x-axis ["2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-24"]
    y-axis "stars" 1255 --> 2319
    line [1343, 1744, 1844, 1917, 1957, 1992, 2033, 2080, 2112, 2152, 2166, 2202, 2218, 2231, 2231]
```

2026-11-08 1,343 → 2026-11-24 2,231（+888）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `c7a87702e643` · [字段定义](../../DATASET.md)*
