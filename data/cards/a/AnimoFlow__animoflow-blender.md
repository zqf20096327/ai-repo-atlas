# AnimoFlow/animoflow-blender

⭐ 10 · Python · GPL-3.0 · 推送 2026-08-13 · [GitHub](https://github.com/AnimoFlow/animoflow-blender) · [官网](https://animoflow.ai/guide/blender) · 组织维护

**Blender 插件：从文本生成角色动画并导入场景**

面向 Blender 用户的动作生成插件，支持四种任务编写方式：单段文本提示、地面绘制轨迹、多段时间线拼接、路标点标记，底层调用 MDM、MoMask、PriorMDM、Kimodo 等模型。生成结果以 glTF 自动导入场景并匹配 FPS。运行方式分云模式（Hugging Face ZeroGPU 配额，免费约 5 分钟/日）与自托管本地服务器模式。支持 Blender 3.6–5.0，纯 stdlib 实现，无 Python 依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四种动作编写方式：prompt、轨迹、时间线、路标点
- 云模式使用用户自己的 Hugging Face ZeroGPU 配额
- 支持自托管本地服务器（Server URL 可配置）
- 生成结果以 glTF 自动导入并同步场景 FPS

## 适用场景

- 在 Blender 视口内用文字描述生成角色动画
- 通过绘制曲线让角色沿指定路径运动
- 用自托管服务器离线运行动作生成流水线

## 场景标签

 · 领域:3D 动画/内容生成

## 证据(README 行号)

> L3: Blender addon for AnimoFlow — generate character motion and import it straight into your scene. Supports all four An
> L60: Generation runs on your own Hugging Face ZeroGPU quota (free ≈ 5 min GPU/day, PRO ≈ 25 min/day).


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `d84a2c6a9cc8` · [字段定义](../../DATASET.md)*
