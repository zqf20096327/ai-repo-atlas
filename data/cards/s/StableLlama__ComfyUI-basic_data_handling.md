# StableLlama/ComfyUI-basic_data_handling

⭐ 52 · Python · GPL-3.0 · 推送 2026-10-16 · [GitHub](https://github.com/StableLlama/ComfyUI-basic_data_handling) · 个人维护

**给 ComfyUI 用户的通用数据操作节点包**

为 ComfyUI 提供基础 Python 数据操作的自定义节点集合，覆盖布尔逻辑、类型转换、比较、控制流、列表/字典/集合/字符串操作、数学与三角函数、文件路径与文件读写、PyTorch 张量操作及日期时间处理等类别。节点轻量，无额外依赖。文档说明 data list/LIST/SET 三种集合类型的区别与选用时机。安装方式为通过 ComfyUI-Manager 查找扩展或手动克隆到 custom_nodes 目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖布尔/比较/控制流/集合/字符串/数学等十余类数据操作节点
- PyTorch 张量操作节点（算术、reshape、切片、join）
- 文件路径操作与图片/掩码/字符串的加载保存
- 无额外依赖，经 ComfyUI-Manager 或手动克隆安装

## 适用场景

- 在 ComfyUI 工作流中做分支与条件判断等控制流
- 工作流内处理列表、字典、集合与字符串数据
- 加载/保存图片与掩码文件并做张量运算

## 场景标签

 · 领域:AI 工作流/节点扩展

## 证据(README 行号)

> L3: Basic Python functions for manipulating data that every programmer is used to. These nodes are very lightweight and
> L18: 2. Clone this repository under `ComfyUI/custom_nodes`

## 星数曲线

```mermaid
xychart-beta
    title "StableLlama/ComfyUI-basic_data_handling 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-27 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a2cbb4a0588a` · [字段定义](../../DATASET.md)*
