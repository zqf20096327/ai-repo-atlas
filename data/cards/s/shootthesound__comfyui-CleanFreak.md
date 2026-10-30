# shootthesound/comfyui-CleanFreak

⭐ 34 · JavaScript · 推送 2026-06-07 · [GitHub](https://github.com/shootthesound/comfyui-CleanFreak) · 个人维护

**ComfyUI 工作流按角色一键整理的自定义节点扩展**

ComfyUI 自定义节点：通过右键菜单将画布节点按角色分类并自动排列，划分为 loaders、encoders、conditioning、samplers、decoders、post、outputs 等桶，每桶一列（或一行），列宽取桶内最宽节点，可加彩色分组卡片，连接线不动。分类采用五级查找链：会话覆盖、用户保存的覆盖表、内置类名映射（1200+ 节点类，覆盖原生节点与多个社区包）、节点 CATEGORY、类名正则。提供交互式弹窗重分配角色并持久化到 role_overrides.json。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按角色分列的一键整理（横/竖、可选彩色分组）
- 1200+ 节点类预分类，覆盖原生与 Impact-Pack、rgthree、KJNodes 等社区包
- 五级分类查找链，用户覆盖保存到磁盘并持续积累
- 子图/组节点递归展平后再整理的选项

## 适用场景

- 把杂乱的 ComfyUI 工作流一键按角色分区排列
- 为常用节点包自定义角色分配并长期复用
- 批量删除画布上的分组卡片

## 场景标签

 · 领域:生成式AI/ComfyUI 工具

## 证据(README 行号)

> L3:  One-click tidy by role for any ComfyUI workflow.
> L5:  Ships pre-classified for the entire stock node set plus the most-used community packs — Impact-Pack, controlnet_aux
> L21: ### What it does

## 星数曲线

```mermaid
xychart-beta
    title "shootthesound/comfyui-CleanFreak 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-30 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c69c7381a20d` · [字段定义](../../DATASET.md)*
