# spawner1145/CUI-Lumina2-TeaCache

⭐ 20 · Python · GPL-3.0 · 推送 2026-02-02 · [GitHub](https://github.com/spawner1145/CUI-Lumina2-TeaCache) · 个人维护

**ComfyUI 节点：为 Lumina-Image-2.0 移植 TeaCache 推理加速**

将 TeaCache 缓存加速方法移植到 ComfyUI 的自定义节点，作用于 Lumina-Image-2.0 图像生成模型：把 TeaCache 节点接入 UNet Loader 与 KSampler 之间，通过设置 rel_l1_thresh 阈值与多项式系数调节加速程度，训练无关。README 给出低/高步数下的推荐参数组合，并在单张 4090 上列出 50 步推理延迟对比（约 25s 降至 10s）。安装支持 git clone 到 custom_nodes 或经 ComfyUI-Manager 安装。加速以图像质量下降为代价。

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

- TeaCache 训练无关加速移植到 ComfyUI 节点
- rel_l1_thresh 与系数可按步数调节质量/速度权衡
- 4090 上 50 步推理约 25s 降至 10s（阈值 0.5）
- 支持 git clone 与 ComfyUI-Manager 两种安装方式

## 适用场景

- 在 ComfyUI 中加速 Lumina-Image-2.0 出图
- 按质量/速度需求调节缓存阈值
- 低步数场景下进一步压缩生成时间

## 场景标签

`图像生成` `推理引擎` · 领域:内容生成

## 证据(README 行号)

> L2: ## referenced from https://github.com/ali-vilab/TeaCache/tree/main/TeaCache4Lumina2
> L24: 1. Connect the `TeaCache` node between the `UNet Loader` and `KSampler` in your workflow.
> L34: TeaCache can speedup Lumina-Image-2.0 without much visual quality degradation, in a training-free manner. The follo

## 星数曲线

```mermaid
xychart-beta
    title "spawner1145/CUI-Lumina2-TeaCache 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d32c505a6921` · [字段定义](../../DATASET.md)*
