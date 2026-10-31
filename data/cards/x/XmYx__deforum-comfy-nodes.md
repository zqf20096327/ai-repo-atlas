# XmYx/deforum-comfy-nodes

⭐ 198 · Python · MIT · 推送 2026-06-01 · [GitHub](https://github.com/XmYx/deforum-comfy-nodes) · [官网](https://deforum.studio/) · 组织维护

**在 ComfyUI 中运行 Deforum 的动画生成节点包**

将 Deforum 集成到 ComfyUI 的自定义节点包：安装后可在 ComfyUI 工作流中使用 Deforum 生成逐帧动画，README 给出加载示例工作流、逐帧或批量排队生成动画的用法。安装途径包括 ComfyUI Manager 内搜索安装，或 git clone 到 custom_nodes 目录手动安装；要求已安装 ComfyUI 并使用 Python 3.10，建议虚拟环境。另列出 rgthree、AudioScheduler、IPAdapter_plus 等推荐配合节点。MIT 许可，附 Discord 社区。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Deforum 功能以 ComfyUI 自定义节点形式提供
- 通过 ComfyUI Manager 或 git clone 到 custom_nodes 安装
- 提供示例工作流，支持自动排队与批量生成动画帧
- 列出多个推荐配合使用的第三方节点

## 适用场景

- 在 ComfyUI 中搭建 Deforum 动画生成工作流
- 加载示例工作流快速生成逐帧动画
- 结合 AudioScheduler、IPAdapter 等节点扩展动画效果

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: Deforum integration for ComfyUI.
> L35: 3. Queue prompt, this will generate your first frame, you can enable Auto queueing, or batch as many images as long

## 星数曲线

```mermaid
xychart-beta
    title "XmYx/deforum-comfy-nodes 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 197 --> 199
    line [198, 198]
```

2026-10-18 198 → 2026-10-31 198（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `09dbc1034851` · [字段定义](../../DATASET.md)*
